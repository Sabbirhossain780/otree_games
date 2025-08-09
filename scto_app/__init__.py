# __init__.py
from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = 'scto_game'
    PLAYERS_PER_GROUP = 1
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


# First page: capture params from GET request
class GetParams(Page):
    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        self.player.name = self.request.GET.get('name', 'Unknown')
        self.player.age = int(self.request.GET.get('age', 0))
        self.player.education = self.request.GET.get('education', 'Unknown')
        # Example computed result: name + double the age
        self.player.computed_result = f"{self.player.name}_{self.player.age * 2}"


# Second page: show data for confirmation
class Introduction(Page):
    def vars_for_template(self):
        return dict(
            name=self.player.name,
            age=self.player.age,
            education=self.player.education
        )


# Third page: redirect back to SurveyCTO
class RedirectBack(Page):
    def is_displayed(self):
        return self.round_number == 1

    def app_after_this_page(self, upcoming_apps):
        result = self.player.computed_result
        # Replace the link with your actual SurveyCTO return link
        return f"https://sabbir01.surveycto.com/forms/bgwe_endline/designer.html?view=test&caseid={result}"


page_sequence = [GetParams, Introduction, RedirectBack]
