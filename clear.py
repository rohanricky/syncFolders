#To remove all the files from Droid A and Droid B.

import subprocess

try:
    subprocess.run('rm DroidA/* DroidB/*',shell=True)
except:
    pass
