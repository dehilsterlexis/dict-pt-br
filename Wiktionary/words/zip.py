import os
import shutil

wordCount = 0
currentDir = os.getcwd()
   
for root, dirs, files in os.walk(currentDir):
    for dir in dirs:
        print('zipping: ',dir)
        shutil.make_archive(dir, 'zip', currentDir)
        wordCount += 1