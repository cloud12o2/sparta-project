import requests
from bs4 import BeautifulSoup

# 왓챠피디아
# https://pedia.watcha.com/ko-KR

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://pedia.watcha.com/ko-KR/',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

sections = soup.find_all(class_='css-gxko42-StyledHomeListContainer ebeya3l2')

all_ranking = []
for section in sections:
    all_ranking.append(section.find_all(class_='css-8y23cj'))

# 박스오피스 순위
def box_office():
    box_office_ranking = []
    for ranking in all_ranking[0]:
        box_office_link = 'https://pedia.watcha.com' + ranking.find('a')['href']
        box_office_rank = ranking.find(class_='css-csn5n').text
        box_office_img = ranking.find('img')['src']
        box_office_title = ranking.find(class_="css-5yuqaa").text
        box_office_release = ranking.find(class_="css-6t186m-StyledContentYearAndNation ebeya3l12").text[0:4]
        box_office_countries = ranking.find(class_="css-6t186m-StyledContentYearAndNation ebeya3l12").text[7:9]

        box_office_dict = {
            'movie_link': box_office_link,
            'rank': box_office_rank,
            'img': box_office_img,
            'title': box_office_title,
            'release_year': box_office_release,
            'countries': box_office_countries
        }
        box_office_ranking.append(box_office_dict)

    return box_office_ranking


# 왓챠영화 순위
def watcha():
    watcha_ranking = []
    for ranking in all_ranking[1]:
        watcha_link = 'https://pedia.watcha.com' + ranking.find('a')['href']
        watcha_rank = ranking.find(class_='css-csn5n').text
        watcha_img = ranking.find('img')['src']
        watcha_title = ranking.find(class_="css-5yuqaa").text
        watcha_release = ranking.find(class_="css-6t186m-StyledContentYearAndNation ebeya3l12").text[0:4]
        watcha_countries = ranking.find(class_="css-6t186m-StyledContentYearAndNation ebeya3l12").text[7:9]

        watcha_dict = {
            'movie_link': watcha_link,
            'rank': watcha_rank,
            'img': watcha_img,
            'title': watcha_title,
            'release_year': watcha_release,
            'countries': watcha_countries
        }
        watcha_ranking.append(watcha_dict)

    return watcha_ranking

# 넷플릭스 영화 순위
def netflix():
    netflix_ranking = []
    for ranking in all_ranking[2]:
        netflix_link = 'https://pedia.watcha.com' + ranking.find('a')['href']
        netflix_rank = ranking.find(class_='css-csn5n').text
        netflix_img = ranking.find('img')['src']
        netflix_title = ranking.find(class_="css-5yuqaa").text
        netflix_release = ranking.find(class_="css-6t186m-StyledContentYearAndNation ebeya3l12").text[0:4]
        netflix_countries = ranking.find(class_="css-6t186m-StyledContentYearAndNation ebeya3l12").text[7:9]

        watcha_dict = {
            'movie_link': netflix_link,
            'rank': netflix_rank,
            'img': netflix_img,
            'title': netflix_title,
            'release_year': netflix_release,
            'countries': netflix_countries
        }
        netflix_ranking.append(watcha_dict)

    return netflix_ranking