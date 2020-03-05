import sqlite3

conn = sqlite3.connect('titanic.db')
curs = conn.cursor()
curs.execute('''SELECT * FROM titanic''')             
# fetch all entries in 1 go
alld = curs.fetchall()
print(len(alld))
print(alld[0])
# (0, u'male', 22.0, 7.25, u'S', u'Third', u'man', None, u'Southampton')
# select entries 3rd class and male
sm3 = [ x[0] for x in alld if x[5]=='Third' and x[1]=='male' ]
# survival rate
print(float(sum(sm3))/len(sm3))

