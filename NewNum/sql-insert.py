import sqlite3
import random

with sqlite3.connect('newnum.db') as connection:
	c = connection.cursor()
	c.execute("CREATE TABLE newnumbers(numbers INT)")

	for i in range(100):
		num = random.randint(0, 100)
		c.execute("INSERT INTO newnumbers VALUES(?)", (num,))


