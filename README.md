# Metacritic Scraper
This is the source code for the Metacritic scraper developed on my [YouTube channel.](https://youtu.be/hj6QbUdEx6U)

The scraper scrapes the data of all the video games listed on [metacritic.com](https://metacritic.com/) until February 2024 (more than 13k games), it gets the name, description, developer, genre, users score, users reviews, critics score, and critics review of every game and exports them in a CSV file.

## Instructions to run the scraper
1. Make sure you have at least the Python 3.8 version installed in your computer.
2. Clone this repo.
3. Got to the folder and create a Python virtual environment by using:
  - Windows and Linux: `python -m venv venv`
  - MacOS: `python3 -m venv venv`
4. Activate the venv by using:
  - Windows: `.\venv\Scripts\activate`
  - Linux and MacOS: `source venv/bin/activate`

5. Install the packages by using `pip install -r requirements.txt`.
6. If you want you can run the script `scrape-links.py` by using `python scrape-links.py` to get the most updated links from Metacritic.
7. Then you can tun the Jupyter Notebook `metacritic_scraper.ipynb` by opening it on a Jupyter server or by using the venv you created and Visual Studio Code.
8. Enjoy!
