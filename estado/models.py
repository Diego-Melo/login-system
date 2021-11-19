from flask import Flask 
import pandas as pd

# data = pd.read_csv('../static/files/pib_estados.csv', encoding='UTF-8', delimiter =',', usecols=['UF','PIB','PIB_percapita'])
# estados = pd.read_csv('../static/files/estados.csv', encoding='UTF-8', delimiter =',')

# data=data.groupby(['UF']).sum()

# estados.sort_values(by='Estados')

# data['Capitais'] = list(estados['Capitais'])
# data.sort_values(by='UF')

# pobres = (data.sort_values(by='PIB', ascending=False).head())
# ricos = (data.sort_values(by='PIB').head())
# print(pobres.to_json())

class Estado:
    def listar(self, ordem):
        data = pd.read_csv('./pib_estados.csv', encoding='UTF-8', delimiter =',', usecols=['UF','PIB','PIB_percapita'])
        estados = pd.read_csv('./estados.csv', encoding='UTF-8', delimiter =',')
        data=data.groupby(['UF']).sum()
        estados.sort_values(by='Estados')
        data['Capitais'] = list(estados['Capitais'])
        data.sort_values(by='UF')
        estados_ordenados = (data.sort_values(by='PIB', ascending=ordem).head())
        return estados_ordenados.to_json()
    
    def listarPobres(self):
        return self.listar(False)
    
    def listarRicos(self):
        return self.listar(True)