# plugins/geometry.py

import re
import math

def handle(user):
    u = user.lower()

    nums = list(map(float, re.findall(r'\d+\.?\d*', u)))

    # ====================================
    # AREA OF CIRCLE
    # ====================================
    if "circle" in u and "area" in u:
        if len(nums) < 1:
            return "❌ Radius missing."

        r = nums[0]
        area = math.pi * r * r

        return (
            f"📐 GEOMETRY RESULT\n"
            f"────────────────────\n"
            f"Shape: Circle\n"
            f"Radius: {r}\n"
            f"Formula: πr²\n"
            f"Answer: {area:.2f}\n"
            f"────────────────────\n"
            f"✔ Area of circle = {area:.2f}"
        )

    # ====================================
    # CIRCLE PERIMETER
    # ====================================
    if "circle" in u and "perimeter" in u:
        if len(nums) < 1:
            return "❌ Radius missing."

        r = nums[0]
        peri = 2 * math.pi * r

        return (
            f"📐 GEOMETRY RESULT\n"
            f"────────────────────\n"
            f"Shape: Circle\n"
            f"Radius: {r}\n"
            f"Formula: 2πr\n"
            f"Answer: {peri:.2f}\n"
            f"────────────────────\n"
            f"✔ Perimeter = {peri:.2f}"
        )

    # ====================================
    # RECTANGLE AREA
    # ====================================
    if "rectangle" in u and "area" in u:
        if len(nums) < 2:
            return "❌ Length aur width dono chahiye."

        l, w = nums[0], nums[1]
        area = l * w

        return (
            f"📐 GEOMETRY RESULT\n"
            f"────────────────────\n"
            f"Shape: Rectangle\n"
            f"Length: {l}\n"
            f"Width: {w}\n"
            f"Formula: l × w\n"
            f"Answer: {area}\n"
            f"────────────────────\n"
            f"✔ Area = {area}"
        )

    # ====================================
    # RECTANGLE PERIMETER
    # ====================================
    if "rectangle" in u and "perimeter" in u:
        if len(nums) < 2:
            return "❌ Length aur width dono chahiye."

        l, w = nums[0], nums[1]
        peri = 2 * (l + w)

        return (
            f"📐 GEOMETRY RESULT\n"
            f"────────────────────\n"
            f"Shape: Rectangle\n"
            f"Length: {l}\n"
            f"Width: {w}\n"
            f"Formula: 2(l+w)\n"
            f"Answer: {peri}\n"
            f"────────────────────\n"
            f"✔ Perimeter = {peri}"
        )

    # ====================================
    # TRIANGLE AREA
    # ====================================
    if "triangle" in u and "area" in u:
        if len(nums) < 2:
            return "❌ Base aur height chahiye."

        b, h = nums[0], nums[1]
        area = 0.5 * b * h

        return (
            f"📐 GEOMETRY RESULT\n"
            f"────────────────────\n"
            f"Shape: Triangle\n"
            f"Base: {b}\n"
            f"Height: {h}\n"
            f"Formula: ½ × b × h\n"
            f"Answer: {area}\n"
            f"────────────────────\n"
            f"✔ Area = {area}"
        )

    return None
