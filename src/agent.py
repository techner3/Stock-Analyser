import os 
import sys
from src.logger import logging
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from src.prompt import analyse_prompt
from src.exception import StockAnalyserException
from langchain.agents import AgentExecutor, create_tool_calling_agent
from src.tools import get_financialstatements_tool, get_stockprice_tool, newssearch_tool, tickersearch_tool, chat

load_dotenv()

def create_stock_analyser_agent():

    try:
        tools=[tickersearch_tool,newssearch_tool,get_financialstatements_tool,get_stockprice_tool]
        logging.info("Tools Imported")

        agent = create_tool_calling_agent(chat, tools, analyse_prompt)
        agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
        logging.info("Stock Analyser Agent Created")
        return agent_executor

    except Exception as e: 
        raise StockAnalyserException(e,sys)