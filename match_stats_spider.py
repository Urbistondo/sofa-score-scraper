from selenium import webdriver
import pandas as pd
import numpy as np


def get_summary_stats(driver, save):
    player_names = driver.find_elements_by_xpath(
        "//div[@class='js-sorter-group js-sorter-group-summary tab-pane"
        " active']//table[@class='table table--statistics js-sorter-body"
        " sort-by-rating']"
        "//td[@class='u-tL ff-medium player-stat-player-name']"
    )

    player_links = driver.find_elements_by_xpath(
        "//div[@class='js-sorter-group js-sorter-group-summary tab-pane"
        " active']//table[@class='table table--statistics js-sorter-body"
        " sort-by-rating']"
        "//td[@class='u-tL ff-medium player-stat-player-name']//a"
    )

    player_minutes = driver.find_elements_by_xpath(
        "//div[@class='js-sorter-group js-sorter-group-summary tab-pane"
        " active']"
        "//table[@class='table table--statistics js-sorter-body"
        " sort-by-rating']"
        "//td[@class='js-sorter-sort-field"
        " js-sorter-sort-field-minutesPlayed player-stat-minutesPlayed ']"
    )
    player_position = driver.find_elements_by_xpath(
        "//div[@class='js-sorter-group js-sorter-group-summary tab-pane"
        " active']"
        "//table[@class='table table--statistics js-sorter-body"
        " sort-by-rating']"
        "//td[@class='js-sorter-sort-field js-sorter-sort-field-position"
        " player-stat-position ']"
    )

    player_rating = driver.find_elements_by_xpath(
        "//div[@class='js-sorter-group js-sorter-group-summary tab-pane"
        " active']"
        "//table[@class='table table--statistics js-sorter-body"
        " sort-by-rating']"
        "//td[@class='js-sorter-sort-field js-sorter-sort-field-rating"
        " player-stat-rating ']"
    )

    player_objects = list()
    for i in range(len(player_names)):
        player_objects.append(
            [player_names[i].text, player_links[i].get_attribute('href'),
             player_minutes[i].text, player_position[i].text,
             player_rating[i].text]
        )

    players = pd.DataFrame(player_objects)
    players.columns = ['Player', 'Link', 'Minutes', 'Position', 'Rating']
    if save:
        players.to_csv('summaryStats.csv', sep=',', line_terminator='\n')
        print('Summary stats collected successfully')
    else:
        print('Summary stats collected successfully')
        return players


def get_attacking_stats(driver, save):
    driver.find_element_by_xpath("//a[@class='js-squad-stats-groups-nav-tab player-stat-group-attack']").click()
    player_names = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-attack tab-pane"
                                                 "  active']//table[@class='table table--statistics js-sorter-body"
                                                 " sort-by-rating']"
                                                 "//td[@class='u-tL ff-medium player-stat-player-name']")

    player_shots_info = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-attack"
                                                           " tab-pane  active']"
                                                           "//table[@class='table table--statistics js-sorter-body"
                                                           " sort-by-rating']"
                                                           "//td[@class='js-sorter-sort-field"
                                                           " js-sorter-sort-field-totalScoringAttempts"
                                                           " player-stat-totalScoringAttempts ']")
    player_dribbles_info = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-attack tab-pane"
                                                    "  active']"
                                                    "//table[@class='table table--statistics js-sorter-body"
                                                    " sort-by-rating']"
                                                    "//td[@class='js-sorter-sort-field"
                                                    " js-sorter-sort-field-totalContest player-stat-totalContest ']")
    player_goals = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-attack tab-pane"
                                                 "  active']"
                                                 "//table[@class='table table--statistics js-sorter-body"
                                                 " sort-by-rating']"
                                                 "//td[@class='js-sorter-sort-field"
                                                 " js-sorter-sort-field-goals player-stat-goals ']")
    player_assists = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-attack tab-pane"
                                                   "  active']"
                                                   "//table[@class='table table--statistics js-sorter-body"
                                                   " sort-by-rating']"
                                                   "//td[@class='js-sorter-sort-field js-sorter-sort-field-goalAssist"
                                                   " player-stat-goalAssist ']")
    player_notes = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-attack tab-pane"
                                                 "  active']"
                                                 "//table[@class='table table--statistics js-sorter-body"
                                                 " sort-by-rating']"
                                                 "//td[@class='js-sorter-sort-field js-sorter-sort-field-notes"
                                                 " player-stat-notes u-fs11']")
    player_position = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-attack tab-pane"
                                                    "  active']"
                                                    "//table[@class='table table--statistics js-sorter-body"
                                                    " sort-by-rating']"
                                                    "//td[@class='js-sorter-sort-field js-sorter-sort-field-position"
                                                    " player-stat-position ']")
    player_rating = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-attack tab-pane"
                                                  "  active']"
                                                  "//table[@class='table table--statistics js-sorter-body"
                                                  " sort-by-rating']"
                                                  "//td[@class='js-sorter-sort-field js-sorter-sort-field-rating"
                                                  " player-stat-rating ']")

    player_objects = list()
    for i in range(len(player_names)):
        player_shots, player_shots_on_target = player_shots_info[i].text.split('(')
        player_shots = player_shots[:-1]
        player_shots_on_target = player_shots_on_target[:-1]
        player_dribbles, player_successful_dribbles = player_dribbles_info[i].text.split('(')
        player_dribbles = player_dribbles[:-1]
        player_successful_dribbles = player_successful_dribbles[:-1]
        player_objects.append(
            [player_names[i].text, player_shots, player_shots_on_target,
             player_dribbles, player_successful_dribbles,
             player_goals[i].text, player_assists[i].text, player_notes[i].text,
             player_position[i].text, player_rating[i].text])
    players = pd.DataFrame(player_objects)
    players.columns = ['Player', 'Shots', 'Shots on target', 'Dribbles',
                       'Successful dribbles', 'Goals', 'Assists',
                       'Notes (Attacking)', 'Position', 'Rating']
    if save:
        players.to_csv('attackingStats.csv', sep=',', line_terminator='\n')
        print('Attacking stats collected successfully')
    else:
        print('Attacking stats collected successfully')
        return players


