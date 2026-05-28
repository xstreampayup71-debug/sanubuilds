# plugins/vedic_math.py

import re

def handle(user):
    u = user.lower()

    nums = list(map(int, re.findall(r'\d+', u)))

    if len(nums) < 1:
        return None

    # ====================================
    # SQUARE
    # ====================================
    if "square" in u:
        n = nums[0]
        result = n * n

        return (
            f"⚡ VEDIC MATH RESULT\n"
            f"────────────────────\n"
            f"Number: {n}\n"
            f"Formula: n²\n"
            f"Answer: {result}\n"
            f"────────────────────\n"
            f"✔ {n}² = {result}"
        )

    # ====================================
    # CUBE
    # ====================================
    if "cube" in u:
        n = nums[0]
        result = n * n * n

        return (
            f"⚡ VEDIC MATH RESULT\n"
            f"────────────────────\n"
            f"Number: {n}\n"
            f"Formula: n³\n"
            f"Answer: {result}\n"
            f"────────────────────\n"
            f"✔ {n}³ = {result}"
        )

    # ====================================
    # PERCENTAGE
    # ====================================
    if "percent" in u or "%" in u:
        if len(nums) < 2:
            return "❌ Do numbers chahiye."

        a, b = nums[0], nums[1]

        result = (a / b) * 100

        return (
            f"⚡ PERCENTAGE RESULT\n"
            f"────────────────────\n"
            f"Formula: (a/b) × 100\n"
            f"Calculation: ({a}/{b}) × 100\n"
            f"Answer: {result:.2f}%\n"
            f"────────────────────\n"
            f"✔ Percentage = {result:.2f}%"
        )

    return None