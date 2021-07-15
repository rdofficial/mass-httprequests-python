"""
main.py - Mass HTTP Requests

This script serves the functionality of sending mass HTTP GET requests on an user specified URL, also with the amount of requests being user decided. The script uses the requests module in order to power the GET requests.

Author : Rishav Das (https://github.com/rdofficial/)
Created on : July 15, 2021

Last modified by : -
Last modified on : -

Authors contributed to this script (Add your name below if you have contributed) :
1. Rishav Das (github:https://github.com/rdofficial/, email:rdofficial192@gmail.com)
"""

# Importing the required functions and modules
import requests
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from base64 import b64decode

def request(url, index):
	""" This function serves the functionality of executing a HTTP GET request on the user specified URL and then returns the response code back. If there are any errors encountered during the process, then the error message is returned instead of regular result. """

	try:
		html = requests.get(url, stream = True)
		return f'[Request no-{index + 1}] Response code : {html.status_code}'
	except KeyboardInterrupt:
		exit()
	except requests.exceptions.RequestException as e:
		return f'[Request no-{index + 1}] Error encountered : {e}'

def runner(url, index):
	""" This function serves the functionality of starting multiple threads of running an another function request(), as well as displays the result of the function on the console screen. This function takes in 2 arguments : url, index. The url argument is the URL of the website or webpage specified by the user to send mass HTTP requests. """

	threads = []
	with ThreadPoolExecutor(max_workers = 20) as executor:
		try:
			for i in range(index):
				file_name = uuid.uuid1()
				threads.append(executor.submit(request, url, i))
            
			for task in as_completed(threads):
				print(task.result())
		except KeyboardInterrupt:
			exit()

try:
	# Asking the user for the URL of the website or webpage
	url = input('Enter the URL : ')

	# Asking the user to enter the amount of requests to be sent
	amount = int(input('Enter the amount of requests to be sent : '))

	# Calling the runner() function to start the process
	runner(url, amount)
except Exception as e:
	# If there are any errors encountered during the process, then we display the error message on the console screen and exit

	print(f'[ Error : {e} ]')
	exit()
