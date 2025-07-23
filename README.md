# AML-Project: Lung & Colon Cancer Histopathological Image Classification (Automated Pipeline)

[![CI](https://github.com/AmirAynede/AML-Project/actions/workflows/run_ml_pipeline.yml/badge.svg)]()
[![Citation](https://img.shields.io/badge/Citation-CFF-lightgrey?style=flat-square&logo=academia&logoColor=black)](https://github.com/AmirAynede/LC25000-Cancer-Classification/blob/main/CITATION.cff)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC--BY--NC--SA--4.0-orange?style=flat-square&logo=creativecommons&logoColor=white)](https://github.com/AmirAynede/LC25000-Cancer-Classification/blob/main/LICENSE.md)
[![LC25000 Cancer Classification](https://img.shields.io/badge/LC25000%20Cancer%20Classification-Main%20Repository-blue?style=flat-square&logo=github&logoColor=white)](https://github.com/AmirAynede/LC25000-Cancer-Classification/edit/main/README.md)




---
## Overview

This repository contains a full end-to-end machine learning pipeline for classifying lung and colon cancer histopathological images (LC25000 dataset). It covers data download, preprocessing, train/validation split, model training, evaluation, and visual explanations via Grad-CAM, all orchestrated via GitHub Actions.

---

## Repository Structure
```bash
.
├── .github
│   └── workflows
│       └── run_ml_pipeline.yml   # GitHub Actions CI pipeline
├── data
│   └── lc25000_split             # train/val/test splits (auto-generated)
├── outputs                       # evaluation & Grad-CAM results
├── results
│   ├── class_names.json          # mapping of class indices to labels
│   └── metrics.json              # evaluation metrics (auto-generated)
├── saved_models                  # model checkpoint(s)
├── scripts
│   ├── split_dataset.py          # create train/val/test splits
│   ├── train.py                  # training script (entry point: -m scripts.train)
│   ├── evaluate_on_test.py       # evaluation on held-out test set
│   └── gradcam.py                # generate Grad-CAM visualizations
├── requirements.txt              # Python dependencies
└── README.md                     # this file
```
---

## .gitignore

To keep your commits clean, add the following to `.gitignore`:

```gitignore
# macOS
.DS_Store

# Vim swap files
*.swp
```
---

## Prerequisites

Python 3.11
GitHub account with Kaggle credentials stored as secrets:
KAGGLE_USERNAME
KAGGLE_KEY

---

## Installation & Setup

1. Clone the repo
```
git clone https://github.com/AmirAynede/AML-Project.git
cd AML-Project
```
2. Install dependencies
```
python -m pip install --upgrade pip
pip install -r scripts/requirements.txt
pip install kaggle kagglehub

```
3. Configure Kaggle API
Store your Kaggle credentials in GitHub Secrets and (locally) at `~/.kaggle/kaggle.json`:

```
{
  "username":"<your_username>",
  "key":"<your_key>"
}
chmod 600 ~/.kaggle/kaggle.json

```
---

## Usage

1. Download & Extract Data
```
mkdir -p data
kaggle datasets download andrewmvd/lung-and-colon-cancer-histopathological-images -p data/
unzip data/*.zip -d data/Lung_and_Colon_Cancer

```
2. Create Train/Val/Test Splits
```
python3 scripts/split_dataset.py
# generates `data/lc25000_split/{train,val,test}` folders
```
3. Train the Model
```
python3 -m scripts.train
# checkpoints saved to `saved_models/`
```
4. Evaluate on Test Set
```
python3 -m scripts.evaluate_on_test
# metrics written to `results/metrics.json`

```
5. Generate Grad-CAM Visualizations
```
python3 -m scripts.gradcam
# visualizations saved to `outputs/`
```
---

## Continuous Integration (GitHub Actions)
On every push to main (or via manual dispatch), the workflow will:

1.Set up Python 3.11

2.Install dependencies

3.Download and unzip the LC25000 dataset
4.Split the dataset

5.Train the model

6.Evaluate & generate Grad-CAM

7.Upload all artifacts (`lc25000-split`, `best-model`, `class-names`, `eval-gradcam-results`, and consolidated `ml-results`)

To see the artifacts follow this [link](https://github.com/AmirAynede/AML-Project/actions/runs/16198342699)

You can monitor pipeline runs on the [Actions tab](https://github.com/AmirAynede/AML-Project/actions)

---

## Contributing
1.Fork this repository

2.Create a feature branch (`git checkout -b feature/XYZ`)

3.Commit your changes (`git commit -m "Add XYZ"`)

4.Push to your branch (`git push origin feature/XYZ`)

5.Open a Pull Request

---

## Related Repository

This repository is an automated, “reproducibility‐friendly” version of the project.  
For the full, detailed version (including proposal and final report), see the main repository:  
**LC25000 Cancer Classification (full version)**  
https://github.com/AmirAynede/LC25000-Cancer-Classification

When citing or referring to the license, please use the Education Use License and citation information provided in the **main** repository README.




