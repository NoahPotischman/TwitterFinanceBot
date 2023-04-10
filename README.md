# Twitter Bot for Crypto and Stock Market Data

This Twitter bot tweets the current prices and 24-hour percent change for cryptocurrencies (Bitcoin and Ethereum) and major stock market indices (S&P 500, Dow Jones, and Nasdaq).

## Components

### main.py
`main.py` is the main script that combines all other components and sends a tweet containing the information from both `crypto_data.py` and `market_data.py`. It uses the Tweepy library to authenticate with Twitter and send the tweet.

### market_data.py
`market_data.py` fetches the current price and 24-hour percent change for the major stock market indices using the yfinance library.

### crypto_data.py
`crypto_data.py` fetches the current price and 24-hour percent change for Bitcoin and Ethereum using the CoinGecko API.

### keys.py
`keys.py` contains your Twitter API keys and access tokens. Make sure to replace the placeholders with your actual keys and tokens.

## Setup

1. Install the required libraries: 
```pip install tweepy yfinance pycoingecko```


2. Create a `keys.py` file and include your Twitter API keys and access tokens.

3. Run the `main.py` script to send a tweet containing the current prices and 24-hour percent change for cryptocurrencies and stock market indices.

## Twitter API

To obtain your Twitter API keys and access tokens, follow the instructions in the Twitter Developer documentation: https://developer.twitter.com/en/docs/authentication/oauth-1-0a


