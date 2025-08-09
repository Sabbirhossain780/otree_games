from otree.api import *
# init_py = ""

# models.py
# models_py =
from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = 'scto_game'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    name = models.StringField()
    age = models.IntegerField()
    education = models.StringField()
    computed_result = models.StringField()


# pages.py
# pages_py =
# from ._builtin import Page
# from .models import Player

class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return dict(
            name=self.player.name,
            age=self.player.age,
            education=self.player.education
        )

    def before_next_page(self):
        self.player.name = self.request.GET.get('name', 'Unknown')
        self.player.age = int(self.request.GET.get('age', 0))
        self.player.education = self.request.GET.get('education', 'Unknown')
        self.player.computed_result = f"{self.player.name}_{self.player.age * 2}"

class RedirectBack(Page):
    def is_displayed(self):
        return self.round_number == 1

    def app_after_this_page(self, upcoming_apps):
        result = self.player.computed_result
        return f"https://sabbir01.surveycto.com/forms/bgwe_endline/designer.html?view=test&caseid={result}"

page_sequence = [Introduction, RedirectBack]