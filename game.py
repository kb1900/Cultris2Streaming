import pyautogui
import os
import time

class Game():
	@staticmethod
	def startup_login():
		#openc2
		os.startfile("C:\Program Files (x86)\Cultris II\Cultris II.exe")
		time.sleep(20)

		pyautogui.press('enter')  # press the Enter key
		pyautogui.press('enter')  # press the Enter key
		pyautogui.press('enter')  # press the Enter key
		#sleep waiting to log in
		time.sleep(4)
		#we will use a guest account
		pyautogui.press('right')  # press the Rightarrow key
		pyautogui.press('enter')  # press the Enter key
		pyautogui.press('enter')  # press the Enter key


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
