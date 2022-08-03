import heuristic
import locale
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

table_1= df_and.drop(4)   # Dataframe que contém a opção 1
table_5 = df_and.drop(0)   # Dataframe que contém a opção 5

case_array = [[table_1, orcamento], [table_5, orcamento]] # Array contendo os cases específicos

### Resolve
# Calcula o valor ótimo para cada case
chosen_items = []
for case in case_array:
    chosen_items.append(heuristic.resolve(case[0], case[1]))

# Adiciona os dados de cada case para futura comparação
results, models = [], []
for i in range(len(chosen_items)):
    results.append({'Items': [], 'Custo': 0, 'Retorno': 0})
    models.append([results[i], chosen_items[i]])

for model in models:
    for item in model[1]:
        model[0]['Items'].append(item.item)
        model[0]['Custo'] += item.custo
        model[0]['Retorno'] += item.retorno

# Comparação de cases e solução
max_retorno = 0
custo_total = 0
solution = []
for model in models:
    if model[0]['Retorno'] > max_retorno:
        max_retorno = model[0]['Retorno']
        custo_total = model[0]['Custo']
        solution = model[0]['Items']

### Mensagens
solution.sort()
t = ''
for i in solution:
    aux = df[df['Opção'] == i]['Descrição'].to_string(index=False)
    t += f'    - {i}: {aux}\n'

msg = (
    f'A melhor solução contém os seguintes investimentos: \n{t}'
    f'\nEsta solução consome {currency(custo_total)} do orçamento, tem um retorno de {currency(max_retorno)}!!!'
)
print(msg)

