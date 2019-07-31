import requests
import json as js

class trello:

    def __init__ (self):
        self.key = 'SUA CHAVE'
        self.token = 'SEU TOKEN'
        self.board = 'tS9UQn66'


    def getBoard(self):
        url = "https://api.trello.com/1/boards/" + self.board

        querystring = {"actions":"all","boardStars":"none","cards":"none","card_pluginData":"false","checklists":"none","customFields":"false","fields":"name,desc,descData,closed,idOrganization,pinned,url,shortUrl,prefs,labelNames","lists":"open","members":"none","memberships":"none","membersInvited":"none","membersInvited_fields":"all","pluginData":"false","organization":"false","organization_pluginData":"false","myPrefs":"false","tags":"false","key":self.key,"token":self.token}

        response = requests.request("GET", url, params=querystring)

        print(response.text)

    def getCards(self):
        self.limit = '30'
        url = 'https://api.trello.com/1/boards/' + self.board + '/cards/?limit=' + self.limit + '&fields=name&members=true&member_fields=fullName&key=' + self.key + '&token=' + self.token

        headers = {
            'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
        }

        call = requests.get(url , headers=headers)
        dic = js.loads(call.text)

        print(dic)


    def getCardID(self):
        self.idCard = '5825f7408fc73004763693d7'
        
        url = 'https://trello.com/1/boards/' + self.board + '/cards/' + self.idCard + '?key=' + self.key + '&token=' + self.token

        headers = {
            'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
        }

        call = requests.get(url , headers=headers)
        dic = js.loads(call.text)

        print(dic)

    def getMember(self):
        self.member = '550a1457c58a3212b6851477'

        url = "https://api.trello.com/1/members/" + self.member

        querystring = {"boardBackgrounds":"none","boardsInvited_fields":"name,closed,idOrganization,pinned","boardStars":"false","cards":"none","customBoardBackgrounds":"none","customEmoji":"none","customStickers":"none","fields":"all","organizations":"none","organization_fields":"all","organization_paid_account":"false","organizationsInvited":"none","organizationsInvited_fields":"all","paid_account":"false","savedSearches":"false","tokens":"none","key": self.key,"token":self.token}

        response = requests.request("GET", url, params=querystring)

        print(response.text)