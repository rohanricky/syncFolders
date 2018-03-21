import tarfile

'''
Large files may need compression. Something better than this.
'''

def file_to_compress(file_name):
    with tarfile.open("sample.tar.gz", "w") as tar:
        tar.add(file_name)


if __name__=='__main__':
    file_to_compress('DroidA/how')

'''
import tarfile

def file_to_compress(file):
    save_data = zipfile.Zipfile('damn.tar.gz','w')
    save_data.write('/home/rohan/github/socialcops-challenge/folderToShare/shit.py')
'''
