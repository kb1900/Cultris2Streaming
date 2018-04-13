from web import Web
from game import Game
import time
import pyautogui

running = True
while running == True:
    try:

        online_status = 'status_three' 
        streaming = False

        #we want to generate the liveinfo.aspx data and parse it @ status_three or status_two
        while online_status == 'status_three' or online_status == 'status_two': 
            #values stores all the web data available
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

            #check_player_status returns an array with the status of the user [0], and roomid [1]
            #status_one: player is online and NOT AFK
            #status_two: player is online but AFK
            #status_three: player is offline OR player is online but not in a room
            status = Web.check_player_status(player_name='кв σғ υsα',players_online=players_online,rooms=rooms)
            online_status = status[0]

        if online_status == 'status_one': #player is online and not afk
            roomid = status[1]

            print('roomid is', roomid)
            Game.startup_login() #opens C2 and logs in
            finding_player_room = True
            down_count = 4 #how many 'down presses' the bot will do in finding the correct room, if it is not ffa
            while finding_player_room == True:

                if roomid == 0:
                    Game.ffa() #bot enters FFA and F4's
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

                    #we are requering the web data such that we can confirm the bot and the player are in the same room - shuld be refactored
                    status = Web.check_player_status(player_name='кв σғ υsα',players_online=players_online,rooms=rooms)
                    roomid = status[1]
                    bot_status = Web.check_player_status(player_name='recording',players_online=players_online,rooms=rooms)
                    bot_online_status = bot_status[0]
                    bot_roomid = bot_status[1]

                    #check if room is correct
                    if roomid == bot_roomid:
                        print('success, recording bot is in the correct room.')
                        finding_player_room = False #exit loop
                #else, we need to go down 4 rooms (1 = ffa, 2= rookieplayground, 3 = cheese, 4 = first room to check)
                else:
                    Game.enter_room(down_count) #enters the 'down_count' room
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
                    
                    #we are requering the web data such that we can confirm the bot and the player are in the same room - shuld be refactored
                    status = Web.check_player_status(player_name='кв σғ υsα',players_online=players_online,rooms=rooms)
                    roomid = status[1]
                    bot_status = Web.check_player_status(player_name='recording',players_online=players_online,rooms=rooms)
                    bot_online_status = bot_status[0]
                    bot_roomid = bot_status[1]

                #check if room is correct
                if roomid == bot_roomid:
                    print('success, recording bot is in the correct room.')
                    finding_player_room = False #exit loop
               #if the room is not correct, we need to check the next room (5th room, 6th...etc.)
                else:
                    down_count = down_count + 1
                    Game.exitroom()
                            #we escape + enter -> downarrow + enter - > repeat
       
        #the bot and the player are confirmed to be in the same room
        while finding_player_room == False:
            Game.startstream()
            streaming = True

            #while streaming is True, we want to continually check that the player is offline ever 10 seconds.
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
                

                #we are requering the web data such that we can confirm the bot and the player are in the same room - shuld be refactored
                status = Web.check_player_status(player_name='кв σғ υsα',players_online=players_online,rooms=rooms)
                roomid = status[1]
                bot_status = Web.check_player_status(player_name='recording',players_online=players_online,rooms=rooms)
                bot_online_status = bot_status[0]
                bot_roomid = bot_status[1]

                #if the player is offline or the bot somehow ends up offline (DC), it will stop the stream, reset variables such that the script starts over
                if status[0] == 'status_three' or bot_status[0] == 'status_three':
                    Game.stopstream()
                    online_status = 'status_three'
                    finding_player_room = True
                    streaming = False

                #if the check passes, the stream continues
                elif roomid == bot_roomid:
                    if status[0] == 'status_one' or status[0] == 'status_two':
                        print('recording bot is in the correct room, continuing stream!')

                #if the player is not online/actively playing OR if the bot's roomid is incorrect, it will stop the stream, reset variables such that the script starts over
                elif status[0] != 'status_one' or roomid != bot_roomid:
                    Game.stopstream()
                    online_status = 'status_three'
                    finding_player_room = True
                    streaming = False
    #some times the web query fails, in which case the error is printed and the script continues
    except Exception as e:
        print(e)
        running = False
        running = True
