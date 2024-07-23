import os
import shutil

work = "/home/saturn/iwai/iwai113h/"
path = os.path.join(work, "MSLUB")
destination_path_seg = os.path.join(path, "seg/")
if not os.path.exists(destination_path_seg):
    os.mkdir(destination_path_seg)
destination_path_t2 = os.path.join(path,"t2/")
if not os.path.exists(destination_path_t2):
    os.mkdir(destination_path_t2)
patients =[d for d in os.listdir(path) if "patient" in d and not ".csv" in d]
for patient in patients:
    mri_scans = os.listdir(os.path.join(path,patient))
    for scan in mri_scans:
        if "T2W.nii.gz" in scan:
            src = os.path.join(path,patient,scan)
            dest = os.path.join(destination_path_t2,scan)
            shutil.copy2(src,dest)
        if "consensus_gt" in scan:
            src = os.path.join(path,patient,scan)
            dest = os.path.join(destination_path_seg,scan)
            shutil.copy2(src,dest)
print("DONE")

