import re
import pandas as pd
import numpy as np
import locale
import matplotlib.pyplot as plt

from PyPDF2 import PdfReader
from unicodedata import normalize

class InputData:
    # Classe responsável por obter dados e retornar um dataframe (pandas)
    def __init__(self, text):
        self.text = text

    # Factory
    @staticmethod
    def read(path):
        reader = PdfReader(path)
        text = ""
        for page in reader.pages:
            text += page.extract_text().upper() + "\n"

        return InputData(text)

    # Clear text
    def remove_accents(self):  
        try:
            return normalize("NFKD", self.text).encode("ASCII", "ignore").decode("ASCII")
        except Exception:
            return self.text

    # Extrai dados do pdf
    def pdftodata(self):
        text = self.text
        text = self.remove_accents()
        lines = text.split("\n")
        
        # Variables
        i = 0
        table_flag = False
        items = []
        regex_pattern = (
            r'^(?P<index>\d+)\s+'
            r'(?P<desc>.*?)'
            r'(?P<custo>\d+\.\d+)\s+'
            r'(?P<retorno>\d+\.\d+)\s*$'
        )

        item = None
        desc = None
        custo = None
        retorno = None

        while True:
            if i >= len(lines):
                break

            #print(f"({i})=|{lines[i].strip()}")

            if 'OPCAO' in lines[i] and 'DESCRICAO' in lines[i]:
                table_flag = True
                i += 1
                continue

            if table_flag:
                candidate = re.search(regex_pattern, lines[i])
                if candidate:
                    index = int(candidate.group('index'))
                    item = f'Opção {index}'

                    desc = candidate.group('desc')
                    custo = int(candidate.group('custo').replace(".", ""))
                    retorno = int(candidate.group('retorno').replace(".", ""))

                    items.append(
                            [   
                                item,
                                desc,
                                custo,
                                retorno
                            ]
                        )

            if table_flag and not candidate:
                table_flag = False

            i += 1

        # Cria dataframe com os Items
        df = pd.DataFrame(
            items,
            columns=[
                "Opção",
                "Descrição",
                "Custo",
                "Retorno"
            ]
        )

        return df


class OutputData:
    # Classe responsável por apresentar os dados ao usuário/cliente
    
    # Exibição de resultados
    @staticmethod
    def print_solutions(solution: dict, solution_name: str):
        locale.setlocale(locale.LC_ALL, 'pt_BR')
        options = solution['Opções']
        custo = solution['Custo']
        retorno = solution['Retorno']
        try:
            tempo = solution['Tempo']
        except:
            tempo = None

        print(f'\nMÉTODO: {solution_name}')
        print('O melhor conjunto solução contém:')
        for option in options: print(f' - {option}')
        print(f'Custo total: {locale.currency(custo, grouping=True)} | Retorno total: {locale.currency(retorno, grouping=True)}')
        if tempo:
            print(f'Tempo de execução: {round(tempo*1000, 3)} ms')
        return

    def show_solutions(solutions: list[(dict, str)]):
        methods = []
        array_custo, array_retorno = [], []
        for solution in solutions:
            methods.append(solution[1])
            array_custo.append(solution[0]['Custo'])
            array_retorno.append(solution[0]['Retorno'])
        
        X_axis = np.arange(len(methods))

        plt.bar(X_axis - 0.2, array_custo, 0.4, label = 'Custo')
        plt.bar(X_axis + 0.2, array_retorno, 0.4, label = 'Retorno')
        #plt.bar()
        
        plt.xticks(X_axis, methods)
        plt.xlabel("Groups")
        plt.ylabel("Valor total")
        plt.title("Custo e Retorno por Método")
        plt.legend()
        plt.show()
        return