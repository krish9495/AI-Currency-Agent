import streamlit as st
import requests
import os
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_structured_chat_agent
from langchain_core.tools import tool
from langchain import hub
from langchain_community.callbacks import StreamlitCallbackHandler


st.title("AI Currency Conversion Agent")

st.info("This app uses a LangChain agent to convert currencies. You will need API keys for both OpenAI (or a compatible service like OpenRouter) and ExchangeRate-API.")

with st.sidebar:
    st.header("API Keys")
    openai_api_key = st.text_input("OpenAI API Key", type="password")
    openai_api_base = st.text_input("OpenAI API Base (optional, for OpenRouter)", value="https://openrouter.ai/api/v1")
    exchange_api_key = st.text_input("ExchangeRate-API Key", type="password")

if not openai_api_key or not exchange_api_key:
    st.warning("Please provide all required API keys in the sidebar.")
else:
    # Set credentials for LangChain
    os.environ['OPENAI_API_KEY'] = openai_api_key
    if openai_api_base:
        os.environ['OPENAI_API_BASE'] = openai_api_base

    # --- Tool Definitions ---
    # We define the tool inside this block so it can capture the `exchange_api_key`
    @tool
    def get_conversion_factor(base_currency: str, target_currency: str) -> str:
        """This function fetches the currency conversion factor between the base currency and the target currency."""
        url = f'https://v6.exchangerate-api.com/v6/{exchange_api_key}/pair/{base_currency}/{target_currency}'
        response = requests.get(url)
        data = response.json()
        if data.get('result') == 'success':
            return f"The conversion rate from {base_currency} to {target_currency} is {data['conversion_rate']}"
        else:
            return f"Error from API: {data.get('error-type', 'Unknown error')}"

    @tool
    def convert(base_amount: float, conversion_rate: float) -> float:
        """Given a conversion rate this function will calculate the target currency value from a base currency value."""
        return base_amount * conversion_rate

    tools = [get_conversion_factor, convert]

    # --- Agent Initialization ---
    try:
        prompt = hub.pull("hwchase17/structured-chat-agent")
        llm = ChatOpenAI(temperature=0, streaming=True)
        agent = create_structured_chat_agent(llm, tools, prompt)
        agent_executor = AgentExecutor(
            agent=agent,
            tools=tools,
            verbose=True,
            handle_parsing_errors=True
        )

        st.header("Ask the Agent")
        user_query = st.text_input("Enter your conversion query (e.g., 'Convert 10 USD to INR')", "Convert 10 USD to INR")

        if st.button("Run Agent"):
            if user_query:
                st.header("Agent Output")
                st_callback = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
                response = agent_executor.invoke(
                    {"input": user_query},
                    {"callbacks": [st_callback]}
                )
                st.success("Final Answer:")
                st.write(response.get("output"))
            else:
                st.warning("Please enter a query.")

    except Exception as e:
        st.error(f"An error occurred during agent initialization or execution: {e}") 