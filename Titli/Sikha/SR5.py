#!/usr/bin/python

###
# Asset Name: SHIKHA
# Version : 1.0
# Code Developed by: NAST Team
# Code Developper: Suhas Bhatt ML
# This framework recognises voice and retrieves tool based information:
# Tools:
# 1. ServiceNow : Below are the available options
#    A. Incident: All Incidents, Resolved Incidents
#    B. Problem: All Problems, Open problems
# Usage examples:
# Run the python script, follow the displayed instructions and voice in the option.
#
# For More information on the Asset contact:
# 	daya.krishna.suyal, nikhil.a.sureka, zubeen.shaikh, suhas.m.l.bhatt
# 
#
###
### Importing Modules
try:
    import speech_recognition as sr
    import win32com.client as wincl
    import requests
    import json
    import os
    import sqlite3
    import array
    import sys
    import time
    import threading
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

except ModuleNotFoundError as e:
    print(f"Your system is missing the required package as : {e}")
    print("-" * 10)
    print('''tips:
                use pip3 install (Python2.7)
                        or
                use pip install (Python3+)''')
    print("-" * 10)



chromedriver = 'C:\\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)
browser.maximize_window()
###



#calling authentication function from auth.py
from auth import auth

#calling nltk function from nltk_process.py
from nltk_process import preprocess_Text

#Rest URI for connecting ServiceNow
baseUrl = 'https://dev57834.service-now.com/'

#Credentials for connecting ServiceNow
user = 'Admin'
pwd = 'Nast@4321'

#rest header
headers = {"Content-Type":"application/json","Accept":"application/json"}

# clear screen
clear = lambda: os.system('cls')

#db call 
conn = sqlite3.connect('shikha.db')
c = conn.cursor()

#VoiceOut
def voiceOut(toolResponse):
	speak = wincl.Dispatch("SAPI.SpVoice")
	speak.Speak(toolResponse)
	


# listen1 function get audio from the microphone  
r = sr.Recognizer()
def listen1 (data1):
	with sr.Microphone() as source:
		print(data1)                                                                                   
		audio = r.listen(source) 
	return audio
	
# listen2 function recognises the speech and exits after 3 failed trials 
def listen2 (data2):
	i = 0
	select = "exit"	
	while i < 3:
		audio = listen1 (data2)	
		try:
			#print("You said " + r.recognize_google(audio))
			select = r.recognize_google(audio)
			break
		except sr.UnknownValueError:
			print("\nCould not understand audio please say again\n")
			voiceOut('Sorry i Could not understand the audio, can you please say again')
			i += 1
		except sr.RequestError as e:
			print("Could not process request; {0}".format(e))
	if select == "exit":
		print("\nMaximum number of trials exceeded,\nThank you for connecting")
		voiceOut('I am very sorry, i thnk i am not abot to understand you. there might me a problem with my listening, can you please restart me')
		exit()
	return select

# restcall function connects to tool using rest api and returns the response 	
def restcall (url):
	response = requests.get(url, auth=(user, pwd), headers=headers  )
	if response.status_code != 200: 
		#print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
		print("Error in tool response, please find the details below:")
		print('Status:', response.status_code,'\n\nError Response:',response.json())
		exit()
		#return "Please try later"
	else:
		data = response.json()
		py_json = json.dumps(data)
		return py_json
		
		
