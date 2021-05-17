from bs4 import BeautifulSoup as get_soup
import requests
import random
def movies(url):
    page = requests.get(url)
    soup = get_soup(page.text, 'html.parser')
    movies = soup.find_all("td", class_="titleColumn")
    random.shuffle(movies)
    return movies
def summary(url):
    movie_page = requests.get(url)
    soup = get_soup(movie_page.text, 'html.parser')
    return soup.find("div", class_="summary_text").contents[0].strip()

def info(movie):
    movie_title = movie.a.contents[0]
    movie_year = movie.span.contents[0]
    movie_url = 'http://www.imdb.com' + movie.a['href']
    return movie_title, movie_year, movie_url

def imd_movie_picker():
    ctr=0
    print("____________________________________________")
    for movie in movies('https://www.imdb.com/chart/top'):
        movie_title, movie_year, movie_url = info(movie)
        movie_summary = summary(movie_url)
        print(movie_title, movie_year)
        print(movie_summary)
        print("____________________________________________")
        ctr=ctr+1
        if (ctr==5):
          break;
if __name__ == '__main__':
    imd_movie_picker()
