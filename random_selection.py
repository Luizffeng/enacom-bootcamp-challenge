import numpy as np
import pandas as pd
from typing import List
from dataclasses import dataclass, replace

def solution(case_array: list, max_iter: int):
    max_custo, max_retorno = 0, 0
    
    for case in case_array:
        _orcamento = case[1]
        _df = case[0]
        
        for i in range(max_iter):
            for j in range(_df.shape[0]):
                df = _df.sample(n = j, replace = False)
                if df['Custo'].sum() <= _orcamento and df['Retorno'].sum() > max_retorno:
                    solution = df
                    max_custo = df['Custo'].sum()
                    max_retorno = df['Retorno'].sum()

    options = []
    for index, row in solution.iterrows():
        options.append(row['Opção'])

    solution = {
        'Opções': options, 
        'Custo': max_custo, 
        'Retorno': max_retorno
        }

    return solution