from ParticipantRepository import ParticipantRepository
from ParticipantReader import ParticipantReader
from UploadService import UploadService


def main():
    uploadService = UploadService(ParticipantReader(), ParticipantRepository())
    uploadService.run()

if __name__ == "__main__":
    main()
