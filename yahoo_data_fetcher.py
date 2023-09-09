import requests


def get_price(ticker: str, verbose: bool = False) -> dict:
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
    user_agent = {'User-agent': 'Mozilla/5.0'}
    r = requests.get(url=url, headers=user_agent).json()

    precio = r['chart']['result'][0]['meta']['regularMarketPrice']
    currency = r['chart']['result'][0]['meta']['currency']

    if verbose:
        print(f"{ticker}: {precio} {currency}")
    return {
        "ticker": ticker,
        "precio": precio,
        "moneda": currency
    }