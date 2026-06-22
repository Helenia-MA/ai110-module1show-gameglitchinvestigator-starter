import pytest

from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    new_game_state,
    update_score,
)

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_win_on_first_attempt_awards_full_points():
    # First-attempt win earns the full 100 points: 100 - 10 * (1 - 1)
    result = update_score(current_score=0, outcome="Win", attempt_number=1)
    assert result == 100


def test_win_points_decay_per_attempt():
    # Each later attempt costs 10 points: attempt 5 -> 100 - 10 * 4 = 60
    result = update_score(current_score=0, outcome="Win", attempt_number=5)
    assert result == 60


def test_win_points_never_drop_below_floor():
    # A very late win is floored at 10 points, not 0 or negative
    result = update_score(current_score=0, outcome="Win", attempt_number=20)
    assert result == 10


def test_win_adds_to_existing_score():
    # Points are added to the current score, not replacing it
    result = update_score(current_score=50, outcome="Win", attempt_number=1)
    assert result == 150


def test_too_high_subtracts_five():
    # A "Too High" guess penalizes 5 points
    result = update_score(current_score=20, outcome="Too High", attempt_number=3)
    assert result == 15


def test_too_low_subtracts_five():
    # A "Too Low" guess penalizes 5 points
    result = update_score(current_score=20, outcome="Too Low", attempt_number=3)
    assert result == 15


def test_unknown_outcome_leaves_score_unchanged():
    # An unrecognized outcome should not alter the score
    result = update_score(current_score=42, outcome="Mystery", attempt_number=2)
    assert result == 42


# --- get_range_for_difficulty ---

@pytest.mark.parametrize(
    "difficulty, expected",
    [
        ("Easy", (1, 20)),
        ("Normal", (1, 50)),
        ("Hard", (1, 100)),
    ],
)
def test_known_difficulties_return_expected_range(difficulty, expected):
    # Each named difficulty maps to its documented inclusive range
    assert get_range_for_difficulty(difficulty) == expected


def test_unknown_difficulty_falls_back_to_normal():
    # An unrecognized difficulty should default to the Normal range
    assert get_range_for_difficulty("Impossible") == (1, 50)


def test_difficulty_lookup_is_case_sensitive():
    # Lowercase input is not a known key, so it falls back to the default
    assert get_range_for_difficulty("easy") == (1, 50)


# --- new_game_state (starting a new game) ---

def test_new_game_resets_all_progress_fields():
    # A fresh game zeroes attempts/score and clears history
    state = new_game_state(1, 50)
    assert state["attempts"] == 0
    assert state["score"] == 0
    assert state["history"] == []


def test_new_game_status_is_playing():
    # Status must reset to "playing" so a finished game is playable again
    # (this is the bug the New Game button was failing to fix)
    state = new_game_state(1, 50)
    assert state["status"] == "playing"


def test_new_game_contains_exactly_the_expected_keys():
    # Guards against missing/extra session fields when starting a new game
    state = new_game_state(1, 50)
    assert set(state) == {"attempts", "score", "history", "secret", "status"}


@pytest.mark.parametrize("difficulty", ["Easy", "Normal", "Hard"])
def test_new_game_secret_is_within_difficulty_range(difficulty):
    # The secret must fall inside the difficulty's inclusive range
    low, high = get_range_for_difficulty(difficulty)
    # Run several times since the secret is random
    for _ in range(100):
        secret = new_game_state(low, high)["secret"]
        assert low <= secret <= high


def test_new_game_history_is_a_fresh_list_each_call():
    # Each new game must get its own history list, not a shared reference
    first = new_game_state(1, 50)
    first["history"].append("guess")
    second = new_game_state(1, 50)
    assert second["history"] == []
