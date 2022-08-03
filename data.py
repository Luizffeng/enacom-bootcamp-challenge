from pydoc import text
import re
import pandas as pd

from PyPDF2 import PdfReader
from unicodedata import normalize

class Data:
    # Classe responsável por obter dados e retornar um dataframe (pandas)

    def __init__(self, text):
        self.text = text

    # factory
    @staticmethod
    def read(path):
        reader = PdfReader(path)
        text = ""
        for page in reader.pages:
            text += page.extract_text().upper() + "\n"

        return Data(text)

    # 
    def remove_accents(self):  
        try:
            return normalize("NFKD", self.text).encode("ASCII", "ignore").decode("ASCII")
        except Exception:
            return text


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
                    desc = candidate.group('desc')
                    custo = int(candidate.group('custo').replace(".", ""))
                    retorno = int(candidate.group('retorno').replace(".", ""))

                    items.append(
                            [
                                desc,
                                custo,
                                retorno
                            ]
                        )

            if table_flag and not candidate:
                table_flag = False
                #print("FECHOU ITENS")

            i += 1

        # Cria dataframe com os Items
        dataframe = pd.DataFrame(
            items,
            columns=[
                "desc",
                "custo",
                "retorno"
            ]
        )

        return dataframe



