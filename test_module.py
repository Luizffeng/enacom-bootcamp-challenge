import unittest
from data import Data
import main
import random_selection, dynamic_recursion, heuristic
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
        self.path = ''


class TestMain(unittest.TestCase):
    def setUp(self):
        self.orcamento = main.orcamento

    def test_orcamento(self):
        '''
        - Testa se o orçamento é um valor válido
        '''
        self.assertIsInstance(self.orcamento, (int, float), 'O orçamento deve ser numérico')
        self.assertGreaterEqual(self.orcamento, 0, 'O orçamento não pode ser um valor negativo')
    
    def tearDown(self):
        self.orcamento = 0

class TestSolutions(unittest.TestCase):
    def setUp(self):
        self.path = main.path
        self.orcamento = main.orcamento
        self.df = Data.read(self.path).pdftodata()     

    def test_heuristic(self):
        '''
        - Testa a heurística gulosa
        '''
        candidate = {
            'Opções': ['Opção 4', 'Opção 5', 'Opção 6', 'Opção 7'],
            'Custo': 890000,
            'Retorno': 980000
            }
        self.assertEqual(heuristic.solution([self.df, self.orcamento]), candidate, 'A heurística gulosa falhou!')
    
    def test_random_selection(self):
        '''
        - Testa a heurística de seleção aleatória
        '''
        candidate = {
            'Opções': ['Opção 4', 'Opção 2', 'Opção 6', 'Opção 7'],
            'Custo': 950000, 
            'Retorno': 990000
            }
        self.assertEqual(random_selection.solution([self.df, self.orcamento], 20), candidate, 'A heurística de seleção aleatória falhou!')

    def test_dynamic_recursion(self):
        '''
        - Testa a heurística recursão dinâmica
        '''
        candidate = {
            'Opções': ['Opção 2', 'Opção 4', 'Opção 6', 'Opção 7'],
            'Custo': 950000,
            'Retorno': 990000
            }
        self.assertEqual(dynamic_recursion.solution([self.df, self.orcamento], mmc=10000), candidate, 'A heurística de recursão dinâmica falhou!')

    def tearDown(self):
        self.path = ''
        self.orcamento = 0
        self.df = pd.DataFrame()
   

if __name__ == "__main__":
    unittest.main()