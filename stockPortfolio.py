import stock

class stockPortfolio(stock):

    def __init__(self):
        self.stocks = []
        super(stockPortfolio, self).__init__()

    def addNewStock(self, stock):
        self.stocks.append(stock)
        #TODO check if stock name entered already exists, and group it within that individual stock

    def updatePortfolio(self):
