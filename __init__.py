# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy
from . code_sync import (SyncFromDevice, SyncToDevice, DeleteTexts,
                         DeleteFiles, BackUpScripts)
from . live_sync import StartLiveSync, StopLiveSync
from . sync_panel import SyncPanel


bl_info = {
    "name": "CodeSync",
    "description": "Script sync tools for blender and upbge.",
    "author": "rynpix(rayane866)",
    "version": (0, 0, 1),
    "blender": (2, 91, 0),
    "location": "Texts",  # idk exactly ¯\_(ツ)_/¯
    "warning": "",
    "wiki_url": "",
    "tracker_url": "https://github.com/rynpix/codesync/issues",
    "support": "COMMUNITY",
    "category": "Text Editor"
}


classes = {SyncFromDevice, SyncToDevice, DeleteTexts, DeleteFiles,
           BackUpScripts, SyncPanel, StartLiveSync, StopLiveSync}


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
