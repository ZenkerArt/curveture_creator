import os

import bpy
from ...base_panel import BasePanel


class ZENU_OT_import_stl(bpy.types.Operator):
    bl_label = 'Import STL'
    bl_idname = 'zenu.import_stl'

    def execute(self, context: bpy.types.Context):
        path = bpy.path.abspath(context.scene.zenu_import_export_path)
        bpy.ops.import_mesh.stl(global_scale=.001, filepath=path)
        return {'FINISHED'}


class ZENU_OT_export_stl(bpy.types.Operator):
    bl_label = 'Export STL'
    bl_idname = 'zenu.export_stl'

    def execute(self, context: bpy.types.Context):
        path = bpy.path.abspath(os.path.splitext(context.scene.zenu_import_export_path)[0])
        bpy.ops.export_mesh.stl(global_scale=1000, filepath=path + '_exported.stl', check_existing=False)
        return {'FINISHED'}


class ZENU_PT_curvature_export_import(BasePanel):
    bl_label = 'Export Import'
    bl_parent_id = 'ZENU_PT_curvature_creator'

    def draw(self, context: bpy.types.Context):
        layout = self.layout
        col = layout.column_flow(align=True)
        col.prop(bpy.context.scene, 'zenu_import_export_path', text='')
        if bpy.context.scene.zenu_import_export_path:
            col.operator(ZENU_OT_import_stl.bl_idname)
            col.operator(ZENU_OT_export_stl.bl_idname)


classes = (
    ZENU_OT_import_stl,
    ZENU_OT_export_stl,
    ZENU_PT_curvature_export_import
)
