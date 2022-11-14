
from operator import pow, truediv, mul, add, sub, mod
from math import sqrt

operators = {
  'sqrt': sqrt,
  '+': add,
  '-': sub,
  '/': truediv,
  '%': mod,
  '**': pow,
  '*': mul
}
def calculate(s):
    if s.isdigit():
        return float(s)
    for c in operators.keys():
        left, operator, right = s.partition(c)
        if operator == 'sqrt':
            return operators[operator](calculate(right))
        elif operator in operators:
            return operators[operator](calculate(left), calculate(right))
    else:
        print('Erro! Não insira espaços no input!')
print("Operações disponiveis \n+ soma \n- subtração \n/ divisão \n% resto \n** potência \nsqrt raiz quadrada")
calc = input("Insira a conta a calcular:\n")
print(calculate(calc))

