import sys
from pathlib import Path

# Make sure the project root is on sys.path so imports work when pytest runs
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from logic_utils import check_guess


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


def test_string_secret_hint_correctness():
    """Regression test: when the secret is stored as a string (e.g. '2'), a
    large numeric guess like 50 must be classified as Too High (user should be
    instructed to go lower). This checks the bug reported in the reflection.
    """
    result = check_guess(50, "2")
    assert result == "Too High"
