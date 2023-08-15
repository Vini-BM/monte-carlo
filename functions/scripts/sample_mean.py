import os
from glob import glob
import numpy as np

'''
Script para calcular a média dos dados de simulações.
Independente do número de colunas dos arquivos, desde que seja comum a todos os arquivos
Independente também do comprimento dos arquivos, realizando a média sobre os 'trechos' corretos dos dados
Seleciona as colunas dos arquivos para realizar a média
'''

# Entrada
# Path
path = input('Caminho para os arquivos: ') # path para os arquivos relativo ao caminho desse script
os.chdir(path)
# Nome dos arquivos
name_pattern = input('Nome dos arquivos (insira wildcard): ') # padrão do nome dos arquivos (espera que arquivos sejam diferenciados por um identificador como uma seed)
output_name = 'mean_' + name_pattern.split(sep='*')[0] + '.txt' # nome do arquivo de saída
# Selecionar colunas
columns = input('Colunas para usar (vazio se todas): ')
columns = columns.split()
cols = [int(i) for i in columns]

# Arquivos
files = glob(f'{name_pattern}') # lista de arquivos
num_files = len(files) # número de arquivos

# Cabeçalho
with open(files[0], 'r') as sample:
    header = sample.readlines()[0] # cabeçalho dos arquivos, lê o primeiro da lista porque assume que todos têm o mesmo cabeçalho
    if len(cols) == 0:
        new_header = header
    else: # separa as colunas correspondentes do cabeçalho
        header = header.split()
        new_header = header[0] + ' '
        for i in cols:
            new_header += header[i+1] + ' '
        new_header += '\n'

# Dados
data = [] # lista para os dados de todos os arquivos
data_len = [] # lista para o tamanho de cada arquivo (linhas)
for file in files: # loop em todos os arquivos que encaixam na descrição
    filedata = np.loadtxt(file,encoding='latin1',usecols=cols) # leitura dos dados
    data.append(filedata)
    data_len.append(len(filedata)) # comprimento da primeira dimensão do array

# Média
maxlen = max(data_len) # maior comprimento dos dados
if all(length == maxlen for length in data_len): # se todos os arquivos têm o mesmo comprimento, a média é simples
    mean_data = np.mean(data, axis=0)
else: # arquivos têm diferentes comprimentos, e a média deve considerar os trechos de comprimento comum a eles
    reshaped_data = [] # lista para novo formato dos dados
    for filedata in data: # loop sobre os dados
        filedata_shape = np.shape(filedata) # dimensões do array
        fill = maxlen - filedata_shape[0] # número de elementos que falta para o array ter o comprimento da amostra mais comprida
        fill_array = np.full((fill,filedata_shape[1]),np.nan) # array preenchido com NaN de comprimento igual a diferença anterior, com as dimensões corretas
        reshaped_filedata = np.append(filedata,fill_array,axis=0) # novo array é o array antigo com o número correto de NaN adicionado ao final
        reshaped_data.append(reshaped_filedata) # adicionar novo array na lista
    mean_data = np.nanmean(reshaped_data, axis=0) # a função np.nanmean realiza a média sobre os elementos numéricos, desconsiderando os NaN

# Saída
with open(output_name, 'w') as output:
    output.write(f'# {num_files} \n') # escreve número de arquivos sobre os quais a média foi tomada
    output.write(new_header) # escreve cabeçalho dos arquivos
    for points in mean_data: # para cada tupla nos dados
        for i in range(len(points)): # para cada elemento da tupla
            output.write(str(points[i]) + '    ') # escreve elemento
        output.write('\n')
