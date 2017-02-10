from auctionhouse.auction import (
    BUY_NOW_AUCTION, BID_AUCTION,
    AUCTION_STATUS_NEW, AUCTION_STATUS_ACTIVE, AUCTION_STATUS_FINISHED,
    RequestContext
)


class ReportingException(Exception):
    pass


class SimpleReporter(object):
    def __init__(self):
        self.totalBid = 0
        self.totalBidPrice = 0
        self.totalBuyNow = 0
        self.totalBuyNowPrice = 0
        self.totalNewAuctions = 0
        self.totalActiveAuctions = 0
        self.totalFinishedAuctions = 0

    def create_all_auctions_report(self, auctions):
        return 'Sample All Auctions Report'

    def create_bid_auctions_report(self, auctions):
        return 'Sample Bid Auctions Report'

    def create_buy_now_auctions_report(self, auctions):
        return 'Sample Buy Now Auctions Report'

    @property
    def request_context(self):
        return RequestContext(None)

    def clear(self):
        self.totalBid = 0
        self.totalBidPrice = 0
        self.totalBuyNow = 0
        self.totalBuyNowPrice = 0
        self.totalNewAuctions = 0
        self.totalActiveAuctions = 0
        self.totalFinishedAuctions = 0

class DetailedAllAuctionsReporter(SimpleReporter):
    def create_all_auctions_report(self, auctions, str_list):

        c = self.request_context

        str_list.append("ANNUAL SUMMARY OF ALL AUCTIONS.\n")
        str_list.append("*******************************\n\n")

        month = c.getNow().month

        print("Month -> " + str(month))

        if month > 0 and month <= 2:
            str_list.append("Report period: 01/01/2012 and 31/03/2012\n")
        elif month > 2 and month <= 5:
            str_list.append("Report period: 01/04/2012 and 30/06/2012\n")
        elif month > 5 and month <= 8:
            str_list.append("Report period: 01/07/2012 and 30/09/2012\n")
        elif month > 8 and month <= 11:
            str_list.append("Report period: 01/10/2012 and 31/12/2012\n")
        else:
            raise ReportingException("Critical issue")

        total_number_of_auctions = len(auctions) if auctions else 0
        str_list.append("Total number of auctions: " + str(
            total_number_of_auctions))
        str_list.append("\n")

        for auction in auctions:
            self.data(auction)

        str_list.append("Including ")
        str_list.append(str(self.totalBid))
        str_list.append(" bid auctions and ")
        str_list.append(str(self.totalBuyNow))
        str_list.append(" buy now auctions\n")

        str_list.append(str(self.totalNewAuctions))
        str_list.append(" auctions are ")
        str_list.append(self.description_for(AUCTION_STATUS_NEW))
        str_list.append("\n")

        str_list.append(str(self.totalActiveAuctions))
        str_list.append(" auctions are ")
        str_list.append(self.description_for(AUCTION_STATUS_ACTIVE))
        str_list.append("\n")

        str_list.append(str(self.totalFinishedAuctions))
        str_list.append(" auctions are ")
        str_list.append(self.description_for(AUCTION_STATUS_FINISHED))
        str_list.append("\n")

        str_list.append("Total buy now price: ")
        str_list.append("{0:.2f}".format(float(self.totalBuyNowPrice / 100)))
        str_list.append(" zl\n")

        str_list.append("Total bid price: ")
        str_list.append("{0:.2f}".format(float(self.totalBidPrice / 100)))
        str_list.append(" zl\n")

        return ''.join(str_list)

    def description_for(self, status):
        status_to_desc = {
            AUCTION_STATUS_NEW: 'new',
            AUCTION_STATUS_ACTIVE: 'active',
            AUCTION_STATUS_FINISHED: 'finished',
        }
        return status_to_desc.get(status)

    def data(self, auction):
        if auction.type == BID_AUCTION:
            self.totalBid += 1
            if not auction.bids:
                self.totalBidPrice += auction.startingPrice
            else:
                # sort list by propery , get last one
                bids = sorted(
                    auction.bids, key=lambda bid: bid.bidDate, reverse=True)
                self.totalBidPrice += bids[0].price
        elif auction.type == BUY_NOW_AUCTION:
            self.totalBuyNow += 1
            self.totalBuyNowPrice += auction.buyNowPrice
        else:
            raise ReportingException("Not recognized auction type")

        if auction.auctionStatusEnum == AUCTION_STATUS_NEW:
            self.totalNewAuctions += 1
        elif auction.auctionStatusEnum == AUCTION_STATUS_ACTIVE:
            self.totalActiveAuctions += 1
        elif auction.auctionStatusEnum == AUCTION_STATUS_FINISHED:
            self.totalFinishedAuctions += 1
        else:
            raise ReportingException("Not recognized auction status")

    def create_bid_auctions_report(self, auctions):
        return ReportingException(
            'For Bid Auctions Report ask DetailedBidAuctionsReporter')

    def create_buy_now_auctions_report(self, auctions):
        return ReportingException(
            'For Buy Now Auctions Report ask DetailedBuyNowAuctionsReporter')
