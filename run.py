import sqlite3
import logging
import sys
import datetime

conn = sqlite3.connect('users2.db')
c = conn.cursor()

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%a %d %b %Y - %H:%M:%S', filename='logtest.log',level=logging.DEBUG,)

#this is supposed to look up the user connected to the rfid
def input_rfid(rfid):

	try:
		rfids = rfid.partition("!")
	except ValueError:
		print('value error')
		pass

	mifare = rfids[0]
	em = rfids[2]
	todaydate = datetime.date.today()
	weekday = datetime.datetime.today().weekday()

	c.execute("SELECT username FROM 'users' where mifare = ? or em = ?", (mifare, em,))
	uname = c.fetchone()


	if mifare != '' and em != '' and uname != None:
		print('Mifare and em is ok')
		c.execute('INSERT INTO input (mifare, em, [date], weekday) VALUES (?, ?, ?, ?)', (mifare, em, todaydate, weekday,))
		
	elif mifare == '' and uname != None:
		print('Mifare is not okay!')
		c.execute('INSERT INTO input (mifare, em, [date], weekday) VALUES (?, ?, ?, ?)', (mifare, em, todaydate, weekday,))

	elif em == '' and uname != None:
		print('Em is not okay!')
		c.execute('INSERT INTO input (mifare, em, [date], weekday) VALUES (?, ?, ?, ?)', (mifare, em, todaydate, weekday,))

	else:
		print('[ERROR] - user not regisetered')

	conn.commit()
x = input('Press [ENTER] to start')

while x != False:
	input_rfid(str(input('-')))