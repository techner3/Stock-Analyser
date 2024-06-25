import os
import re
import sys
import json 
import yfinance as yf
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from src.prompt import ticker_prompt
from langchain.tools import StructuredTool
from src.exception import StockAnalyserException
from langchain_community.utilities import GoogleSerperAPIWrapper

load_dotenv()

chat = ChatGroq(temperature=0,model="Llama3-70b-8192",api_key=os.getenv("GROQ_API_KEY"))

def get_stock_ticker(query):

    try:
        chain=ticker_prompt|chat
        return json.loads(chain.invoke({"query":query}).content)

    except Exception as e:
        raise StockAnalyserException(e,sys)

def get_stock_price(ticker,history=15):

    try:
        if "." in ticker:
            ticker=ticker.split(".")[0]
        ticker=ticker+".NS"
        stock = yf.Ticker(ticker)
        df = stock.history(period="1y")
        df=df[["Close","Volume"]]
        df.index=[str(x).split()[0] for x in list(df.index)]
        df.index.rename("Date",inplace=True)
        df=df[-history:]
        return df.to_string()

    except Exception as e:
        raise StockAnalyserException(e,sys)

def get_financial_statements(ticker):

    try: 
        if "." in ticker:
            ticker=ticker.split(".")[0]
        else:
            ticker=ticker
        ticker=ticker+".NS"    
        company = yf.Ticker(ticker)
        balance_sheet = company.balance_sheet
        if balance_sheet.shape[1]>=3:
            balance_sheet=balance_sheet.iloc[:,:3]   
        balance_sheet=balance_sheet.dropna(how="any")
        balance_sheet = balance_sheet.to_string()
        return balance_sheet

    except Exception as e:
        raise StockAnalyserException(e,sys)

news_search=GoogleSerperAPIWrapper(serper_api_key="",type="news")

get_stockprice_tool = StructuredTool.from_function(func=get_stock_price,name="Get Stock Price",
                        description="Useful to get the stock price of a company")
get_financialstatements_tool = StructuredTool.from_function(func=get_financial_statements,name="Get Financial Statements",
                        description="Useful to get the financial statements of a company")
newssearch_tool = StructuredTool.from_function(name="Company News",func=news_search.run,description="Useful to get the latest news of a company")
tickersearch_tool = StructuredTool.from_function(name="Ticker Symbol",func=get_stock_ticker,description="Use this to get the ticker symbol of the company from the internet")