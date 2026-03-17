from backend.TimeLapse import TimeLapse
from backend._common import ChoiceEnum
from backend.Village import Village



class GlobalManager:
    INSTANCE = None

    def __init__(self, year):
        GlobalManager.INSTANCE = self

        self.choice = None
        self.time   = TimeLapse(year)
    # #enddef

    def set_choice(self, choice):
        if (self.choice == ChoiceEnum.ALL_TO_A or self.choice == ChoiceEnum.ALL_TO_B) and choice == ChoiceEnum.SHARED:
            if self.choice == ChoiceEnum.ALL_TO_A:
                Village.VILLAGGIO_A.riserva_acqua -= 30
                Village.VILLAGGIO_B.modifica_riserva_acqua(30)
            else:
                Village.VILLAGGIO_B.riserva_acqua -= 30
                Village.VILLAGGIO_A.modifica_riserva_acqua(30)
        self.choice = choice
    # #enddef

    def year_flow(self):
        self.time.year_flow(self.choice)
    # #enddef
# #enclass