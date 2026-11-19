"""公差測試片：用來量印表機的真實偏差。

印出來後用游標卡尺量：
  1. 外尺寸 80 x 20 x 5 mm：實測值 - 設計值 = 外尺寸偏差
  2. 6 個孔，名義直徑由左到右 3.0 / 3.2 / 3.4 / 3.6 / 3.8 / 4.0 mm：
     用鑽頭或螺絲試插，找出 M3 螺絲剛好能順利穿過的最小孔，
     該孔的名義直徑 - 3.0 = 孔偏差，寫回 params.PRINTERS 的 hole_offset

這個零件刻意**不套用**孔徑補償，因為它的目的就是量出補償值。
"""
import cadquery as cq

LENGTH = 80.0
WIDTH = 20.0
THICKNESS = 5.0
HOLE_DIAMETERS = [3.0, 3.2, 3.4, 3.6, 3.8, 4.0]
FIRST_HOLE_X = 10.0   # 第一個孔距左端
HOLE_PITCH = 12.0     # 孔間距


def make():
    body = cq.Workplane("XY").box(LENGTH, WIDTH, THICKNESS)
    for i, d in enumerate(HOLE_DIAMETERS):
        x = -LENGTH / 2 + FIRST_HOLE_X + i * HOLE_PITCH
        cutter = (
            cq.Workplane("XY")
            .workplane(offset=-THICKNESS / 2)
            .center(x, 0)
            .circle(d / 2)
            .extrude(THICKNESS)
        )
        body = body.cut(cutter)
    return body
