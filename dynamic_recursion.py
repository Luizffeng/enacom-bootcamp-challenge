import numpy as np
import pandas as pd

def solution(case_array: list, mmc=1) -> list:

    for case in case_array:
        _orcamento = case.copy()[1]/mmc
        _df = case.copy()[0]
        _df['Custo'], _df['Retorno'] = _df['Custo'].div(mmc), _df['Retorno'].div(mmc)
        
        value_matrix = np.zeros((int(_orcamento) + 1, _df.shape[0] + 1), int)
        binary_matrix = value_matrix.copy()

        for i in range(1, int(_orcamento + 1)):
            binary_matrix[i] *= 0
            for j in range(1, _df.shape[0] + 1):
                custo = _df.iloc[j-1]['Custo']
                retorno = _df.iloc[j-1]['Retorno']
                
                if custo <= i:
                    new_value = retorno + value_matrix[i - int(custo)][j-1]
                    old_value = value_matrix[i][j-1]
                    if new_value > old_value:
                        binary_matrix[i][j] = 1 
                    else:
                        binary_matrix[i][j] = 0


                    value_matrix[i][j] = max(new_value, old_value)

                else:
                    value_matrix[i][j] = value_matrix[i][j-1]

        #print(value_matrix)
        for i in range(len(value_matrix) - 1, 1, -1):
            for j in range(len(value_matrix[i]) - 1, 1, -1):
                #print(value_matrix[i][j])
                pass

        for i in range(len(value_matrix)):
            print(f'{i} => {binary_matrix[i]}')
        
        for i in range(len(value_matrix)):
            print(f'{i} => {value_matrix[i]}')
    
        #print(value_matrix)
    max_retorno = 0
    result = None

    return {
        'Opções': None,
        'Custo': None,
        'Retorno': max_retorno
    }