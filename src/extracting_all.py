import os
import tarfile
import bz2


base_dir = "data" 
extract_dir = os.path.join(base_dir, "extracted_emails")


os.makedirs(extract_dir, exist_ok=True)


files = [f for f in os.listdir(base_dir) if f.endswith(".tar.bz2")]

def extract_tar_bz2(file_path, destination):
    """Extracts a .tar.bz2 file."""
    try:
        tar_path = file_path[:-4]  
        with bz2.BZ2File(file_path, "rb") as bz2_file, open(tar_path, "wb") as tar_file:
            tar_file.write(bz2_file.read())

        with tarfile.open(tar_path, "r") as tar:
            tar.extractall(path=destination)
        print(f"✅ Extracted: {file_path} -> {destination}")

        os.remove(tar_path)  #

    except Exception as e:
        print(f"❌ Error extracting {file_path}: {e}")


for file in files:
    file_path = os.path.join(base_dir, file)  
    if os.path.exists(file_path):
        extract_tar_bz2(file_path, extract_dir)
    else:
        print(f"⚠️ File not found: {file_path}")
