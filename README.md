### Currency Convertor
A simple currency converter application built with Streamlit. It allows users to convert amounts between different currencies using exchange rates.
### Features
- Convert amounts between various currencies.
- User-friendly interface with Streamlit.
### Installation
1. Clone the repository:
   ```bash
   git clone 
   cd Currency-Convertor
   ```
2. Install the required packages:
   ```bash   
   pip install -r requirements.txt
   ```
2. pythonpath set to src folder:
   ```bash
   export PYTHONPATH="${PYTHONPATH}:$(pwd)"
   ```   

3. Obtain an API key from [ExchangeRate API](https://www.exchangerate-api.com/) and set it as an environment variable:
   ```bash
   export EXCHANGE_RATE_API_KEY='your_api_key_here'
   ```
### Usage
Run the Streamlit application:
```bash
streamlit run src/dashboard.py
```

### Functions
- `get_exchange_rate(from_currency, to_currency)`: Fetches the exchange rate between two currencies. cached for efficiency.
- `convert_currency(amount, from_currency, to_currency)`: Converts a specified amount from one currency to another using the exchange rate.  
### Constants
- `CURRENCIES`: A list of supported currency codes getting from ExchangeRate API.
### Project Structure
```
Currency-Convertor/
│├── src/
│   ├── dashboard.py        # Streamlit application
│   ├── main.py             # Core logic for currency conversion
│   ├── constants.py        # Constants used in the project
│├── README.md              # Project documentation
│├── requirements.txt       # Required packages
```