from langchain_core.prompts import ChatPromptTemplate

analyse_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Give detail stock analysis, Use the available data and provide investment recommendation. \
             The user is fully aware about the investment risk, dont include any kind of warning like 'It is recommended to conduct further research and analysis or consult with a financial advisor before making an investment decision' in the answer \
             User question: {query} \
             Fetch the ticker symbol of the company first. Collect all the necessary information and then proceed with analysis. Write (5-8) pointwise investment analysis to answer user query, At the end conclude with proper explaination.Try to Give positives and negatives  : \
               "
        ),
        ("user", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)

ticker_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
           "From the query from the user provide only the company name and its corresponding ticker symbol in NSE in json format. Dont provide any text other than that.\
            Query : {query}"
        ),
        ("user", "{query}"),
    ]
)