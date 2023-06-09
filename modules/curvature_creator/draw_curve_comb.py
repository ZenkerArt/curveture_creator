from dataclasses import dataclass

import numpy as np

from mathutils import Vector
from . import Draw3D
from .bezier import Bezier
from .bezier_draw import bezier_draw
import bpy


@dataclass
class CurveComb:
    length: float = 0
    curvature: float = 0
    curvature_abs: float = 0
    point: Vector = Vector((0, 0, 0))
    radius: float = 0


def draw_curve_comb(spline: bpy.types.Spline, draw: Draw3D):
    points = spline.bezier_points

    comb = CurveComb()
    count = 0

    for index, i in enumerate(points):
        if index + 1 >= len(points):
            break
        p0 = i.co
        p1 = i.handle_right
        p2 = points[index + 1].handle_left
        p3 = points[index + 1].co
        curve = Bezier(*np.array((
            (p0[0], p0[2]),
            (p1[0], p1[2]),
            (p2[0], p2[2]),
            (p3[0], p3[2]),
        )))
        k, ka, c, max_point, max_radius = bezier_draw(curve, draw, scale=bpy.context.scene.zenu_curve_comb_scale,
                                          steps=bpy.context.scene.zenu_curve_comb_steps, draw_circle=index == 1)
        count += c
        comb.curvature += k
        comb.curvature_abs += ka
        if index == 1:
            comb.point = max_point
            comb.radius = max_radius * bpy.context.scene.zenu_curve_comb_scale


    comb.length = spline.calc_length()
    comb.curvature /= count
    comb.curvature_abs /= count
    return comb
