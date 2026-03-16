def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    #FIX: Implemented range mapping with AI-assisted refactor
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    #FIX: Parsing logic moved from app.py to logic_utils.py in pair-programming session
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # Normalize secret to int when possible (the app sometimes stores it as a str)
    #FIX: Normalization logic implemented with AI guidance to handle string secrets
    try:
        secret_int = int(secret)
    except Exception:
        # Fall back to string comparison if secret isn't numeric
        g = str(guess)
        if g == str(secret):
            return "Win"
        if g > str(secret):
            return "Too High"
        return "Too Low"

    # Numeric comparison
    if guess == secret_int:
        return "Win"
    if guess > secret_int:
        return "Too High"
    return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    #FIX: Scoring logic ported from app.py as part of the refactor with AI
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
