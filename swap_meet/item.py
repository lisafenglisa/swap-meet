class Item:
    def __init__(self, category="", condition=0.0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition ==  5:
            return "New"
        elif self.condition == 4:
            return "Like New"
        elif self.condition == 3:
            return "Very Good"
        elif self.condition == 2:
            return "Good"
        elif self.condition == 1:
            return "Acceptable"
        elif self.condition == 0:
            return "As Is"

