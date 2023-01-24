from mycroft import MycroftSkill, intent_file_handler


class NbaResults(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('results.nba.intent')
    def handle_results_nba(self, message):
        self.speak_dialog('results.nba')


def create_skill():
    return NbaResults()

