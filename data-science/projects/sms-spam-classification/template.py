import os

dirs = [
    os.path.join("data", "raw"),
    os.path.join("data", "processed"),
    "notebooks",
    "saved_models",
    "src",
]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass

files = [
    "params.yaml",
    ".gitignore",
    os.path.join("src", "__init__.py"),
    os.path.join("notebooks", "1_Data_Cleaning_and_EDA.ipynb"),
    os.path.join("notebooks", "2_Data_Preprocessing.ipynb"),
    os.path.join("notebooks", "3_Token_Visualization.ipynb"),
]

for file_ in files:
    with open(file_, "w") as f:
        pass