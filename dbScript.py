import time
import sqlite3

conn = sqlite3.connect('./db.sqlite3')
c = conn.cursor()

item=["ramseed20","123","345","344"]
#while(1):
#  time.sleep(2)  
#  item[0]=str(int(item[0])+1)
c.execute("insert into jsonGet_stockn values (?,?,?,?)",tuple(item))
