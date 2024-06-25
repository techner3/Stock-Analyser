import streamlit as st
from src.agent import create_stock_analyser_agent

def main():
    st.title("Stock Analyser")
    st.divider()

    query = st.text_input("Question related to stocks in NSE")

    if st.button("Submit"):
        sa_agent=create_stock_analyser_agent()
        response=sa_agent.invoke({"query": query})
        st.write(response['output'])

if __name__ == "__main__":
    main()