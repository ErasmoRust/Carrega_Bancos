# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:22:07 2024

@author: erasmo.morais
"""

#%%
import pandas as pd
import numpy as np

#%%
#importando os bancos de dados em CSV

dados_cvm = pd.read_csv('nomecsv.csv',
                        sep=';', #tipo de separador
                        encoding = 'latin1')#caso contenha caracteres especiais



#%% 
#importando os bancos de dados em XLSX
nome_objeto1 = pd.read_excel('nometabela.xls')
nome_objeto2 = pd.read_excel('nometabela')
