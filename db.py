from couchdb import Server, Session
from io import BytesIO

#from couchdb import json

auth = Session()
auth.name = "rohan"
auth.password = "secret"
couchserver = Server('http://localhost:5984/', session=auth)
db=couchserver['sync']

#sync_folders = ["DroidA","DroidB"]

def store_file(f,folder):
	file_name=folder+"/"+f.filename
	doc={'name':file_name}
#	f=open(file_name,'r')
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
		return doc_name,document,doc_id

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

if __name__=='__main__':
	clear_all_files()

'''
if __name__=='__main__':
	db=couchserver['sync']
	for doc_id in db:
		doc=db.get(doc_id,attachments=True)
		doc_name=doc['name']
		document=db.get_attachment(doc_id,doc_name)
		try:
			doctype=document.read().decode()
			print(doctype)
		except:
			pass
'''
'''
for doc_id in db:
	doc=db.get(doc_id,attachments=True)
#		print(doc_id)
	doc_name=doc['name']
	print(doc['_attachments'][doc_name]['data'])
	for single in doc['_attachments']:
		print(single)
'''
'''
jsondoc=json.encode(doc)
doc=json.dumps(jsondoc)
print(doc)

	doc_id, doc_rev = db.save({'key': file_name})
	print(db[doc_id]['key'])

	with open(db[doc_id]['key'],'w') as fromFile:
		toFile='DroidB/'
		fromFile.write(toFile)
'''
