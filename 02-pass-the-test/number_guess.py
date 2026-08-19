"""A Number Guessing Game (1-10).

Runs WITHOUT any user input - guesses are made programmatically in main()
to demonstrate the NumberGuessingGame class.

BUGS: This file intentionally contains bugs. Find them and fix them so that
all 36 tests in test_number_guess.py pass.
"""

import random


class NumberGuessingGame:
    """Guess a secret number between 1 and 10 within a limited attempt count."""

    def __init__(self, answer=None, max_attempts=3):
        if answer is None:
            self.answer = random.randint(1, 10)
        else:
            self.answer = answer
        self.max_attempts = max_attempts
        self.attempts = 0
        self.guesses = []
        self.won = False

    def guess(self, number):
        """Submit a guess.

        Returns one of:
          "correct", "too high", "too low", "out of range",
          "invalid" (non-integer), "game over".
        A "game over" result is returned whenever the game is already over.
        Out-of-range guesses are rejected and do NOT count as attempts.
        """
        if self.is_game_over():
            return "game over"
        if not isinstance(number, int):
            return "invalid"
        if number < 1 or number > 10:
            return "out of range"
        self.attempts += 1
        self.guesses.append(number)
        if number == self.answer:
            self.won = True
            return "correct"
        if number > self.answer:
            return "too high"
        return "too low"

    def is_won(self):
        """True once the secret number has been guessed."""
        return self.won

    def is_game_over(self):
        """True after a win OR once attempts are exhausted."""
        return self.won or self.attempts >= self.max_attempts

    def attempts_used(self):
        """Number of counted (in-range) guesses so far."""
        return self.attempts

    def remaining_attempts(self):
        """Number of guesses still allowed."""
        return self.max_attempts - self.attempts

    def guesses_made(self):
        """All counted guesses, in order."""
        return self.guesses

    def last_guess(self):
        """The most recent counted guess, or None if none yet."""
        if self.guesses:
            return self.guesses[-1]
        return None

    def hint(self):
        """The secret number."""
        return self.answer

    def reset(self, answer=None):
        """Start a fresh game (optionally with a new secret number)."""
        self.attempts = 0
        self.guesses = []
        self.won = False
        if answer is not None:
            self.answer = answer


def main():
    game = NumberGuessingGame(answer=7)
    for guess in (3, 9, 7):
        print(f"Guess {guess}: {game.guess(guess)}")
    print("Won:", game.is_won())
    print("Attempts used:", game.attempts_used())


if __name__ == "__main__":
    main()