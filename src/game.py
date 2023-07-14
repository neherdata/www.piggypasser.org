class Pig:
    def __init__(self, name, image, value, state):
        self.name = name
        self.image = image
        self.value = value
        self.state = state

    def set_state(self, state):
        if state == "unselected":
            self.state = "unselected"
            self.image = self.name + "-single.jpg"
            document.getElementById(self.name).className = "pig-btn"
        elif state == "single":
            self.state = "single"
            self.image = self.name + "-single.jpg"
            document.getElementById(self.name).className = "pig-btn single"
        elif state == "double":
            self.state = "double"
            self.image = self.name + "-double.jpg"
            document.getElementById(self.name).className = "pig-btn double"
        elif state == "disabled":
            self.state = "disabled"
            self.image = self.name + "-single.jpg"
            document.getElementById(self.name).className = "pig-btn"
            document.getElementById(self.name).disabled = True
        else:
            print("default")

    def reset_state(self):
        self.state = "unselected"
        self.image = self.name + "-single.jpg"
        document.getElementById(self.name).className = "pig-btn"
        document.getElementById(self.name).disabled = False


class Player:
    def __init__(self, name, total_pts):
        self.name = name
        self.total_pts = total_pts


round = None
roll_score = None
round_score = None