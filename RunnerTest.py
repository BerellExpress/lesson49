import main
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = main.Runner("Walker")
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = main.Runner("Rooney")
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = main.Runner("Alice")
        runner2 = main.Runner("Totoshka")
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertEqual(runner1.distance, runner2.distance)

if __name__ == "__main__":
    main
