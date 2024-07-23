import os
import shutil

work = "/home/saturn/iwai/iwai113h/"
path = os.path.join(work, "BraTS21")
destination_path_seg = os.path.join(path, "seg/")
if not os.path.exists(destination_path_seg):
    os.mkdir(destination_path_seg)
destination_path_t2 = os.path.join(path,"t2/")
if not os.path.exists(destination_path_t2):
    os.mkdir(destination_path_t2)
dirs = [d for d in os.listdir(path) if "BraTS2021" in d]
j = 0
for i,dir in enumerate(dirs):
    if i % 50 == 0:
        print(j*"#")
        j+=1
    mri_scans = os.listdir(os.path.join(path,dir))
    for scan in mri_scans:
        if "t2.nii.gz" in scan:
            src = os.path.join(path,dir,scan)
            dest = os.path.join(destination_path_t2,scan)
            shutil.copy2(src,dest)
        if "seg.nii.gz" in scan:
            src = os.path.join(path,dir,scan)
            dest = os.path.join(destination_path_seg,scan)
            shutil.copy2(src,dest)
print("DONE")