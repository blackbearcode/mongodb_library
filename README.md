# mongodb_library

Being a newbie on python and mongodb, I decided to share a simple library I created to establish the connection to a mongdb database, insert and query data. This is a working in progress that should have more methods added as soon as I acquire additional knowledge on the subject. 

For this exercise I used a layout borrowed from a Mint transactions file in csv format. So the .py files starting with "mint_" contains specific code for this example.

Below the explanation for each of the files:

- mint_insert.py

Initial code to read the records from the input file and insert into the database. It calls the python support libraries, the mongo library and the configuration library. This code calls te mongo_connection library to establish connection, set database, drop and create the collection and insert records into database

- mint_conf.py

Configuration file that contains:
1) Database name
2) Collection name
3) File name to be used for import
4) Table layout and input field mapping

- mongo_connection.py

This class is created with the following methods:

__init__(self, database, collection)

1) Database name
2) Collection name

A message is placed as a checkpoint to indicate the connection was successfull

openDB(self)

Set the database as the current for all actions

openCollection(self)

Set the cursor on the current collection

dropCollection(self)

Drop the current collection removing all documents

addDocument(self, document)

Add the document to the collection

queryDB(self, criteria, fields)

Retrieve documents from the collection with the criteria and fields as parameters. Refer to mongoDB documentation on how to build the criteria and filter

- mint_query.py

This code exemplifies a retrieve of the documenst from the collection and a grouping by the category field. In the mint exercise, the purpose is to sum all amounts for each category. This code needs a revision and a more elegant construction, but for the moment is useful to both check the data was properly inserted and demonstrate how it can be summarized.


















