# 📦 MediaSorter - Photo and Video Organizer

MediaSorter is a Python script that automatically organizes your photos and videos by sorting them into folders based on their creation date. It extracts metadata (EXIF for photos, metadata for videos) and moves files into folders named according to the date they were taken.

## ✅ Prerequisites

* Python 3.x installed on your system (verify with `python --version`)
* The following libraries (installable via pip):
  * `exifread` - For extracting EXIF metadata from photos
  * `hachoir` - For extracting metadata from video files
  * `tqdm` - For displaying progress bars

---

## 🔧 Setup

### 1. Create a virtual environment

In your terminal (CMD or PowerShell), navigate to your project folder, then run:

```bash
python -m venv venv
```

This will create a `venv/` folder containing the virtual environment.

### 2. Activate the virtual environment

On **Windows**:

* With **CMD**:

  ```bash
  venv\Scripts\activate.bat
  ```

* With **PowerShell**:

  ```powershell
  .\venv\Scripts\Activate.ps1
  ```

Once activated, you'll see the environment name (usually `(venv)`) at the beginning of your command line.

### 3. Install dependencies

Make sure the `requirements.txt` file is present, then run:

```bash
pip install -r requirements.txt
```

### 4. Deactivate the virtual environment (optional)

To exit the virtual environment:

```bash
deactivate
```

---

## 📁 Project Structure (example)

```
my-project/
├── venv/               # Virtual environment (don't version control)
├── script.py           # Your main script
├── requirements.txt    # List of dependencies
└── README.md           # This file
```

---

## 🔒 Best Practices

* Add `venv/` to your `.gitignore` if you're using Git.
* Always use a virtual environment to isolate your project dependencies.

---

## 📎 Resources

* [Official Python Documentation – venv](https://docs.python.org/3/library/venv.html)

---

## 📋 Features

* **Automatic Organization** - Sorts photos and videos from a source folder to destination folders organized by date
* **Metadata Extraction** - Uses EXIF data for photos and metadata for videos
* **Supported Formats**:
  * Photos: jpg, jpeg, png, tif, tiff, nef, dng
  * Videos: mp4, mov, avi, mkv
* **Progress Bars** - Displays processing progress with the name of the current file
* **Error Handling** - Robust error processing and ability to properly interrupt with Ctrl+C
* **Placement Verification** - Verification mode to ensure files are in the correct folders

## 🚀 Usage

1. Run the script:
   ```bash
   python mediasorter.py
   ```

2. Choose one of the following options:
   * **1: Sort files** - To organize files from the source folder to destination folders
   * **2: Verify photo placement** - To check if photos are correctly placed
   * **3: Exit** - To quit the program

## ⚙️ Configuration

Folder paths are defined at the beginning of the script:

```python
SOURCE_FOLDER = 'Z:\\bucket'        # Source folder containing files to sort
VIDEO_DEST = 'Z:\\Video'           # Destination for videos
PHOTO_DEST = 'Z:\\Photo\\RAW'      # Destination for photos
```

Modify these variables according to your configuration.

## 🔍 Destination Folder Structure

Files are organized in subfolders named according to the format `YYYYMMDD` (year, month, day).

Example:
```
Z:\Photo\RAW\20250727\photo1.jpg
Z:\Video\20250726\video1.mp4
