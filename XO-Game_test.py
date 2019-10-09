import unittest
import unittest.mock
from XO_game import Game

class TestGame(unittest.TestCase):
    def test_result(self):
        testing_game = Game()
        testing_game.put(0,"X")
        testing_game.put(1,"X")
        testing_game.put(2,"X")
        self.assertEqual(testing_game.result(), "X-player wins")
    def test_put(self):
        testing_game = Game()
        testing_game.put(0, "X")
        self.assertEqual(testing_game.cells[0], "X")
    def test_ask(self):
        with unittest.mock.patch('builtins.input', return_value='0'):
            testing_game = Game()
            testing_game.ask("X")
            self.assertEqual(testing_game.cells[0], "X")

if __name__ == '__main__':
    unittest.main()

