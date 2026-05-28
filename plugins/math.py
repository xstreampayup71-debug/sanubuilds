import re

def handle(user):
    u = user.lower()

    # ----------------------------
    # STEP 1: Extract all numbers
    # ----------------------------
    nums = list(map(int, re.findall(r'-?\d+', u)))

    if len(nums) < 2:
        return None

    # default take first two numbers
    a, b = nums[0], nums[1]

    # ----------------------------
    # STEP 2: Detect intent smartly
    # ----------------------------

    # SUBTRACTION (HIGH PRIORITY)
    if any(k in u for k in ["nikal", "bacha", "minus", "kharch", "spent", "left", "remaining"]):
        result = a - b
        return format_reply(a, b, "-", result, u)

    # DIVISION
    if any(k in u for k in ["divide", "bhag", "divide by"]):
        if b == 0:
            return "Error: Zero se divide nahi hota 😅"
        result = a / b
        return format_reply(a, b, "÷", result, u)

    # MULTIPLICATION
    if any(k in u for k in ["guna", "multiply", "times"]):
        result = a * b
        return format_reply(a, b, "×", result, u)

    # ADDITION
    if any(k in u for k in ["plus", "add", "sum", "kitna", "total"]):
        result = a + b
        return format_reply(a, b, "+", result, u)

    return None


# ----------------------------
# PROFESSIONAL OUTPUT FORMAT
# ----------------------------
def format_reply(a, b, op, result, user_text):
    return (
        f"🧮 Calculation Result\n"
        f"────────────────────\n"
        f"Input: {user_text}\n"
        f"Operation: {a} {op} {b}\n"
        f"Result: {result}\n"
        f"────────────────────\n"
        f"✔ Simple explanation: {a} {op} {b} = {result}"
    )