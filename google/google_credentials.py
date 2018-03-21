
from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from apiclient.http import MediaFileUpload
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.readonly',
'https://www.googleapis.com/auth/drive.appfolder','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/drive.install',
'https://www.googleapis.com/auth/drive.metadata','https://www.googleapis.com/auth/drive.photos.readonly','https://www.googleapis.com/auth/drive.scripts']
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Sync folders through drive'


def get_credentials():
    """Validates user if already not done"""
    """google cloud project needed I guess"""
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'drive-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Google Drive API.

    Creates a Google Drive API service object and outputs the names and IDs
    for up to 10 files.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)

    file_metadata = {'name': 'video.txt'}
    media = MediaFileUpload('video.txt',mimetype='text/plain')
    file = service.files().create(body=file_metadata,media_body=media,fields='id').execute()
    print('File ID: %s' % file.get('id'))

if __name__ == '__main__':
    main()
