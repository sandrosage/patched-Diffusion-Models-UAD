import zipfile
import os
work = "/home/saturn/iwai/iwai113h/"
files = ["archive.zip"]
for file in files:
    print("In processing: ", file)
    path_zip = os.path.join(work, file)
    extract_dir = os.path.join(work, "Archive/")
    with zipfile.ZipFile(path_zip, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    print("DONE: ", file)