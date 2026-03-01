import pandas as pd
from pathlib import Path

def load_data1():
    filepath = Path("../data/raw/data1.csv")
    data1 = pd.read_csv(filepath)
    return data1

def load_data2():
    filepath = Path("../data/raw/data2.csv")
    data2 = pd.read_csv(filepath)
    return data2

def load_data3():
    filepath = Path("../data/raw/data3.csv")
    data3 = pd.read_csv(filepath)
    return data3