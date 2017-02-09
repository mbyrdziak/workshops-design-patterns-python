class PersonalData:
    def __init__(self, name, surname):
        self.surname = surname
        self.name = name


class NewParticipant:
    def __init__(self, participantId, email, personalData: PersonalData):
        self.personalData = personalData
        self.email = email
        self.participantId = participantId


