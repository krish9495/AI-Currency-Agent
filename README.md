# AI Currency Agent

This project is a web-based currency converter powered by a LangChain AI agent. It uses natural language understanding to process user queries, fetches real-time exchange rates from an external API, and performs the currency conversion.

The application is built with Streamlit, providing a user-friendly interface where you can interact with the agent.

## Features
- **Natural Language Queries**: Ask the agent to convert currencies in plain English (e.g., "how much is 15 USD in EUR?").
- **AI Agent Integration**: Utilizes a LangChain structured chat agent to interpret queries and use tools.
- **Real-time Rates**: Fetches the latest conversion rates using the ExchangeRate-API.
- **Interactive UI**: A simple and clean interface built with Streamlit.
- **BYOK (Bring Your Own Key)**: Securely use your own API keys for OpenAI and ExchangeRate-API.

## Setup and Installation

Follow these steps to get the application running locally.

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd <your-repo-directory>
```

### 2. Install Dependencies
Ensure you have Python 3.8+ installed. Then, install the required packages using pip:
```bash
pip install -r requirements.txt
```

### 3. Get API Keys
You will need two API keys to run this application:
- **OpenAI API Key**: For the language model. You can get a key from [OpenAI](https://platform.openai.com/api-keys).
  - Alternatively, this app is configured to use [OpenRouter](https://openrouter.ai/) as a proxy.
- **ExchangeRate-API Key**: For fetching currency conversion rates. Get a free key from [ExchangeRate-API](https://www.exchangerate-api.com/).

## How to Run
1. Open your terminal and navigate to the project directory.
2. Run the Streamlit application using the following command:
   ```bash
   streamlit run app.py
   ```
3. Your web browser will open a new tab with the application.
4. In the sidebar, enter your **OpenAI API Key** and **ExchangeRate-API Key**.
5. Once the keys are entered, you can type your query into the main input box and click "Run Agent".

## Example Usage
Here are a few examples of queries you can try:
- `Convert 1000 JPY to USD`
- `What's the exchange rate between British Pounds and Euros?`
- `How much is 50 CAD worth in AUD?`

The agent will show its thinking process and provide the final answer directly in the app. 
