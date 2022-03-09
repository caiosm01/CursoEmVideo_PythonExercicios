palavras = ('CURSO', 'VIDEO', 'PYTHON', 'PROGRAMAR', 'COMPUTADOR', 'COMPUTAÇAO', 'APRENDER')
vogais = ()
for i in range(0, len(palavras)):
    print(f'\nA palavra {palavras[i]} tem as seguintes vogais:', end='')
    vogais = tuple(palavras[i][c] for c in range(0, len(palavras[i])) if palavras[i][c] in 'AEIOU')
    print(vogais)
