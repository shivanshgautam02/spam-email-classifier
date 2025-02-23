import os
import tarfile
import bz2

base_dir = os.path.join("data")  #Base folder /data
files = ["20021010_easy_ham.tar.bz2", "20030228_spam.tar.bz2"]    # file to extracted
extract_dir = os.path.join(base_dir, "extracted_emails")


os.makedirs(extract_dir, exist_ok=True) # tell the directiory exist

def extract_tar_bz2(file_path, destination):
    """Extracts a .tar.bz2 files."""
    try:
        tar_path = file_path[:-4]  # Remove .bz2 
        with bz2.BZ2File(file_path, "rb") as bz2_file, open(tar_path, "wb") as tar_file:
            tar_file.write(bz2_file.read())

        with tarfile.open(tar_path, "r") as tar:
            tar.extractall(path=destination)
        print(f"Extracted: {file_path} -> {destination}")

        os.remove(tar_path)

    except Exception as e:
        print(f"Error extracting {file_path}: {e}")


for file in files:
    file_path = os.path.join(base_dir, file)  
    if os.path.exists(file_path):
        extract_tar_bz2(file_path, extract_dir)
    else:
        print(f"File not found: {file_path}")
