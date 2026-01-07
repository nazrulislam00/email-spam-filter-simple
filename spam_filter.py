spam_keywords = ["win", "free", "prize", "money", "offer"]

def is_spam(message):
    message = message.lower()
    for word in spam_keywords:
        if word in message:
            return True
    return False

if __name__ == "__main__":
    email = input("Enter email text: ")

    if is_spam(email):
        print("Spam email detected")
    else:
        print("Not spam")
