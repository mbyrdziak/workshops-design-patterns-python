from NewParticipant import NewParticipant, PersonalData


class NewParticipantReader:
    def parse(self):
        print("Reading new participant")
        return NewParticipant(1, "test@email.com",
                              PersonalData("name", "surname"))
