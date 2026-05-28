from flask import Flask, render_template, request, jsonify
import json
import random
import os
import importlib.util
from difflib import get_close_matches

from sympy import symbols, Eq, solve, integrate, diff, factor, expand, simplify
from sympy.parsing.sympy_parser import parse_expr

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FILE = os.path.join(BASE_DIR, "data.json")
CODE_FILE = os.path.join(BASE_DIR, "code_patterns.json")
PLUGIN_FOLDER = os.path.join(BASE_DIR, "plugins")


# =========================
# DATA HANDLING
# =========================

def load_json(file):
    if not os.path.exists(file):
        return {}
    with open(file, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(file, data):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_data():
    return load_json(DATA_FILE)


def save_data(data):
    save_json(DATA_FILE, data)


# =========================
# INTENT DETECTION (IMPORTANT)
# =========================

def detect_intent(user):
    u = user.lower()

    math_kw = ["+", "-", "*", "/", "=", "integrate", "derivative", "differentiate", "factor", "expand"]
    code_kw = ["code", "python", "flask", "html", "program", "function"]
    greet_kw = ["hi", "hello", "hey", "kaise ho"]
    qa_kw = ["what", "why", "how", "explain", "meaning"]

    if any(k in u for k in math_kw):
        return "math"

    if any(k in u for k in code_kw):
        return "code"

    if any(k in u for k in greet_kw):
        return "greet"

    if any(k in u for k in qa_kw):
        return "qa"

    return "chat"


# =========================
# PLUGINS
# =========================

def run_plugins(user):
    if not os.path.exists(PLUGIN_FOLDER):
        os.makedirs(PLUGIN_FOLDER)
        return None

    for file in os.listdir(PLUGIN_FOLDER):
        if file.endswith(".py"):
            path = os.path.join(PLUGIN_FOLDER, file)
            try:
                spec = importlib.util.spec_from_file_location(file[:-3], path)
                plugin = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(plugin)

                if hasattr(plugin, "handle"):
                    reply = plugin.handle(user)
                    if reply:
                        return reply
            except:
                continue

    return None


# =========================
# CODE PATTERN REPLY
# =========================

def code_reply(user):
    patterns = load_json(CODE_FILE)

    for item in patterns.values():
        for keyword in item.get("keywords", []):
            if keyword in user:
                return "Okk babu 😎\n\n" + item.get("code", "")

    return None


# =========================
# MATH ENGINE (IMPROVED)
# =========================

def solve_math(user):
    try:
        user = user.lower().replace("^", "**").strip()
        x = symbols('x')

        if "=" in user:
            left, right = user.split("=", 1)
            eq = Eq(parse_expr(left), parse_expr(right))
            return f"Answer: {solve(eq)}"

        if user.startswith("integrate"):
            expr = user.replace("integrate", "").strip()
            return f"Integration: {integrate(parse_expr(expr), x)}"

        if "derivative" in user or "differentiate" in user:
            expr = user.replace("derivative", "").replace("differentiate", "").strip()
            return f"Derivative: {diff(parse_expr(expr), x)}"

        if user.startswith("factor"):
            expr = user.replace("factor", "").strip()
            return f"Factor: {factor(parse_expr(expr))}"

        if user.startswith("expand"):
            expr = user.replace("expand", "").strip()
            return f"Expand: {expand(parse_expr(expr))}"

        return f" {simplify(parse_expr(user))}"

    except:
        return None


# =========================
# SMART AI BRAIN
# =========================

def smart_reply(user):
    u = user.lower()

    if "what" in u:
        return "Let me explain it simply. It depends on context, but I can break it down step by step if you want."

    if "how" in u:
        return "I'll guide you step by step. Tell me a bit more clearly what you're trying to do."

    if "why" in u:
        return "Good question. The reason depends on logic and context. Can you specify more?"

    if "meaning" in u:
        return "It refers to the core concept behind what you're asking."

    return "I understand your message, but I need a bit more detail to respond accurately."


# =========================
# FLASK ROUTES
# =========================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = load_data()
    user = request.json["message"].strip()

    intent = detect_intent(user)

    # plugin first (highest priority)
    plugin_answer = run_plugins(user)
    if plugin_answer:
        return jsonify({"reply": plugin_answer})

    # math engine
    if intent == "math":
        math_answer = solve_math(user)
        if math_answer:
            return jsonify({"reply": math_answer})

    # code engine
    if intent == "code":
        code_answer = code_reply(user)
        if code_answer:
            return jsonify({"reply": code_answer})

    # trained memory
    if user.lower() in data:
        return jsonify({"reply": data[user.lower()]})

    # fuzzy match
    matches = get_close_matches(user, data.keys(), n=1, cutoff=0.7)
    if matches:
        return jsonify({"reply": data[matches[0]]})

    # smart AI fallback
    return jsonify({"reply": smart_reply(user)})


# =========================
# TRAIN SYSTEM
# =========================

@app.route("/train", methods=["POST"])
def train():
    data = load_data()

    q = request.json["question"].lower().strip()
    a = request.json["answer"].strip()

    if not q or not a:
        return jsonify({"status": "error"})

    data[q] = a
    save_data(data)

    return jsonify({"status": "success"})


# =========================
# RUN APP
# =========================

if __name__ == "__main__":
    app.run(debug=True)