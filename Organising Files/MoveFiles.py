#MoveFiles.py

# This is an example of how pyhton can used to automate the daily yet repetitive works of our daily lives. 

# In this script I had several folders numbered serially. In each folder I had 2 files namely "VOCABULARY" AND "GRAMMAR".

# After running this script we get all the VOCABULARY files in one folder and GRAMMAR files in another.

# YOU CAN CUSTOMISE DEPENDING ON YOUR NEEDS.

import os  # This module helps in interacting with the Operating System
import shutil # This module is mainly used to copy,rename,delete files in Directories

for folder,subfolders,FileNames in os.walk('C:\\Users\\LENOVO!!\\Desktop\\German  (Deutsch)\\Harry Gefangen in der Zeit\\A1'):
    print('FolderName is ' + folder)
    for subfolder in subfolders:
        print('Name of Subfolder is '+ subfolder)
    for name in FileNames:
        if(name[0]=='g'): # Identifying only Grammer Files
            
            Source_file_loc = folder + os.path.sep + name #Source of File to be moved
            Destination_file_Loc = 'C:\\Users\\LENOVO!!\\Desktop\\German  (Deutsch)\\Harry Gefangen in der Zeit\\A1\\Grammar'

        else: # Identifying the Vocabulary files
            
            file_loc = folder +os.path.sep + name
            Destination_file_Loc = 'C:\\Users\\LENOVO!!\\Desktop\\German  (Deutsch)\\Harry Gefangen in der Zeit\\A1\\Vocabulary'
           
        shutil.move(Source_file_loc,Destination_file_Loc)
