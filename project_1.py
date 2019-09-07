import os, shutil
dict_ext = {
     'audio_ext' : ('.mp3','.m4a','.wav','.flac'),
     'video_ext' : ('.mp4','.mkv','.mpeg'),
     'document_ext' : ('.doc','.pdf','.txt'),
     'image_ext' : ('.jpg','.png','.bmp','jpeg'),
     'setup_wizard' : ('.exe','py'),
}

folderpath = input("Enter folder path : ")

def file_finder(folderpath, file_ext):
     files = []
     for file in os.listdir(folderpath):
        for ext in file_ext:
            if file.endswith(ext):
                files.append(file)
     return files
# output = file_finder(folderpath, video_ext)
# print(output)
for ext_type, ext_tuple in dict_ext.items():
     folder_name = ext_type.split("_")[0] + '_files'
     New_folder_path = os.path.join(folderpath,folder_name)
     for item in file_finder(folderpath,ext_tuple):
          if (folder_name in os.listdir(folderpath)) == False and (ext_tuple in os.listdir(folderpath)) == False:
               os.mkdir(New_folder_path)
          # ext = item.split(".")[1]
          # if ext in dict_ext.items():
          # print(f'calling finder function {ext_type}')
          # print(file_finder(folderpath,ext_tuple))
          # print('printing' + ext/)
     
          item_path = os.path.join(folderpath,item)
          new_item_path = os.path.join(New_folder_path,item)
          shutil.move(item_path,new_item_path)
               
