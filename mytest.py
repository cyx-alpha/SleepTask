import numpy as np
split_idx_list = np.load('./split_idx/idx_Sleep-EDF-2018.npy', allow_pickle=True)

for fold in range(len(split_idx_list)):
    print(f"Fold {fold+1}:")
    print("  Train:", split_idx_list[fold]['train'])
    print("  Val:", split_idx_list[fold]['val'])
    print("  Test:", split_idx_list[fold]['test'])
    print("-" * 40)