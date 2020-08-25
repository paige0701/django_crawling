
# Create your views here.
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse


def score_board(request):
    url = "https://sports.news.naver.com/kbaseball/schedule/index.nhn?date=20200825&month=08&year=2020&teamCode="
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    today_schedule = soup.find('ul', {'id': 'todaySchedule'}).findAll('li')

    for schedule in today_schedule:
        state = schedule.find('em', class_='state').text.strip()

        left = schedule.find('div', class_='vs_lft')
        left_team = left.p.strong.text.strip()
        left_team_score = left.find('strong', class_='vs_num').text

        right = schedule.find('div', class_='vs_rgt')
        right_team = right.p.strong.text.strip()
        right_team_score = right.find('strong', class_='vs_num').text

        print(state)
        print(left_team, left_team_score)
        print(right_team, right_team_score)
        print('----------------------------------')

    return HttpResponse('hello world')