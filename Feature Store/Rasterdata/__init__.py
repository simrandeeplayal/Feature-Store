import numpy as np
import pandas as pd
import rasterio
import rasterio.features
import rasterio.warp
from matplotlib import pyplot as plt
from rasterio.plot import show
from configparser import ConfigParser

file =  'config.ini'
config = ConfigParser()
config.read(file)

file1 = config['ECE file path']['ECEpath']
file2 = config['Depth of Soil file path']['Soilpath']
file3 = config['Raw data file']['Rawpath']
file4 = config['Sand file path']['Sandpath']

dataset1 = rasterio.open(file1)
dataset2 = rasterio.open(file2)
dataset3 = rasterio.open(file4)

band1 = dataset1.read(1)
band2 = dataset2.read(1)
band3 = dataset3.read(1)

def featureextract(x,y):
    xs = x
    ys = y
    with dataset1 as src:
        rows1, cols1 = rasterio.transform.rowcol(src.transform, xs, ys)   
    
    with dataset2 as src:
        row2, cols2 = rasterio.transform.rowcol(src.transform, xs, ys)
 
    with dataset3 as src:
        row3, cols3 = rasterio.transform.rowcol(src.transform, xs, ys)
    
    feature1 = band1[rows1, cols1]
    feature2 = band2[row2, cols2]
    feature3 = band3[row3, cols3]
    
    return [feature1, feature2 ,feature3]


def mergingdata():
    df_data = pd.read_csv(file3)
    df_data['ECE'] = 0.5
    df_data['DES'] = 0.5
    df_data['SND'] = 0.5

    for i, row in df_data.iterrows():  
        x = df_data['long'][i]
        y = df_data['lag'][i]
        a, b, c = featureextract(x,y)
        df_data['ECE'][i] = a
        df_data['DES'][i] = b
        df_data['SND'][i] = c
    
    df_data.to_excel("testpackage.xlsx",index=False)

    return df_data

def showmap1():
    show(dataset1)

def showmap2():
    show(dataset2)

def showmap3():
    show(dataset3)

