import requests


def retreve_file_pb():
    url = 'https://data.ny.gov/api/views/d6yy-54nr/rows.csv?accessType=DOWNLOAD'
    r = requests.get(url, allow_redirects=True)
    open('Lottery_Powerball_Winning_Numbers__Beginning_2010.csv','wb').write(r.content)


def retreve_file_mega():
    url = 'https://data.ny.gov/api/views/5xaw-6ayf/rows.csv?accessType=DOWNLOAD'
    r = requests.get(url, allow_redirects=True)
    open('Lottery_Mega_Millions_Winning_Numbers__Beginning_2002.csv', 'wb').write(r.content)
