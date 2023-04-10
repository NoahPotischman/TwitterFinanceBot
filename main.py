import tweepy
from keys import API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from crypto_data import get_crypto_data
from market_data import get_market_data

def client():
    return tweepy.Client(consumer_key=API_KEY,
                         consumer_secret=API_KEY_SECRET,
                         access_token=ACCESS_TOKEN,
                         access_token_secret=ACCESS_TOKEN_SECRET)

def tweet_crypto_data(client: tweepy.Client):
    crypto_data = get_crypto_data()
    market_data = get_market_data()

    btc_price = crypto_data["bitcoin"]["usd"]
    btc_change = crypto_data["bitcoin"]["usd_24h_change"]
    btc_emoji = "📈" if btc_change >= 0 else "📉"

    eth_price = crypto_data["ethereum"]["usd"]
    eth_change = crypto_data["ethereum"]["usd_24h_change"]
    eth_emoji = "📈" if eth_change >= 0 else "📉"

    market_message = ''
    for index, values in market_data.items():
        index_emoji = "📈" if values['percent_change'] >= 0 else "📉"
        market_message += f"{index}: ${values['current_price']:.2f} ({values['percent_change']:+.2f}%) {index_emoji}\n"

    message = f"Current prices:\n\nCrypto:\nBTC: ${btc_price:.2f} ({btc_change:+.2f}%) {btc_emoji}\nETH: ${eth_price:.2f} ({eth_change:+.2f}%) {eth_emoji}\n\nMarket Indices:\n{market_message}"
    
    client.create_tweet(text=message)
    print('Tweeted successfully!')


if __name__ == '__main__':
    client = client()
    tweet_crypto_data(client)
