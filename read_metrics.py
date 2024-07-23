import pickle

path = "logs/runs/DDPM_2D_patched/DDPM_patched_2D_IXI_DDPM_2D_patched__2024-06-30_18-07-44/1_preds_dict.pkl"

print("Start...")
# Read dictionary from a pickle file
with open(path, 'rb') as pickle_file:
    data_loaded = pickle.load(pickle_file)

print(data_loaded)

print("DONE")