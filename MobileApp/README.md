# BioCosMe Mobile Application

## Overview

The BioCosMe mobile application is designed to detect the pH level of the biosensor lipstick through image analysis. It uses the front camera to capture images of lips with the applied lipstick and processes these images to determine saliva pH values based on observed color changes. The app targets pH levels of 5, 6, 7, and 8.

## Features

- **Image Capture**: Utilizes the front camera to capture images of lips with the applied lipstick.
- **pH Detection**: Processes captured images to detect pH levels based on color changes.
- **Color Readout Extraction**: Extracts the readout color from images for server-side processing.
- **ResNet-18 Integration**: Sends color data to a server where a ResNet-18-based CNN analyzes the data and classifies the pH level.

## How It Works

1. **Capture Image**: Open the app and use the front camera to take an image of the lips with the BioCosMe lipstick applied.
2. **Process Image**: The app extracts the color information from the captured image.
3. **Transmit Data**: The color data is sent to a remote server.
4. **Server Processing**: On the server, a ResNet-18-based Convolutional Neural Network (CNN), fine-tuned for our dataset, analyzes the color data to determine the pH level.
5. **Display Result**: The app receives and displays the detected pH level.
