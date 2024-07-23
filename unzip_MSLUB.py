import zipfile
import os
work = "/home/saturn/iwai/iwai113h/"
files = ["3D-MR-MS_patient01-05.zip", "3D-MR-MS_patient06-10.zip", "3D-MR-MS_patient11-15.zip", "3D-MR-MS_patient16-20.zip", "3D-MR-MS_patient21-25.zip", "3D-MR-MS_patient26-30.zip"]
for file in files:
    print("In processing: ", file)
    path_zip = os.path.join(work, file)
    extract_dir = os.path.join(work, "MSLUB/")
    with zipfile.ZipFile(path_zip, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    print("DONE: ", file)