# servicenow function provieds predefined options for getting tool information 
# based on option selected by the user, response is displayed on the screen.
def servicenow():
	voiceOut ("what information you are looking for")
	voiceOut ("Incident")
	voiceOut ("Problem")
	categoryChoice = listen2("\nwhat information you are looking for:\n1.Incident\n2.Problem")
	print("\nYou selected the category: " + categoryChoice)
	# Category choice for ServiceNow
	if categoryChoice == "incident" or categoryChoice == "incidents":
		voiceOut ("what would you like to know about incidents")
		voiceOut ("All Incidents")
		voiceOut ("Open Incidents")
		voiceOut ("Resolved incidents")
		resultChoice = listen2("\nPlease select which information you need:\n1.All Incidents\n2.Open Incidents\n3.Resolved incidents")
		print("\nYou selected the information: " + resultChoice)
		# Information choice for Incidents
		if resultChoice == "all incident" or resultChoice == "all incidents" or resultChoice == "allincident":
			url = baseUrl + "api/now/stats/incident?sysparm_count=true"
			# testing
			#print ("the URL is : " + url)
			jsonResult = restcall(url)
			x = json.loads(jsonResult)
			count1 = x['result']['stats']['count']
			toolResponse = "\n\nTotal Number of incidents are: "+ count1
			browser.get('https://dev57834.service-now.com/nav_to.do?uri=%2Fincident_list.do%3Fsysparm_userpref_module%3Db55b4ab0c0a80009007a9c0f03fb4da9%26sysparm_clear_stack%3Dtrue')
			print (toolResponse)
			voiceOut(toolResponse)			
		
		elif resultChoice == "open incident" or resultChoice == "open incidents" or resultChoice == "openincident":
			url = baseUrl + "api/now/stats/incident?sysparm_count=true&sysparm_query=active=true^state=1^ORstate=2^ORstate=6^ORstate=3"
			jsonResult = restcall(url)
			x = json.loads(jsonResult)
			count1 = x['result']['stats']['count']
			toolResponse = "\n\nTotal Number of open incidents are: "+ count1
			print (toolResponse)
			voiceOut(toolResponse)	
			
		elif resultChoice == "resolved incident" or resultChoice == "resolved incidents" or resultChoice == "resolvedincident":
			url = baseUrl + "api/now/stats/incident?sysparm_count=true&state=6"
			jsonResult = restcall(url)
			x = json.loads(jsonResult)
			count1 = x['result']['stats']['count']
			toolResponse = "\n\nTotal Number of resolved incidents are: "+ count1
			print (toolResponse)
			voiceOut(toolResponse)
		else:
			print("This information is not available currently\nThank you for connecting")
	elif categoryChoice == "problem" or categoryChoice == "problems":
		#do -----------------------------
		voiceOut ("what would you like to know about problems")
		voiceOut ("All Problems")
		voiceOut ("Open Problems")
		resultChoice = listen2("\nPlease select which information you need:\n1.All Problems\n2.Open Problems")
		print("\nYou selected the information: " + resultChoice)
		# Information choice for Problems
		if resultChoice == "all problem" or resultChoice == "all problems" or resultChoice == "allproblem":
			url = baseUrl + "api/now/stats/problem?sysparm_count=true"
			jsonResult = restcall(url)
			x = json.loads(jsonResult)
			count1 = x['result']['stats']['count']
			toolResponse ="\nTotal Number of problems are: "+ count1
			print (toolResponse)
			browser.get('https://dev57834.service-now.com/nav_to.do?uri=%2Fproblem_list.do%3Fsysparm_userpref_module%3Db55f73f8c0a800090175ace6ae472053%26sysparm_clear_stack%3Dtrue')
			voiceOut(toolResponse)
		elif resultChoice == "open problem" or resultChoice == "open problems" or resultChoice == "openproblem":
			url = baseUrl + "api/now/stats/problem?sysparm_count=true&state=4"
			jsonResult = restcall(url)
			x = json.loads(jsonResult)
			count1 = x['result']['stats']['count']
			toolResponse ="\nTotal Number of open problems are: "+ count1
			print (toolResponse)
			voiceOut(toolResponse)
		else:
			print("This information is not available currently\nThank you for connecting")
		
		
	else:
		print("This category is not available currently\nThank you for connecting")
		
	
##########################################################################################	
### Main Execution starts here ###

# clear screen
clear()
# welcome text		
print("\n\n***************************************************************************")
print("*****^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^*****")
#print("***** Hi Welcome to SHIKHA, your voice assistance tool *****")
print("***** Hi Welcome to Titli!!!! Hope you are doing good today *****")
print("***************************************************************************")
print("***************************************************************************\n\n")


c.execute("SELECT phrase from trigger where keyword = 'welcome titli'")
word = c.fetchone()
browser.get('C:/Users/suhas.m.l.bhatt/OneDrive - Accenture/VoiceRec/Shikha/With DB/HTML/Home_Page.html')
voiceOut (word[0])
voiceOut ('your voice assistance tool')
#*****************************chit chat*****************************
c.execute("SELECT phrase from trigger where keyword = 'name'")
word1 = c.fetchone()
voiceOut (word1[0])
name = listen2(word1[0])
voiceOut ("Hello "+name)
print ("Hello "+name)

c.execute("SELECT phrase from trigger where keyword = 'welcome name'")
word1 = c.fetchone()
voiceOut (word1[0])
voiceOut('How are you doing?')
resp = listen2(word1[0])
print (resp)

hppyWords = ['good','fine','all right','happy','wow','excited']
sadWords = ['not','didn\'t','bad','hungry']
busyWords = ['busy','hectic','critical']

nltk_process_result = preprocess_Text(resp,sadWords,hppyWords,busyWords)

if nltk_process_result == 1:
	c.execute("SELECT phrase from trigger where keyword = 'doing bad'")
	word1 = c.fetchone()
	voiceOut (word1[0])
	print(word1[0])
