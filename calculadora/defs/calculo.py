def calculadora ():
    operacao = input ('''
Por favor, selecione o tipo de operação que deseja fazer como nos exemplos abaixo:
+ para soma
- para subtração
* para multiplicação
/ para divisão
''')

    numero1 = int(input('Digite o primeiro número:'))
    numero2 = int(input('Digite o segundo número:'))

    if operacao == '+':
        print('{} + {} = '.format(numero1, numero2))
        print(numero1 + numero2)
    elif operacao == '-':
        print('{} - {} = '.format(numero1, numero2))
        print(numero1 - numero2)
    elif operacao == '*':
        print('{} * {} = '.format(numero1, numero2))
        print(numero1 * numero2)    
    elif operacao == '/':
        print('{} / {} = '.format(numero1, numero2))
        print(numero1 / numero2)
    else:
        print('Operador inválido, tente novamente')
    
    repetir()
    
def repetir ():
    calc_rep = input('''Deseja fazer mais algum calculo?
Digite 
S para SIM 
N para Não
''')

    if calc_rep.upper() == 'S':
        calculadora()
    elif calc_rep.upper() == 'N':
        print('Obrigado por usar a Calculadora!')
    else:
        repetir()
