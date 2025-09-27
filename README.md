
# Vehicle Orientation Classification System

This repository contains the implementation of a deep learning model for **vehicle orientation classification** using TensorFlow and Keras.

## Repository Structure

```
├── Datasets
│   ├── train
│   │   ├── front
│   │   ├── front-left
│   │   ├── front-right
│   │   ├── rear
│   │   ├── rear-left
│   │   ├── rear-right
│   │   └── high-angle-view
│   └── test
│       ├── AutoTest
│       │   ├── front
│       │   ├── front-left
│       │   ├── front-right
│       │   ├── rear
│       │   ├── rear-left
│       │   ├── rear-right
│       │   └── high-angle-view
│       └── ManualTest
│
├── Sample Output.csv
├── Vehicle_Orientation_Classification_System.ipynb
├── Vehicle_Orientation_Classification_System_Report.docx
├── requirements.txt
└── vehicle_orientation_model.keras
```

## Features
- Vehicle orientation classification with 7 classes:
  - `front`, `front-left`, `front-right`, `rear`, `rear-left`, `rear-right`, `high-angle-view`
- Preprocessing and data augmentation.
- Model training with **transfer learning** (fine-tuning).
- Evaluation with precision, recall, F1-score, and confusion matrix.
- Exported trained model (`.keras`).

## Installation

```bash
pip install -r requirements.txt
```

## Usage

1. Train the model:
   ```bash
   jupyter notebook Vehicle_Orientation_Classification_System.ipynb
   ```
2. Evaluate on test datasets (`AutoTest`, `ManualTest`).
3. Check the results in `Sample Output.csv`.

## Requirements
- Python 3.12.11
- TensorFlow 2.19.0
- OpenCV 4.12.0
- NumPy 2.0.2
- Pandas 2.2.2
- Scikit-learn 1.6.1
- Matplotlib 3.10.0
- Seaborn 0.13.2

## Report
Detailed documentation can be found in **Vehicle_Orientation_Classification_System_Report.docx**.

---

Developed for academic and research purposes by Pham Phuoc Minh Hieu.
