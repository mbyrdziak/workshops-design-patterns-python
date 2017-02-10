import datetime
import time

from auctionhouse.auction import User, Auction, RequestContext, AUCTION_STATUS_ACTIVE


class Repository(object):
    def save(self, obj):
        print('simulation of saving item in database')
        time.sleep(1)


class TestAuction(object):
    def setup_method(self, method):
        self.repository = Repository()

    # This is to verify if it's still possible to create auction of type - buy now
    def test_buy_now_auction(self):
        user = User('bob')
        self.repository.save(user)

        ctx = RequestContext(user)

        start_time = datetime.datetime.utcnow() + datetime.timedelta(days=1)
        end_time = datetime.datetime.utcnow() + datetime.timedelta(days=7)

        auction = Auction(
            ctx, 'python in a bag', start_time, end_time, 0, 1000, True)
        self.repository.save(auction)

        assert auction.bids == []
        assert auction.name_of_the_current_auction == 'python in a bag'
        assert auction.st == start_time
        assert auction.et == end_time
        assert auction.type == 1
        assert auction.auctionStatusEnum == 'n'
        assert auction.buyNowPrice == 1000
        assert not hasattr(auction, 'startingPrice')
        assert auction.user == user

    def test_bid_(self):
        user = User('Bob')
        self.repository.save(user)

        ctx = RequestContext(user)

        start_time = datetime.datetime.utcnow() + datetime.timedelta(days=1)
        end_time = datetime.datetime.utcnow() + datetime.timedelta(days=7)

        auction = Auction(
            ctx, 'python in a bag', start_time, end_time, 1000, 0, False)
        self.repository.save(auction)

        assert auction.bids == []
        assert auction.name_of_the_current_auction == 'python in a bag'
        assert auction.st == start_time
        assert auction.et == end_time
        assert auction.type == 2
        assert auction.auctionStatusEnum == 'n'
        assert not hasattr(auction, 'buyNowPrice')
        assert auction.startingPrice == 1000
        assert auction.user == user

        ctx.now = ctx.getNow() + datetime.timedelta(days=2)

        auction.makeAuctionVisibleAndActive(None);

        assert auction.activateDate is not None
        assert auction.activateDate == ctx.getNow()
        assert auction.auctionStatusEnum == AUCTION_STATUS_ACTIVE

        self.repository.save(auction)
