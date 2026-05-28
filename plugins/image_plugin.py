# image_plugin.py
# Advanced Image Plugin with history.json 😎🔥

import json
import random
from datetime import datetime


class AdvancedImagePlugin:

    def __init__(self):

        self.name = "Babu Image AI"
        self.version = "4.0"

        self.history_file = "history.json"

        self.styles = [
            "anime",
            "realistic",
            "cyberpunk",
            "cinematic",
            "fantasy",
            "3d"
        ]

        self.replies = [
            "🎨 Image system ready babu.",
            "🔥 AI image prompt generated.",
            "⚡ Creative engine activated.",
            "🖼️ Banner mode ON babu."
        ]

    # -----------------------------------
    # Detect Image Request
    # -----------------------------------
    def detect_request(self, user):

        triggers = [
            "image",
            "photo",
            "poster",
            "banner",
            "wallpaper",
            "thumbnail",
            "logo"
        ]

        user = user.lower()

        for word in triggers:
            if word in user:
                return True

        return False

    # -----------------------------------
    # Detect Style
    # -----------------------------------
    def detect_style(self, user):

        user = user.lower()

        for style in self.styles:
            if style in user:
                return style

        return "realistic"

    # -----------------------------------
    # Build Smart Prompt
    # -----------------------------------
    def build_prompt(self, user):

        style = self.detect_style(user)

        prompt = (
            f"{user}, "
            f"ultra detailed, "
            f"{style} style, "
            f"cinematic lighting, "
            f"8k quality, "
            f"sharp focus"
        )

        return prompt, style

    # -----------------------------------
    # Save History
    # -----------------------------------
    def save_history(self, user, prompt, style):

        data = {
            "user_input": user,
            "generated_prompt": prompt,
            "style": style,
            "time": str(datetime.now())
        }

        try:

            with open(self.history_file, "r") as file:
                history = json.load(file)

        except:
            history = []

        history.append(data)

        with open(self.history_file, "w") as file:
            json.dump(history, file, indent=4)

    # -----------------------------------
    # Show History
    # -----------------------------------
    def show_history(self):

        try:

            with open(self.history_file, "r") as file:
                history = json.load(file)

            return json.dumps(history, indent=4)

        except:
            return "❌ No history found babu."

    # -----------------------------------
    # Main Handler
    # -----------------------------------
    def handle(self, user):

        user = user.lower()

        # Show history command
        if user == "history":
            return self.show_history()

        # Detect image request
        if not self.detect_request(user):
            return "❌ Image request detect nahi hua."

        # Build AI prompt
        prompt, style = self.build_prompt(user)

        # Save history
        self.save_history(user, prompt, style)

        # Final response
        response = {
            "status": "success",
            "message": random.choice(self.replies),
            "style": style,
            "generated_prompt": prompt
        }

        return json.dumps(response, indent=4)


# -----------------------------------
# Run Plugin
# -----------------------------------

if __name__ == "__main__":

    ai = AdvancedImagePlugin()

    while True:

        user = input("Tum: ")

        if user.lower() in ["exit", "quit"]:
            print("👋 Bye babu.")
            break

        result = ai.handle(user)

        print(result)