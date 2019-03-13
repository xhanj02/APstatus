#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jiří Handzel
#
# Created:     10.02.2019
# Copyright:   (c) JH 2019
#-------------------------------------------------------------------------------
import os
import time
import sqlite3

def main():
    conn = sqlite3.connect("hostnames.db")
    print(sqlite3.connect("hostnames.db").cursor().execute("SELECT * FROM ips").fetchall())
    conn.row_factory = lambda cursor, row: row[0] #dělá z tuplů stringy bez závorek
    cur = conn.cursor()
    cur.execute("SELECT * FROM ips")
    hostnames= cur.fetchall()
    print(hostnames)
    conn.close()
    rep=0
    while True: #rep<12
        conn = sqlite3.connect("hostnames.db")
        conn.row_factory = lambda cursor, row: row[0] #dělá z tuplů stringy bez závorek
        cur = conn.cursor()
        cur.execute("SELECT * FROM ips")
        hostnames= cur.fetchall()
        for i in hostnames:
            conn = sqlite3.connect("hostnames.db")
            conn = sqlite3.connect("hostnames.db")
            response = os.system("ping -c 1 " + i)
            #0 pro odpovídá, else pro cokoliv jiného
            if response == 0:
              print (i, 'is up!')

              #posuneme vše o hodinu dopředu
              a=conn.cursor()
              a.execute('SELECT t10 FROM ips WHERE ip='"'"+i+"'")
              aa=a.fetchall()
              aa=aa[0]
              a.execute('UPDATE ips SET t11 = '+str(aa[0])+' WHERE ip='"'"+i+"'")

              b=conn.cursor()
              b.execute('SELECT t9 FROM ips WHERE ip='"'"+i+"'")
              bb=b.fetchall()
              bb=bb[0]
              b.execute('UPDATE ips SET t10 = '+str(bb[0])+' WHERE ip='"'"+i+"'")

              c=conn.cursor()
              c.execute('SELECT t8 FROM ips WHERE ip='"'"+i+"'")
              cc=c.fetchall()
              cc=cc[0]
              c.execute('UPDATE ips SET t9 = '+str(cc[0])+' WHERE ip='"'"+i+"'")

              d=conn.cursor()
              d.execute('SELECT t7 FROM ips WHERE ip='"'"+i+"'")
              dd=d.fetchall()
              dd=dd[0]
              d.execute('UPDATE ips SET t8 = '+str(dd[0])+' WHERE ip='"'"+i+"'")

              e=conn.cursor()
              e.execute('SELECT t6 FROM ips WHERE ip='"'"+i+"'")
              ee=e.fetchall()
              ee=ee[0]
              e.execute('UPDATE ips SET t7 = '+str(ee[0])+' WHERE ip='"'"+i+"'")

              f=conn.cursor()
              f.execute('SELECT t5 FROM ips WHERE ip='"'"+i+"'")
              ff=f.fetchall()
              ff=ff[0]
              f.execute('UPDATE ips SET t6 = '+str(ff[0])+' WHERE ip='"'"+i+"'")

              g=conn.cursor()
              g.execute('SELECT t4 FROM ips WHERE ip='"'"+i+"'")
              gg=g.fetchall()
              gg=gg[0]
              g.execute('UPDATE ips SET t5 = '+str(gg[0])+' WHERE ip='"'"+i+"'")

              h=conn.cursor()
              h.execute('SELECT t3 FROM ips WHERE ip='"'"+i+"'")
              hh=h.fetchall()
              hh=hh[0]
              h.execute('UPDATE ips SET t4 = '+str(hh[0])+' WHERE ip='"'"+i+"'")

              l=conn.cursor()
              l.execute('SELECT t2 FROM ips WHERE ip='"'"+i+"'")
              ll=l.fetchall()
              ll=ll[0]
              l.execute('UPDATE ips SET t3 = '+str(ll[0])+' WHERE ip='"'"+i+"'")

              j=conn.cursor()
              j.execute('SELECT t1 FROM ips WHERE ip='"'"+i+"'")
              jj=j.fetchall()
              jj=jj[0]
              j.execute('UPDATE ips SET t2 = '+str(jj[0])+' WHERE ip='"'"+i+"'")

              k=conn.cursor()
              k.execute('SELECT t0 FROM ips WHERE ip='"'"+i+"'")
              kk=k.fetchall()
              kk=kk[0]
              k.execute('UPDATE ips SET t1 = '+str(kk[0])+' WHERE ip='"'"+i+"'")



              #a konečně přidáme aktuální hodinu
              add=conn.cursor()
              add.execute('UPDATE ips SET t0 = 0 WHERE ip='"'"+i+"'")
              conn.commit()

            else:
              print (i, 'is down!')

              #posuneme vše o hodinu dopředu

              a=conn.cursor()
              a.execute('SELECT t10 FROM ips WHERE ip='"'"+i+"'")
              aa=a.fetchall()
              aa=aa[0]
              a.execute('UPDATE ips SET t11 = '+str(aa[0])+' WHERE ip='"'"+i+"'")

              b=conn.cursor()
              b.execute('SELECT t9 FROM ips WHERE ip='"'"+i+"'")
              bb=b.fetchall()
              bb=bb[0]
              b.execute('UPDATE ips SET t10 = '+str(bb[0])+' WHERE ip='"'"+i+"'")

              c=conn.cursor()
              c.execute('SELECT t8 FROM ips WHERE ip='"'"+i+"'")
              cc=c.fetchall()
              cc=cc[0]
              c.execute('UPDATE ips SET t9 = '+str(cc[0])+' WHERE ip='"'"+i+"'")

              d=conn.cursor()
              d.execute('SELECT t7 FROM ips WHERE ip='"'"+i+"'")
              dd=d.fetchall()
              dd=dd[0]
              d.execute('UPDATE ips SET t8 = '+str(dd[0])+' WHERE ip='"'"+i+"'")

              e=conn.cursor()
              e.execute('SELECT t6 FROM ips WHERE ip='"'"+i+"'")
              ee=e.fetchall()
              ee=ee[0]
              e.execute('UPDATE ips SET t7 = '+str(ee[0])+' WHERE ip='"'"+i+"'")

              f=conn.cursor()
              f.execute('SELECT t5 FROM ips WHERE ip='"'"+i+"'")
              ff=f.fetchall()
              ff=ff[0]
              f.execute('UPDATE ips SET t6 = '+str(ff[0])+' WHERE ip='"'"+i+"'")

              g=conn.cursor()
              g.execute('SELECT t4 FROM ips WHERE ip='"'"+i+"'")
              gg=g.fetchall()
              gg=gg[0]
              g.execute('UPDATE ips SET t5 = '+str(gg[0])+' WHERE ip='"'"+i+"'")

              h=conn.cursor()
              h.execute('SELECT t3 FROM ips WHERE ip='"'"+i+"'")
              hh=h.fetchall()
              hh=hh[0]
              h.execute('UPDATE ips SET t4 = '+str(hh[0])+' WHERE ip='"'"+i+"'")

              l=conn.cursor()
              l.execute('SELECT t2 FROM ips WHERE ip='"'"+i+"'")
              ll=l.fetchall()
              ll=ll[0]
              l.execute('UPDATE ips SET t3 = '+str(ll[0])+' WHERE ip='"'"+i+"'")

              j=conn.cursor()
              j.execute('SELECT t1 FROM ips WHERE ip='"'"+i+"'")
              jj=j.fetchall()
              jj=jj[0]
              j.execute('UPDATE ips SET t2 = '+str(jj[0])+' WHERE ip='"'"+i+"'")

              k=conn.cursor()
              k.execute('SELECT t0 FROM ips WHERE ip='"'"+i+"'")
              kk=k.fetchall()
              kk=kk[0]
              k.execute('UPDATE ips SET t1 = '+str(kk[0])+' WHERE ip='"'"+i+"'")


              #a konečně přidáme aktuální hodinu
              add=conn.cursor()
              add.execute('UPDATE ips SET t0= 1 WHERE ip='"'"+i+"'")
              conn.commit()
        conn.close()
        time.sleep(60)
    print(sqlite3.connect("hostnames.db").cursor().execute("SELECT * FROM ips").fetchall())
    pass



if __name__ == '__main__':
    main()
