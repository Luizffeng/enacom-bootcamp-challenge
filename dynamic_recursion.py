import numpy as np
import time

def solution(case_array: list, mmc=1) -> dict:
    '''
    Utilizando recursão dinâmica, esta função é capaz de encontrar um solução
    convergente, ou seja, é realmente capaz de encontrar o valor ótimo para 
    cada caso específico. Quanto mais discreto os valores tratados, menor o número
    de iterações necessárias para se alcançar o valor ótimo (serve também para
    o tamanho do dataframe)
    '''
    start_time = time.time()
    results = {'Opções': [], 'Custo': 0, 'Retorno': 0, 'Tempo': 0}
    for case in case_array:
        # orçamento
        _orcamento = int(case.copy()[1]/mmc)

        # cases
        _df = case.copy()[0]    # Copia o df de origem
        _df.sort_values(by=['Custo'], inplace=True, ascending=True) # Ordena os indexes por 'Custo'
        _df = _df.reset_index(drop=True)    # Reseta os indexes do df
        _df['Custo'], _df['Retorno'] = _df['Custo'].div(mmc), _df['Retorno'].div(mmc)   # Divide os valores pelo MMC
        
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
                        binary_matrix[i][j] = custo
                        value_matrix[i][j] = new_value
                    else:
                        binary_matrix[i][j] = 0
                        value_matrix[i][j] = old_value

                    value_matrix[i][j] = max(new_value, old_value)

                else:
                    value_matrix[i][j] = value_matrix[i][j-1]



        # Realiza a iteração inversa, a fim de rastrear a trajetória
        # de construção do valor ótimo
        result, max_custo, max_retorno = [], 0, 0
        i = int(_orcamento)
        j = int(_df.shape[0])
        while i >= 1 and j >= 1:
            #print(i, j, value_matrix[100])
            if value_matrix[i][j] == value_matrix[i][(j-1)]:
                j -= 1
                continue
            
            elif value_matrix[i][j] == value_matrix[i-1][j]:
                i -= 1
                continue

            elif value_matrix[i][j] != value_matrix[i-1][j]:
                i -= int(_df.iloc[j-1]['Custo'])
                result.append(_df.iloc[j-1]['Opção'])
                max_custo += int(_df.iloc[j-1]['Custo'] * mmc)
                max_retorno += int(_df.iloc[j-1]['Retorno'] * mmc)
                continue

        # Seleciona o melhor case (df)
        if max_retorno > results['Retorno']:
            results['Opções'] = result
            results['Custo'] = max_custo
            results['Retorno'] = max_retorno

            results = {
                'Opções': result, 
                'Custo': max_custo, 
                'Retorno': max_retorno
            }

        elif max_retorno == results['Retorno'] and max_custo < results['Custo']:
            results['Opções'] = result
            results['Custo'] = max_custo
            results['Retorno'] = max_retorno

            results = {
                'Opções': result, 
                'Custo': max_custo, 
                'Retorno': max_retorno
            }

    results['Tempo'] = time.time() - start_time

    return results