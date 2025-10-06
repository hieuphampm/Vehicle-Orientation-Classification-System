
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
- Vehicle orientation classification using **ResNet50** with fine-tuning  
- Data augmentation and preprocessing pipeline  
- Class balancing with `compute_class_weight`  
- Training & fine-tuning with **callbacks** (EarlyStopping, ReduceLROnPlateau, ModelCheckpoint)  
- Evaluation on both **AutoTest** and **ManualTest** sets

## Review Datasets
### Front
<p align="center">
  <img src="Datasets/Train/front/front_2.jpg" alt="Front" width="250"/>
  <img src="Datasets/Train/front/front_23.jpg" alt="Front" width="250"/>
  <img src="Datasets/Train/front/front_57.jpg" alt="Front" width="250"/>
</p>

### Front-left
<p align="center">
  <img src="Datasets/Train/front_left/front_left_2.jpg" alt="Front-left" width="250"/>
  <img src="Datasets/Train/front_left/front_left_4.jpg" alt="Front-left" width="250"/>
  <img src="Datasets/Train/front_left/front_left_32.jpg" alt="Front-left" width="250"/>
</p>

### Front-right
<p align="center">
  <img src="Datasets/Train/front_right/front_right_10.jpg" alt="Front-right" width="250"/>
  <img src="Datasets/Train/front_right/front_right_102.jpg" alt="Front-right" width="250"/>
  <img src="Datasets/Train/front_right/front_right_279.jpg" alt="Front-right" width="250"/>
</p>

### Rear
<p align="center">
  <img src="Datasets/Train/rear/rear_2.jpg" alt="Rear" width="250"/>
  <img src="Datasets/Train/rear/rear_19.jpg" alt="Rear" width="250"/>
  <img src="Datasets/Train/rear/rear_253.jpg" alt="Rear" width="250"/>
</p>

### Rear-left
<p align="center">
  <img src="Datasets/Train/rear_left/rear_left_4.jpg" alt="Rear-left" width="250"/>
  <img src="Datasets/Train/rear_left/rear_left_20.jpg" alt="Rear-left" width="250"/>
  <img src="Datasets/Train/rear_left/rear_left_47.jpg" alt="Rear-left" width="250"/>
</p>

### Rear-right
<p align="center">
  <img src="Datasets/Train/rear_right/rear_right_20.jpg" alt="Rear-right" width="250"/>
  <img src="Datasets/Train/rear_right/rear_right_240.jpg" alt="Rear-right" width="250"/>
  <img src="Datasets/Train/rear_right/rear_right_54.jpg" alt="Rear-right" width="250"/>
</p>

### High-angle-view
<p align="center">
  <img src="Datasets/Train/high_angle_view/high_angle_view_2.jpg" alt="High-angle-view" width="250"/>
  <img src="Datasets/Train/high_angle_view/high_angle_view_30.jpg" alt="High-angle-view" width="250"/>
  <img src="Datasets/Train/high_angle_view/high_angle_view_103.jpg" alt="High-angle-view" width="250"/>
</p>

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
