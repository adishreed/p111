import os
import shutil

from_dir = "C:\Users\Nena\Downloads"
to_dir = "C:\My_Data\Document_files" 

listoffiles = os.listdir(from_dir)
#print(listoffiles)

for file_name in listoffiles:
   name,extension = os.path.splitext(file_name)
   print(name)
   print(extension)

   if extension == '':
        continue
   if extension in ['.txt', '.doc', '.docx', '.pdf']:
      path1 = from_dir + '/' + file_name
      path2 = to_dir + '/' + "Document_Files"
      path3 = to_dir + '/' + "Document_Files" + file_name
      print(path3)

      if os.path.exists(path2): 
         print("moving "+file_name+"...")
         shutil.move(path1, path3)
      else: 
         os.makedirs(path2)
         print("moving "+file_name+"...")
         shutil.move(path1, path3)