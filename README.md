# 3D Muscle Segmentation using nnU-Net

This repository provides the code, pre-trained model, and example training data for **3D muscle segmentation** using the **nnU-Net framework**. The project focuses on segmenting major thoracic and lumbar spinal muscles from clinical CT scans, supporting applications in radiotherapy planning, clinical research, and automated muscle analysis.

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Installation and Usage](#installation)    
3. [Input Data Requirements](#input-data-requirements)  
4. [Model Details](#model-details)  
5. [Example Outputs](#example-outputs)  
6. [Anatomical Structure Table](#anatomical-structure-table)  
7. [Citation](#citation)  
8. [Acknowledgements](#acknowledgements)  
9. [License](#license)  
10. [Contact](#contact)  

---

## Project Overview

This project automates the segmentation of major spinal muscles from thoracic and lumbar CT images using the **nnU-Net framework**. Ground-truth muscle annotations were generated following established manual segmentation protocols.

### Key Features
- **Input**: Clinical thoracic and lumbar CT scans with the following field of view (FOV):  
  - **Skin-to-skin FOV**  
- **Output**: Binary segmentation masks for major spinal muscles, including:  
  - Multifidus  
  - Erector Spinae  
  - Psoas  
  - Quadratus Lumborum  
  - Rectus Abdominis  

### Repository Contents
This repository includes:
1. **Pre-trained Model**:  
   `nnUNetTrainer_2000epochs_NoMirroring__nnUNetPlans__2d.zip` (2.5GB)  
2. **Instructions**: Detailed guidance for reproducing segmentation results.

### Applications
The project supports:  
- Clinical radiotherapy treatment planning  
- Automated assessment of spinal muscle anatomy  
- Research into muscle-related diseases and sarcopenia  

---

## Installation

This project can be run in two ways:

1. **Through the 3D Slicer nnU-Net Extension** (recommended for ease of use)
2. **Locally using nnUNet commands** (for full flexibility and automation)

### Prerequisites

- **Python** (3.8 or later)
- **3D Slicer** ([Download here](https://www.slicer.org/))
- **nnU-Net** framework ([Installation Guide](https://github.com/MIC-DKFZ/nnUNet))
- **Required Python packages**:
  ```bash
  pip install numpy SimpleITK torch torchvision
  ```

---

### Option 1: 3D Slicer nnU-Net Extension

1. **Install 3D Slicer**:

   - Download and install from the official site: [3D Slicer Download](https://www.slicer.org/)

2. **Install the nnU-Net Extension**:

   - Follow the setup guide: [SlicerNNUnet Extension](https://github.com/KitwareMedical/SlicerNNUnet)

3. **Load the Pre-trained Model**:

   - Download the model weights:  
     [Pre-trained Model - nnUNetTrainer\_2000epochs\_NoMirroring\_\_nnUNetPlans\_\_2d.zip](<Link to release>)
   - Extract the model files and configure them in the Slicer nnU-Net module.

4. **Run the Segmentation**:

   - Prepare your input CT data in **DICOM** or **NIfTI** format.
   - Use the nnU-Net module in 3D Slicer to perform the segmentation and generate output masks.

---

### Option 2: Run Locally Using nnUNet Commands

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/nilsrehtanz/dl-muscle-segmentation.git
   cd dl-muscle-segmentation
   ```

2. **Install nnU-Net**:  
   Follow the official installation guide:

   ```bash
   pip install nnunet
   ```

3. **Set Up the Pre-trained Model**:

   - Download the model weights:  
     [Pre-trained Model - nnUNetTrainer\_2000epochs\_NoMirroring\_\_nnUNetPlans\_\_2d.zip](<Link to release>)
   - Extract the files:
     ```bash
     mkdir -p nnUNet_pretrained
     unzip nnUNetTrainer_2000epochs_NoMirroring__nnUNetPlans__2d.zip -d nnUNet_pretrained
     ```

4. **Prepare Input Data**:  
   If your CT data is in **DICOM** format, convert it to NIfTI using `dcm2niix`:

   ```bash
   dcm2niix -o /path/to/output /path/to/input_dicom
   ```

5. **Run Inference**:  
   Perform segmentation using the following command:

   ```bash
   nnUNet_predict -i /path/to/input_nifti \
                  -o /path/to/output_masks
   ```

   - Replace `/path/to/input_nifti` and `/path/to/output_masks` with your paths.

---

## Input Data Requirements
- **CT Scans**:
  - Slice thickness: 0.5mm or 1.25mm
  - Pixel size: 0.70-0.98mm
  - Field of View (FOV): Skin-to-skin

Refer to **Supplemental Table S.1** for detailed imaging protocol parameters.

---

## Model Details
- **Training Framework**: nnU-Net (2D Configuration)
- **Ground Truth**: Manual segmentations from thoracic (T4-T7) and lumbar (L2-L5) vertebral levels
- **Evaluation**: Segmentation accuracy validated using a Likert scale (0-5) for clinical acceptability.
- **Performance**: High inter- and intra-rater reliability (ICC: 0.84-0.99).

---

## Example Outputs
Below is an example segmentation output overlaying the binary masks on a CT slice:

![Example Segmentation](images/3D_DL_muscle_model_output.JPG)

---

## Anatomical Structure Table

| Anatomical Structure | Side  | Vertebral Levels |
|-----------------------|-------|------------------|
| Pectoralis Major      | Right | T4 - T9          |
| Pectoralis Major      | Left  | T4 - T9          |
| Rectus Abdominis      | Right | T10 - L5         |
| Rectus Abdominis      | Left  | T10 - L5         |
| Serratus Anterior     | Right | T4 - T11         |
| Serratus Anterior     | Left  | T4 - T11         |
| Latissimus Dorsi      | Right | T4 - L3          |
| Latissimus Dorsi      | Left  | T4 - L3          |
| Trapezius             | Right | T4 - T11         |
| Trapezius             | Left  | T4 - T11         |
| External Oblique      | Right | T10 - L5         |
| External Oblique      | Left  | T10 - L5         |
| Internal Oblique      | Right | L2 - L5          |
| Internal Oblique      | Left  | L2 - L5          |
| Erector Spinae        | Right | T4 - L5          |
| Erector Spinae        | Left  | T4 - L5          |
| Transversospinalis    | Right | T4 - L5          |
| Transversospinalis    | Left  | T4 - L5          |
| Psoas Major           | Right | L1 - L5          |
| Psoas Major           | Left  | L1 - L5          |
| Quadratus Lumborum    | Right | L1 - L4          |
| Quadratus Lumborum    | Left  | L1 - L4          |

### Remark:
Please note that the vertebral segmentations (#28 and higher) depending on the vertebral level present, should not be used for model creations. We have a separate accurate spine vertebral segmenter for cancer spines, or please use TotalSegmentator to segment non-cancer vertebrae ([TotalSegmentator Repository](https://github.com/wasserth/TotalSegmentator)).

---

## Citation
If you use this repository in your work, please cite:

> **3D Muscle Segmentation using nnU-Net**
> Ron N. Alkalay et al.
> [Arxiv Link!!!!]

For now, cite this repository:
```
@misc{3dmuscle_nnUNet,
  author = {Alkalay, Ron N.},
  title = {3D Muscle Segmentation using nnU-Net},
  year = {2024},
  howpublished = {GitHub repository},
  url = {https://github.com/nilsrehtanz/dl-muscle-segmentation}
}
```

---

## Acknowledgements
This work was supported by:
- **National Institute of Arthritis and Musculoskeletal and Skin Diseases**: Research Project Grants (AR055582, R56AR075964, and AR075964) for R. Alkalay and D. Anderson.

Special thanks to contributors:
- Ron N. Alkalay, Beth Israel Deaconess Medical Center, Harvard Medical School
- Dennis Anderson, Beth Israel Deaconess Medical Center, Harvard Medical School
- Steve Pieper, Isomics, Inc., Cambridge, MA 02138
- Csaba Pinter, Ebatinca SL, Las Palmas de Gran Canaria, Spain

---

## License
This project is licensed under the Apache 2.0 License. See the LICENSE file in the repository for details.

---

## Contact
For questions, please contact:
- **Ron N. Alkalay**  
  Beth Israel Deaconess Medical Center, Harvard Medical School  
  Email: [rn_alkalay@bidmc.harvard.edu](mailto:rn_alkalay@bidmc.harvard.edu)
