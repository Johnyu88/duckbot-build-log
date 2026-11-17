"""建置所有零件：檢查外框尺寸、估重、匯出 STL/STEP。

用法：cd hardware/cad && python build.py
"""
import sys

from common import bbox, export, mass_g
from parts import tolerance_coupon

# 登記格式：名稱 -> (make 函式, 預期外框尺寸 (x, y, z), 容許誤差 mm)
PARTS = {
    "tolerance_coupon": (tolerance_coupon.make, (80.0, 20.0, 5.0), 0.01),
}


def main():
    failed = False
    for name, (make, expected, tol) in PARTS.items():
        shape = make()
        size = bbox(shape)
        ok = all(abs(a - b) <= tol for a, b in zip(size, expected))
        print(
            f"{name}: bbox={tuple(round(v, 2) for v in size)} "
            f"expected={expected} mass~{mass_g(shape):.2f} g "
            f"{'OK' if ok else 'FAIL'}"
        )
        if not ok:
            failed = True
            continue
        export(shape, name)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
