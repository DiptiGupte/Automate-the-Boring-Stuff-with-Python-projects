import os, shutil

#walk through a folder tree and search for files with a certain file extension (such as .jpg)
#copy these files from whatever location they are in to a new file
def selectiveCopy():
    #finding folder to copy
    print('Enter a folder to search through')
    f = input()
    folder = '/Users/diptigupte/Desktop/photos/' + f

    #creating new folder
    newFolder = os.path.basename(folder) + '_copied'
    newFolder = os.path.abspath(newFolder)
    os.makedirs(newFolder)

    #copying files into new folder
    for foldername, subfolders,filenames in os.walk(folder):
        #print('files in %s...'%(foldername))
        for filename in filenames:
            if filename.endswith('.JPG'):
                image_path = os.path.join(foldername, filename)     #https://stackoverflow.com/questions/35447755/first-practice-project-in-automate-the-boring-stuff-with-python-ch-9
                shutil.copy(image_path, newFolder)
    print('done.')

selectiveCopy()
