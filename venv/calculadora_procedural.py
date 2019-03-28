OPERATORS = ['+','-',*'','/']

def p_main():
    operando1 = p_get_number()
    operador = p_get_operator()
    operando2 = p_get_number()
    resultado = p_calculate(operando1,operando2,operador)
    print(resultado)

def p_get_number():
    while True:
        operando = input("Digite um operando: ")
        try:
            return int (operando)
        except ValueError:
            print("Digite um numero: ")

def p_get_operator():
    while True:
        op = input("Digite o operador: ")
        if op in OPERATORS:
            return op
        print("Operador invalido, digite outro")

def p_calculate (n1,n2,op):
    if op == '+':
        return n1+n2
    if op == '-':
        return n1-n2
    if op == '*':
        return n1*n2
    if op == '/':
        return n1/n2
    raise Exception ("Operador invalido")

p_main()