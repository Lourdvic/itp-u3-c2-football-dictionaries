def players_by_country_and_position(squads_list):
    player_dict = {}
    for pos, players in squads_list.items():
        for player in players:
            country = player['country']
            player_dict.setdefault(country, player_dict.setdefault(pos, []))
            player_dict = {country : pos for (pos, players) in squads_list.items()}
    return player_dict
        
            #for country in pos:
              #  print(player['country'])
            #player_dict.setdefault(country, [])
        #player_dict[country].append(position)
        
    #return player_dict

SQUADS_DATA = {'GK': [{'number': '1', 'position': 'GK', 'name': 'Juan Botasso', 'date_of_birth': '(1908-10-23)23 October 1908 (aged 21)', 'caps': '', 'club': 'Quilmes', 'country': 'Argentina', 'club_country': 'Argentina', 'year': '1930'}, 
{'number': '-', 'position': 'GK', 'name': 'Jean De Bie', 'date_of_birth': '(1892-05-09)9 May 1892 (aged 38)', 'caps': '37', 'club': 'Royal Racing Club de Bruxelles', 'country': 'Belgium', 'club_country': 'Belgium', 'year': '1930'}], 'FW': [{'number': '9', 'position': 'FW', 'name': 'Roberto Cherro', 'date_of_birth': '(1907-02-23)23 February 1907 (aged 23)', 'caps': '', 'club': 'Boca Juniors', 'country': 'Argentina', 'club_country': 'Argentina', 'year': '1930'}, {'number': '-', 'position': 'FW', 'name': 'Lee Keun-Ho', 'date_of_birth': '(1985-04-11)11 April 1985 (aged 29)', 'caps': '62', 'club': 'Sangju Sangmu', 'country': 'South Korea', 'club_country': 'South Korea', 'year': '2014'}, {'number': '-', 'position': 'FW', 'name': 'Koo Ja-Cheol', 'date_of_birth': '(1989-02-27)27 February 1989 (aged 25)', 'caps': '35', 'club': 'Mainz 05', 'country': 'South Korea', 'club_country': 'Germany', 'year': '2014'}, {'number': '-', 'position': 'FW', 'name': 'Kim Shin-Wook', 'date_of_birth': '(1988-04-14)14 April 1988 (aged 26)', 'caps': '26', 'club': 'Ulsan Hyundai', 'country': 'South Korea', 'club_country': 'South Korea', 'year': '2014'}], 'MF': [{'number': '-', 'position': 'MF', 'name': 'Pierre Braine', 'date_of_birth': '(1900-10-26)26 October 1900 (aged 29)', 'caps': '42', 'club': 'Royal Beerschot AC', 'country': 'Belgium', 'club_country': 'Belgium', 'year': '1930'}, {'number': '-', 'position': 'MF', 'name': 'Alexis Chantraine', 'date_of_birth': '(1901-03-16)16 March 1901 (aged 29)', 'caps': '0', 'club': 'Royal FC Liegeois', 'country': 'Belgium', 'club_country': 'Belgium', 'year': '1930'}, {'number': '-', 'position': 'MF', 'name': 'Oscar', 'date_of_birth': '(1991-09-09)9 September 1991 (aged 22)', 'caps': '29', 'club': 'Chelsea', 'country': 'Brazil', 'club_country': 'England', 'year': '2010'}, {'number': '-', 'position': 'MF', 'name': 'Paulinho', 'date_of_birth': '(1988-07-25)25 July 1988 (aged 25)', 'caps': '25', 'club': 'Tottenham Hotspur', 'country': 'Brazil', 'club_country': 'England', 'year': '2010'}, {'number': '-', 'position': 'MF', 'name': 'Hernanes', 'date_of_birth': '(1985-05-29)29 May 1985 (aged 29)', 'caps': '23', 'club': 'Internazionale', 'country': 'Brazil', 'club_country': 'Italy', 'year': '2014'}, {'number': '-', 'position': 'MF', 'name': 'Luiz Gustavo', 'date_of_birth': '(1987-07-23)23 July 1987 (aged 26)', 'caps': '17', 'club': 'VfL Wolfsburg', 'country': 'Brazil', 'club_country': 'Germany', 'year': '2014'}, {'number': '-', 'position': 'MF', 'name': 'Fernandinho', 'date_of_birth': '(1985-05-04)4 May 1985 (aged 29)', 'caps': '6', 'club': 'Manchester City', 'country': 'Brazil', 'club_country': 'England', 'year': '2014'}, {'number': '-', 'position': 'MF', 'name': 'Willian', 'date_of_birth': '(1988-08-09)9 August 1988 (aged 25)', 'caps': '5', 'club': 'Chelsea', 'country': 'Brazil', 'club_country': 'England', 'year': '2014'}]}

#print(players_by_country_and_position(SQUADS_DATA))

def test_assignment_3():
    result = players_by_country_and_position(SQUADS_DATA)
    assert len(result) == 4

    expected_countries = {'Argentina', 'Belgium', 'Brazil', 'South Korea'}
    assert set(result.keys()) == expected_countries

    # Argentina
    argentina = result['Argentina']
    assert len(argentina) == 2

    ar_goalkeepers = argentina['GK']
    ar_forwards = argentina['FW']
    assert len(ar_goalkeepers) == 1
    assert len(ar_forwards) == 1

    # Brazil

    brazil = result['Brazil']
    assert len(brazil) == 1  # Only midfielders

    br_midfielders = brazil['MF']
    assert len(br_midfielders) == 6

    assert br_midfielders[0] == {
        'caps': '29',
        'club': 'Chelsea',
        'club_country': 'England',
        'country': 'Brazil',
        'date_of_birth': '(1991-09-09)9 September 1991 (aged 22)',
        'name': 'Oscar',
        'number': '-',
        'position': 'MF',
        'year': '2010'
    }

    assert br_midfielders[-1] == {
        'caps': '5',
        'club': 'Chelsea',
        'club_country': 'England',
        'country': 'Brazil',
        'date_of_birth': '(1988-08-09)9 August 1988 (aged 25)',
        'name': 'Willian',
        'number': '-',
        'position': 'MF',
        'year': '2014'
    }

print(test_assignment_3())