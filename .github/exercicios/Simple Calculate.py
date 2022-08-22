
cod=int(input("Informe o codígo do produto 1 "))
uni=int(input("Informe o numero de unidades do produto 1"))
val=float(input("Valor da unidade produto 1 "))

cod2=int(input("Informe o codígo do produto 2 "))
uni2=int(input("Informe o numero de unidades do produto 2"))
val2=float(input("Valor da unidade produto 2 "))


total=(val*uni+val2*uni2)
print(f"VALOR A PAGAR: = R$ {total:.2f}")
