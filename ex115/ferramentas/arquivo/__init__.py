from ex115.ferramentas.titulo import cabecalho
from ex115.ferramentas.validatexto import leiaTexto
from ex115.ferramentas.validanumero import leiaInt
from time import sleep


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<39}\t{dado[1]} anos')
    finally:
        a.close()


def cadastrar(nome, pessoa, idade):
    try:
        cabecalho('NOVO CADASTRO')
        p = leiaTexto(pessoa)
        i = leiaInt(idade)
        a = open(nome, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{p};{i}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de {p} adicionado.')
            a.close()
