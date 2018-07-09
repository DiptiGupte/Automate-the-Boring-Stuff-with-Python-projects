import os

#walks through folder tree and searches for exceptionally large files or folders (100MB or greater)
#print these files with their absolute path to screen
def delUnneededFiles():
    print('Enter a folder to search through')
    f = input()
    folder = '/Users/diptigupte/Desktop/' + f
    for foldername, subfolders,filenames in os.walk(folder):
        print('deleting...')
        for filename in filenames:
            size = os.path.getsize(filename)
            if size >= 100000000:
                print(os.path.abspath(filename))
                print(size)
                print('')
                os.unlink(os.path.abspath(filename))
    print('done')

delUnneededFiles()
