# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 12:40:22 2021

@author: Yong Sheng
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 12:39:20 2021

@author: Yong Sheng
"""

import pandas as pd

x = pd.read_csv('aviation_main.csv')
y = pd.read_csv('aviation_inflow.csv')

new_x = pd.concat([x.tail(len(x) - 1000), y.head(1000)], ignore_index = True)
new_y = pd.concat([y.tail(len(y) - 1000), x.head(1000)], ignore_index = True)
