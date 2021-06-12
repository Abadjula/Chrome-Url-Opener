import time
import os

url = input("Enter the url: ")

while True:
	os.system(f"start chrome.exe {url}")
	print(f"Opened google and went to this url: {url} - opening a new one in the next 30 seconds")
	time.sleep(30)