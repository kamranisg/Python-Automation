#MoveFiles.py

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
