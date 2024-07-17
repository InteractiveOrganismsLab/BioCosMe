# Machine Learning for Image Classification

This repository demonstrates various machine learning methods used for image classification.

## Setup

### 1. Prepare the Environment

Set up a virtual environment and install the required dependencies using `requirements.txt`.

```sh
# Create a virtual environment
python -m venv myenv  # or python3 -m venv myenv for macOS and Linux

# Activate the virtual environment
# For Windows
myenv\Scripts\activate

# For macOS and Linux
source myenv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Download Dataset

Download Paper.zip from https://drive.google.com/drive/u/2/folders/1qq6l7d5GhKywF7OMcMr4rxqVE8LBk1ne
Create a new folder named content and place the downloaded dataset folder inside content.
```sh
mkdir content
# Move the downloaded dataset into the 'content' folder
```

### 3. Setup Results Folder

Create a new folder named results to store the trained models.
```sh
mkdir results
```

## Usage

### Start Training
Run the following command to train and test the model:
```sh
python3 main.py
```

### Test with Trained Model
Run the following command to test the model with a trained model:
```sh
python3 test.py
```

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request.
