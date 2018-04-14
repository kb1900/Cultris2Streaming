# Cultris2 Streaming Bot
An attempt to create an autonomous streaming program for Cultris 2


# Dependencies: 
Python3, Pyautogui, pywinauto (pip install pywinauto)


# To do:
* Refactoring of code (quite messy at the moment)
* Minimize pyautogui automation -> use a new method to start/stop stream with OBS (current method uses coords and a simulated mouse click)
* Create a hierarchy of what to stream and when (i.e. If there are >5 players in FFA and user is offline, stream FFA. Else, wait for user to be online)
* Create a second C2 instance to display stats on stream 24/7 (should just be some c+p)
* ~Bot should not restart stream if user changes rooms~
