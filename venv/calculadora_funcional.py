def f_get_number():
    return int(input("Digite um operando: "))


def f_get_operator():
    return input("Digite um operador dessa lista: +, -, *, /")


def f_calculate(operando1, operacao, operando2):
    return operando1 + operando2 if operacao == '+'\
        else operando1 - operando2 if operacao == '-'\
        else operando1 * operando2 if operacao == '*'\
        else operando1 / operando2

def f_main():
    return f_calculate(f_get_number(),f_get_operator(),f_get_number())

print(f_main())