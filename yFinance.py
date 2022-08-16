import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

# def getInput():
# ticker = input("Enter ticker name ").upper()
# startDate = input("Enter a start date in format of 'YYYY-MM-DD' ")
# endDate = input("Enter a start date in format of 'YYYY-MM-DD' ")
    # return ticker, startDate, endDate

class FinanceInstrument():
    def __init__(self, ticker, startDate, endDate):
        self.ticker = ticker
        self.startDate = startDate
        self.endDate = endDate
        self.getData()
        self.log_return()
        self.plot()
        self.price_plot()
        self.return_plot()

    def __repr__(self):
        return "FinanceInstrument(ticker={}, startDate={}, endDate={})".format(self.ticker, self.startDate, self.endDate)
        
        
    def getData(self):
        raw = yf.download(self.ticker, self.startDate, self.endDate)
        raw.rename(columns = {"Close":"price"}, inplace = True)
        self.data = raw
        print(self.data)

    def log_return(self):
        # print(self.data)
        price = self.data["price"]
        print(price)
        self.data["Log_Return"] = np.log(price/price.shift(1))
        print(self.data)

    def plot(self):
        # self.data.Log_Return.plot()
        # plt.show()
        # self.data.Log_Return.hist(bins=100)
        # plt.show()
        pass

    def price_plot(self):
        self.data.price.plot(figsize = (12, 8))
        plt.title("Return {}".format(self.ticker), fontsize = 15)
        plt.show()

    def return_plot(self, kind = "hist"):
        if kind == "ts":
            self.data.price.plot(figsize = (12, 8))
            plt.title("Return {}".format(self.ticker), fontsize = 15)
            plt.show()
        elif kind == "hist":
            self.data.price.hist(figsize = (12,8), bins = int(np.sqrt(len(self.data))))
            plt.title ("Frequency of Return {}".format(self.ticker), fontsize=15)
            plt.show()


stock = FinanceInstrument("AAPL","2000-01-01","2022-01-01")
print(stock)
# getInput()ticker, startDate, endDate


