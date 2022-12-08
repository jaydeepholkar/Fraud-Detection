# Exploratory Data Analysis
# Q1 a)
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
df = pd.read_csv(r'D:\Data science\Day04_Assignment_Datasets\Q1_a.csv')
df
df.info()
#MEAN
df.dist.mean()
df.speed.mean()
#MEDIAN
df.dist.median()
df.speed.median()
#MODE
df.dist.mode()
df.speed.mode()
#VARIANCE
df.dist.var()
df.speed.var()
#STANDARD DEVIATION
df.dist.std()
df.speed.std()
#SKEWNESS
df.dist.skew()
df.speed.skew()
#KURTOSIS
df.dist.kurt()
df.speed.kurt()
# BOX-PLOT for to check the outliers
plt.boxplot(df.speed)
plt.boxplot(df.dist)


#TO CHECK THE NORMALITY
import scipy.stats as stats
import pylab
speedplt = stats.probplot(df.speed, dist="norm", plot=pylab)
disrplt = stats.probplot(df.dist, dist='norm', plot=pylab)

# Q1 B)
df2 = pd.read_csv(r'D:\Data science\Day04_Assignment_Datasets\Q2_b.csv')
df2
df2.info()
#MEAN
df2.WT.mean()
df2.SP.mean()
#MEDIAN
df2.SP.median()
df2.WT.median()
#MODE
df2.SP.mode()
df2.WT.mode()
#VARIANCE
df2.SP.var()
df2.WT.var()
#STANDARD DEVIATION
df2.WT.std()
df2.SP.std()
#SKEWNESS
df2.WT.skew()
df2.SP.skew()
#KURTOSIS
df2.WT.kurt()
df2.SP.kurt()
# BOX-PLOT for to check the outliers
plt.boxplot(df2.SP)
plt.boxplot(df2.WT)
#TO CHECK THE NORMALITY
import scipy.stats as stats
import pylab
speedplt = stats.probplot(df2.SP, dist="norm", plot=pylab)
disrplt = stats.probplot(df2.WT, dist='norm', plot=pylab)