def get_defending_stats(driver, save):
    driver.find_element_by_xpath("//a[@class='js-squad-stats-groups-nav-tab player-stat-group-defence']").click()
    player_names = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-defence tab-pane"
                                                 "  active']"
                                                 "//table[@class='table table--statistics js-sorter-body"
                                                 " sort-by-rating']"
                                                 "//td[@class='u-tL ff-medium player-stat-player-name']")

    player_clearances = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-defence tab-pane"
                                                      "  active']"
                                                      "//table[@class='table table--statistics js-sorter-body"
                                                      " sort-by-rating']"
                                                      "//td[@class='js-sorter-sort-field"
                                                      " js-sorter-sort-field-totalClearance"
                                                      " player-stat-totalClearance ']")
    player_shots_blocked = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-defence"
                                                         " tab-pane  active']"
                                                         "//table[@class='table table--statistics js-sorter-body"
                                                         " sort-by-rating']"
                                                         "//td[@class='js-sorter-sort-field"
                                                         " js-sorter-sort-field-outfielderBlock"
                                                         " player-stat-outfielderBlock ']")
    player_interceptions = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-defence"
                                                         " tab-pane  active']"
                                                         "//table[@class='table table--statistics js-sorter-body"
                                                         " sort-by-rating']"
                                                         "//td[@class='js-sorter-sort-field"
                                                         " js-sorter-sort-field-interceptionWon"
                                                         " player-stat-interceptionWon ']")
    player_tackles = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-defence tab-pane"
                                                   "  active']"
                                                   "//table[@class='table table--statistics js-sorter-body"
                                                   " sort-by-rating']"
                                                   "//td[@class='js-sorter-sort-field js-sorter-sort-field-totalTackle"
                                                   " player-stat-totalTackle ']")
    player_notes = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-defence tab-pane"
                                                 "  active']"
                                                 "//table[@class='table table--statistics js-sorter-body"
                                                 " sort-by-rating']"
                                                 "//td[@class='js-sorter-sort-field js-sorter-sort-field-notes"
                                                 " player-stat-notes u-fs11']")
    player_position = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-defence tab-pane"
                                                    "  active']"
                                                    "//table[@class='table table--statistics js-sorter-body"
                                                    " sort-by-rating']"
                                                    "//td[@class='js-sorter-sort-field js-sorter-sort-field-position"
                                                    " player-stat-position ']")
    player_rating = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-defence tab-pane"
                                                  "  active']"
                                                  "//table[@class='table table--statistics js-sorter-body"
                                                  " sort-by-rating']"
                                                  "//td[@class='js-sorter-sort-field js-sorter-sort-field-rating"
                                                  " player-stat-rating ']")

    player_objects = list()
    for i in range(len(player_names)):
        player_objects.append([player_names[i].text, player_clearances[i].text, player_shots_blocked[i].text,
                               player_interceptions[i].text, player_tackles[i].text, player_notes[i].text,
                               player_position[i].text, player_rating[i].text])
    players = pd.DataFrame(player_objects)
    players.columns = ['Player', 'Clearances', 'Blocked shots', 'Interceptions', 'Tackles', 'Notes (Defending)',
                       'Position', 'Rating']
    if save:
        players.to_csv('defendingStats.csv', sep=',', line_terminator='\n')
        print('Defending stats collected successfully')
    else:
        print('Defending stats collected successfully')
        return players


