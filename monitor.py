import sys
import time
import logging
import cv2 as cv
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler
import os
import shutil

import watchdog as wd
#print(wd.__spec__)

# img= cv.imread('C:/Users/nagar/Desktop/foviatech/tasks/monitor/qr_images/QR1/LHS/bottle.jpg')
# print(img.shape)

class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return
        print(f'Change detected: {event.event_type} - {event.src_path}')
    
        if event.event_type == 'created':
            print( 'the new file is added')
            print('event.src_path', event.src_path)
            
            modified_path = '"' + str(event.src_path) + '"'
            
            create_folder(modified_path)      

        else :
            print('not created')
    
#define the function

def create_folder(path):
    # img= cv.imread('C:\\Users\\nagar\\Desktop\\foviatech\\tasks\\monitor\\qr_images\\QR1\\LHS\\bottle.jpg')
    # print(img.shape)
    print('src_path:', path)
    #os.chdir(path)
    print('type', type(path))
    src_path = path

    folders = []
    while True:
        path, folder = os.path.split(path)
        if folder != "":
            folders.insert(0, folder)
        else:
            break

    print(folders)
    qr_name = folders[folders.index('qr_images') + 1]
    side = folders[folders.index('qr_images') + 2]
    print('side', side)
    img_name = folders[folders.index('qr_images') + 3]
    #qr_name = folders[folders.index('qr_images') + 1]
    print('qr_name', qr_name)

    parent_path =("C:\\Users\\nagar\\Desktop\\foviatech\\tasks\\monitor\\results")
    #qr_name = input(qr_name)
    #side = 'RHS'
    print(type(qr_name))

    if side == 'LHS':
        print(side)
        full_path = os.path.join(parent_path, qr_name , side)
        os.makedirs(full_path)

        #input = src_path
        #input= r"C:\Users\nagar\Desktop\foviatech\tasks\monitor\bottle.jpg"
       # input= r"C:\Users\nagar\Desktop\foviatech\tasks\monitor\qr_images\QR1\LHS\bottle.jpg"
       # img= cv.imread('C:/Users/nagar/Desktop/foviatech/tasks/monitor/qr_images/QR1/LHS/bottle.jpg')
       # img= cv.imread('C:\\Users\\nagar\\Desktop\\foviatech\\tasks\\monitor\\qr_images\\QR1\\LHS\\bottle.jpg')
        #img= cv.imread(r'C:/Users/nagar/Desktop/foviatech/tasks/monitor/qr_images/QR1/LHS/bottle.jpg')
        # input= r'{}'.format(src_path)
        # input = src_path
        input = src_path.encode('unicode_escape')
        print('input_src', input)
        img= cv.imread(input)
        print(img.shape)
        height = 1000
        width = 1000
        resize_image = cv.resize(img, (height,width))
        print('resize_image_shape', resize_image.shape)
        # output_image_path = full_path / 'resized_image.jpg'
        # cv.imwrite(str(output_image_path),resize_image )
 
    elif side == 'RHS':
        print('RHS')
        full_path = os.path.join(parent_path, qr_name , side)
        os.makedirs(full_path)

   





# if __name__ == "__main__":
#     path1 = 'C:\\Users\\nagar\\Desktop\\foviatech\\tasks\\monitor\\qr_images'  # Path to the directory you want to monitor
#     event_handler = MyHandler()
#     observer = Observer()
#     observer.schedule(event_handler, path1, recursive=True)
#     #observer.schedule(event_handler, path2, recursive=True)
#     observer.start()

#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         observer.stop()
#     observer.join()


path1 = 'C:\\Users\\nagar\\Desktop\\foviatech\\tasks\\monitor\\qr_images'
#path1 = 'C:\\Users\\nagar\\Desktop\\qr_images'   # Path to the directory you want to monitor
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path1, recursive=True)
#observer.schedule(event_handler, path2, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()