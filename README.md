# File Organizer using Python

This is a simple Python project that helps organize files in a folder (like Downloads) by automatically moving them into separate folders such as Images, Videos, Documents, etc.

### Features:
- Sorts files based on their extensions.
- Automatically creates folders like:
  - Images (.jpg, .png)
  - Videos (.mp4, .mkv)
  - Documents (.pdf, .docx, .txt)
  - Audio (.mp3, .wav)
  - Others (everything else)
- Works on both **PC** and **Android**.

### How It Works:
The script checks each file in the folder, identifies its type based on extension, and moves it to the correct folder. If it doesn't match any category, it's moved to a folder called `Others`.

### Requirements:
- Python 3
- No external libraries (uses only `os` and `shutil`)

### How to Run (on PC):
1. Install Python 3 from [https://python.org](https://python.org)
2. Paste the code into a new file and save it as `file_organizer.py`.
3. Change the `folder_path` variable to your folder (e.g., `C:/Users/YourName/Downloads`).
4. Run the file in your code editor or terminal.

### How to Run (on Android using Pydroid 3):
1. Install [Pydroid 3](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3).
2. Paste the code into a new file and save it as `file_organizer.py`.
3. Update the `folder_path` variable if needed.
4. Tap the Run button — your files will be sorted!

### Example:
Before:

Downloads/ ├── file1.jpg ├── file2.mp3 ├── file3.pdf

After running script:

Downloads/ ├── Images/ │   └── file1.jpg ├── Audio/ │   └── file2.mp3 ├── Documents/ │   └── file3.pdf
