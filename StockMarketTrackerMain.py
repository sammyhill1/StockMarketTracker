from stockDatabase import stockPortfolio, stockQuery

def main():

    #while True:
    #These are our objects for our portfolio and our queries
    sp = stockPortfolio()
    sq  = stockQuery()

    sp.newPurchase("MSFT", 78, 5, 0.1)
    sp.newPurchase("TGI", 24, 32, 0.9)

    print (sp.stocks[0].percentRtnDesired)
    # print (sp.stocks[0].symbol)
    # print (sp.stocks[0].stockShares[0].purchasePrice)
    # print (sp.stocks[0].percentRtnDesired)
    # print (sp.stocks[1].symbol)
    # print (sp.stocks[1].stockShares[0].purchasePrice)

    sp.newPurchase("MSFT",24, 2, 0.4)
    sp.newPurchase("TGI", 25, 3)
    sp.newPurchase("XN", 25, 3, 0.1)
    print(sp.stocks[0].getTotalInvestment())
    print(sp.stocks[0].getTotalReturn())
    sp.newSell("MSFT", 10000, 1)
    sp.newSell("TGI", 10, 1)
    sp.stocks[0].changeDesiredPercentRtn(0.4)
    print(sp.stocks[0].getTotalReturn())
    # print (sp.stocks[0].percentRtnDesired)
    # print (sp.stocks[0].stockShares[1].sharesPurchased)


    #Run the program!
    #Let's get some user input too! Probably in a different thread

if __name__ == '__main__':

    main()
