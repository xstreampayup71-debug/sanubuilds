# plugins/formulas.py

def handle(user):
    u = user.lower()

    formulas = {
        "pythagoras": "a² + b² = c²",
        "area of circle": "πr²",
        "perimeter of circle": "2πr",
        "rectangle area": "l × w",
        "simple interest": "(P × R × T)/100",
        "speed": "distance / time",
        "density": "mass / volume",
        "force": "mass × acceleration",
        "percentage": "(value / total) × 100"
    }

    for key, value in formulas.items():
        if key in u:
            return (
                f"📘 FORMULA KNOWLEDGE\n"
                f"────────────────────\n"
                f"Topic: {key.title()}\n"
                f"Formula: {value}\n"
                f"────────────────────\n"
                f"✔ Formula loaded successfully"
            )

    return None