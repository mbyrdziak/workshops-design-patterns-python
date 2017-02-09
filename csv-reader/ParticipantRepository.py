from Participant import Participant


class ParticipantRepository:
    def save(self, participant: Participant):
        if not type(participant) is Participant:
            raise Exception("Incorrect class {} should be {}".format(
                str(type(participant)), str(Participant)))
        print("Persisting participant")
