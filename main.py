from data_loader import dataLoader
from evaluations import evaluation
from training import train
import torch


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