elif nltk_process_result == 2:
	c.execute("SELECT phrase from trigger where keyword = 'doing good'")
	word1 = c.fetchone()
	voiceOut (word1[0])
	print(word1[0])
elif nltk_process_result == 3:
	c.execute("SELECT phrase from trigger where keyword = 'doing busy'")
	word1 = c.fetchone()
	voiceOut (word1[0])
	print(word1[0])
else:
	c.execute("SELECT phrase from trigger where keyword = 'welcome name'")
	word1 = c.fetchone()
	voiceOut ('thank you for letting me know')
	print(word1[0])

c.execute("SELECT phrase from trigger where keyword = 'help'")
word1 = c.fetchone()
voiceOut (word1[0])

numberOfClients = 2
client1 = 'BHP a leading global resources company'
client2 = 'Rio Tinto a leading global mining group'

intro1 = "Well I have"+ str(numberOfClients) +"clients in my portfolio as of now. I shall name it for you,"
intro2 = "one of them is " +client1+", and the other one is " +client2

voiceOut(intro1)
voiceOut(intro2)

askChoice = name + ' let me know whats your choice is'
voiceOut(askChoice)
detailRequested = listen2(askChoice)

term1 = 'BHP'
term2 = 'Rio'


print(detailRequested)
words = detailRequested.split()
print(words)

if (term1 in words):
	#c.execute("SELECT phrase from trigger where keyword = 'welcome1'")
	#word1 = c.fetchone()

	voiceOut ('ok you are interested in '+term1)
	voiceOut('well let me fetch relavent business details on it')
	#print (word1[0])
	
elif term2 in words:
	voiceOut ('ok you are interested in Rio Tinto')
	voiceOut('well let me fetch relavent business details on it')
else:
	#c.execute("SELECT phrase from trigger where keyword = 'no option'")
	#word1 = c.fetchone()
	voiceOut ('sory ' +name)
	voiceOut('as of now we dont have that option, but i can help you with business details of bhp')
	print ('as of now we dont have that option, but i can help you with business details of bhp')





#*****************************Log in *****************************
c.execute("SELECT phrase from trigger where keyword = 'passcode'")
browser.get('C:/Users/suhas.m.l.bhatt/OneDrive - Accenture/VoiceRec/Shikha/With DB/HTML/titli.html')
word1 = c.fetchone()
voiceOut (word1[0])
passCount=0
while 1:
	passcode = listen2 (word1[0])
	print('****')
	authReturn = auth(passcode)

	if (authReturn == 0):
		passCount+=1
		if passCount == 3:
			c.execute("SELECT phrase from trigger where keyword = 'wrong auth'")
			word1 = c.fetchone()
			print(word1[0])
			voiceOut (word1[0])
			c.execute("SELECT phrase from trigger where keyword = 'exit'")
			word1 = c.fetchone()
			print(word1[0])
			voiceOut (word1[0])
			sys.exit()
			
		c.execute("SELECT phrase from trigger where keyword = 'wrong passcode'")
		word1 = c.fetchone()
		voiceOut (word1[0])
#		print(word1[0])
	else:
		break
		

		
#		sys.exit()



#c.execute("SELECT phrase from trigger where keyword = 'correct passcode'")
#word1 = c.fetchone()

####################
c.execute("SELECT phrase from trigger where keyword = 'connect'")
word4 = c.fetchone()

v1 = 'i am validating your Credentials with multifactor authentication, by this way we can make sure that our client data is safe and secure'
v2 = ' please wait while i gather the information'

###################
##voiceOut(v1)#t2 ecec
################



#voiceOut ('thank you '+name+' for giving the passcode')
#t1 = threading.Thread(voiceOut(v1))



#voiceOut (word4[0])
#print(word4[0])	



#print(word1[0])
# c.execute("SELECT phrase from trigger where keyword = 'connect'")
# word2 = c.fetchone()
# voiceOut (word1[0])
# voiceOut (word2[0])

#******************************************************************************
# #Tool select		
# voiceOut ("do you want me to connect to service now")
# toolChoice = listen2 ("do you want me to connect to service now")
# print("You said: "+toolChoice)

# #print("\nYou selected the tool: " + toolChoice)


# # once the tool is selected respective module is called
# if toolChoice == "yes" or toolChoice == "s":
	# print("Please wait while we are connecting you to Service Now")
	# voiceOut ("Please wait while we are connecting you to Service Now")
#******************************************************************************	


def getAuth():
	browser.get('https://dev57834.service-now.com/')
	voiceOut(v2)
	browser.switch_to.frame("gsft_main")
	username = browser.find_element_by_id("user_name")
	username.send_keys(user)
	password = browser.find_element_by_id("user_password")
	password.send_keys(pwd)
	browser.find_element_by_id("sysverb_login").click()
	
