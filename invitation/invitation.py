class Invitation:
    def __init__(self, inviteId, startDate, endDate, type, status, createdBy,
                 createdDate, executedBy, executedDate, participantEmails):
        self.inviteId = inviteId  # mandatory
        self.startDate = startDate  # mandatory
        self.endDate = endDate  # optional
        self.type = type  # mandatory email/post
        self.status = status or "new"  # optional
        self.createdBy = createdBy  # optional
        self.createdDate = createdDate  # optional
        self.executedBy = executedBy  # optional
        self.executedDate = executedDate  # optional
        self.participantEmails = participantEmails  # mandatory
