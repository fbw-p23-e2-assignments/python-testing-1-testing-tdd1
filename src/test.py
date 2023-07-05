import unittest
from cat_controller import CatController


class TestCatController(unittest.TestCase):
    """Test case for CatController class"""

    def setUp(self):
        """Set up the test fixture"""
        self.cat_controller = CatController()

    def test_01_cat_cage_open_false_by_default(self):
        """Test if cat cage is initially closed"""
        self.assertFalse(self.cat_controller.cat_cage_open)

    def test_02_daily_food_intake(self):
        """Test daily food intake"""
        self.cat_controller.daily_food_intake()
        food_items = self.cat_controller.food_items
        self.assertListEqual(food_items, ["1 mouse", "1 hamster", "1 chicken"])

    def test_03_feeding_hours(self):
        """Test feeding hours"""
        feeding_hours = [8, 12, 17]
        for hour in range(24):
            actions = self.cat_controller.hourly_run(hour)
            if hour in feeding_hours:
                self.assertTrue(any(action.startswith("Feed") for action in actions))
            else:
                self.assertFalse(any(action.startswith("Feed") for action in actions))

    def test_04_cat_cage_opening_hours(self):
        """Test cat cage opening hours"""
        opening_hours = [7]
        non_opening_hours = [hour for hour in range(24) if hour not in opening_hours]
        for hour in range(24):
            actions = self.cat_controller.hourly_run(hour)
            if hour in opening_hours:
                self.assertIn("Open cat cage.", actions)
                self.assertTrue(self.cat_controller.cat_cage_open)
            elif hour in non_opening_hours:
                self.assertNotIn("Open cat cage.", actions)
                self.assertFalse(self.cat_controller.cat_cage_open)

    def test_05_water_hours(self):
        """Test water hours"""
        water_hours = [hour for hour in range(24) if hour != 7]
        non_water_hours = [7]
        for hour in range(24):
            actions = self.cat_controller.hourly_run(hour)
            if hour in water_hours:
                self.assertIn("Give water.", actions)
            elif hour in non_water_hours:
                self.assertNotIn("Give water.", actions)

    def tearDown(self):
        """Tear down the test fixture"""
        self.cat_controller = None


if __name__ == '__main__':
    unittest.main()
