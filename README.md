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
Or try to install these pip packages
```sh
pip install torch
pip install torchvision
pip install opencv-python
pip install matplotlib
pip install scikit-learn
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

##Fabrication
###Lipstick
Ingredients:
Commercial Lipstick Base from TKB (33.3%) https://tkbtrading.com/products/lip-stick-base
Cetyl alcohol (8.3%) https://a.co/d/3L3egQI
Non-Nano Titanium Dioxide (8.3%) https://a.co/d/bC0Dbmd
Skin Safe Primer Adhesive (8.3%) https://a.co/d/55gygY8
Clear Silver Mica Powder (8.3%) https://tkbtrading.com/collections/mica?utm_source=google&utm_medium=cpc&utm_campaign=shopping&tw_source=google&tw_adid=&tw_campaign=17686575245&gad_source=1&gclid=CjwKCAjwzIK1BhAuEiwAHQmU3tBe1-ueAhJVZIbTSuUVLRqkPKtolYCYwpfHtHFUPN45eAudbUZM-hoCZkAQAvD_BwE
Red Cabbage Powder (33.3%) https://suncorefoods.com/products/cosmos-red-cabbage-powder


1. Heat lipstick base until fully melted (175ºF)
2. Mix in Cetyl Octanoate, Non-Nano Titanium Dioxide, Skin Safe Primer Adhesive until melted (175ºF)
3. Magnetic stir for around 20 minutes
4. Lower temperature to 165ºF
5. Mix in Clear Silver Mica Powder, Red Cabbage Powder
6. Magnetic stir for around 10 minutes
7. Hand blend for around 15 minutes 
8. Pour into pre-chilled mold (35°F)
9. Chill for 10 minutes before demolding 


###Lipgloss
Ingredients:
Commercial Lipgloss Base from TKB (25%) https://tkbtrading.com/products/tkb-lip-gloss-base-flexagel?_pos=1&_sid=86a78b527&_ss=r
Glycerin (8.3%) https://tkbtrading.com/collections/tkb-lip-gloss-versagel/products/glycerine
Cetyl Octanoate (8.3%)
Non-Nano Titanium Dioxide (8.3%)
Skin Safe Primer Adhesive (8.3%)
Clear Silver Mica Powder (8.3%)
Red Cabbage Powder (33.3%)


1. Heat lipgloss base until it is less viscous (175ºF)
2. Mix in glycerin 
3. Put in magnetic stirrer
4. Mix in Cetyl Octanoate, Non-Nano Titanium Dioxide, Skin Safe Primer Adhesive until melted (175ºF)
5. Magnetic stir for around 20 minutes
6. Lower temperature to 165ºF
7. Mix in Clear Silver Mica Powder, Red Cabbage Powder
8. Magnetic stir for around 10 minutes
9. Hand blend for around 15 minutes 
10. Cool till it is below 130°F to safely pour into container


###Lip stain/tint
Ingredients:
30 g Red Cabbage Powder
8 g Clear Silver Mica Powder 
200 mL Deionized Water
80 mL Vegetable Glycerin
5 mL Phenoxyethanol https://a.co/d/9Vzw30U
3 mL Polysorbate 80 6 oz https://a.co/d/a4YhhxH 


1. mixing 80 g of cold water, from the total 280 g,  with red cabbage powder gradually until well combined
2. Add in glycerin 
3. Magnetic stir at 165°F
4. Gradually add in the remaining water until the mixture reaches a thickness similar to room-temperature olive oil
5. Lower temperature to 120°F
6. add in the Phenoxyethanol and Polysorbate 80
7. Stir for 20 minutes
8. Put into containers

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request.
