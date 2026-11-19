"""共用工具：孔徑補償、量測、匯出。"""
from pathlib import Path

import cadquery as cq

import params


def hole_d(nominal, printer=None):
    """名義孔徑 -> 設計孔徑（加上印表機的孔偏差補償）。"""
    printer = printer or params.DEFAULT_PRINTER
    return nominal + params.PRINTERS[printer]["hole_offset"]


def bbox(shape):
    """回傳外框尺寸 (x, y, z)。"""
    b = shape.val().BoundingBox()
    return (b.xlen, b.ylen, b.zlen)


def mass_g(shape, material="PLA"):
    """以密度估算重量（克），實心估算，實際會依填充率變輕。"""
    volume_mm3 = shape.val().Volume()
    return volume_mm3 / 1000.0 * params.DENSITY[material]


def export(shape, name, outdir="build"):
    """同時輸出 STL（列印）和 STEP（交換）。"""
    Path(outdir).mkdir(exist_ok=True)
    cq.exporters.export(shape, f"{outdir}/{name}.stl")
    cq.exporters.export(shape, f"{outdir}/{name}.step")
