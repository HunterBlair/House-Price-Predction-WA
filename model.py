# importing packages
from flask import Flask
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

app = Flask(__name__)

"""
Next Clean data to get the variables that we want to 
train our model with. I will be using number of beds, number
of baths, sqft of living area, condition and, water front.
"""


