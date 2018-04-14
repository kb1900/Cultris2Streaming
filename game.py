import pyautogui
import os
import time
from web import Web
from pywinauto import Application
import win32ui




class Game():
	@staticmethod
	def startup_login():
		#openc2
		try:
			if win32ui.FindWindow("LWJGL", None):
				print("its running")
		except win32ui.error:
			print("its not running!")
			os.startfile("C:\Program Files (x86)\Cultris II\Cultris II.exe")
		time.sleep(25)

		pyautogui.press('enter')  # press the Enter key
		pyautogui.press('enter')  # press the Enter key
		pyautogui.press('enter')  # press the Enter key
		#sleep waiting to log in
		time.sleep(4)
		#we will use a guest account
		pyautogui.press('right')  # press the Rightarrow key
		pyautogui.press('enter')  # press the Enter key
		pyautogui.press('enter')  # press the Enter key

		return True
	@staticmethod
	def find_correct_room(roomid):
		app = Application().connect(class_name="LWJGL")
		app.top_window().set_focus()

		finding_player_room = True
		down_count = 3
		print('finding correct room')
		while finding_player_room == True:
			if roomid == 0:
				Game.ffa() #bot enters FFA and F4's
				if Game.is_correct_room() == True:
					print('success, recording bot is in the correct room.')
					finding_player_room = False
			else:
				print('player not in ffa, finding room...')
				Game.enter_room(down_count)

			if Game.is_correct_room() == True:
				print('success, recording bot is in the correct room.')
				finding_player_room = False

			else:
				down_count = down_count+1
				Game.exitroom()
		return True


	@staticmethod
	def is_correct_room():
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
			return True
		else:
			return False


	@staticmethod
	def ffa():
		pyautogui.press('enter')
		pyautogui.press('enter')

		time.sleep(2)
		pyautogui.press('enter')
		time.sleep(2)
		pyautogui.press('f4')  # press the F4 key
		pyautogui.press('f4')  # press the F4 key


	@staticmethod
	def enter_room(down_count):
		for i in range(down_count):
			pyautogui.press('down')
			time.sleep(0.3)



		pyautogui.press('enter')
		pyautogui.press('enter')
		pyautogui.press('enter')


		time.sleep(2)

		pyautogui.press('enter')
		time.sleep(4)
		pyautogui.press('f4')  # press the F4 key
		time.sleep(10)

	@staticmethod
	def exitroom():
		pyautogui.press('escape')
		pyautogui.press('enter')

	@staticmethod
	def nextroom():
		pyautogui.press('down')
		#pyautogui.press('down')

		pyautogui.press('enter')
		pyautogui.press('enter')

		pyautogui.press('f4')  # press the F4 key
		pyautogui.press('f4')  # press the F4 key
		time.sleep(10)
	@staticmethod
	def startstream():
		#print('starting stream now')
		pyautogui.click(x=1897, y=889)

		print('stream has begun!')
	@staticmethod
	def stopstream():
		pyautogui.click(x=1897, y=889)
		pyautogui.click(x=1845, y=57)
		print('stream has ended!')
