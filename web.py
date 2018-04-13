import urllib.request, json
import requests

class Web():
    @staticmethod
    def get_web_data():
        url = urllib.request.urlopen("http://gewaltig.net/liveinfo.aspx")
        values = json.load(url)
        return values

    @staticmethod
    def check_player_status(player_name, players_online, rooms):

        if player_name in players_online:

            index = players_online.index(player_name)
            room_index = index + 1
            afk_index = index + 2

            roomid = players_online[room_index]
            afk = players_online[afk_index]

            if roomid is False:
                print(player_name,'is  online but not in a room')
                online = 'status_three' #offline
            else:
                #if roomid !=0:
                roomname_index = rooms.index(roomid) + 1
                roomname = rooms[roomname_index]

                if afk == False:
                    online =  'status_one' #online and not afk
                    print(player_name, 'is online and playing in room:', roomname)

                elif afk == True:
                    online =  'status_two' #online but afk
                    print(player_name, 'is online and afk in room:', roomname)


        else:
            print(player_name,'is offline')
            online = 'status_three' #offline
            roomid = False
        status = [online, roomid]
        return status
