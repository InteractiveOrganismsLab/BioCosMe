import torch
from torch.utils.data import DataLoader, Subset
import torchvision.datasets as datasets
import torchvision.transforms as transforms

import numpy as np
import cv2
import os


class ImageFolderWithPaths(datasets.ImageFolder):
    """Custom dataset that includes image file paths and converts images to LAB color space. Extends
    torchvision.datasets.ImageFolder.
    """

    def __getitem__(self, index):
        # This is what ImageFolder normally returns
        original_tuple = super(ImageFolderWithPaths, self).__getitem__(index)
        # The image file path
        path = self.imgs[index][0]
        file_name = os.path.basename(path)

        # Convert the image tensor to a NumPy array
        image_rgb_tensor = original_tuple[0]
        image_np = image_rgb_tensor.permute(
            1, 2, 0).numpy()  # Convert to HWC format

        # Convert the NumPy array from RGB to LAB
        image_np_uint8 = (image_np * 255).astype(np.uint8)  # Convert to uint8
        image_lab = cv2.cvtColor(image_np_uint8, cv2.COLOR_RGB2LAB)

        # Convert the LAB image back to a tensor
        image_lab_tensor = torch.from_numpy(
            image_lab).permute(2, 0, 1).float() / 255.0

        # Make a new tuple that includes original and the path
        tuple_with_lab_and_path = (
            image_rgb_tensor, original_tuple[1], file_name)
        return tuple_with_lab_and_path


def dataloader_origin_test(base_path):
    '''Load the dataset and split it into training and test sets'''

    # Initialize transformations for data augmentation
    transform = transforms.Compose([
        transforms.Resize((324, 324)),
        # transforms.CenterCrop(324),
        transforms.RandomHorizontalFlip(),
        transforms.RandomVerticalFlip(),
        transforms.RandomCrop((224, 224)),
        transforms.ToTensor(),
    ])

    # Load the ImageNet Object Localization Challenge dataset
    origin_dataset = ImageFolderWithPaths(
        root=base_path,
        transform=transform
    )

    n = len(origin_dataset)  # total number of examples
    n_test = int(0.1 * n)  # take ~10% for test
    print('training: ', n-n_test, 'test: ', n_test)

    train_dataset, test_dataset = torch.utils.data.random_split(
        origin_dataset, [n-n_test, n_test])

    return train_dataset, test_dataset


def dataLoader_cross(origin_dataset, train_idx, val_idx):
    '''Create data loaders for training and validation sets'''
    batch_size = 8

    train_dataset = Subset(origin_dataset, train_idx)
    validation_dataset = Subset(origin_dataset, val_idx)

    train_loader = DataLoader(
        train_dataset, batch_size=batch_size, shuffle=True, num_workers=1)
    valid_loader = DataLoader(
        validation_dataset, batch_size=batch_size, shuffle=False, num_workers=1)

    return train_loader, valid_loader


def dataLoader(base_path):
    '''Load the dataset and split it into training, validation, and test sets, including data augmentation'''
    batch_size = 8

    # Initialize transformations for data augmentation
    transform = transforms.Compose([
        transforms.Resize((512, 512)),
        transforms.RandomHorizontalFlip(),
        transforms.RandomVerticalFlip(),
        transforms.RandomCrop((224, 224)),
        transforms.ToTensor(),
    ])

    origin_dataset = ImageFolderWithPaths(
        root=base_path,
        transform=transform
    )

    n = len(origin_dataset)  # total number of examples
    n_test = int(0.1 * n)  # take ~10% for test
    n_validation = int(0.2 * n)  # take ~10% for validation
    print('training: ', n-n_test-n_validation, 'test: ',
          n_test, 'validation: ', n_validation)

    train_dataset, validation_dataset, test_dataset = torch.utils.data.random_split(
        origin_dataset, [n-n_test-n_validation, n_test, n_validation])

    train_loader = torch.utils.data.DataLoader(
        train_dataset, batch_size=batch_size, shuffle=True, num_workers=1)
    valid_loader = torch.utils.data.DataLoader(
        validation_dataset, batch_size=batch_size, shuffle=True, num_workers=1)
    test_loader = torch.utils.data.DataLoader(
        test_dataset, batch_size=batch_size, shuffle=True, num_workers=1)

    return train_loader, valid_loader, test_loader
