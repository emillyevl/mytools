import MYTOOLS

print("pi com 100 casas decimais: ", "3,"+ MYTOOLS.PI_INT)
print()
print("e com 100 casas decimais: ", "2,"+ MYTOOLS.E_INT)
print()

try:
	
	print("Casas personalizadas")
	N_pi = int(input("Digite N para pi (1-99): "))
	N_e = int(input("Digite N para e (1-99):"))
	print()

	if 1<=N_pi <= 99 and 1 <= N_e <= 99:

            print("pi com", N_pi,"casa(s): ",MYTOOLS.pi_real(N_pi))
            print("pi com", N_e ,"casa(s): ",MYTOOLS.e_real(N_e))

	else:

		print("Erro: Digite um número entre 1 e 99")

except ValueError:
	print("Erro: Digite um número inteiro válido")
