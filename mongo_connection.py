from pymongo import MongoClient

class mydbConnection():
	
	"""
	Iniates object with 2 main attributes:
	mydb = database name
	mycollection = collection name 
	"""
	
	def __init__(self, mydb,mycollection):
		self.mydb = mydb
		self.mycollection = mycollection
		# Connection to Mongo DB
		try:
			client=MongoClient()	
			self.client = client
			print("Connected successfully!!!")
			
			
		except errors.ConnectionFailure:
			print("Could not connect to MongoDB")

	def openDB(self):
		
		# Setting the database
		db = self.client[self.mydb]
		self.db = db
				
	def openCollection(self):
		# Setting the collection

		cursor = self.db[self.mycollection].find()
		
		# Display test results
		#for document in cursor:
		#	print(document)
	
	def dropCollection(self):
		# Drop the colletion
		
		self.db[self.mycollection].drop()
	
	def addDocument(self, record):
		# Insert document into collection
		self.db[self.mycollection].insert(record)
				
	def queryDB(self, criteria, fields):
		cursor = self.db[self.mycollection].find(criteria,fields)
		return(cursor)
		
		
		
	
			
