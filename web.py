from __future__ import print_function
import json
import os
import requests
from flask import Flask, request ,Response
import configparser
import sys
import sqlite3
from flask_uploads import UploadSet, configure_uploads, DOCUMENTS
from werkzeug import secure_filename
from db import store_file,get_file,clear_files
import sys

app = Flask(__name__)
#app.config['UPLOADED_TEXTFILES_DEST'] = '/DroidB'
#docs = UploadSet('textfiles', DOCUMENTS)
#configure_uploads(app,'txt')

#conn.execute('CREATE TABLE IF NOT EXISTS students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
#print("Table created successfully")

#config = configparser.ConfigParser()
#config.read('config.ini')
#access_token=config['HOST']
# send post request to my computer

@app.route('/file', methods=['POST'])
def file():
    if request.method=='POST' and 'upload_file' in request.files:
        f = request.files['upload_file']
        x=request.values['folder']
#        f.save('DroidB/'+secure_filename(f.filename))
        print(x, file=sys.stdout)
        store_file(f,x)
        return f.filename

@app.route('/file_get',methods=['POST'])
def create():
    if request.method=='POST':
        try:
            doc_name, data, doc_id=get_file()
            print(type(doc_name), file=sys.stdout)
        except:
            pass
        try:
            data=data.decode()
        except:
            data=''
        complete_data = {'name':doc_name,'data':data,'id':doc_id}
        json_data= json.dumps(complete_data)
        return json_data

@app.route('/file_remove',methods=['POST'])
def remove():
    if request.method=='POST':
        x=request.values['id']
        print(x,file=sys.stdout)
        clear_files(x)
        return x


# do the terminal thing also

if __name__=='__main__':
    app.run(host='127.0.0.1', port=int(os.environ.get('PORT', 5000)), debug=True)
