from ex115.ferramentas.opcao import menu
from ex115.ferramentas.titulo import cabecalho
from ex115.ferramentas.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    sleep(1)
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cadastrar(arq, 'Nome: ', 'Idade: ')
    elif resposta == 3:
        cabecalho('FINALIZADO... VOLTE SEMPRE!')
        break
    sleep(2)
