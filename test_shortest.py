import unittest

from main import make_network, get_shortest
from io_handler import network_processer

class TestShortest(unittest.TestCase):
    def test_shortest(self):
        network_descriptor = "./Networks/first_example.csv"
        nodes = network_processer(network_descriptor)
        start, end = "A", "F"
        color = ""

        network = make_network(nodes, color)
        visited_str = get_shortest(network, start, end)
        self.assertEqual(visited_str, "A->B->C->D->E->F")

    def test_shortest_red(self):
        network_descriptor = "./Networks/first_example.csv"
        nodes = network_processer(network_descriptor)
        start, end = "A", "F"
        color = "red"

        network = make_network(nodes, color)
        visited_str = get_shortest(network, start, end)
        self.assertEqual(visited_str, "A->B->C->H->F")

    def test_shortest_green(self):
        network_descriptor = "./Networks/first_example.csv"
        nodes = network_processer(network_descriptor)
        start, end = "A", "F"
        color = "green"

        network = make_network(nodes, color)
        visited_str = get_shortest(network, start, end)
        posible_answers = ["A->B->C->D->E->F", "A->B->C->G->I->F"]
        self.assertIn(visited_str, posible_answers)

if __name__ == '__main__':
    unittest.main()


