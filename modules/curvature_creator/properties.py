import math

import bpy


class CurvePointInfo(bpy.types.PropertyGroup):
    distance: bpy.props.FloatProperty(name='Distance', soft_min=.1 / 1000, soft_max=50 / 1000, subtype='DISTANCE')
    angle: bpy.props.FloatProperty(name='Angle', soft_max=math.pi / 2, soft_min=-math.pi / 2, subtype='ANGLE')


def update_curve_radius(self, context: bpy.types.Context):
    if bpy.context.object is None or not isinstance(bpy.context.object.data, bpy.types.Curve):
        return
    curve_data = bpy.context.object.data
    curve_data.bevel_depth = context.scene.zenu_active_curve_bevel


def init_properties():
    divide = 1000

    bpy.types.Scene.zenu_curve_point_b = bpy.props.PointerProperty(type=CurvePointInfo)
    bpy.types.Scene.zenu_curve_point_c = bpy.props.PointerProperty(type=CurvePointInfo)
    bpy.types.Scene.zenu_curve_height = bpy.props.FloatProperty(name='Y', soft_min=.01, soft_max=.05,
                                                                subtype='DISTANCE')

    bpy.types.Scene.zenu_circle_radius = bpy.props.FloatProperty(name='Circle Radius', soft_min=.01 / divide,
                                                                 soft_max=.05 / divide,
                                                                 subtype='DISTANCE', default=.01)
    bpy.types.Scene.zenu_curve_comb_steps = bpy.props.IntProperty(name='Comb Steps', min=1, soft_max=100, default=50)

    bpy.types.Scene.zenu_curve_comb_scale = bpy.props.FloatProperty(name='Comb Scale', min=.002 / divide,
                                                                    soft_max=.03 / divide,
                                                                    subtype='DISTANCE', default=.00005)

    bpy.types.Scene.zenu_curve_comb_show = bpy.props.BoolProperty(name='Comb Show', default=False)

    bpy.types.Scene.zenu_active_curve_bevel = bpy.props.FloatProperty(name='Curve Radius', soft_min=.1 / divide,
                                                                      soft_max=10 / divide, update=update_curve_radius,
                                                                      subtype='DISTANCE')

    bpy.types.Scene.zenu_import_export_path = bpy.props.StringProperty(name='File Path', subtype='FILE_PATH')
    bpy.types.Scene.zenu_pruett_radius = bpy.props.FloatProperty(name='Pruett Radius',
                                                                 soft_min=.1 / divide, soft_max=50 / divide, default=5 / divide,
                                                                 subtype='DISTANCE')
    bpy.types.Scene.zenu_pruett_radius_show = bpy.props.BoolProperty(name='Pruett Radius Show', default=True)
    bpy.types.Scene.zenu_comb_circle_show = bpy.props.BoolProperty(name='Comb Circle', default=False)


classes = (
    CurvePointInfo,
)
