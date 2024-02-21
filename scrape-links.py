import csv
import requests

from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def get_game_links(base_url, num_pages=546):
    all_links = []
    for page_num in range(1, num_pages+1):
        url = f'{base_url}&page={page_num}'
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.content, 'html.parser')
        game_links = soup.find_all('a', class_="c-finderProductCard_container")
        for link in game_links:
            href = link.get('href')
            if href:
                all_links.append(href)
    return all_links

def save_links_to_csv(links, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['game_links']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for link in links:
            writer.writerow({'game_links': link})

base_url = 'https://www.metacritic.com/browse/game/?releaseYearMin=1958&releaseYearMax=2024'
print("Extrayendo información de los mejores videojuegos de la historia:\n")
game_links = get_game_links(base_url)

save_links_to_csv(game_links, 'game_links.csv')
print("Los enlaces se han guardado en game_links.csv")