import pandas as pd
from bs4 import BeautifulSoup
import csv
from selenium import webdriver


def DataCollection():
    driver = webdriver.Firefox()
    base_url = 'https://www.transfermarkt.com/spieler-statistik/marktwertalter/marktwertetop?position=alle&land_id=0&altersklasse=u19&plus='
    for i in range(1, 8):
        url = base_url + str(i) + '&page=' + str(i)
        print(url)
        driver.get(url)
        page = driver.page_source
        out_file = 'data/page' + str(i) + '.html'
        file = open(out_file, 'w')
        file.write(page)
        file.close()


def Scrape():
    for i in range(1, 8):
        page_path = 'data/page' + str(i) + '.html'
        page = open(page_path)
        soup = BeautifulSoup(page, 'html.parser')
        table = soup.find_all('table')
        df = pd.read_html(str(table))
        df[1].to_csv('result.csv')
        print(df[1])


def Clean():
    infile = 'result.csv'
    players = []

    with open(infile, 'r') as rdr:
        next(rdr)
        reader = csv.reader(rdr)
        headers = ['Name',
                   'Position',
                   'Age',
                   'Club',
                   'Country',
                   'Peak market value',
                   'Current market value',
                   'Market value at that time']

        players.append(headers)
        for row in reader:
            if row[-1] != '':
                new_row = [row[4],
                           row[5],
                           int(row[7][:-2]),
                           row[10],
                           row[11],
                           money_formatter(row[12]),
                           money_formatter(row[13]),
                           money_formatter(row[14])
                           ]

                players.append(new_row)

    df = pd.DataFrame(players)
    df.to_csv('clean.csv', index=False)

    # use selenium to get pages 2-7

    # inflation adjusted for destination country


def money_formatter(value):
        if 'Mill' in value:
            comma = str(value).find(',')
            short_value = value[0:int(comma)]
            formatted_value = short_value +'000000'
            return formatted_value

        elif 'Th.' in value:
            comma = str(value).find(',')
            thousands_marker = str(value).find('T')
            short_value = value[0:(int(thousands_marker) - 1)]
            formatted_value = short_value + '000'
            return formatted_value


if __name__ == '__main__':
    DataCollection()
    Scrape()
    Clean()
