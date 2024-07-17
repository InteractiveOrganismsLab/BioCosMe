import torch
from torch.utils.data import DataLoader
from data_loader import dataloader_origin_test, dataLoader
from evaluations import evaluation


def test_k_fold(device, base_path,result_folder):
    origin_dataset, test_dataset = dataloader_origin_test(base_path)
    test_loader = DataLoader(test_dataset, batch_size=8, shuffle=True, num_workers=1)
    model, test_plots, test_acc = evaluation(device, test_loader, result_folder,'best_1.pth', model_type = 'resnet18', num_classes = 4)

def test(base_path,result_folder):
    if torch.backends.mps.is_available():
        mps_device = torch.device("mps" if torch.cuda.is_available() else "cpu")
    else:
        # gpu_device = torch.device("cuda" if torch.cuda.is_available() else "cpu") # use gpu_device if not Mac or Macbook
        train_loader, valid_loader, test_loader = dataLoader(base_path)
    model, test_plots, test_acc = evaluation(mps_device, test_loader, result_folder,'best_50.pth', model_type = 'resnet18', num_classes = 4)

if __name__ == "__main__":
    torch.manual_seed(99)
    base_path = './content/Paper/'
    result_folder = './results/0716/'
    test(base_path,result_folder)
    