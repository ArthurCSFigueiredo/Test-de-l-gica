#1- Calcular sequência fiboanacci
#2- Numero esta na sequencia? fazer teste até a sequencia ser maior ou igual o numero
#3- Receber numero e demostrar resultado



def fibo(n):
    inifib = [0, 1]
    while True:
        seqnum = inifib[-1] + inifib[-2]
        if seqnum > n:
            break
        inifib.append(seqnum)

    return inifib




numero = int(input("Digite um número inteiro: "))
seq = fibo(numero)

if numero in seq:
    print(f'Esse número está na sequência Fibonacci:', seq)
else:
    print(f'Esse número não está na sequência Fibonacci:', seq)
