from Participant import Participant


class ParticipantRepository:
    def save(self, participant: Participant):
        if not type(participant) is Participant:
            raise Exception("Incorrect class " + str(
                type(participant)) + " should be " + str(Participant))
        print("Persisting participant")
