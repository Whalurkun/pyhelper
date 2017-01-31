import sqlite3
import logging
import sys

conn = sqlite3.connect('users2.db')
c = conn.cursor()

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%a %d %b %Y - %H:%M:%S', filename='logtest.log',level=logging.DEBUG,)

def adduser(rfid, user_name):

	try:
		rfids = rfid.partition("!")
	except ValueError:
		print('value error')
	mfare = rfids[0]
	em = rfids[2]

	c.execute("SELECT username FROM 'users' where mifare = ?", (mfare,))
	row = c.fetchone()
	c.execute("SELECT username FROM 'users' where em = ?", (em,))
	row2 = c.fetchone()

	if em is '':
		print('em is none, not adding card due to known bug.')
		return
	if row != None:
		print('Card is already added in the database')
		logging.warning('[INFO]  - Card already in database as user {}'.format(row[0]))
		logging.info('[INFO]  - Not adding new card')

		r = str(input('Boop new card or press ctrl+c to exit:'))

		u = str(input('Type new username:'))
		adduser(r, u)
		return

	if row2 != None:
		print('Card is already added in the database')
		logging.warning('[INFO]  - Card already in database as user {}'.format(row[0]))
		logging.info('[INFO]  - Not adding new card')

		r = str(input('Boop new card or press ctrl+c to exit:'))

		u = str(input('Type new username:'))
		adduser(r, u)
		return

	if mfare is '':
		print('mfare is none')

	user_info = [(mfare, em, user_name)]
	c.executemany('INSERT INTO users VALUES (?,?,?)', user_info)


	logging.info('[INFO]  - Added card {} with username {}'.format(rfid, user_name))
	conn.commit()
	logging.info('[INFO]  - Added user: {} with card: {}'.format(user_name, rfid))
x = str(input('Boop card:'))
y = str(input('Whos card is this:'))

adduser(x, y)

