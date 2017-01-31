import sqlite3
import logging
import sys
import datetime

conn = sqlite3.connect('/home/valen/project/project1.5/users2.db')
c = conn.cursor()
todaydate = datetime.date.today()


try:
	formdate = sys.argv[1]

	c.execute('SELECT users.username, COUNT(*) FROM input INNER JOIN users ON input.mifare=users.mifare OR input.em=users.em WHERE input.date=? GROUP BY username ORDER BY count(*) DESC', (str(formdate),))
	tota = c.fetchall()
	
	for x in tota:
		uname = x[0]
		booped = x[1]
		print("<li>")
		print(uname, end=' ')
		print(booped)
		print('</li>')


except IndexError:
	c.execute('SELECT users.username, COUNT(*) FROM input INNER JOIN users ON input.mifare=users.mifare OR input.em=users.em WHERE input.date=? GROUP BY username ORDER BY count(*) DESC', (str(todaydate),))
	tota = c.fetchall()
	
	for x in tota:
		uname = x[0]
		booped = x[1]
		print("<li>")
		print(uname, end=' ')
		print(booped)
		print('</li>')


try:
	if sys.argv[1] == '-a':
		c.execute('SELECT users.username, COUNT(*) FROM input INNER JOIN users ON input.mifare=users.mifare OR input.em=users.em GROUP BY username ORDER BY count(*) DESC')
		tota = c.fetchall()
	
		for x in tota:
			uname = x[0]
			booped = x[1]
			print("<li>")
			print(uname, end=' ')
			print(booped)
			print('</li>')

except IndexError:
	pass