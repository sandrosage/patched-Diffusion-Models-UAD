import os

work = "/home/saturn/iwai/iwai113h/"
mslub = os.path.join(work, "MSLUB/")
brats21 = os.path.join(work, "BraTS21/")
ixi = os.path.join(work, "IXI/")
preprocessing_paths = ["v1resampled", "v2skullstripped", "v3registered_non_iso", "v3registered_non_iso_cut", "v4correctedN4_non_iso_cut", "Data"]

t2 = "t2"
seg = "seg"
mask = "mask"

mslub_t2 = os.path.join(mslub,t2)
mslub_seg = os.path.join(mslub,seg)
ixi_t2 = os.path.join(ixi,t2)
brats_t2 = os.path.join(brats21,t2)
brats_seg = os.path.join(brats21,seg)

mslub_t2_n = len(os.listdir(mslub_t2))
mslub_seg_n = len(os.listdir(mslub_seg))
ixi_t2_n = len(os.listdir(ixi_t2))
brats_t2_n = len(os.listdir(brats_t2))
brats_seg_n = len(os.listdir(brats_seg))
with open('summary.txt', 'w') as file:
    file.write("IXI----------------- \n")
    file.write(ixi_t2 + ": " + str(ixi_t2_n) + "\n")
    file.write("MSLUB--------------- \n")
    file.write(mslub_t2 + ": " + str(mslub_t2_n) + "\n")
    file.write(mslub_seg + ": " + str(mslub_seg_n) + "\n")
    file.write("BraTS21--------------\n")
    file.write(brats_t2 + ": " + str(brats_t2_n) + "\n")
    file.write(brats_seg + ": " + str(brats_seg_n) + "\n")
    for path in preprocessing_paths:
        file.write(path + "-------------\n")
        prep_dir = os.path.join(work, path)
        if path == "Data":
            prep_dir = path
        for d in os.listdir(prep_dir):
            if (".txt" in d) or ("splits" in d):
                continue
            for a in os.listdir(os.path.join(prep_dir,d)):
                path_name = os.path.join(prep_dir,d,a)
                path_number = len(os.listdir(path_name))
                file.write(path_name + ": " + str(path_number) + "\n")
                for j in os.listdir(path_name):
                    sub_name = os.path.join(path_name,j)
                    if os.path.isdir(sub_name):
                        path_number = len(os.listdir(sub_name))
                        file.write(sub_name + ": " + str(path_number) + "\n")