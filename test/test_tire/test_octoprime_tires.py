import unittest

from tire.octoprime_tires import OctoprimeTires

class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_false1(self):
        tire = OctoprimeTires(0.5,0.1,0.2,0.3)
        self.assertFalse(tire.needs_service())
    def test_needs_service_false2(self):
        tire = OctoprimeTires(0.9,0.3,0.1,0.1)
        self.assertFalse(tire.needs_service())
    def test_needs_service_true1(self):
        tire = OctoprimeTires(1,1,0.9,0.1)
        self.assertTrue(tire.needs_service())
    def test_needs_service_true2(self):
        tire = OctoprimeTires(0.9,0.9,0.9,0.3)
        self.assertTrue(tire.needs_service())
if __name__ == '__main__':
    unittest.main()