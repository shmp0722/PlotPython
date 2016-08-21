# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 15:53:11 2016

@author: shumpei
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#import pivottablejs.pivot_ui as pvui 

df=pd.read_csv('unrestricted_hcp_freesurfer.csv')

# plot distribution
sns.distplot(df.FS_3rdVent_Vol)
#plt.savefig('distExample.eps')

# load example small data set 
iris = sns.load_dataset("iris")  ## Rでお馴染みのアヤメの統計データ
sns.pairplot(iris, hue="species")

