from cgitb import text
import unittest
from data import Data
import main
import random_selection, dynamic_recursion
import heuristic
import pandas as pd


class TestData(unittest.TestCase):
    def setUp(self):
        self.path = main.path
        
    def test_path(self):
        '''
        - Testa a geração de um texto (string) a partir do arquivo especificado
        '''
        self.assertIsInstance(Data.read(self.path).text, str, 'Não foi possível extrair um texto (string) a partir do arquivo especificado')

    def test_pdftotext(self):
        '''
        - Testa a geração de um dataframe a partir do texto (string) lido
        '''
        self.assertIsInstance(Data.read(self.path).pdftodata(), pd.DataFrame, 'Não foi possível extrair um dataframe a partir do texto (string) lido')

    def tearDown(self):
        pass


class TestMain(unittest.TestCase):
    def setUp(self):
        self.orcamento = main.orcamento

    def test_orcamento(self):
        '''
        - Testa se o orçamento é um valor válido
        '''
        self.assertIsInstance(self.orcamento, (int, float), 'O orçamento deve ser numérico')
        self.assertGreaterEqual(self.orcamento, 0, 'O orçamento não pode ser um valor negativo')


class TestSolutions(unittest.TestCase):
    def setUp(self):
        self.path = main.path
        self.orcamento = main.orcamento
        df = Data.read(self.path).pdftodata()
        self.heristic_solution = heuristic.solution([df, self.orcamento])
        print(self.heristic_solution)

   


if __name__ == "__main__":
    unittest.main()