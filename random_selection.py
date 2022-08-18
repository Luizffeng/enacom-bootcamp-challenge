import numpy as np
import pandas as pd

def solution(case_array: list[pd.DataFrame, int], max_iter: int) -> list:
    custo, retorno = 0, 0
    results = []
    for case in case_array:
        _orcamento = case.copy()[1]
        _df = case.copy()[0]
        
        for i in range(max_iter):
            for j in range(1, _df.shape[0]):
                df = _df.sample(n = j, replace = False)
                if df['Custo'].sum() <= _orcamento and df['Retorno'].sum() > retorno:
                    result = df['Opção'].to_list()
                    custo = df['Custo'].sum()
                    retorno = df['Retorno'].sum()
                    results.append([result, custo, retorno])

        result, max_custo, max_retorno = None, 0, 0
    
    for result in results:
        if result[2] >= max_retorno:
            max_retorno = result[2]
            max_custo = result[1]
            solution = result[0]

        elif result[2] == max_retorno:
            if result[1] <= max_custo:
                max_custo = result[1]
                solution = result[0]

    results = {'Opções': solution, 'Custo': max_custo, 'Retorno': max_retorno}
    return results