import random

# added for testing convenience, but also useful for code organization.
# added the initialization of the score and status fields to ensure they are refreshed accordingly when starting a new game.
def new_game_state(low: int, high: int):
    """Return a fresh game state dict for starting a new game."""
    return {
        "attempts": 0,
        "score": 0,
        "history": [],
        "secret": random.randint(low, high),
        "status": "playing",
    }

# Switched the 'noraml' and 'difficulty' level ranges to match the difficulty selection expected.
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 50


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
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

# inversing the hint messages to display the correct hint based on the guess being too high or too low.
def check_guess(guess, secret):
    """
    Compare guess to secret and return the outcome string.

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win"

    if guess > secret:
        return "Too High"

    return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    # changed score calculation logic, to ensure winning on first try gives 100 points,
    # removed the parity logic since it wasn't a logical metric to use for calculating scores based on attempts used.
    if outcome == "Win":
        points = 100 - 10 * (attempt_number - 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
