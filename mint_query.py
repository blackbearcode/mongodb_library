from mongo_connection import mydbConnection
from collections import defaultdict
import mint_conf
import sys
import string

mydb = mint_conf.mydb
mycollection = mint_conf.mycollection

mymint = mydbConnection(mydb,mycollection)


mymint.openDB()
mymint.openCollection()

myQueryCategory = mymint.queryDB({"type":"credit"},{"category":1,"amount":1})

mySummCategory = {}

for document in myQueryCategory:
	if str(document["category"]) in mySummCategory:
		mySummCategory[mykey] = mySummCategory[mykey] + document["amount"]
	else:
		mykey = str(document["category"])
		mySummCategory[mykey] = document["amount"]
		

print("This is the output: " + str(mySummCategory))

for category in mySummCategory:
	print(category,mySummCategory[category])
