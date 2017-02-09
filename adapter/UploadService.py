class UploadService:
    def __init__(self, participantReader, participantRepository):
        self.participantRepository = participantRepository
        self.participantReader = participantReader

    def run(self):
        participant = self.participantReader.parse()
        self.participantRepository.save(participant)
