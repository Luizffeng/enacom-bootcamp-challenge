import numpy as np
import pandas as pd
from typing import List
from dataclasses import dataclass

@dataclass
class ValuableItem:
    item: int
    custo: int
    retorno: int

    @property
    def value_density(self) -> float:
        return self.retorno / (self.custo + 1e-9)


def items_to_table(items: List[ValuableItem]) -> pd.DataFrame:
    records = [{
            'Item': i.item,
            'Custo (R$)': i.custo,
            'Retorno (R$)': i.retorno
        } for i in items]
    return pd.DataFrame.from_records(records)


def greedy_knapsack(
    orcamento: int, 
    available_items: List[ValuableItem]
) -> List[ValuableItem]:
    chosen_items = list()

    sorted_items = sorted(
        available_items, 
        key=lambda i: i.value_density,
        reverse=True)

    for item in sorted_items:
        if item.custo <= orcamento:
            chosen_items.append(item)
            orcamento -= item.custo
    return chosen_items


def resolve(df, orcamento) -> pd.DataFrame:
    available_items = [ValuableItem(u, v, w) for i, (u, v, w) in enumerate(zip(df['Opção'], df['Custo'], df['Retorno']))]
    chosen_items = greedy_knapsack(orcamento, available_items)
    return chosen_items

# Cria uma lista de 'chosen_items', tranforma cada um
# em um modelo contido em 'models' e faz uma comparação,
# retornando um dict de solution
#def solution(df_list: list[pd.DataFrame], orcamento) -> list:
def solution(case_array: list[pd.DataFrame, int]) -> list:
    chosen_items_list = []
    for case in case_array:
        #print(case)
        chosen_items_list.append(resolve(case[0], case[1]))

    results, models = [], []
    for i in range(len(chosen_items_list)):
        results.append({'Items': [], 'Custo': 0, 'Retorno': 0})
        models.append([results[i], chosen_items_list[i]])

    for model in models:
        for item in model[1]:
            model[0]['Items'].append(item.item)
            model[0]['Custo'] += item.custo
            model[0]['Retorno'] += item.retorno

    max_retorno = 0
    custo_total = 0
    options = []
    for model in models:
        if model[0]['Retorno'] > max_retorno:
            max_retorno = model[0]['Retorno']
            custo_total = model[0]['Custo']
            options = model[0]['Items']
            options.sort()
    
    return {
        'Opções': options, 
        'Custo': custo_total, 
        'Retorno': max_retorno
        }