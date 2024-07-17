from data_loader import dataLoader_cross, dataloader_origin_test, dataLoader
from evaluations import evaluation
from training import train
from testing import test_k_fold
import torch
from sklearn.model_selection import KFold
from torch.utils.data import DataLoader
import os


def k_fold_cross_validation(device):
    '''K-Fold Cross Validation analysis'''
    base_path = './content/Paper/'
    k = 5
    origin_dataset, test_dataset = dataloader_origin_test(base_path)
    kf = KFold(n_splits=k, shuffle=True)
    fold = 0
    all_fold_accuracies = []
    result_folder = './results/0716/'

    for train_idx, val_idx in kf.split(origin_dataset):
        print(f'Fold {fold + 1}/{k}')
        train_loader, valid_loader = dataLoader_cross(
            origin_dataset, train_idx, val_idx)
        folder_name = result_folder + f'results_fold_{fold + 1}/'
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        best_model_name = train(folder_name, train_loader, valid_loader, model_type='resnet18',
                                num_epochs=101, learning_rate=0.001, pretrained=False, num_classes=4)
        all_fold_accuracies.append(best_model_name)
        fold += 1

    print('Cross-validation results:')
    for i, model_name in enumerate(all_fold_accuracies):
        print(f'Fold {i + 1}: Best model saved as {model_name}')

    test_k_fold(device, base_path, result_folder)


if __name__ == "__main__":
    torch.manual_seed(99)
    if torch.backends.mps.is_available():
        mps_device = torch.device("mps" if torch.cuda.is_available() else "cpu")
    else:
        # gpu_device = torch.device("cuda" if torch.cuda.is_available() else "cpu") # use gpu_device if not Mac or Macbook
        print("MPS device not found.")
    base_path = './content/Paper/'
    result_folder = './results/0716/'
    train_loader, valid_loader, test_loader = dataLoader(base_path)
    best_model_name = train(mps_device, result_folder, train_loader, valid_loader, model_type='resnet18',
                            num_epochs=50, learning_rate=0.001, pretrained=False, num_classes=4)
    model, test_plots, test_acc = evaluation(mps_device, test_loader, result_folder,'best_1.pth', model_type = 'resnet18', num_classes = 4)
