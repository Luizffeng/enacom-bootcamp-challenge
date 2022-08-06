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


def solution(case_array: list, orcamento: int, mmc=1) -> list:

    for case in case_array:
        _orcamento = int(case[1]/mmc)
        _df = case[0]
        print(_df)
        
        value_matrix = np.zeros((_orcamento + 1, _df.shape[0] + 1), int)
        binary_matrix = value_matrix.copy()

        options = []

        #print(df.shape)
        for i in range(1, _orcamento):
            for j in range(1, _df.shape[0]):
                if _df.iloc[j-1]['Retorno'] <= i:
                    new_value = _df[j-1]['Custo'] + value_matrix[i - _df[0][j - 1]]
                    old_value = value_matrix[i][j-1]
                    value_matrix = max(new_value, old_value)
                else:
                    value_matrix[i][j] = value_matrix[i][j-1]


    print(value_matrix)
    print(binary_matrix)

    return 