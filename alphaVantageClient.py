#Reference https://www.alphavantage.co/documentation/
import json
import time
import logging
import requests

from apiCallTypes import apiCallTypes

# alphavantage_api_token = os.environ['alphavantage_api_token']


#This creates the logfile
#todo: call this in a higher class maybe for global access?

#timestr = time.strftime("%Y_%m_%d-%H%M%S")
#filename = 'log_%s.log'%(timestr)
#logging.basicConfig(filename=filename,level=logging.DEBUG)

class alphaVantageClient():

    def __init__(self, symbol):
        self.symbol = symbol
        super(alphaVantageClient, self).__init__()

    def request(self, symbol):
        # payload = {"url": url, "token": token}
        json_data = None # Initialize Json Data so that it returns a null value if the call is bad

        try:
            # print "Requesting response from {0} for Post ID: {1} : {2}".format(self.base_url, post_id, time.asctime( time.localtime(time.time()) ))
            print ("Hello")
            #response.raise_for_status() #Eventually include to check for HTML Server Response Errors TMT
            # response = requests.get(self.format_url(api, version), params=payload)

            #response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&apikey=0MO8EWOIHYCQAHRW', headers=headers)
            #response.raise_for_status()
            # json_data = response.json()

        except:
            pass
            #todo log

        return json_data

    # Formats the url for the api call
    #TODO make a class method?
    def format_url(self, function, symbol, interval, timePeriod, apikey):

        base_url = "https://www.alphavantage.co/query?"

        return '{}{}/{}'.format(base_url, version, api)
