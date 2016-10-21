#Initial mongodb configuration for mint collection

mydb = 'dbName'
mycollection = 'mint'
file_source = "transactions_test.csv"

def set_record(row):
	myrecord = {
			"date": ["Date"], 
			'short_description': row['Description'],
			'long_description': row['Original Description'],
			'amount': float(row['Amount']),
			'type': row['Transaction Type'],
			'category': row['Category'],
			'account': row['Account Name'],
			'labels': row['Labels'],
			'notes' : row['Notes']
			}
	return myrecord
