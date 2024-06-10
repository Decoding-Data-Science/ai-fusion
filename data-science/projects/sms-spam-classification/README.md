# Building SMS Spam Classifier Model

Our main goal of this project is to create SMS Spam Classifier Model. We will be using the dataset for building our Machine Learning Model from [here](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset).

In real world scenario, it is important for interpreting the how the model works and based on what the model is created. Therefore, to help us with that, we will first perform basic data cleaning (check for missing values, duplicated values, unwanted features etc) followed by exploratory data analysis. Then, we will perform data preprocessing and visualize the tokens further to understand how models will classify whether the sms message is spam or non-spam message. Note that the steps are not linear. Therefore, we will go back to the previous step if we find any inconsistency. Once done with this, we will be ready to create our machine learning model. After we are happy with our optimal model, we will be wrapping it with FastAPI, Dockerize it and deploy it in cloud.

Lets follow the steps to complete this project.

1 - Create conda environment.

```bash
create conda -n sms_spam_classification python=3.10
```

2 - Activate the environment.

```bash
create activate sms_spam_classification
```

3 - Create a new file `requirements.txt` in the workspace, copy the dependencies from the repository and install the dependencies.

```bash
pip install -r requirements.txt --no-cache-dir
```

4 - Create a python script in the main folder -> `template.py` and copy the code from this repository and paste it in python script file followed by running it.

```bash
python template.py
```

5 - File structure in our workspace folder should resemble as follows.

```bash
├── data
│   ├── processed
│   └── raw
├── notebooks
│   ├── 1_Data_Cleaning_and_EDA.ipynb
│   ├── 2_Data_Preprocessing.ipynb
│   └── 3_Token_Visualization.ipynb
├── params.yaml
├── requirements.txt
├── saved_models
├── src
│   └── __init__.py
└── template.py
```

6 - Download the dataset and place in data/raw folder.

7 - Perform Data Cleaning, Exploratory Data Analysis, Data Preprocessing and Token Visualizations in the notebooks present in the notebooks folder.

8 - Make a new directory utils. Under this folder create `__init__.py` and `helper.py`. Copy the contents of `helper.py` from this repository and paste it in the file. 