import unittest


from tires.Octoprime_tires import Octoprimetires
class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.8, 0.8, 0.8, 0.7]
        tires = Octoprimetires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.1, 0.2, 0.4, 0.2]
        tires = Octoprimetires(tire_wear)
        self.assertFalse(tires.needs_service())