from couchdb import Server, Session
from io import BytesIO

auth = Session()
auth.name = "rohan"
auth.password = "secret"
couchserver = Server('http://localhost:5984/', session=auth)
db=couchserver['sync']

'''
For creating a document
from uuid import uuid4
doc_id = uuid4().hex
db[doc_id] = {'type': 'person', 'name': 'John Doe'}
'''

sync_folders = ["DroidA","DroidB"]
'''
Make this a class
'''

def store_file(f,folder):
	file_name=folder+"/"+f.filename
	doc={'name':file_name}
#	f=open(file_name,'r')
	for doc_id in db:
		document=db.get(doc_id,attachments=True)
		doc_name=document['name']
		if doc_name == file_name:
			db.delete_attachment(document,filename=file_name)
			db.delete(document)
	db.save(doc)
	db.put_attachment(doc,f,filename=file_name)

def get_file():
	for doc_id in db:
		doc=db.get(doc_id,attachments=True)
		doc_name=doc['name']
		document=db.get_attachment(doc_id,doc_name)
		try:
			document=document.read()
		except:
			document=''
		return doc_name,document,doc_id, doc

def clear_files(file_id):
	rows = db.view('_all_docs', include_docs=True)
	docs = []
	for row in rows:
		if file_id == row['id']:
			doc=row['doc']
			doc['_deleted'] = True
			docs.append(doc)
	db.update(docs)

def clear_all_files():
	rows = db.view('_all_docs', include_docs=True)
	docs = []
	for row in rows:
		if row['id'].startswith('_'):
			continue
		doc = row['doc']
		doc['_deleted'] = True
		docs.append(doc)
	db.update(docs)

def sync_at_same_time():
	droidA, droidB = [], []
	for doc_id in db:
		doc=db.get(doc_id,attachments=True)
		doc_name=doc['name']
		if doc_name.startswith(sync_folders[0]):
			sync_folders[0].append(doc_name.split("/")[1])
		elif doc_name.startswith(sync_folders[1]):
			sync_folders[1].append(doc_name.split("/")[1])
	print(droidA)
	print(droidB)
	for x in droidA:
		for y in droidB:
			if x==y:
				print('same')


if __name__=='__main__':
	sync_at_same_time()
