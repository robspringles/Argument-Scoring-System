# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from essay_features import inf_summary

text = "Hello world! this is a test. This is another test."
print (inf_summary(text))