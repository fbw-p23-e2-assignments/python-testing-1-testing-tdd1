class CatController:
    """Class representing a cat controller."""

    def __init__(self):
        """Initialize the CatController object."""
        self.cat_cage_open = False
        self.food_items = []
        self.water_items = []

    def daily_food_intake(self):
        """Set the daily food intake for the cat."""
        self.food_items = ["1 mouse", "1 hamster", "1 chicken"]

    def hourly_run(self, hour):
        """Perform hourly actions based on the current hour."""
        actions = []
        if hour in [8, 12, 17]:
            actions.append("Feed " + ", ".join(self.food_items))
        if hour == 7:
            actions.append("Open cat cage.")
            self.cat_cage_open = True
        else:
            actions.append("Close cat cage.")
            self.cat_cage_open = False
            actions.append("Give water.")
            self.water_items.append("Water bowl filled at hour " + str(hour))
        return actions
