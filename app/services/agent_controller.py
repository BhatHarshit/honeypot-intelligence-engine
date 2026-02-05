# app/services/agent_controller.py

def next_agent_message(state: dict, scam_detected: bool) -> (str, dict):
    """
    Decide next message of the agent and update conversation state.

    Args:
        state (dict): Contains 'turn_count' and other info
        scam_detected (bool): Result from scam detection

    Returns:
        Tuple[str, dict]: agent response, updated state
    """
    turn = state.get("turn_count", 0) + 1

    if not scam_detected:
        response = "Thank you for your message."
    else:
        # Simple persona for first few turns
        if turn == 1:
            response = "I am not very good with apps, can you guide me?"
        elif turn == 2:
            response = "Could you please explain step by step?"
        else:
            response = "I will ask my friend to help, thanks!"

    state["turn_count"] = turn
    return response, state

# Optional local test
if __name__ == "__main__":
    conv_state = {}
    messages = [
        "Send me ₹5000 via UPI immediately",
        "Click here to claim your prize",
        "Hello"
    ]
    from scam_detector import is_scam
    for msg in messages:
        scam_info = is_scam(msg)
        resp, conv_state = next_agent_message(conv_state, scam_info["scam_detected"])
        print(f"Message: {msg}")
        print(f"Agent Response: {resp}")
        print(f"State: {conv_state}\n")
