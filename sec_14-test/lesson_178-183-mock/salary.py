import requests

class ThirdPartyBounusRestApi(object):
    def bonus_price(self, year):
        r = requests.get('http://localhost/bonus', params={'year': year})
        return r.json()['bonus']
    

class Salary(object):
    def __init__(self, base=100, year=2017):
        self.bonus_api = ThirdPartyBounusRestApi()
        self.base = base
        self.year = year

    def calcuration_salary(self):
        bonus = 0
        if self.year < 2020:
            bonus = self.bonus_api.bonus_price(year=self.year)
        return self.base + bonus

