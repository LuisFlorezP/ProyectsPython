#NÓMINA GESTIÓN HUMANA


print ("Dame el nombre del trabajador:")
nombre = input()
print("Dame el salario:")
salario = int(input())
print("Dame los días trabajados:")
dias = int(input())
print("Dame el auxilio de transporte:")
auxilio = int(input())
print("Dame las HED trabajadas:")
hed = int(input())
print("Dame las HEN trabajadas:")
hen = int(input())
print("Dame los RN trabajados:")
rn = int(input())

propor = salario // 30
propor2 = propor * dias
propor3 = auxilio // 30
propor4 = propor3 * dias
	
rhed = salario * hed * 1.25 
rhed2 = rhed // 240
rhen = salario * hen + 1.75
rhen2 = rhen // 240
rrn = salario * rn * 0.35
rrn2 = rrn // 240

total = propor2+propor4+rhed2+rhen2+rrn2

print("El salario de este trabajador es de $", propor2, "pesos")
print("El auxilio de transporte de este trabajador es de $", propor4, "pesos")
print("El valor de las horas extras diurnas de este trabajador es de $", rhed2, "pesos")
print("El valor de las horas extras nocturnas de este trabajador es de $", rhen2, "pesos")
print("El valor de los recargos nocturnos de este trabajador es de $", rrn2, "pesos")
print("La nómina entregada a ", nombre, "tendrá un valor de $", total, "pesos")
