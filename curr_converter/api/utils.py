import requests
from bs4 import BeautifulSoup


def get_quote(from_curr: str, to_curr: str):
    """Returns the quote of the target currency based on origin currency.
    
    Parameters
    ----------
        - from_curr (str): The origin currency.
        - to_curr (str): The target currency.

    Returns
    -------
        - rate (float): The quote of the target currency.
    """

    try:
        # Scraping proccess on the Google Finance site - Inversion of control needed
        base_url = f"https://www.google.com/finance/quote/{from_curr}-{to_curr}"
        response = requests.get(base_url)
        html = response.content
        scrapy = BeautifulSoup(html, 'html.parser')
        # Getting the quote based on HTML page pattern
        rate = scrapy.find("div", class_="YMlKec fxKbKc")
        
        # Returning the formatted rate
        rate = float(rate.string.replace(",", ""))
        return rate
    except:
        return 0.0