def get_passing_stats(driver, save):
    driver.find_element_by_xpath("//a[@class='js-squad-stats-groups-nav-tab player-stat-group-passing']").click()
    player_names = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-passing tab-pane"
                                                 "  active']"
                                                 "//table[@class='table table--statistics js-sorter-body"
                                                 " sort-by-rating']//td[@class='u-tL ff-medium"
                                                 " player-stat-player-name']")

    player_passes_info = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-passing tab-pane"
                                                  "  active']"
                                                  "//table[@class='table table--statistics js-sorter-body"
                                                  " sort-by-rating']"
                                                  "//td[@class='js-sorter-sort-field js-sorter-sort-field-accuratePass"
                                                  " player-stat-accuratePass ']")
    player_key_passes = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-passing tab-pane"
                                                      "  active']"
                                                      "//table[@class='table table--statistics js-sorter-body"
                                                      " sort-by-rating']"
                                                      "//td[@class='js-sorter-sort-field js-sorter-sort-field-keyPass"
                                                      " player-stat-keyPass ']")
    player_crosses_info = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-passing tab-pane"
                                                   "  active']"
                                                   "//table[@class='table table--statistics js-sorter-body"
                                                   " sort-by-rating']"
                                                   "//td[@class='js-sorter-sort-field js-sorter-sort-field-totalCross"
                                                   " player-stat-totalCross ']")
    player_long_balls_info = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-passing tab-pane"
                                                      "  active']"
                                                      "//table[@class='table table--statistics js-sorter-body"
                                                      " sort-by-rating']"
                                                      "//td[@class='js-sorter-sort-field"
                                                      " js-sorter-sort-field-totalLongBalls"
                                                      " player-stat-totalLongBalls ']")
    player_notes = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-passing tab-pane"
                                                 "  active']"
                                                 "//table[@class='table table--statistics js-sorter-body"
                                                 " sort-by-rating']"
                                                 "//td[@class='js-sorter-sort-field js-sorter-sort-field-notes"
                                                 " player-stat-notes u-fs11']")
    player_position = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-passing tab-pane"
                                                    "  active']"
                                                    "//table[@class='table table--statistics js-sorter-body"
                                                    " sort-by-rating']"
                                                    "//td[@class='js-sorter-sort-field js-sorter-sort-field-position"
                                                    " player-stat-position ']")
    player_rating = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-passing tab-pane"
                                                  "  active']"
                                                  "//table[@class='table table--statistics js-sorter-body"
                                                  " sort-by-rating']"
                                                  "//td[@class='js-sorter-sort-field js-sorter-sort-field-rating"
                                                  " player-stat-rating ']")

    player_objects = list()
    for i in range(len(player_names)):
        player_passes, player_pass_accuracy = player_passes_info[i].text.split('(')
        player_passes = player_passes[:-1]
        player_pass_accuracy = player_pass_accuracy[:-2]
        player_crosses, player_crosses_successful = player_crosses_info[i].text.split('(')
        player_crosses = player_crosses[:-1]
        player_crosses_successful = player_crosses_successful[:-1]
        player_long_balls, player_long_balls_successful = player_long_balls_info[i].text.split('(')
        player_long_balls = player_long_balls[:-1]
        player_long_balls_successful = player_long_balls_successful[:-1]
        player_objects.append([player_names[i].text, player_passes, player_pass_accuracy,
                               player_key_passes[i].text,
                               player_crosses, player_crosses_successful,
                               player_long_balls, player_long_balls_successful, player_notes[i].text,
                               player_position[i].text, player_rating[i].text])
    players = pd.DataFrame(player_objects)
    players.columns = ['Player', 'Passes', 'Pass accuracy', 'Key passes', 'Crosses', 'Successful crosses', 'Long balls', 'Successful long balls',
                       'Notes (Passing)', 'Position', 'Rating']
    if save:
        players.to_csv('passingStats.csv', sep=',', line_terminator='\n')
        print('Passing stats collected successfully')
    else:
        print('Passing stats collected successfully')
        return players


