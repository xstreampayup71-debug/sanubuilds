def handle(user):
    words = user.lower().split()

    if "ai" in words or "chatgpt" in words or "smart" in words:
        return "Okk babu 😎 main AI mode me hoon. Tum jo puchoge uska answer apne training data se dunga."

    return None