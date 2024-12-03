# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:22:07 2024

@author: erasmo.morais
"""

#%%
import pandas as pd

#%% 
#importando os bancos de dados em XLSX

nome_objeto = pd.read_excel('nome_tabela.xls')

#%%

#importando os bancos de dados em CSV

nome_objeto = pd.read_csv('nome_arquivo.csv', 
                          sep=',')   #Tipo de separador
                                     

nome_objeto = pd.read_csv('nome_arquivo.csv',
                        sep=';', #Tipo de separador
                        encoding = 'latin1')#caso contenha caracteres especiais

#%%
