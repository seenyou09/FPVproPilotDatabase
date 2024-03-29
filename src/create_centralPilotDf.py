#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 15:16:13 2023

@author: seanyoo
"""
import pandas as pd 


multigp_df= pd.read_csv('/Users/seanyoo/Desktop/central_database_fpvPilot /csv/MultiGP.csv')
mldr_df = pd.read_csv('/Users/seanyoo/Desktop/central_database_fpvPilot /csv/MLDR.csv')
bdra_df= pd.read_csv('/Users/seanyoo/Desktop/central_database_fpvPilot /csv/BDRA.csv')
dcl_df= pd.read_csv('/Users/seanyoo/Desktop/central_database_fpvPilot /csv/DCL.csv')

mldr_df = mldr_df.rename(columns = {"Handle":"Name"})
mldr_df = mldr_df.rename(columns=lambda x: x.capitalize())
mldr_df.columns = mldr_df.columns.str.strip()
mldr_df = mldr_df[["Name","Type of pilot","Youtube", "Instagram"]]

bdra_df = bdra_df.rename(columns=lambda x: x.capitalize())
bdra_df = bdra_df[["Name","Type of pilot","Youtube", "Instagram"]]

dcl_df =dcl_df.rename(columns={"Type of Pilot" : "Type of pilot"})
dcl_df = dcl_df[["Name","Type of pilot","Youtube","Instagram"]]

multigp_df = multigp_df.rename(columns= {"Type of Pilot" : "Type of pilot"})
multigp_df = multigp_df[["Name","Type of pilot","Youtube", "Instagram"]]

df = pd.concat([multigp_df, dcl_df, bdra_df,mldr_df], ignore_index=True, sort=False)