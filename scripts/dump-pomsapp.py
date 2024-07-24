import MySQLdb
import datetime
import os

DBmachine = "my-stg-1.cch.kcl.ac.uk"
DBaccount = "xxxxxxx"
DBpassword = "yyyyyyy"
DBdatabase = "poms"
"""
'NAME': 'poms',  # poms_stg_new / poms_temp
        'USER': 'poms',
        'PASSWORD': 'poms',
        'HOST': '127.0.0.1'
"""

firsttime = True

def processTable(tname, filename):
    global firsttime
    cmd = "mysqldump -u"+DBaccount+" -p"+DBpassword+" -h"+DBmachine+" "+DBdatabase+" "+tname
    if firsttime:
        firsttime = False
        cmd += ">"+filename
    else:
        cmd += ">>"+filename
    print (tname)
    os.system(cmd)

today = datetime.date.today()
todayStr = today.isoformat()
filename = "poms."+todayStr+".sql.txt"

db = MySQLdb.connect(DBmachine, DBaccount, DBpassword, DBdatabase)
c = db.cursor()
c.execute("show tables")
for row in c:
    tname = row[0]
    if tname.startswith("pomsapp"):
        processTable(tname, filename)
db.close()
