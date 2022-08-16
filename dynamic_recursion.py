import numpy as np

def solution(case_array: list, mmc=1) -> list:

    for case in case_array:
        _orcamento = int(case.copy()[1]/mmc)
        _df = case.copy()[0]
        _df.sort_values(by=['Custo'], inplace=True, ascending=True)
        _df['Custo'], _df['Retorno'] = _df['Custo'].div(mmc), _df['Retorno'].div(mmc)
        
        value_matrix = np.zeros((_orcamento + 1, _df.shape[0] + 1), int)
        binary_matrix = value_matrix.copy()

        for i in range(1, _orcamento + 1):
            binary_matrix[i] *= 0
            for j in range(1, _df.shape[0] + 1):
                custo = _df.iloc[j-1]['Custo']
                retorno = _df.iloc[j-1]['Retorno']
                
                if custo <= i:
                    new_value = retorno + value_matrix[i - int(custo)][j-1]
                    old_value = value_matrix[i][j-1]
                    if new_value > old_value:
                        #binary_matrix[i] = np.zeros(_df.shape[0] + 1, int)
                        binary_matrix[i][j] = custo
                        value_matrix[i][j] = new_value
                    else:
                        binary_matrix[i][j] = 0
                        value_matrix[i][j] = old_value


                    value_matrix[i][j] = max(new_value, old_value)

                else:
                    value_matrix[i][j] = value_matrix[i][j-1]

        for i in range(len(value_matrix)):
            #print(f'{i} => {binary_matrix[i]} -- {value_matrix[i]}')
            pass
        
        result, max_custo, max_retorno = [], 0, 0
        i = int(_orcamento)
        j = int(_df.shape[0] - 1)
        print(value_matrix[100][6])
        while i >= 1 and j >= 1:
            print(i, j, value_matrix[100])
            if value_matrix[i][j] == value_matrix[i][int(j-1)]:
                print(value_matrix[i][j])
                print(value_matrix[i][j-1])
                j -= 1
                print(type(j), type(i))
                continue
            
            elif value_matrix[i][j] == value_matrix[i-1][j]:
                i -= 1
                continue

            elif value_matrix[i][j] != value_matrix[i-1][j]:
                i -= _df.iloc[j]['Custo']
                result.append(_df.iloc[j]['Opção'])
                max_custo += _df.iloc[j]['Custo']
                max_retorno += _df.iloc[j]['Retorno']
                continue
            
    
    
    
    
    
        #print(value_matrix)
    #result = None

    return {
        'Opções': result,
        'Custo': max_custo,
        'Retorno': max_retorno
    }