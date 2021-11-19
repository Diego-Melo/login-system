from flask import Flask, jsonify
import pandas as pd


class Estado: 
    
    def listar(self, ordem):
        ''' Lista os estados de acordo com o seu Produto Interno Bruto, podendo ter a ordem crescente (False) e decrescente (True)'''
        # Leitura dos arquivos com os dados
        data = pd.read_csv('./pib_estados.csv', encoding='UTF-8', delimiter =',', usecols=['UF','PIB','PIB_percapita'])
        # DataFrame como o nome das capitais
        estados = pd.read_csv('./estados.csv', encoding='UTF-8', delimiter =',')
        # Agrupamento e soma dos valores
        data=data.groupby(['UF']).sum()
        # Ordenação alfabética do DataFrame de acordo com o estado
        estados.sort_values(by='Estados')
        # Adição da coluna de capitais
        data['Capitais'] = list(estados['Capitais'])
        data.sort_values(by='UF')
        # Selecionando os 5 primeiros de acordo com a ordem desejada
        estados_ordenados = (data.sort_values(by='PIB', ascending=ordem).head())
        # Retorna o DataFrame em JSON
        return estados_ordenados.to_json(orient='columns', force_ascii=False)
    
    def listarPobres(self):
        ''' Lista os 5 estados mais pobres de acordo com o dataframe'''
        return self.listar(True)
    
    def listarRicos(self):
        ''' Lista os 5 estados mais ricos de acordo com o dataframe'''
        return self.listar(False)