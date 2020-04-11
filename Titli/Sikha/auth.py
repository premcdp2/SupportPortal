import speech_recognition as sr 
import win32com.client as wincl 
import requests
import json
import os
import sqlite3


conn = sqlite3.connect('shikha.db')
c = conn.cursor()


def auth(logpwd):
	c.execute('SELECT user from auth where password=?',(logpwd,))
	user=c.fetchone() is not None
#	print(user)
	if (user == False):
		return(0)
	elif(user==True):
		return(1)

#x = auth('1')
#print(x)