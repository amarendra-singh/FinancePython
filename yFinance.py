import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

# def getInput():
ticker = input("Enter ticker name ").upper()
startDate = input("Enter a start date in format of 'YYYY-MM-DD' ")
endDate = input("Enter a start date in format of 'YYYY-MM-DD' ")
    # return ticker, startDate, endDate

class FinanceInstrument():
    def __init__(self, ticker, startDate, endDate):
        self.ticker = ticker
        self.startDate = startDate
        self.endDate = endDate
        self.getData()



    def getData(self):
        raw = yf.download(self.ticker, self.startDate, self.endDate)
        raw.rename(columns = {"Close":"price"}, inplace = True)
        self.data = raw
        print(ticker, "--", startDate,"--", endDate)
        print(self.data)

    def log_return(self):
        self.data["Log_Return"] = np.log(self.data.price/self.price.shift(1))


# getInput()
fI = FinanceInstrument(ticker, startDate, endDate)