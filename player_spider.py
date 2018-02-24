import _csv
from urllib3 import request
from selenium import webdriver

from panenka.crawler import db_driver


def download_photo(player_url, photo_url, file_path):
    extension = photo_url.split('.')[-1]
    file_name = player_url.split('/')[-2]
    destination_path = '%s/%s.%s' % (file_path, file_name, extension)
    try:
        request.urlretrieve(photo_url,  destination_path)
        return '%s.%s' % (file_name, extension)
    except Exception as e:
        print(str(e))


chromepath = "selenium/webdriver/chrome/chromedriver.exe"
driver = webdriver.Chrome(chromepath)

team_links = {
    '3': ['Athletic Bilbao', 'https://www.sofascore.com/team/football/athletic-bilbao/2825'],
    '4': ['Atlético Madrid',  'https://www.sofascore.com/team/football/atletico-madrid/2836'],
    '2': ['Deportivo Alavés',  'https://www.sofascore.com/team/football/deportivo-alaves/2885'],
    '12': ['Leganés', 'https://www.sofascore.com/team/football/leganes/2845'],
    '9': ['Getafe', 'https://www.sofascore.com/team/football/getafe/2859'],
    '14': ['Málaga', 'https://www.sofascore.com/team/football/malaga/2830'],
    '19': ['Valencia', 'https://www.sofascore.com/team/football/valencia/2828'],
    '20': ['Villarreal', 'https://www.sofascore.com/team/football/villarreal/2819'],
    '6': ['Deportivo La Coruña', 'https://www.sofascore.com/team/football/deportivo-la-coruna/2832'],
    '1': ['Barcelona', 'https://www.sofascore.com/team/football/barcelona/2817'],
    '18': ['Sevilla', 'https://www.sofascore.com/team/football/sevilla/2833'],
    '10': ['Girona', 'https://www.sofascore.com/team/football/girona/24264'],
    '5': ['Celta Vigo', 'https://www.sofascore.com/team/football/celta-vigo/2821'],
    '8': ['Espanyol', 'https://www.sofascore.com/team/football/espanyol/2814'],
    '15': ['Real Betis', 'https://www.sofascore.com/team/football/real-betis/2816'],
    '16': ['Real Madrid', 'https://www.sofascore.com/team/football/real-madrid/2829'],
    '17': ['Real Sociedad', 'https://www.sofascore.com/team/football/real-sociedad/2824'],
    '7': ['Eibar', 'https://www.sofascore.com/team/football/eibar/2839'],
    '13': ['Levante', 'https://www.sofascore.com/team/football/levante/2849'],
    '11': ['Las Palmas', 'https://www.sofascore.com/team/football/las-palmas/6577'],
}
player_paths = []
for key, value in team_links.items():
    print('Extracting %s player links...' % value[0])
    driver.get(value[1])
    squad = driver.find_element_by_class_name('squad')
    players = squad.find_elements_by_tag_name('a')
    for p in players:
        player_paths.append(p.get_attribute('href'))
players_list = []
player_counter = 1
for p in player_paths:
    driver.get(p)
    player = driver.find_element_by_xpath("//h2[@class='page-title']").text
    photo = driver.find_element_by_xpath("//img[@class='img--x75 img--circle u-va-top']").get_attribute('src')
    team = driver.find_element_by_xpath("//a[@class='js-link ff-medium u-fs15 u-text-regular']").text
    box = driver.find_element_by_xpath("//div[@class='cell u-tC u-flex-wrap u-mT32']").text.split('\n')
    info_box = {
        'Nationality': '',
        'Age': '',
        'Height': '',
        'Preferred foot': '',
        'Position': '',
        'Shirt number': '',
        'Player value': ''
    }
    for index, value in enumerate(box):
        if index % 1 == 0:
            info_box[value] = box[index - 1]
    id_player = 'player%d' % player_counter
    player_dict = {
        'id_player': '',
        'player_shirt': '',
        'player_number': '',
        'player_birth': '',
        'player_value': '',
        'player_position': '',
        'player_link': '',
        'id_country': '',
        'id_club': '',
        'photo': ''
    }
    if info_box['Shirt number'] == '':
        info_box['Shirt number'] = '-1'
    if info_box['Age'] == '':
        info_box['Age'] = '-1'
    if info_box['Nationality'] == '':
        info_box['Nationality'] = 'Unknown'
    player_dict['id_player'] = player_counter,
    player_dict['player_shirt'] = player,
    player_dict['player_number'] = info_box['Shirt number']
    player_dict['player_birth'] = info_box['Age'].split('(')[1][:-1]
    player_dict['player_value'] = info_box['Player value'][:-2]
    player_dict['player_position'] = info_box['Position']
    player_dict['player_link'] = p
    player_dict['id_country'] = info_box['Nationality']
    if len([key for key, value in team_links.items() if value[0] == team]) > 0:
        player_dict['id_club'] = [key for key, value in team_links.items() if value[0] == team][0]
    else:
        player_dict['id_club'] = '-1'
    player_dict['photo'] = download_photo(p, photo, 'players')
    players_list.append(player_dict)
    player_counter += 1

with open('players.csv', mode='w', encoding='utf-8') as output_file:
    writer = _csv.writer(output_file, delimiter=',', quoting=_csv.QUOTE_MINIMAL, lineterminator='\n')
    for p in players_list:
        player_info_box = [p['id_player'][0], p['player_shirt'][0],
                           p['player_number'], p['player_birth'],
                           p['player_value'], p['player_position'],
                           p['player_link'], p['id_country'], p['id_club'],
                           p['photo']
                           ]
        writer.writerow(player_info_box)
driver.quit()
