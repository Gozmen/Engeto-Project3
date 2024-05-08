"""
projekt_3.py: Election Scraper projekt do Engeto Online Python Akademie

author: Jakub Dostál
email: gozo.jakub@gmail.com
discord: gozo197, Gozo#2494
"""

import sys
import csv
import requests
from bs4 import BeautifulSoup

def get_soup(url):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        print("Downloading data from URL:", url)
        return BeautifulSoup(response.text, "html.parser")
    except requests.RequestException as e:
        print(f"Error accessing URL {url}: {e}")
        sys.exit()

def validate_args():
    if len(sys.argv) != 3:
        print('Incorrect number of arguments. Must be 2: URL in quotes, and output .csv file name.')
        sys.exit()

def extract_data(soup):
    towns = [town.text for town in soup.find_all("td", "overflow_name")]
    town_ids = [i.text for i in soup.find_all("td", "cislo")]
    links = [f"https://volby.cz/pls/ps2017nss/{link.a['href']}" for link in soup.find_all("td", "cislo", "href")]
    return towns, town_ids, links

def get_voting_details(links):
    voters, attendance, valid_votes = [], [], []
    for link in links:
        soup = get_soup(link)
        voters += [v.text.replace('\xa0', ' ') for v in soup.find_all("td", headers="sa2")]
        attendance += [a.text.replace('\xa0', ' ') for a in soup.find_all("td", headers="sa3")]
        valid_votes += [c.text.replace('\xa0', ' ') for c in soup.find_all("td", headers="sa6")]
    return voters, attendance, valid_votes

def get_party_names(link):
    soup = get_soup(link)
    return [party.text for party in soup.find_all("td", "overflow_name")]

def collect_votes(links):
    votes = []
    for link in links:
        soup = get_soup(link)
        town_votes = [v.text.replace('\xa0', '') for v in soup.find_all("td", "cislo", headers=["t1sb3", "t2sb3"])] 
        votes.append(town_votes)
    return votes

def create_csv_rows(towns, town_ids, voters, attendance, valid_votes, votes):
    zipped = zip(town_ids, towns, voters, attendance, valid_votes)
    rows = []
    for (i, t, v, a, vo), vs in zip(zipped, votes):
        rows.append([i, t, v, a, vo] + vs)
    return rows

def write_csv(filename, header, rows):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)

def main():
    validate_args()
    url, filename = sys.argv[1], sys.argv[2]
    soup = get_soup(url)
    towns, town_ids, links = extract_data(soup)
    if not links:
        print("No links found, please check the URL.")
        sys.exit()
    voters, attendance, valid_votes = get_voting_details(links)
    party_names = get_party_names(links[0])
    votes = collect_votes(links)
    header = ['Kód obce', 'Název obce', 'Voliči v seznamu', 'Vydané obálky', 'Platné hlasy'] + party_names
    rows = create_csv_rows(towns, town_ids, voters, attendance, valid_votes, votes)
    write_csv(filename, header, rows)
    print("Data saved to file:", filename)
    print("Program completed:", sys.argv[0])

if __name__ == '__main__':
    main()
