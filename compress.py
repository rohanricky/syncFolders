import tarfile


def file_to_compress(file_name):
    with tarfile.open("sample.tar", "w") as tar:
        tar.add(file_name)

file_to_compress('folderToShare/shit.py')

'''
import tarfile

def file_to_compress(file):
    save_data = zipfile.Zipfile('damn.tar.gz','w')
    save_data.write('/home/rohan/github/socialcops-challenge/folderToShare/shit.py')
'''
