import os
import shutil

# This is the folder where my files are
folder_path = '/storage/emulated/0/Download'  # for Android in Pydroid

# These are the folders I want to move files into
folders = {
    'Images': ['.jpg', '.jpeg', '.png'],
    'Videos': ['.mp4', '.mkv'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Audio': ['.mp3', '.wav'],
    'Others': []
}

# Looping through all files in the folder
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    
    # Only move files, not folders
    if os.path.isfile(file_path):
        moved = False
        for folder_name, extensions in folders.items():
            for ext in extensions:
                if file_name.lower().endswith(ext):
                    # Make folder if not already there
                    new_folder = os.path.join(folder_path, folder_name)
                    os.makedirs(new_folder, exist_ok=True)
                    # Move file
                    shutil.move(file_path, os.path.join(new_folder, file_name))
                    print(f"Moved {file_name} to {folder_name}")
                    moved = True
                    break
            if moved:
                break
        
        # If no extension matched, put in 'Others'
        if not moved:
            other_folder = os.path.join(folder_path, 'Others')
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, file_name))
            print(f"Moved {file_name} to Others")