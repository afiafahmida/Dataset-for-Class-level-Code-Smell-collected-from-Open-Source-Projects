# Dataset for Class level Code Smell collected from Open Source Projects


This repository accompanies the thesis **"An Interpretable Framework for Code Smell Detection Using Transformers, AutoML, and Explainable AI"**. It provides metadata, documentation, and sample scripts related to the dataset and framework described in the research.

## DESCRIPTION

The dataset consists of structural software metrics and labeled code smell annotations collected from multiple open-source Java projects. It supports research on automated code smell detection, transferability, and explainability using deep learning, AutoML, and SHAP. The considered code smells are: Anti singleton, Class Data Should be Private, Base Class should be Abstract, Blob, Complex Class, Large Class and Lazy Class

## Folder Informations
__Final Datasets: This folder contains binary data on existence of code smell of seven code smells individually.  
__7 smell Dataset: This folder contains seven folder of seven code smells. Each folder has a compilation of that smell from open source projects.

## Steps of how the Dataset was created:
1. Setup "Understand" tool.
2. We have collected .java files of code smells from this research paper: https://shorturl.at/ZAiAk
3. Create **.und** files of the real source codes and .java files of smelly codes using Understand tool to collect information of all metrics of the codes:
     -Go to File > New > Project
     -Select the source file of the project from "Root Directory" and press "Next"
     -Select Languages & Compilers and press next
     -Press "Create Project"
4. Both the files are are converted to CSV files using a python script "MakeProjectCSV.py" from CODE folder.
      -Modify Understand API path sys.path.insert(0, r"Demo->E:/Thesis/SciTools/bin/pc-win64/Python") and Python path to locate DLLs os.add_dll_directory(r"Demo->E:/Thesis/SciTools/bin/pc-win64/")
      -Modify und_file_path and csv_output_file each time for each files
6. Merge the smelly csv files with all metrics from source code pointing out smell or not using "mergingcsv.py" from CODE folder
      -Modify source_csv = r"path"  # All Java class metrics
           smelly_csv = r"path"  # Smelly class metrics
           output_csv = r"path"  # Final output file
7. After the creation of all .csv file from individual projects merge them into individual code smells. In our case we handled the last step manually in excel sheet and the result .csv binary files are in **__Final Datasets folder**

<!-- ## REPOSITORY CONTENTS

- `docs/` — Documentation describing the data collection, metrics, and labeling process.
- `sample/` — Small, anonymized sample files illustrating the data format.
- `scripts/` — Example scripts for loading and preprocessing metrics.
- `README.md` — This file. -->


## **Note:**
For further queries, please contact any of the authors:

> **Name:** AFIA FAHMIDA  
> **Email:** afiafahmida.p@outlook.com  
> **Institution:** Ahsanullah University of Science and Technology

> **Name:** ZENUN CHOWDHURY  
> **Email:**   Zenun786@gmail.com
> **Institution:** Ahsanullah University of Science and Technology 


> **Name:** AMRITA DEWANJEE  
> **Email:** dewanjeeamrita06@gmail.com  
> **Institution:** Ahsanullah University of Science and Technology



<!-- ## How to Use

You can use the provided scripts to:
- Load the sample data.
- Test preprocessing pipelines.
- Understand the structure and expected format.


## Citation

If you use this dataset or framework in your research, please cite:

> **  **

Or refer to the accompanying thesis.

## Contact

For questions, please open an issue or email [your.email@domain.com].

---

**License:** [Choose an appropriate license, e.g., CC BY-NC 4.0 for academic use]

-->

