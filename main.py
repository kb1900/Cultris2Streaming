from web import Web
from game import Game
import time
import pyautogui

running = True
while running == True:
    try:
        online_status = 'status_three'
        streaming = False

        while online_status == 'status_three' or online_status == 'status_two':
            values = Web.get_web_data()
            players_online = []
            rooms = []

            for room in values['rooms']:
                rooms.append(room['id'])
                rooms.append(room['name'])

            for player in values['players']:
                players_online.append(player['name'])
                players_online.append(player['room'])
                players_online.append(player['afk'])

            status = Web.check_player_status(player_name='кв σғ υsα',players_online=players_online,rooms=rooms)
            online_status = status[0]

        if online_status == 'status_one':
            roomid = status[1]

            print('roomid is', roomid)
            Game.startup_login()
            finding_player_room = True
            down_count = 4
            while finding_player_room == True:

                if roomid == 0:
                    Game.ffa()
                    values = Web.get_web_data()
                    players_online = []
                    rooms = []

                    for room in values['rooms']:
                        rooms.append(room['id'])
                        rooms.append(room['name'])

                    for player in values['players']:
                        players_online.append(player['name'])
                        players_online.append(player['room'])
                        players_online.append(player['afk'])
                    status = Web.check_player_status(player_name='кв σғ υsα',players_online=players_online,rooms=rooms)
                    roomid = status[1]
                    bot_status = Web.check_player_status(player_name='recording',players_online=players_online,rooms=rooms)
                    bot_online_status = bot_status[0]
                    bot_roomid = bot_status[1]
                    if roomid == bot_roomid:
                        print('success, recording bot is in the correct room.')
                        finding_player_room = False
                else:
                    Game.enter_room(down_count)
                    values = Web.get_web_data()
                    players_online = []
                    rooms = []

                    for room in values['rooms']:
                        rooms.append(room['id'])
                        rooms.append(room['name'])

                    for player in values['players']:
                        players_online.append(player['name'])
                        players_online.append(player['room'])
                        players_online.append(player['afk'])

                    status = Web.check_player_status(player_name='кв σғ υsα',players_online=players_online,rooms=rooms)
                    roomid = status[1]
                    bot_status = Web.check_player_status(player_name='recording',players_online=players_online,rooms=rooms)
                    bot_online_status = bot_status[0]
                    bot_roomid = bot_status[1]
                if roomid == bot_roomid:
                    print('success, recording bot is in the correct room.')
                    finding_player_room = False
                else:
                    down_count = down_count + 1
                    Game.exitroom()
                            #we escape + enter -> downarrow + enter - > repeat
        while finding_player_room == False:
            Game.startstream()
            streaming = True
            while streaming == True:
                time.sleep(10)
                values = Web.get_web_data()
                players_online = []
                rooms = []

                for room in values['rooms']:
                    rooms.append(room['id'])
                    rooms.append(room['name'])

                for player in values['players']:
                    players_online.append(player['name'])
                    players_online.append(player['room'])
                    players_online.append(player['afk'])
                status = Web.check_player_status(player_name='кв σғ υsα',players_online=players_online,rooms=rooms)
                roomid = status[1]
                bot_status = Web.check_player_status(player_name='recording',players_online=players_online,rooms=rooms)
                bot_online_status = bot_status[0]
                bot_roomid = bot_status[1]
                if status[0] == 'status_three' or bot_status[0] == 'status_three':
                    Game.stopstream()
                    online_status = 'status_three'
                    finding_player_room = True
                    streaming = False
                elif roomid == bot_roomid:
                    if status[0] == 'status_one' or status[0] == 'status_two':
                        print('recording bot is in the correct room, continuing stream!')
                elif status[0] != 'status_one' or roomid != bot_roomid:
                    Game.stopstream()
                    online_status = 'status_three'
                    finding_player_room = True
                    streaming = False
    except Exception as e:
        print(e)
        running = False
        running = True
