from mongo_connection import mydbConnection
import mint_conf
import sys
import string
import csv

mydb = mint_conf.mydb
mycollection = mint_conf.mycollection
myfile = mint_conf.file_source

myconn = mydbConnection(mydb,mycollection)


myconn.openDB()
myconn.openCollection()
myconn.dropCollection()


print("Process started") 

try:
	with open(myfile,'r') as file_object:
		count = sum(1 for line in file_object)
		print("File contains " + str(count) + " transactions")
		
except FileNotFoundError:
	print("Filename " + myfile + " was not found!")
	sys.exit()

with open(myfile) as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         record = mint_conf.set_record(row)
         myconn.addDocument(record)


print("\nProcess completed successfully!")

