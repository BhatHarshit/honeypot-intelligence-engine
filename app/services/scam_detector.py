

scam_keywords = [
    "send money", "kyc", "upi", "account", "prize", "winner", "transfer",
    "gift card", "loan", "urgent", "click here"
]

def is_scam(message: str) -> dict:
    """
    Determines if a message is a scam.

    Args:
        message (str): Incoming message text.

    Returns:
        dict: scam_detected (bool) and confidence (0-1)
    """
    message_lower = message.lower()
    score = sum(word in message_lower for word in scam_keywords) / len(scam_keywords)
    scam_detected = score > 0.2  # threshold
    return {
        "scam_detected": scam_detected,
        "confidence": round(score, 2)
    }

# Optional local test
if __name__ == "__main__":
    test_messages = [
        "Send me ₹5000 via UPI immediately",
        "Hello friend, how are you?",
        "Congratulations! You won a prize, click here"
    ]
    
    for msg in test_messages:
        print(msg, "=>", is_scam(msg))
