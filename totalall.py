import sqlite3
import logging
import sys
import datetime

conn = sqlite3.connect('/home/valen/project/project1.5/users2.db')
c = conn.cursor()
todaydate = datetime.date.today()

c.execute('SELECT COUNT(*) FROM input WHERE input.date=?', (str(todaydate),))
row = c.fetchone()

print(row[0])