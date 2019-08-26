# NIDExtractor (OCR implementation with pytesseract)

Email me at <anindya23@gmail.com>

## Introduction
NIDExtractor is just fun project to test the basic implementation of Tesseract (Google's OCR).
This project extracts NID from the National ID Card of Bangladesh. This project is developed by python along with the implementation of pytesseract libraries.

## Requirements
- Ubuntu (>=16.04)
- Python (>=3.6)

## Installation
* Download latest release
* Unzip the downloaded file
* Go to the root directory of the project from the terminal
* Run the following command to install the dependencies into ./vendor directory
```
pip3 install -r requirements.txt -t ./vendor/
```

## Run the project
* Go to the project's root directory
* Run main.py with the following command
```
python3.6 main.py
```

## Important Notes
In this project, I tried to make it as simple as possible. As I didn't follow the standard way to read the NID from the image, it has some limitations as follows:
* This project is completely dependant on Tesseract in case of segmentation.
* I didn't implemented any training process explicitely. Rather implemented Tesseract Internal process.
* Recognition process completely based on Tesseract.
* Not production ready
* No noise minimization process while segmentation. So input images must be in high quality and properly cropped.
* No multilingual recognition support 

