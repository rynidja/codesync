import bpy
from . sync_utils import pull_text, create_text, update_text, delete_text
import os
import datetime


""" Sync functions """


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
                with open(os.path.join(scripts_path, name), "w", encoding="utf-8") as file:
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
                with open(os.path.join(scripts_path, file), "r", encoding="utf-8") as f:
                    data = f.read()
                create_text(file)
                update_text(file, data)
        return {'FINISHED'}


class BackUpScripts(bpy.types.Operator):
    """BuckUp to device"""
    bl_idname = "texts.back_up"
    bl_label = "CodeSync > BuckUp to device"

    def execute(self, context):
        fname = str(datetime.datetime.now()
                    ).replace(' ', '_').replace(":", "-").split('.')[0]+"\\"
        scripts_path = os.path.join(os.path.dirname(bpy.data.filepath),
                                    "scripts\\")
        buckups_path = os.path.join(scripts_path, ".BuckUp\\")
        buckup_path = os.path.join(buckups_path, fname)
        os.mkdir(scripts_path) if not os.path.exists(scripts_path) else None
        os.mkdir(buckups_path) if not os.path.exists(buckups_path) else None
        os.mkdir(buckup_path) if not os.path.exists(buckup_path) else None
        for text in bpy.data.texts:
            name = text.name
            if name.endswith(".py"):
                with open(os.path.join(buckup_path, name), "w", encoding="utf-8") as file:
                    file.write(pull_text(name))
        return {'FINISHED'}


class DeleteFiles(bpy.types.Operator):
    """Delete all files"""
    bl_idname = "texts.delete_files"
    bl_label = "CodeSync > Delete all files"

    def execute(self, context):
        scripts_path = os.path.dirname(bpy.data.filepath)+"\\scripts\\"
        os.mkdir(scripts_path) if not os.path.exists(scripts_path) else None
        for file in os.listdir(scripts_path):
            if (os.path.isfile(os.path.join(scripts_path, file)) and
                    file.endswith(".py")):
                os.remove(os.path.join(scripts_path, file))
        return {'FINISHED'}


class DeleteTexts(bpy.types.Operator):
    """Delete all texts"""
    bl_idname = "texts.delete_all"
    bl_label = "CodeSync > Delete all texts"

    def execute(self, context):
        for text in bpy.data.texts:
            if text.name.endswith(".py"):
                delete_text(text.name)
        return {'FINISHED'}
