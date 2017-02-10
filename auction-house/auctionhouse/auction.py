import logging
import datetime


class ModelException(Exception):
    pass


# types
BUY_NOW_AUCTION = 1
BID_AUCTION = 2

AUCTION_TYPES = [
    BUY_NOW_AUCTION,
    BID_AUCTION,
]

# statuses
AUCTION_STATUS_NEW = 'n'
AUCTION_STATUS_ACTIVE = 'a'
AUCTION_STATUS_FINISHED = 'f'

AUCTION_STATUSES = [
    AUCTION_STATUS_NEW,
    AUCTION_STATUS_ACTIVE,
    AUCTION_STATUS_FINISHED,
]

# events
HISTORY_EVENT_AUCTION_CREATED = 'c'
HISTORY_EVENT_AUCTION_FINISHED = 'f'
HISTORY_EVENT_BID_ADDED = 'b'

# mail templates
MAIL_TEMPLATE_YOU_BOUGHT_AUCTION = 'b'
MAIL_TEMPLATE_YOUR_AUCTION_IS_SOLD = 's'
MAIL_TEMPLATE_YOUR_AUCTION_WAS_NOT_SOLD = 'ns'

import random


class Bid(object):
    def __init__(self, auction, price, buyer, bidDate):
        self.id = random.randint(1, 10000000)
        self.price = price
        self.buyer = buyer
        self.bidDate = bidDate
        self.auction = auction


import time


class HistoryProvider(object):
    def saveHistory(self, event):
        # simulation of method with remote resource access
        time.sleep(1)


class MailProvider(object):
    def sendMail(self, template):
        # simulation of method with remote resource access
        time.sleep(1)


class User(object):
    def __init__(self, name):
        self.id = random.randint(1, 10000000)
        self.name = name


class RequestContext(object):
    def __init__(self, user):
        self.user = user
        self.now = datetime.datetime.utcnow()

        self.historyProvider = HistoryProvider()
        self.mailProvider = MailProvider()

    def getUser(self):
        return self.user

    def getNow(self):
        return self.now

    def getHistoryProvider(self):
        return self.historyProvider

    def getMailProvider(self):
        return self.mailProvider


class Auction(object):
    def __init__(self, p_ctx, p_auctionName, p_startT, p_endT, p_startingPrice, p_buyNowPrice, buy_now):
        self.context = p_ctx
        if p_startT < p_ctx.getNow():  # start time validation
            raise ModelException("Given time must be from future")
        if p_endT < p_ctx.getNow():  # end time validation (must be from past)
            raise ModelException("Given time must be from future")
        if p_endT < p_startT:  # end time validation (must be from future)
            raise ModelException("End time must be after current time and start time")

        self.name_of_the_current_auction = p_auctionName
        self.st = p_startT
        self.et = p_endT

        # buy now price should be set only when creating BUY_NOW_AUCTION
        if buy_now:
            self.type = BUY_NOW_AUCTION
            self.buyNowPrice = p_buyNowPrice
        else:  # starting price  should be set only when creating BUY_NOW_AUCTION
            self.type = BID_AUCTION
            self.startingPrice = p_startingPrice

        self.user = p_ctx.getUser()
        self.auctionStatusEnum = AUCTION_STATUS_NEW
        self.bids = []

        p_ctx.getHistoryProvider().saveHistory(HISTORY_EVENT_AUCTION_CREATED)

    # represents current web context
    def update_context(self, context):
        self.context = context

    def add_bid(self, pl_price, p_he):  # p_he stands for history_event
        """
            Validates auction status and user and then adds new Bid to the setOfBids
        """
        if self.auctionStatusEnum not in [AUCTION_STATUS_ACTIVE]:
            raise ModelException(
                "Current auction auctionStatusEnum is {0}, expected {1}".format(
                    self.auctionStatusEnum, [AUCTION_STATUS_ACTIVE]))
        if self.user != self.context.getUser():
            raise ModelException("Operation not allowed for auction user")

        logging.debug("Adding bid of price " + pl_price)

        bid = Bid(self, pl_price, self.context.getUser(), self.context.getNow())
        if hasattr(self, 'bids'):
            self.bids.append(bid)
        else:
            self.bids = []
            self.bids.append(bid)

        self.context.getHistoryProvider().saveHistory(p_he)

    def makeAuctionVisibleAndActive(self, p_event):  # p_event stans for history event
        '''
            Method responsible for activating auction,
            should set activateDate and status,
            history is saved only if auction is
            activated by system
        '''
        exptectedStatus = [AUCTION_STATUS_NEW]
        if self.auctionStatusEnum not in exptectedStatus:
            raise ModelException(
                "Current auction auctionStatusEnum is {0}, expected {1}".format(
                    self.auctionStatusEnum, exptectedStatus))
        if self.st > self.context.getNow():
            raise ModelException("Given time must be from past")

        if p_event:
            logging.debug("Activating auction with history event " + p_event)

        self.auctionStatusEnum = AUCTION_STATUS_ACTIVE
        self.activateDate = self.context.getNow()
        if p_event:
            self.context.getHistoryProvider().saveHistory(p_event)

    def finish(self):
        '''
            * finish auction and send mail to user, true if successful
        '''
        onlyActiveStatus = [AUCTION_STATUS_ACTIVE]
        if self.auctionStatusEnum not in onlyActiveStatus:
            raise ModelException(
                "Current auction auctionStatusEnum is {0}, expected {1}".format(
                    self.auctionStatusEnum, onlyActiveStatus))
        if self.type == BID_AUCTION and self.et < self.context.getNow():
            raise ModelException("Auction has to be after its finish time")

        logging.debug("number of bids: " + len(self.bids))
        # send mail to buyer
        if len(self.bids) != 0:
            self.context.getMailProvider().sendMail(MAIL_TEMPLATE_YOU_BOUGHT_AUCTION)
            self.context.getHistoryProvider().saveHistory(HISTORY_EVENT_AUCTION_FINISHED)

        logging.debug("Finishing auction and sending mails")

        mailProvider = self.context.getMailProvider()
        # send mail to sender
        if len(self.bids) != 0:
            mailProvider.sendMail(MAIL_TEMPLATE_YOUR_AUCTION_IS_SOLD)
        else:
            mailProvider.sendMail(MAIL_TEMPLATE_YOUR_AUCTION_WAS_NOT_SOLD)
        # set status
        self.auctionStatusEnum = AUCTION_STATUS_FINISHED

        return True

    def bid(self, p_pfb):  # current bid price
        if not self.type == BID_AUCTION:
            raise ModelException("Expecte BID_AUCTION type")

        if self.startingPrice > p_pfb:
            raise ModelException("Current bid price must be heigher than starting price")

        logging.debug("bid requested")

        if hasattr(self, 'bids') and len(self.bids) != 0:
            # get last bid and compare price
            higher_bids = [bid for bid in self.bids if bid.price > p_pfb]
            if higher_bids:
                raise ModelException("Current bid price must be heigher than last bid price")

        self.add_bid(p_pfb, HISTORY_EVENT_BID_ADDED)
