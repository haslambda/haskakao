import requests
from bs4 import BeautifulSoup


def get_raw(y, m, d):
    """
    Gets raw meal HTML from http://hana.hs.kr/life/meal.asp
    """
    date = {"yy": y, "mm": m, "dd": d}
    r = requests.get("http://hana.hs.kr/life/meal.asp", params=date)
    r.encoding = "utf-8"
    return r.text


def parse_meal(raw):
    """
    Parses raw meal HTML into a list
    """
    meals = []
    soup = BeautifulSoup(raw, "lxml")
    for e in soup.select_one(".today_meal").find_all("td"):
        meals.append(e.text)
    return meals
