import sqlite3

def rankFind(form):
    conn = sqlite3.connect('NEF.db')
    c = conn.cursor()
    c.execute("SELECT name,stamps FROM students WHERE form = ? GROUP BY name,stamps ORDER BY stamps DESC LIMIT 3", (form,))
    res = c.fetchall()
    return(res)


p = rankFind("Pasteur")
one=p[0]
two=p[1]
three=p[2]
print(one[0])