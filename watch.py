import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from sync import send_sync
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sync_folders = ["DroidA","DroidB"]

# Watches for changes in below mentioned directories.

class Watcher:
    DIRECTORY_TO_WATCH = dir_path+"/DroidA"
    SECOND = dir_path+"/DroidB"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.schedule(event_handler,self.SECOND,recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()

'''
join() : This blocks the calling thread until the thread whose join() method is called terminates
 – either normally or through an unhandled exception or until the optional timeout occurs.

Use send sync method to send to server / to google drive
'''

class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        else:
            x=event.src_path.split("/")[-2:][0]
            y=send_sync(event.src_path,x)
            print(y)
            print(type(y['upload_file']))           #send to server
            if event.event_type == 'created':
                # Takes action here when a file is first created.
                print("Received created event - %s." % event.src_path)

            elif event.event_type == 'modified':
                # Takes action here when a file is modified.
                print("Received modified event - %s." % event.src_path)

if __name__ == '__main__':
    w = Watcher()
    w.run()
