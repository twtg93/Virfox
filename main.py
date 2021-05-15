import time, sys, os
from selenium import webdriver

def slow_print(string):
	for letter in(string):
		sys.stdout.write(letter)
		time.sleep(0.03)
		sys.stdout.flush()
	print()

slow_print('Loading, please wait...')
time.sleep(1)
os.system('clear')

print('\033[91mPlease beware of the threat of\nXSS, DoS, and DDoS attacks while browsing.')
print("\33[37mCookies, site data, bookmarks, browsing history, and form data will not be saved when you're done browsing.")
driver = webdriver.Firefox()
