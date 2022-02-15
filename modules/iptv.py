import requests, json, os

class Iptv:
    def login(url):
        url = url.replace('player.php', 'player_api.php')
        r = requests.get(url).text

        data = json.loads(r)

        #USUARIO & SERVER
        user_info = data['user_info']
        server_info = data['sever_info']

        username = user_info['username']
        password = user_info['password']

        host = server_info['url']
        port = server_info['port']

        url = f'http://{host}:{port}/'

    def code_status(text):
        text = text[11:]
        text = text[:3]
        return text

    def getChannels(url, username, password):
        host = f'{url}player_api.php?username={username}&password={password}&action=get_live_streams'

        r = requests.get(host).text
        data = json.loads(r)

        return data



Iptv.code_status('<Response [200]>')