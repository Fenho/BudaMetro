import unittest

from main import make_network, get_shortest
from io_handler import network_processer

def test_helper(network_descriptor, start, end, color):
    nodes = network_processer(network_descriptor)
    network = make_network(nodes, color)
    return get_shortest(network, start, end)

class TestShortest(unittest.TestCase):
    def test_task_example_no_color(self):
        network_descriptor = "./Networks/first_example.csv"
        start, end = "A", "F"
        color = ""
        visited_str = test_helper(network_descriptor, start, end, color)
        self.assertEqual(visited_str, "A->B->C->D->E->F")

    def test_task_example_red(self):
        network_descriptor = "./Networks/first_example.csv"
        start, end = "A", "F"
        color = "red"
        visited_str = test_helper(network_descriptor, start, end, color)
        self.assertEqual(visited_str, "A->B->C->H->F")

    def test_task_example_green(self):
        network_descriptor = "./Networks/first_example.csv"
        start, end = "A", "F"
        color = "green"
        visited_str = test_helper(network_descriptor, start, end, color)
        posible_answers = ["A->B->C->D->E->F", "A->B->C->G->I->F"]
        self.assertIn(visited_str, posible_answers)

    def test_second_middle(self):
        network_descriptor = "./Networks/second_example.csv"
        start, end = "A", "I"
        color = ""
        visited_str = test_helper(network_descriptor, start, end, color)
        posible_answers = ["A->B->C->F->I", "A->B->G->H->I"]
        self.assertIn(visited_str, posible_answers)

    def test_second_three_connections(self):
        network_descriptor = "./Networks/second_example.csv"
        start, end = "A", "E"
        color = "green"
        visited_str = test_helper(network_descriptor, start, end, color)
        posible_answers = ["A->B->D->E", "A->B->F->E"]
        self.assertIn(visited_str, posible_answers)

    def test_second_three_connections(self):
        network_descriptor = "./Networks/second_example.csv"
        start, end = "A", "I"
        color = "green"
        visited_str = test_helper(network_descriptor, start, end, color)
        self.assertEqual(visited_str, "A->B->F->I")

    def test_second_red(self):
        network_descriptor = "./Networks/second_example.csv"
        start, end = "A", "I"
        color = "red"
        visited_str = test_helper(network_descriptor, start, end, color)
        self.assertEqual(visited_str, "A->C->I")

if __name__ == '__main__':
    unittest.main()


