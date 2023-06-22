from mycroft import MycroftSkill, intent_file_handler


class Pineapple(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('pineapple.intent')
    def handle_pineapple(self, message):
        self.speak_dialog('pineapple')


def create_skill():
    return Pineapple()

