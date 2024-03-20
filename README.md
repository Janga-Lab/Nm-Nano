# Nm-Nano
Nm-Nano: A framework for predicting 2´-O-Methylation (Nm) Sites in Nanopore RNA Sequencing Data

# Getting Started and pre-requisites
The following softwares and modules should be installed before using  Nm-Nano

python 3.7.13

minimpa2 (https://github.com/lh3/minimap2)

Nanopolish (https://github.com/jts/nanopolish)

samtools (http://www.htslib.org/)

numpy 1.19.5

pandas 1.2.4

scikit-learn 1.0.2 

tensorflow 2.6.0

keras 2.6.0 (using Tensorflow backend)

gensim  4.2.0

The easiest way to get all python packages installed and running without root access is through conda. create the conda environment with the provided yml file and activate the environment

conda env create -f Nm-nano.yml

conda activate Nm-nano


# Running  Nm-Nano:

In order to run  Nm-Nano, the user has to choose one of Nm-nano machine learning models (xgboost or Random forest with embeeding) and run one of following python commands:

python test_xgboost.py      #To run the xgboost model

Or 

python RF_embedding.py           #To run the RF with embeeding model


# Note:
- The user should include the benchmark dataset in the same path of test_xgboost.py and RF_embedding.py

- All files required to generate the benchmark dataset are included in the generate_benchmark folder. To allow users to practice with Nm-nano predictors, we include a small benchmark dataset sample for Hela cell line. However, the user is free to generate a benchmark benchmark dataset for any other cell lines based on the instructions mentioned in README file in generate_benchmark folder.
