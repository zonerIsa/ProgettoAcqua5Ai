from backend.GlobalManager import GlobalManager

class GameState:

    def __init__(self):

        self.year = GlobalManager.INSTANCE.time.year

        self.water_a = 100
        self.water_b = 100

        self.dam_built = False
        self.request_done = False
        self.war = False
