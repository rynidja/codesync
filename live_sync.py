import bpy
from . sync_utils import rename_text, create_text, delete_text, update_text
import os
import functools
import platform


is_live = False
previous = {}
current = {}


class StartLiveSync(bpy.types.Operator):
    bl_idname = "texts.start_live_sync"
    bl_label = "CodeSync > Start live sync"

    def execute(self, context):
        global is_live
        scripts_path = os.path.dirname(bpy.data.filepath)+"\\scripts\\"
        os.mkdir(scripts_path) if not os.path.exists(scripts_path) else None
        if not is_live:
            is_live = True
            bpy.app.timers.register(functools.partial(watcher, scripts_path))
        return {'FINISHED'}


class StopLiveSync(bpy.types.Operator):
    bl_idname = "texts.stop_live_sync"
    bl_label = "CodeSync > Stop live sync"

    def execute(self, context):
        global is_live
        is_live = False
        return {'FINISHED'}


def watcher(path):
    global is_live, previous, current
    if not is_live:
        return None

    current = dict((file, os.stat(os.path.join(path, file))
                    ) for file in os.listdir(path) if (os.path.isfile(
                        os.path.join(path, file))
        and file.endswith(".py")))
    added = dict((file, current[file])
                 for file in current if file not in previous)
    removed = dict((file, previous[file])
                   for file in previous if file not in current)
    not_added = dict((file, current[file])
                     for file in current if file not in added)
    modified = dict((file, not_added[file])
                    for file in not_added
                    if not_added[file].st_mtime != previous[file].st_mtime)

    if platform.system() == "Windows":
        for new in added:
            for old in removed:
                if added[new].st_ctime == removed[old].st_ctime:
                    removed = dict((file, removed[file])
                                   for file in removed if not file == old)
                    added = dict((file, added[file])
                                 for file in added if not file == new)
                    rename_text(old, new)
                    break
    for file in added:
        create_text(file)
        if added[file].st_size:  # In case of pasting or undeleting files
            update_text(file, path=os.path.join(path, file))
    for file in removed:
        delete_text(file)
    for file in modified:
        update_text(file, path=os.path.join(path, file))

    previous = current
    return .1
