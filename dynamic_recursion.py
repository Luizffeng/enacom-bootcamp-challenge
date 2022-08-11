import numpy as np
import pandas as pd
from typing import List
from dataclasses import dataclass

@dataclass
class DataClass:
    item: int
    custo: int
    retorno: int


def items_to_table(items: List[DataClass]) -> pd.DataFrame:
    records = [{
            'Item': i.item,
            'Custo (R$)': i.custo,
            'Retorno (R$)': i.retorno
        } for i in items]
    return pd.DataFrame.from_records(records)


def solution(case_array: list, mmc=1) -> list:

    for case in case_array:
        _orcamento = case[1]/mmc
        print(_orcamento)
        _df = case[0]
        _df['Custo'], _df['Retorno'] = _df['Custo'].div(mmc), _df['Retorno'].div(mmc)
        print(_df)
        
        value_matrix = np.zeros((int(_orcamento) + 1, _df.shape[0] + 1), int)
        binary_matrix = value_matrix.copy()

        options = []

        #print(df.shape)
        for i in range(1, int(_orcamento + 1)):
            binary_matrix *= 0
            for j in range(1, _df.shape[0] + 1):
                custo = _df.iloc[j-1]['Custo']
                retorno = _df.iloc[j-1]['Retorno']
                
                #print(custo, retorno, i, j, sep=' | ')
                if custo <= i:
                    new_value = retorno + value_matrix[i - int(custo)][j-1]
                    old_value = value_matrix[i][j-1]
                    if new_value > old_value:
                        binary_matrix[i][j] = 1 
                    else:
                        binary_matrix[i][j] = 0

                    value_matrix[i][j] = max(new_value, old_value)
                    #last = 
                else:
                    value_matrix[i][j] = value_matrix[i][j-1]
                
            print(f'{i} = {value_matrix[i]} >< {binary_matrix[i]}')
            #print(f'{i} = {value_matrix[i]}')

        #print(binary_matrix)
        print('>>>>', value_matrix[-1][-1])

    ##print(value_matrix)
    ##print(binary_matrix)

    return 