#t2 = threading.Thread(getAuth)

t1=threading.Thread(target=voiceOut, args=(v1,))
t2=threading.Thread(target=getAuth)

t1.start()
t2.start()

t1.join()
t2.join()


#t2.start()

#t1.join()
#t2.join()

	
	#extract basic info
	
# extracting number of new incidents opened today	
url = baseUrl + "api/now/stats/incident?sysparm_count=true&sysparm_query=sys_created_onONToday%40javascript%3Ags.beginningOfToday()%40javascript%3Ags.endOfToday()"
jsonResult = restcall(url)
x = json.loads(jsonResult)
incidentToday = x['result']['stats']['count']
# extracting number of incidents which were raised and resolved today
url = baseUrl + "api/now/stats/incident?sysparm_count=true&sysparm_query=sys_created_onONToday%40javascript%3Ags.beginningOfToday()%40javascript%3Ags.endOfToday()&state=6"
jsonResult = restcall(url)
x = json.loads(jsonResult)
incidentResolvedToday = x['result']['stats']['count']


# extracting number of problems which were raised and resolved today
url = baseUrl + "api/now/stats/problem?sysparm_count=true&sysparm_query=sys_created_onONToday%40javascript%3Ags.beginningOfToday()%40javascript%3Ags.endOfToday()"
jsonResult = restcall(url)
x = json.loads(jsonResult)
problemsToday = x['result']['stats']['count']



# extracting number of problems which were raised and resolved today
url = baseUrl + "api/now/stats/problem?sysparm_count=true&sysparm_query=sys_created_onONToday%40javascript%3Ags.beginningOfToday()%40javascript%3Ags.endOfToday()&state=4"
jsonResult = restcall(url)
x = json.loads(jsonResult)
problmesResolvedToday = x['result']['stats']['count']


c.execute("SELECT phrase from trigger where keyword = 'connected'")
word5 = c.fetchone()
voiceOut (word5[0])	

c.execute("SELECT phrase from trigger where keyword = 'brief'")
browser.get('https://dev57834.service-now.com/nav_to.do?uri=%2Fincident_list.do%3Fsysparm_first_row%3D1%26sysparm_query%3Dsys_created_onONToday%2540javascript%253Ags.beginningOfToday%2528%2529%2540javascript%253Ags.endOfToday%2528%2529%26sysparm_view%3D')
word3 = c.fetchone()
voiceOut (word3[0])	
	
#	print("you are connected to servicenow")
#	voiceOut ("you are connected to service now")
#	voiceOut ("here is todays brief update")
#	print()


voiceOut('Looks like there were less tickets to worry today compared to yesterday.')
todayUpdate1 = ("There were total "+ incidentToday +" incident opened today and out of which " +incidentResolvedToday+" was resolved")
print("There were total "+ incidentToday +" incident opened today and out of which " +incidentResolvedToday+" was resolved")
voiceOut (todayUpdate1)

browser.get('https://dev57834.service-now.com/nav_to.do?uri=%2Fproblem_list.do%3Fsysparm_query%3Dclosed_atONToday@javascript:gs.beginningOfToday()@javascript:gs.endOfToday()%26sysparm_first_row%3D1%26sysparm_view%3D')
todayUpdate2 = ("and "+ problemsToday +" problem were created out of which " +problmesResolvedToday+" was resolved")
print("and "+ problemsToday +" problem were created out of which " +problmesResolvedToday+" was resolved")
voiceOut (todayUpdate2)
voiceOut('we can see the whole system is stable with not much issues') 
#voiceOut('looks like you are quite happy with the less number of tickets')
 
	#servicenow()
while 1:
	voiceOut("suhas "+" would you like to know more")
	cont = listen2 ("Would you like to know more")
	print ("you said: "+cont)
	moreResp = 'yes'
	if moreResp in cont:
		servicenow()
	else:
		break
browser.get('C:/Users/suhas.m.l.bhatt/OneDrive - Accenture/VoiceRec/Shikha/With DB/HTML/thankyou.html')
voiceOut ("Thank you for using Thithlee")
voiceOut ("have a nice day")
print("Thank you for using Thithlee \nHave a nice day")
# elif 	toolChoice == "futuretool" or toolChoice == "futuretool":
# else:
	# print("ServiceNow is the only tool available now. we will notify you once Shikha is enabled with other tools.\nThank you for connecting")
	# voiceOut ("Service now is the only tool available now")
	# voiceOut ("we will notify you once Shikha is enabled with other tools")
	# voiceOut ("Thank you for connecting. have a nice day ")

### End of the framework ###
##########################################################################################	