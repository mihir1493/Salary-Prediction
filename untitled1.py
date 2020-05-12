# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:00:13 2020

@author: LENOVO
"""

import glassdoor_scraper as gs
import pandas as pd
path = "C:/Users/LENOVO/Desktop/ds_salary/chromedriver"
df = gs.get_jobs('data scientist', 15, False, path, 15 ) 