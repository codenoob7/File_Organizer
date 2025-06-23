import os
import shutil

FOLDER_PATH =  "C:\\Users\\admin\\Downloads"

os.chdir(FOLDER_PATH)
print(os.getcwd())

Extension_Map = {
    "Images": [".jpg", ".jpeg", ".png", ".gif",".svg",".bmp"],
    "Videos": [".mp4",".mov",".avi",".wmv",".mkv",".webm"],
    "Audios": [".mp3",'.wav',".aac",".flac"],
    "Documents": [".pdf", ".docx", ".txt",'.xlsx','.csv','.pptx'],
    "Archives": [".zip", ".rar",'.tar','.gz'],
    "Design Files":[".psd",".ai"],
    "Web Files": [".html",".htm",".css",".js",".php",".asp",".xml"],
    "Applications": [".app", ".applescript", ".exe"],
}

def get_folder_name(extension):
    for folder,ext_list in Extension_Map.items():
        if extension in ext_list:
            return folder
    return "Others"

def organize_folder():
    for filename in os.listdir(FOLDER_PATH):
        file_path = os.path.join(FOLDER_PATH,filename)

        if os.path.isdir(file_path):
            continue

        _,ext = os.path.splitext(filename)      #This is same as os.path.splitext(filename)[-1], '_' is used to tell to ignore the base name that is filename.
        folder_name = get_folder_name(ext)
        target_folder = os.path.join(FOLDER_PATH, folder_name)
        os.makedirs(target_folder, exist_ok=True)

        shutil.move(file_path, os.path.join(target_folder,filename))
        print(f'Moved: {filename} --> {target_folder}')


if __name__ == "__main__":
    organize_folder()