def get_duel_stats(driver, save):
    driver.find_element_by_xpath("//a[@class='js-squad-stats-groups-nav-tab player-stat-group-duels']").click()
    player_names = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-duels tab-pane"
                                                 "  active']"
                                                 "//table[@class='table table--statistics js-sorter-body"
                                                 " sort-by-rating']"
                                                 "//td[@class='u-tL ff-medium player-stat-player-name']")

    player_duels_info = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-duels tab-pane"
                                                 "  active']"
                                                 "//table[@class='table table--statistics js-sorter-body"
                                                 " sort-by-rating']"
                                                 "//td[@class='js-sorter-sort-field js-sorter-sort-field-totalDuels"
                                                 " player-stat-totalDuels ']")
    player_dispossessed = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-duels tab-pane"
                                                        "  active']"
                                                        "//table[@class='table table--statistics js-sorter-body"
                                                        " sort-by-rating']"
                                                        "//td[@class='js-sorter-sort-field"
                                                        " js-sorter-sort-field-dispossessed"
                                                        " player-stat-dispossessed ']")
    player_fouled = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-duels tab-pane"
                                                  "  active']"
                                                  "//table[@class='table table--statistics"
                                                  " js-sorter-body sort-by-rating']"
                                                  "//td[@class='js-sorter-sort-field js-sorter-sort-field-wasFouled"
                                                  " player-stat-wasFouled ']")
    player_fouls = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-duels tab-pane"
                                                 "  active']"
                                                 "//table[@class='table table--statistics js-sorter-body"
                                                 " sort-by-rating']"
                                                 "//td[@class='js-sorter-sort-field js-sorter-sort-field-fouls"
                                                 " player-stat-fouls ']")
    player_position = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-duels tab-pane"
                                                    "  active']"
                                                    "//table[@class='table table--statistics js-sorter-body"
                                                    " sort-by-rating']"
                                                    "//td[@class='js-sorter-sort-field js-sorter-sort-field-position"
                                                    " player-stat-position ']")
    player_rating = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-duels tab-pane"
                                                  "  active']"
                                                  "//table[@class='table table--statistics js-sorter-body"
                                                  " sort-by-rating']"
                                                  "//td[@class='js-sorter-sort-field js-sorter-sort-field-rating"
                                                  " player-stat-rating ']")

    player_objects = list()
    for i in range(len(player_names)):
        player_duels, player_duels_won = player_duels_info[i].text.split('(')
        player_duels = player_duels[:-1]
        player_duels_won = player_duels_won[:-1]
        print(player_names[i].text, player_fouled[i].text, player_fouls[i].text, player_position[i].text)
        player_objects.append([player_names[i].text, player_duels, player_duels_won, player_dispossessed[i].text,
                               player_fouled[i].text, player_fouls[i].text, player_position[i].text,
                               player_rating[i].text])
    players = pd.DataFrame(player_objects)
    players.columns = ['Player', 'Duels', 'Duels won', 'Dispossessions', 'Fouled', 'Fouls', 'Position', 'Rating']
    if save:
        players.to_csv('duelStats.csv', sep=',', line_terminator='\n')
        print('Duel stats collected successfully')
    else:
        print('Duel stats collected successfully')
        return players


