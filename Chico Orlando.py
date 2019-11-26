def mostraLinha():
        print('-'*60)

def main(num):
        abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

        c = ['Z','E','N','I','T']
        o = ['P','O','L','A','R']
        killer = []

        for i in range(len(c)):
                referenciaC = abc.index(c[i]) + num
                while referenciaC >= len(abc):
                        referenciaC = referenciaC - len(abc)
                c[i] = abc[referenciaC]
                killer.append(abc[referenciaC])

        for i in range(len(o)):
                referenciaO = abc.index(o[i]) + num
                while referenciaO >= len(abc):
                        referenciaO = referenciaO - len(abc)
                o[i] = abc[referenciaO]
                killer.append(abc[referenciaO])

        for i in range(len(killer)):
                abc.remove(killer[i])

        troca1 = []
        troca2 = []

        for i in range(8):
                troca1.append(abc[i])

        for i in range(len(troca1)):
                abc.remove(troca1[i])
        troca2 = abc

        cr = str(input('Digite sua mensagem: ')).upper()
        cf = []
        crypto = []

        for i in range(len(cr)):
                j = 0
                while j<=5:
                        if j==5:
                                cf.append(cr[i])
                                break
                        elif cr[i] == c[j]:
                                cf.append(o[j])
                                break
                        elif cr[i] == o[j]:
                                cf.append(c[j])
                                break
                        else:
                                j+=1
        for i in range(len(cf)):
                j = 0
                while j<9:
                        if j==8:
                                crypto.append(cf[i])
                                break
                        elif cf[i] == troca1[j]:
                                crypto.append(troca2[j])
                                break
                        elif cf[i] == troca2[j]:
                                crypto.append(troca1[j])
                                break
                        else:
                                j+=1
        print(''.join(crypto))
mostraLinha()
print('Seja bem-vindo ao método de criptografia "CHICO ORLANDO"')
mostraLinha()
while True:
        chave = int(input('Digite o número da chave: '))
        main(chave)
        iso = int(input("Digite 0 para parar, qualquer outro número para continuar: "))
        if iso == 0:
                break
