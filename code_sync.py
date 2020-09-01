import bpy
from . sync_utils import pull_text, create_text, update_text, delete_text
import os
import datetime


class SyncToDevice(bpy.types.Operator):
    """Sync to device"""
    bl_idname = "texts.sync_to_device"
    bl_label = "CodeSync > Sync to device"

    def execute(self, context):
        scripts_path = os.path.dirname(bpy.data.filepath)+"\\scripts\\"
        os.mkdir(scripts_path) if not os.path.exists(scripts_path) else None
        for text in bpy.data.texts:
            name = text.name
            if name.endswith(".py"):
                with open(os.path.join(scripts_path, name), "w",
                          encoding="utf-8") as file:
                    file.write(pull_text(name))
        return {'FINISHED'}


class SyncFromDevice(bpy.types.Operator):
    """Sync from device"""
    bl_idname = "texts.sync_from_device"
    bl_label = "CodeSync > Sync from device"

    def execute(self, context):
        scripts_path = os.path.dirname(bpy.data.filepath)+"\\scripts\\"
        os.mkdir(scripts_path) if not os.path.exists(scripts_path) else None
        for file in os.listdir(scripts_path):
            if (os.path.isfile(os.path.join(scripts_path, file)) and
                    file.endswith(".py")):
                create_text(file)
                update_text(file, path=os.path.join(scripts_path, file))
        return {'FINISHED'}


class BackUpScripts(bpy.types.Operator):
    """BackUp to device"""
    bl_idname = "texts.back_up"
    bl_label = "CodeSync > BackUp to device"

    def execute(self, context):
        fname = str(datetime.datetime.now()
                    ).replace(' ', '_').replace(":", "-").split('.')[0]+"\\"
        scripts_path = os.path.join(os.path.dirname(bpy.data.filepath),
                                    "scripts\\")
        backups_path = os.path.join(scripts_path, ".backUp\\")
        backup_path = os.path.join(backups_path, fname)
        os.mkdir(scripts_path) if not os.path.exists(scripts_path) else None
        os.mkdir(backups_path) if not os.path.exists(backups_path) else None
        os.mkdir(backup_path) if not os.path.exists(backup_path) else None
        for text in bpy.data.texts:
            name = text.name
            if name.endswith(".py"):
                with open(os.path.join(backup_path, name), "w",
                          encoding="utf-8") as file:
                    file.write(pull_text(name))
        return {'FINISHED'}


class DelDeviceScripts(bpy.types.Operator):
    """Delete all files"""
    bl_idname = "texts.del_device_scripts"
    bl_label = "CodeSync > Delete in-device scripts"

    def execute(self, context):
        scripts_path = os.path.dirname(bpy.data.filepath)+"\\scripts\\"
        os.mkdir(scripts_path) if not os.path.exists(scripts_path) else None
        for file in os.listdir(scripts_path):
            if (os.path.isfile(os.path.join(scripts_path, file)) and
                    file.endswith(".py")):
                os.remove(os.path.join(scripts_path, file))
        return {'FINISHED'}


class DelBlendScripts(bpy.types.Operator):
    """Delete all texts"""
    bl_idname = "texts.del_blend_scripts"
    bl_label = "CodeSync > Delete in-blend scripts"

    def execute(self, context):
        for text in bpy.data.texts:
            if text.name.endswith(".py"):
                delete_text(text.name)
        return {'FINISHED'}
