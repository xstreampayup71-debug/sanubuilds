def handle(user):
    if "image" in user or "photo" in user or "banner" in user:
        return "Okk babu 😎 image/banner ke liye pehle prompt do, jaise: modern business banner blue color me."

    return None