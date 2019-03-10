#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jirka
#
# Created:     10.03.2019
# Copyright:   (c) Jirka 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

print ("python 3.7.2")

import os
import time
import sqlite3

def addhostname(*args):
    conn = sqlite3.connect("hostnames.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS ips (ip text)''')
    for newhostname in args:
        insert ="INSERT INTO ips VALUES ('"+newhostname+"')"
        c.execute(insert)
        print("added hostname", newhostname)
    conn.commit()
    conn.close()
    pass

addhostname("google.com", "seznam.cz","google.cz","gjk.cz")

def main():

    conn = sqlite3.connect("hostnames.db")
    conn.row_factory = lambda cursor, row: row[0] #dělá z tumplů stringy bez závorek
    cur = conn.cursor()
    cur.execute("SELECT * FROM ips")
    hostnames= cur.fetchall()
    conn.close()
    print(hostnames)
    rep=0
    while rep<2:
        for i in hostnames:
            response = 0
            #response = os.system("ping -c 1 " + i)
            #0 pro odpovídá, else pro cokoliv jiného
            if response == 0:
              print (i, 'is up!')
            else:
              print (hostnames, 'is down!')
            if i in locals():
                #přidej do dict nebo db?
                pass
            else:
                #vytvoř dict nebo db?
                pass
        rep=rep+1
        time.sleep(1)

    pass




if __name__ == '__main__':
    main()