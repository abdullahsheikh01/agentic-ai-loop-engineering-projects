"""36 pytest tests describing the expected (correct) behaviour of the game.

These tests encode the specification. They are written against the FIXED
behaviour, so several currently fail against the buggy number_guess.py - fix
the bugs in number_guess.py until every test here passes.
"""

import pytest

from number_guess import NumberGuessingGame


# --- basic guess results ----------------------------------------------------

def test_guess_correct_returns_correct():
    game = NumberGuessingGame(answer=5)
    assert game.guess(5) == "correct"


def test_guess_correct_sets_won():
    game = NumberGuessingGame(answer=5)
    game.guess(5)
    assert game.is_won() is True


def test_guess_too_high():
    game = NumberGuessingGame(answer=5)
    assert game.guess(7) == "too high"


def test_guess_too_low():
    game = NumberGuessingGame(answer=5)
    assert game.guess(3) == "too low"


def test_guess_out_of_range_high():
    game = NumberGuessingGame(answer=5)
    assert game.guess(11) == "out of range"


def test_guess_out_of_range_low():
    game = NumberGuessingGame(answer=5)
    assert game.guess(0) == "out of range"


def test_guess_out_of_range_negative():
    game = NumberGuessingGame(answer=5)
    assert game.guess(-5) == "out of range"


def test_guess_invalid_non_integer():
    game = NumberGuessingGame(answer=5)
    assert game.guess("x") == "invalid"


# --- attempt accounting ------------------------------------------------------

def test_out_of_range_guess_does_not_count_attempt():
    game = NumberGuessingGame(answer=5)
    game.guess(11)
    assert game.attempts_used() == 0


def test_invalid_guess_does_not_count_attempt():
    game = NumberGuessingGame(answer=5)
    game.guess("x")
    assert game.attempts_used() == 0


def test_out_of_range_guess_not_recorded():
    game = NumberGuessingGame(answer=5)
    game.guess(11)
    assert game.guesses_made() == []


def test_correct_guess_is_recorded():
    game = NumberGuessingGame(answer=5)
    game.guess(5)
    assert game.guesses_made() == [5]


def test_attempt_increments_on_guess():
    game = NumberGuessingGame(answer=5)
    game.guess(7)
    assert game.attempts_used() == 1


def test_attempts_used_zero_initial():
    assert NumberGuessingGame(answer=5).attempts_used() == 0


def test_remaining_attempts_initial():
    assert NumberGuessingGame(answer=5).remaining_attempts() == 3


def test_remaining_attempts_after_guess():
    game = NumberGuessingGame(answer=5)
    game.guess(7)
    assert game.remaining_attempts() == 2


def test_remaining_attempts_zero_after_loss():
    game = NumberGuessingGame(answer=5)
    game.guess(1)
    game.guess(2)
    game.guess(3)
    assert game.remaining_attempts() == 0


# --- game over ---------------------------------------------------------------

def test_game_over_true_after_win():
    game = NumberGuessingGame(answer=5)
    game.guess(5)
    assert game.is_game_over() is True


def test_game_over_true_after_attempts_exhausted():
    game = NumberGuessingGame(answer=5)
    game.guess(1)
    game.guess(2)
    game.guess(3)
    assert game.is_game_over() is True


def test_game_over_false_early():
    assert NumberGuessingGame(answer=5).is_game_over() is False


def test_guess_returns_game_over_after_loss():
    game = NumberGuessingGame(answer=5)
    game.guess(1)
    game.guess(2)
    game.guess(3)
    assert game.guess(5) == "game over"


def test_guess_returns_game_over_after_win():
    game = NumberGuessingGame(answer=5)
    game.guess(5)
    assert game.guess(3) == "game over"


# --- guesses history ---------------------------------------------------------

def test_last_guess_none_initial():
    assert NumberGuessingGame(answer=5).last_guess() is None


def test_last_guess_after_wrong_guess():
    game = NumberGuessingGame(answer=5)
    game.guess(7)
    assert game.last_guess() == 7


def test_last_guess_after_correct_guess():
    game = NumberGuessingGame(answer=5)
    game.guess(5)
    assert game.last_guess() == 5


def test_guesses_made_sequence():
    game = NumberGuessingGame(answer=5)
    game.guess(7)
    game.guess(3)
    game.guess(8)
    assert game.guesses_made() == [7, 3, 8]


# --- boundaries and flows ----------------------------------------------------

def test_boundary_guess_one_is_valid():
    game = NumberGuessingGame(answer=5)
    assert game.guess(1) != "out of range"


def test_boundary_guess_ten_is_valid():
    game = NumberGuessingGame(answer=5)
    assert game.guess(10) == "too high"


def test_win_within_attempt_limit():
    game = NumberGuessingGame(answer=5)
    game.guess(7)
    game.guess(3)
    assert game.guess(5) == "correct"


def test_attempts_used_after_win():
    game = NumberGuessingGame(answer=5)
    game.guess(7)
    game.guess(5)
    assert game.attempts_used() == 2


def test_remaining_after_win():
    game = NumberGuessingGame(answer=5)
    game.guess(7)
    game.guess(5)
    assert game.remaining_attempts() == 1


def test_hint_returns_answer():
    assert NumberGuessingGame(answer=5).hint() == 5


# --- reset -------------------------------------------------------------------

def test_reset_clears_attempts():
    game = NumberGuessingGame(answer=5)
    game.guess(7)
    game.reset()
    assert game.attempts_used() == 0


def test_reset_clears_guesses():
    game = NumberGuessingGame(answer=5)
    game.guess(7)
    game.reset()
    assert game.guesses_made() == []


def test_reset_clears_won():
    game = NumberGuessingGame(answer=5)
    game.guess(5)
    game.reset()
    assert game.is_won() is False


def test_reset_changes_answer():
    game = NumberGuessingGame(answer=5)
    game.reset(answer=8)
    assert game.hint() == 8
    assert game.guess(8) == "correct"