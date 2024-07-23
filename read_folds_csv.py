import csv
import os

csv_files = os.listdir("Data/splits/")
train_fold_sum = 0
val_fold_sum = 0
for file in csv_files:
    filename = os.path.join("Data/splits",file)
    with open(filename, mode='r') as file:
        csv_reader = csv.reader(file)
        row_count = sum(1 for row in csv_reader)
        if "IXI" in filename[12:-4]:
            if "train" in filename[12:-4]:
                train_fold_sum += (row_count-1)
            elif "val" in filename[12:-4]:
                val_fold_sum += (row_count-1)

            print(filename[12:-4] + ": " + str(row_count-1)) #-1 because of header
        else:
            print(filename[12:-4] + ": " + str(row_count-1)) #-1 because of header
        
print("Train IXI: ", train_fold_sum)
print("Val IXI: ", val_fold_sum)