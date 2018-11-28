import pytest
import app
import requests


def test_scrape():
    # Test url is available
    url = 'https://www.transfermarkt.com/spieler-statistik/marktwertalter/marktwertetop?position=alle&land_id=0&altersklasse=u19&plus=1'
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    assert r.status_code == 200

    # Test stored scraped pages are present

    # Test soup of pages is correct

# def test_clean():
    # use test csv
    # check output csv


def test_money_formatter():
    assert app.money_formatter("45,00 Mill. €") == "45000000"
    assert app.money_formatter("300 Th. €") == "300000"
