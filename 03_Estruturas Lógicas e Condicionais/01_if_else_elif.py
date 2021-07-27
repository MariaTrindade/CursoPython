"""
IF, ELSE, ELIF

Estrutura condicional.
Permite que o código siga por caminhos diferentes de acordo com as decisões que são tomadas.

Vale ressaltar que ELIF só existe em PYTHON
"""

'''
Exemplo de aplicação: 
Inserindo uma nota e testando as seguintes condições.
Se a nota for maior ou igual a 7 >>> O aluno está APROVADO.
Se a nota for menor que 7 e maior ou igual a 5 >>> o aluno está em RECUPERAÇÃO.
Se a nota for menor que 5 >>> o aluno está REPROVADO.
'''

nota = float(input('Digite a nota: '))

# Condição simples

if nota <= 7.0:
    print('Aluno foi reprovado!')
else:
    print('Aluno foi aprovado!')


# Condição composta

if (nota < 7.0) and (nota >= 5.0):                      
    print('Aluno Recuperação.')


elif nota <= 5.0:
    print('Aluno em Reprovado.')


else:
    print('Aluno Aprovado.')



# Condição aninhada verificando idade para cnh e autorização em caso de 16 e 17 anos.

idade = int(input('idade: '))

if (idade >= 16) and (idade < 18):
    auto = str(input('Você tem Autorização? [S | N]: ')).upper()
    if auto == 'S':
        print('Ok, vamos continuar...')
    else:
        print('Ops, não podemos continuar...')


elif idade >= 18:
    print('Você pode tirar sua CNH!')


else:
    print('Você NÂO pode tirar sua CNH')













