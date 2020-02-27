import string
txt="""
Ich verstehe aber hierunter nicht eine Kritik der Buecher und Systeme,
sondern die des Vernunftvermoegens ueberhaupt, in Ansehung aller
Erkenntnisse, zu denen sie, unabhaengig von aller Erfahrung, streben
mag, mithin die Entscheidung der Moeglichkeit oder Unmoeglichkeit
einer Metaphysik ueberhaupt und die Bestimmung sowohl der Quellen, als
des Umfanges und der Grenzen derselben, alles aber aus Prinzipien.
"""

#t1 = string.printable
t1 = string.ascii_letters

t2 = t1[4:]+t1[:4]

tt = str.maketrans( t1, t2) # method in str class  

print (txt.translate( tt ))
