import sqlite3

print("hello")

con = sqlite3.connect("../database/test.db")
print("hello")
cur = con.cursor()
print("hello")
cur.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")
print("hello")

cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")
res = cur.execute("SELECT * FROM movie")



print(res.fetchone())
print(res.fetchone())
print(res.fetchone())

con.commit()
