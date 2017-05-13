import sqlite3


def initialise_db():
    conn = sqlite3.connect("teas.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE teas (name text, variety text, last_used date)''')
    with open('teas.txt') as f:
        line = f.readlines()
        for tea in line:
            # strip out whitespace and new lines
            tea.strip()
            tea = tea.rstrip('\n')
            t = tea.split(",")
            c.execute('''INSERT INTO teas (name, variety) VALUES(?,?)''', (t[0], t[1]))
            print(t, ' inserted')

    conn.commit()


def select_tea():
    conn = sqlite3.connect("teas.db")
    c = conn.cursor()
    c.execute('''SELECT name, variety, last_used FROM teas WHERE (last_used != date('now') or last_used != date('now') -1 or last_used IS NULL) ORDER BY RANDOM() LIMIT 1''')

    all_rows = c.fetchall()
    for row in all_rows:
        print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))
        c.execute('''UPDATE teas SET last_used = date('now') WHERE name = ?''', (row[0],))

    conn.commit()

select_tea()






