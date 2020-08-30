import bpy


class SyncPanel(bpy.types.Panel):
    bl_idname = "panel.codesync_panel"
    bl_space_type = "TEXT_EDITOR"
    bl_region_type = "UI"
    bl_category = "Text"
    bl_label = "CodeSync"

    def draw(self, context):
        self.layout.label(text="Sync tools")
        self.layout.operator("texts.sync_to_device", icon="FILE_SCRIPT",
                             text="Sync to device")
        self.layout.operator("texts.sync_from_device", icon="FILE_SCRIPT",
                             text="Sync from device")
        self.layout.operator("texts.back_up", icon="FILE_BACKUP",
                             text="BackUp to device")
        self.layout.separator()
        self.layout.label(text="Live sync")
        lsrow = self.layout.row(align=True)
        lsrow.operator("texts.start_live_sync", icon="PASTEDOWN",
                       text="Start")
        lsrow.operator("texts.stop_live_sync", icon="PANEL_CLOSE",
                       text="Stop")
        self.layout.separator()
        self.layout.label(text="Delete scripts")
        self.layout.operator("texts.delete_files", icon="REMOVE",
                             text="Delete device files")
        self.layout.operator("texts.delete_all", icon="REMOVE",
                             text="Delete blender texts")
