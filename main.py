from operator import index
import numpy as np
import pandas as pd
import heuristic
from typing import List
from tkinter import E
from data import Data
from dataclasses import dataclass


### ROTINA
# Rules
orcamento = 10**6

# Data
path = 'ENACOM Optimization Bootcamp - Desafio.pdf'
df = Data.read(path).pdftodata()

df_and = df.copy()
df_or = df.copy()

# Heuristic
soma_custo = df['custo'].iloc[1] + df['custo'].iloc[3]
soma_retorno = df['retorno'].iloc[1] + df['retorno'].iloc[3]
df_and.loc[1]=['OPÇÃO AUXILIAR PARA REPRESENTAR PÇÕES 2 E 4', soma_custo, soma_retorno]
df_and = df_and.drop(3)
print(df_and)


print(df.iloc[1])
chosen_items = heuristic.resolve(df['custo'], df['retorno'], orcamento)
print(heuristic.items_to_table(chosen_items))
