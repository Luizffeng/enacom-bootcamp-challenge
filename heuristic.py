import numpy as np
import pandas as pd
from typing import List
from tkinter import E
from data import Data
from dataclasses import dataclass

@dataclass
class ValuableItem:
    index: int
    custo: int
    retorno: int

    @property
    def value_density(self) -> float:
        return self.retorno / (self.custo + 1e-9)


def items_to_table(items: List[ValuableItem]) -> pd.DataFrame:
    records = [{
            'Item': i.index,
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
        else:
            break
    return chosen_items


def resolve(custo, retorno, orcamento) -> pd.DataFrame:
    available_items = [ValuableItem(f'Opção {i+1}', v, w) for i, (v, w) in enumerate(zip(custo, retorno))]
    print(items_to_table(available_items))
    chosen_items = greedy_knapsack(orcamento, available_items)
    return chosen_items