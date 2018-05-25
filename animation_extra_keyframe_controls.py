# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Extra Keyframe Controls",
    "author": "quollism",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "description": "Extra keyframing controls in Timeline to assist with animation and layout",
    "warning": "This may stop working with 2.8 API changes or it might stop being useful if someone puts the controls back. Works as of 25 May 2018.",
    "category": "Animation"
}

import bpy

def timeline_extra_controls(self, context):
    if context.space_data.mode == 'TIMELINE':
        layout = self.layout
        toolsettings = context.tool_settings
        scene = context.scene
        layout.separator()
        row = layout.row(align=True)
        row.prop(toolsettings, "use_keyframe_insert_auto", text="", toggle=True)
        if toolsettings.use_keyframe_insert_auto:
            row.prop(toolsettings, "use_keyframe_insert_keyingset", text="", toggle=True)
        row.prop_search(scene.keying_sets_all, "active", scene, "keying_sets_all", text="")
        row.operator("anim.keyframe_insert", text="", icon='KEY_HLT')
        row.operator("anim.keyframe_delete", text="", icon='KEY_DEHLT')
        layout.separator()
        row = layout.row(align=True)
        row.prop(context.user_preferences.edit, "keyframe_new_interpolation_type", text="", icon_only=True)
        layout.separator()
        row = layout.row(align=True)
        row.prop(toolsettings, "keyframe_type", text="", icon_only=True)

def register():
    bpy.types.TIME_HT_editor_buttons.append(timeline_extra_controls)

def unregister():
    bpy.types.TIME_HT_editor_buttons.remove(timeline_extra_controls)

if __name__ == "__main__":
    register()