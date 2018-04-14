from web import Web
from game import Game
import time
import pyautogui
from pywinauto import Application

i = 1
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

            print(i)
            #print('roomid is', roomid)
            print('starting game')
            Game.startup_login()
            Game.find_correct_room(roomid=roomid)

            #the bot and the player are confirmed to be in the same room
            Game.startstream()
            streaming = True
            app = Application().connect(class_name="LWJGL")
            app.top_window().set_focus()

            #while streaming is True, we want to continually check that the player is offline every 20 seconds.
            while streaming == True:
                time.sleep(20)
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
                    streaming = False

                #if the check passes, the stream continues
                elif Game.is_correct_room() == True:
                    if status[0] == 'status_one' or status[0] == 'status_two':
                        print('recording bot is in the correct room, continuing stream!')

                elif Game.is_correct_room() == False:
                    if status[0] == 'status_one' or status[0] == 'status_two':
                        print('bot is not in correct room but player is still online! Continuing stream and finding correct room...')
                        Game.find_correct_room(roomid=roomid)

    #some times the web query fails, in which case the error is printed and the script continues
    except Exception as e:
        print(e)
        running = False
        running = True
