import locale
import pandas as pd

import heuristic
import dynamic_recursion
import random_selection
from data import Data

### Setup
# Definição de moeda local
def currency(value):
    return locale.currency(value, grouping=True)

locale.setlocale(locale.LC_ALL, 'pt_BR')

# Exibição de resultados
def print_solutions(solution: dict, solution_name: str):
    options = solution['Opções']
    custo = solution['Custo']
    retorno = solution['Retorno']

    print(f'MÉTODO: {solution_name}')
    print('O melhor conjunto solução contém:')
    for option in options: print(f'{option}')
    print(f'Custo total: {custo} | Retorno total: {retorno}\n')
    return


### Dataframe
path = 'ENACOM Optimization Bootcamp - Desafio.pdf'
df = Data.read(path).pdftodata()    # Lê o pdf e extrai os dados para um Dataframe
df_ = df.copy()  # Faz um cópia do DF original para aplicar as restrições


### Rules
orcamento = 10**6


### Restrictions
soma_custo = df['Custo'].iloc[1] + df['Custo'].iloc[3]
soma_retorno = df['Retorno'].iloc[1] + df['Retorno'].iloc[3]
df_2_4, df_4 = df_.copy(), df_.copy()

df_2_4.loc[df['Opção'] == 'Opção 2'] = ['Opção 2+4', 'OPÇÃO AUXILIAR PARA REPRESENTAR OPÇÕES 2 E 4', soma_custo, soma_retorno]
df_2_4 = df_2_4.drop(df.index[df['Opção'] == 'Opção 4']) # Dataframe contendo a opção 2+4
df_4 = df_.drop(df.index[df['Opção'] == 'Opção 2']) # DF contendo a opção 4 e excluindo a opção 2

df_1_2_4 = df_2_4.drop(df.index[df['Opção'] == 'Opção 5'])   # Dataframe contendo a opção 1 e 2+4
df_5_2_4 = df_2_4.drop(df.index[df['Opção'] == 'Opção 1'])   # Dataframe contendo a opção 5 e 2+4
df_1_4 = df_4.drop(df.index[df['Opção'] == 'Opção 5'])   # Dataframe contendo a opção 1 e 4 (apenas)
df_5_4 = df_4.drop(df.index[df['Opção'] == 'Opção 1'])   # Dataframe contendo a opção 5 e 4 (apenas)

# Array contendo os cases específicos
# Vale lembrar que, separando o orçamento das demais 
# restrições (cases), podemos também trabalhar com o mesmo
case_array = [
    [df_1_2_4, orcamento],
    [df_5_2_4, orcamento],
    [df_1_4, orcamento],
    [df_5_4, orcamento]
    ]


### Resolve
# Calcular o conjunto de opções ótimas para
# cada case contida no 'case_array' (dataframe específico de cada cenário),
# em cada um dos métodos utilizados, retornando a melhor solução de acordo
# com o método

# Heurística gulosa
heuristic_solution = heuristic.solution(case_array)

# Heurística aleatória
random_solution = random_selection.solution(case_array, max_iter=100)

# Heurística de recursão dinâmica
dynamic_solution = dynamic_recursion.solution(case_array, mmc=10000)

# Algoritmo Genético

# Otimização ENACOM


### Mensagens
print_solutions(heuristic_solution, 'Heurística Gulosa')
print_solutions(random_solution, 'Seleção Aleatória')
print_solutions(dynamic_solution, 'Recursão Dinâmica')
