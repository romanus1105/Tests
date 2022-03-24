import requests
from getpass import getpass

class YaDisk:
    def __init__(self, token_yd):
        self.token_yd = token_yd
        self.yd_file_list = []
        self.file_path = ''

    def yd_folder_create(self, folder_name):
        self.file_path = str(folder_name)
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token_yd)
            }
        params = {
            'path': self.file_path 
            }
        response = requests.put(url=url, headers=headers, params=params)
        if response.status_code == 201:
            print(f'Папка {self.file_path} создана')
        elif response.status_code == 409:
            print(f'Папка {self.file_path} уже была создана')
        else:
            print('Ошибка', response)
        return response

    def checking_avaliability(self):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token_yd)
            }
        params = {
            'path': 'disk:/'
            }
        response = requests.get(upload_url, headers=headers, params=params)
        for i in range(0, len(response.json()['_embedded']['items'])):
            self.yd_file_list.append(response.json()['_embedded']['items'][i]['name'])
        print('Список файлов на Яндекс-диске', self.yd_file_list)
        return self.yd_file_list

if __name__ == "__main__":
    yd = YaDisk(getpass("Введите Я.Диск-токен: "))
    yd.yd_folder_create('tmp_dir')
    yd.checking_avaliability()