def get_goalkeeping_stats(driver, save):
    driver.find_element_by_xpath("//a[@class='js-squad-stats-groups-nav-tab player-stat-group-goalkeeper']").click()
    player_names = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-goalkeeper tab-pane"
                                                 "  active']"
                                                 "//table[@class='table table--statistics js-sorter-body"
                                                 " sort-by-rating']"
                                                 "//td[@class='u-tL ff-medium player-stat-player-name']")

    player_saves = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-goalkeeper tab-pane"
                                                 "  active']"
                                                 "//table[@class='table table--statistics js-sorter-body"
                                                 " sort-by-rating']"
                                                 "//td[@class='js-sorter-sort-field js-sorter-sort-field-saves"
                                                 " player-stat-saves ']")
    player_punches = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-goalkeeper tab-pane"
                                                   "  active']"
                                                   "//table[@class='table table--statistics js-sorter-body"
                                                   " sort-by-rating']"
                                                   "//td[@class='js-sorter-sort-field js-sorter-sort-field-punches"
                                                   " player-stat-punches ']")
    player_run_outs_info = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-goalkeeper tab-pane"
                                                    "  active']"
                                                    "//table[@class='table table--statistics js-sorter-body"
                                                    " sort-by-rating']"
                                                    "//td[@class='js-sorter-sort-field js-sorter-sort-field-runsOut"
                                                    " player-stat-runsOut ']")
    player_high_claims = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-goalkeeper"
                                                       " tab-pane  active']"
                                                       "//table[@class='table table--statistics js-sorter-body"
                                                       " sort-by-rating']"
                                                       "//td[@class='js-sorter-sort-field"
                                                       " js-sorter-sort-field-goodHighClaim"
                                                       " player-stat-goodHighClaim ']")
    player_notes = driver.find_elements_by_xpath("//div[@class='js-sorter-group js-sorter-group-goalkeeper tab-pane"
                                                 "  active']"
                                                 "//table[@class='table table--statistics js-sorter-body"
                                                 " sort-by-rating']"
                                                 "//td[@class='js-sorter-sort-field js-sorter-sort-field-notes"
                                                 " player-stat-notes u-fs11']")

    player_objects = list()
    for i in range(len(player_names)):
        player_run_outs, player_run_outs_successful = player_run_outs_info[i].text.split('(')
        player_run_outs = player_run_outs[:-1]
        player_run_outs_successful = player_run_outs_successful[:-1]
        player_objects.append([player_names[i].text, player_saves[i].text, player_punches[i].text,
                               player_run_outs, player_run_outs_successful, player_high_claims[i].text,
                               player_notes[i].text])
    players = pd.DataFrame(player_objects)
    players.columns = ['Player', 'Saves', 'Punches', 'Run-outs',
                       'Successful run-outs', 'High claims',
                       'Notes (Goalkeeping)'
                       ]
    if save:
        players.to_csv('goalkeepingStats.csv', sep=',', line_terminator='\n')
        print('Goalkeeping stats collected successfully')
    else:
        print('Goalkeeping stats collected successfully')
        return players


def collect_data(driver):
    summary_stats = get_summary_stats(driver, False)
    attacking_stats = get_attacking_stats(driver, False)
    matches = [item for item in summary_stats.columns if
               item in attacking_stats.columns]
    total_stats = pd.merge(summary_stats, attacking_stats, on=matches)
    defending_stats = get_defending_stats(driver, False)
    matches = [item for item in total_stats.columns if
               item in defending_stats.columns]
    total_stats = pd.merge(total_stats, defending_stats, on=matches)
    passing_stats = get_passing_stats(driver, False)
    matches = [item for item in total_stats.columns if
               item in passing_stats.columns]
    total_stats = pd.merge(total_stats, passing_stats, on=matches)
    duel_stats = get_duel_stats(driver, False)
    matches = [item for item in total_stats.columns if
               item in duel_stats.columns]
    total_stats = pd.merge(total_stats, duel_stats, on=matches)
    goalkeeping_stats = get_goalkeeping_stats(driver, False)
    total_stats = pd.merge(total_stats, goalkeeping_stats, on='Player',
                           how='outer')
    total_stats.replace(np.nan, '-', inplace=True)
    total_stats.to_csv('totalStats.csv', sep=',', line_terminator='\n',
                       encoding='utf-8')


chromepath = "selenium/webdriver/chrome/chromedriver.exe"
driver = webdriver.Chrome(chromepath)
links = [
    'https://www.sofascore.com/getafe-celta-vigo/wgbsjhb',
    'https://www.sofascore.com/leganes-real-madrid/EgbsVgb',
    'https://www.sofascore.com/deportivo-la-coruna-espanyol/ogbsHgb',
    'https://www.sofascore.com/eibar-celta-vigo/wgbsOgb',
    'https://www.sofascore.com/deportivo-alaves-real-madrid/EgbsKhb'
]
for link in links:
    driver.get(link)
    driver.find_element_by_xpath("//li[@class='nav__item hidden-mobile']").click()
    collect_data(driver)
