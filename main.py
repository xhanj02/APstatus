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
    c.execute('''CREATE TABLE IF NOT EXISTS ips (ip text PRIMARY KEY, t11 integer, t10 integer, t9 integer, t8 integer, t7 integer, t6 integer, t5 integer, t4 integer, t3 integer, t2 integer, t1 integer, t0 integer)''')
    #c.execute('''CREATE TABLE IF NOT EXISTS status (id integer PRIMARY KEY, t11 integer, t10 integer, t9 integer, t8 integer, t7 integer, t6 integer, t5 integer, t4 integer, t3 integer, t2 integer, t1 integer, t0 integer)''')
    for newhostname in args:
        insert ="INSERT INTO ips(ip,t11,t10,t9,t8,t7,t6,t5,t4,t3,t2,t1,t0) VALUES ('"+newhostname+"',2,2,2,2,2,2,2,2,2,2,2,2)"
        c.execute(insert)
        print("added hostname", newhostname)
    conn.commit()
    conn.close()
    pass

#addhostname("google.com", "seznam.cz","google.cz","gjk.cz")

def main():

    conn = sqlite3.connect("hostnames.db")
    print(sqlite3.connect("hostnames.db").cursor().execute("SELECT * FROM ips").fetchall())
    conn.row_factory = lambda cursor, row: row[0] #dělá z tuplů stringy bez závorek
    cur = conn.cursor()
    cur.execute("SELECT * FROM ips")
    hostnames= cur.fetchall()
    print(hostnames)
    rep=0
    while rep<1:
        for i in hostnames:
            response = 2
            #response = os.system("ping -c 1 " + i)
            #0 pro odpovídá, else pro cokoliv jiného
            if response == 0:
              print (i, 'is up!')

              #posuneme vše o hodinu dopředu
              a=conn.cursor()
              a.execute('SELECT t10 FROM ips WHERE ip='"'"+i+"'")
              aa=a.fetchall()
              a=conn.cursor()
              a.execute('UPDATE ips SET t11 = '+str(aa[0])+' WHERE ip='"'"+i+"'")

              b=conn.cursor()
              b.execute('SELECT t9 FROM ips WHERE ip='"'"+i+"'")
              bb=b.fetchall()
              b.execute('UPDATE ips SET t10 = '+str(bb[0])+' WHERE ip='"'"+i+"'")

              c=conn.cursor()
              c.execute('SELECT t8 FROM ips WHERE ip='"'"+i+"'")
              cc=c.fetchall()
              c.execute('UPDATE ips SET t9 = '+str(cc[0])+' WHERE ip='"'"+i+"'")

              d=conn.cursor()
              d.execute('SELECT t7 FROM ips WHERE ip='"'"+i+"'")
              dd=d.fetchall()
              d.execute('UPDATE ips SET t8 = '+str(dd[0])+' WHERE ip='"'"+i+"'")

              e=conn.cursor()
              e.execute('SELECT t6 FROM ips WHERE ip='"'"+i+"'")
              ee=e.fetchall()
              e.execute('UPDATE ips SET t7 = '+str(ee[0])+' WHERE ip='"'"+i+"'")

              f=conn.cursor()
              f.execute('SELECT t5 FROM ips WHERE ip='"'"+i+"'")
              ff=f.fetchall()
              f.execute('UPDATE ips SET t6 = '+str(ff[0])+' WHERE ip='"'"+i+"'")

              g=conn.cursor()
              g.execute('SELECT t4 FROM ips WHERE ip='"'"+i+"'")
              gg=g.fetchall()
              g.execute('UPDATE ips SET t5 = '+str(gg[0])+' WHERE ip='"'"+i+"'")

              h=conn.cursor()
              h.execute('SELECT t3 FROM ips WHERE ip='"'"+i+"'")
              hh=h.fetchall()
              h.execute('UPDATE ips SET t4 = '+str(hh[0])+' WHERE ip='"'"+i+"'")

              l=conn.cursor()
              l.execute('SELECT t2 FROM ips WHERE ip='"'"+i+"'")
              ll=l.fetchall()
              l.execute('UPDATE ips SET t3 = '+str(ll[0])+' WHERE ip='"'"+i+"'")

              j=conn.cursor()
              j.execute('SELECT t1 FROM ips WHERE ip='"'"+i+"'")
              jj=j.fetchall()
              j.execute('UPDATE ips SET t2 = '+str(jj[0])+' WHERE ip='"'"+i+"'")

              k=conn.cursor()
              k.execute('SELECT t0 FROM ips WHERE ip='"'"+i+"'")
              kk=k.fetchall()
              k.execute('UPDATE ips SET t1 = '+str(kk[0])+' WHERE ip='"'"+i+"'")


              #a konečně přidáme aktuální hodinu
              add=conn.cursor()
              add.execute('UPDATE ips SET t0 = 1 WHERE ip='"'"+i+"'")
              conn.commit()

            else:
              print (i, 'is down!')

              #posuneme vše o hodinu dopředu
              a=conn.cursor()
              a.execute('SELECT t10 FROM ips WHERE ip='"'"+i+"'")
              aa=a.fetchall()
              a.execute('UPDATE ips SET t11 = '+str(aa[0])+' WHERE ip='"'"+i+"'")

              b=conn.cursor()
              b.execute('SELECT t9 FROM ips WHERE ip='"'"+i+"'")
              bb=b.fetchall()
              b.execute('UPDATE ips SET t10 = '+str(bb[0])+' WHERE ip='"'"+i+"'")

              c=conn.cursor()
              c.execute('SELECT t8 FROM ips WHERE ip='"'"+i+"'")
              cc=c.fetchall()
              c.execute('UPDATE ips SET t9 = '+str(cc[0])+' WHERE ip='"'"+i+"'")

              d=conn.cursor()
              d.execute('SELECT t7 FROM ips WHERE ip='"'"+i+"'")
              dd=d.fetchall()
              d.execute('UPDATE ips SET t8 = '+str(dd[0])+' WHERE ip='"'"+i+"'")

              e=conn.cursor()
              e.execute('SELECT t6 FROM ips WHERE ip='"'"+i+"'")
              ee=e.fetchall()
              e.execute('UPDATE ips SET t7 = '+str(ee[0])+' WHERE ip='"'"+i+"'")

              f=conn.cursor()
              f.execute('SELECT t5 FROM ips WHERE ip='"'"+i+"'")
              ff=f.fetchall()
              f.execute('UPDATE ips SET t6 = '+str(ff[0])+' WHERE ip='"'"+i+"'")

              g=conn.cursor()
              g.execute('SELECT t4 FROM ips WHERE ip='"'"+i+"'")
              gg=g.fetchall()
              g.execute('UPDATE ips SET t5 = '+str(gg[0])+' WHERE ip='"'"+i+"'")

              h=conn.cursor()
              h.execute('SELECT t3 FROM ips WHERE ip='"'"+i+"'")
              hh=h.fetchall()
              h.execute('UPDATE ips SET t4 = '+str(hh[0])+' WHERE ip='"'"+i+"'")

              l=conn.cursor()
              l.execute('SELECT t2 FROM ips WHERE ip='"'"+i+"'")
              ll=l.fetchall()
              l.execute('UPDATE ips SET t3 = '+str(ll[0])+' WHERE ip='"'"+i+"'")

              j=conn.cursor()
              j.execute('SELECT t1 FROM ips WHERE ip='"'"+i+"'")
              jj=j.fetchall()
              j.execute('UPDATE ips SET t2 = '+str(jj[0])+' WHERE ip='"'"+i+"'")

              k=conn.cursor()
              k.execute('SELECT t0 FROM ips WHERE ip='"'"+i+"'")
              kk=k.fetchall()
              k.execute('UPDATE ips SET t1 = '+str(kk[0])+' WHERE ip='"'"+i+"'")


              #a konečně přidáme aktuální hodinu
              add=conn.cursor()
              add.execute('UPDATE ips SET t0= 0 WHERE ip='"'"+i+"'")
              conn.commit()
        rep=rep+1
        time.sleep(1)
    print(sqlite3.connect("hostnames.db").cursor().execute("SELECT * FROM ips").fetchall())
    conn.close()
    pass




if __name__ == '__main__':
    main()
