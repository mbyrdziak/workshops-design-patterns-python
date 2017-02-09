from Participant import Participant


class ParticipantReader:
    def parse(self):
        print("Reading participant")
        return Participant(1, "test@email.com", "name", "surname")
