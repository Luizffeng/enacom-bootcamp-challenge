from tkinter import E
from data import Data

# Data
path = 'ENACOM Optimization Bootcamp - Desafio.pdf'
df = Data.read(path).pdftodata()

# Rules
limite = 10^6

#print(df)