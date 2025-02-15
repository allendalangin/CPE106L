import unittest
import oxo_logic
import oxo_data

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = oxo_logic.newGame()

    def test_initial_board(self):
        """Test if the board initializes correctly."""
        self.assertEqual(self.game, [" "] * 9)

    def test_place_user_move(self):
        """Test if a user move is placed correctly."""
        oxo_logic.userMove(self.game, 0)
        self.assertEqual(self.game[0], "X")

    def test_invalid_move(self):
        """Test if an invalid move (occupied space) raises an error."""
        oxo_logic.userMove(self.game, 0)
        with self.assertRaises(ValueError):
            oxo_logic.userMove(self.game, 0)

    def test_computer_move(self):
        """Test if the computer places a move correctly."""
        result = oxo_logic.computerMove(self.game)
        self.assertIn(result, ["", "O", "D"])
        self.assertIn("O", self.game)

    def test_winner_detection(self):
        """Test if the game correctly detects a winner."""
        self.game = ["X", "X", "X", " ", " ", " ", " ", " ", " "]
        self.assertTrue(oxo_logic._isWinningMove(self.game))

    def test_no_winner(self):
        """Test if the game correctly identifies no winner."""
        self.game = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
        self.assertFalse(oxo_logic._isWinningMove(self.game))

    def test_save_and_restore_game(self):
        """Test if the game saves and restores correctly."""
        self.game = ["X", "O", "X", " ", "O", "X", "O", "X", "O"]
        oxo_logic.saveGame(self.game)
        restored_game = oxo_logic.restoreGame()
        self.assertEqual(self.game, restored_game)

if __name__ == "__main__":
    unittest.main()
