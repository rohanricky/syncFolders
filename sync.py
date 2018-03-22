import requests
import json
import sys
from couchdb.client import Document

sync_folders = ["DroidA","DroidB"]

url = 'http://127.0.0.1:5000/file'

def send_sync(file_name,fold):
    files = {'upload_file': open(file_name,'rb')}
    values = {'DB': 'photcat', 'OUT': 'csv', 'SHORT': 'short','folder':fold}
    r = requests.post(url, files=files, data=values)
    print(r.text)

def receive_sync():
    r = requests.post(url+"_get")
    x=str(r)
    try:
        data=json.loads(r.text)
    except:
        sys.exit()
    doc_name=data['name'].split("/")[1]
    from_folder=data['name'].split("/")[0]
#    print(from_folder)
    if from_folder == sync_folders[0]:
        to_folder=sync_folders[1]
    else:
        to_folder=sync_folders[0]
    print(data)
    doc=(data['doc'])
#    print(doc.save())
    with open(to_folder+"/"+doc_name,'a') as f:    # use a instead of w to append existing data
        f.write(data['data'])                      # choose when to delete and when to append
    values = {'id':data['id']}
    t=requests.post(url+'_remove',data=values)
    receive_sync()

def try_sync():
    r = requests.post(url+"_get")
    print(r.text)


if __name__=='__main__':
    receive_sync()
#    sync('/home/rohan/github/socialcops-challenge/DroidA/shit')
