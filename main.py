import locale
import pandas as pd

import heuristic
import dynamic_recursion as dynamic
from data import Data

### Setup
# Definição de moeda local
def currency(value):
    return locale.currency(value, grouping=True)

locale.setlocale(locale.LC_ALL, 'pt_BR')

### Dataframe
path = 'ENACOM Optimization Bootcamp - Desafio.pdf'
df = Data.read(path).pdftodata()    # Lê o pdf e extrai os dados para um Dataframe
df_and = df.copy()  # Faz um cópia do DF original para aplicar as restrições

### Rules
orcamento = 10**6

### Restrictions
soma_custo = df['Custo'].iloc[1] + df['Custo'].iloc[3]
soma_retorno = df['Retorno'].iloc[1] + df['Retorno'].iloc[3]
df_and.loc[1]=['Opção 2+4', 'OPÇÃO AUXILIAR PARA REPRESENTAR OPÇÕES 2 E 4', soma_custo, soma_retorno]
df_and = df_and.drop(3) # Dataframe contendo a opção 2+4

table_1 = df_and.drop(4)   # Dataframe contendo a opção 1
table_5 = df_and.drop(0)   # Dataframe contendo a opção 5

# Array contendo os cases específicos
# Vale lembrar que, separando o orçamento das demais 
# restrições (cases), podemos também trabalhar com o mesmo
#case_array = [[table_1, orcamento], [table_5, orcamento]] 
case_array = [[table_1, orcamento]]


### Resolve
# Calcular o conjunto de opções ótimas para
# cada case contida no 'case_array' (dataframe específico de cada cenário),
# em cada um dos métodos utilizados, retornando a melhor solução de acordo
# com o método

# Heurística gulosa
heuristic_solution = heuristic.solution(case_array, orcamento)

# Heurística de recursão dinâmica
dynamic_solution_0 = dynamic.solution(case_array, orcamento, 10000)
#dynamic_solution_1 = dynamic.solution(case_array[1], orcamento[0], 10000)

# Algoritmo Genético

# Otimização ENACOM


### Mensagens
t = ''
for i in heuristic_solution['Opções']:
    aux = df[df['Opção'] == i]['Descrição'].to_string(index=False)
    t += f'    - {i}: {aux}\n'

msg = (
    f'\nA melhor solução contém os seguintes investimentos: \n{t}'
    f'\nEsta solução consome {currency(heuristic_solution["Custo"])}'
    f' do orçamento e tem um retorno de {currency(heuristic_solution["Retorno"])}!!!'
)
print(msg)

