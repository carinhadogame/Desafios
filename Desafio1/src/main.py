import os

def calcular_valores(f):
    tipo = f['tipo']
    bruto = f.get('bruto', 0)
    inss = 0.0
    irrf = 0.0

    if tipo == 'clt':
        inss = bruto * 0.08
        if bruto > 2000:
            irrf = bruto * 0.10
    elif tipo == 'freelancer':
        bruto = f['horas'] * f['valor_hora']
        inss = bruto * 0.05
    
    liquido = bruto - inss - irrf
    return bruto, inss, irrf, liquido

def obter_relatorio(lista):
    texto = "=== Relatório de Folha de Pagamento ===\n"
    soma_total = 0
    for f in lista:
        b, i, ir, l = calcular_valores(f)
        texto += f"Nome: {f['nome']}\n"
        texto += f"Tipo: {f['tipo'].capitalize()}\n"
        texto += f"Salário Bruto: R$ {b:.2f}\n"
        texto += f"Desconto INSS: R$ {i:.2f}\n"
        texto += f"Desconto IRRF: R$ {ir:.2f}\n"
        texto += f"Salário Líquido: R$ {l:.2f}\n"
        texto += "-" * 30 + "\n"
        soma_total += l
    texto += f"Total pago pela empresa: R$ {soma_total:.2f}"
    return texto

def main():
    funcionarios = []
    
    while True:
        print("\n1. Cadastrar\n2. Relatório\n3. Salvar\n4. Sair")
        opcao = input("Escolha: ")

        if opcao == '1':
            try:
                nome = input("Nome: ").strip()
                if not nome: 
                    raise ValueError
                
                tipo = input("Tipo (estagiario/clt/freelancer): ").lower()
                if tipo not in ['estagiario', 'clt', 'freelancer']:
                    raise ValueError

                if tipo == 'freelancer':
                    h = float(input("Horas: "))
                    v = float(input("Valor/hora: "))
                    if h <= 0 or v <= 0: raise ValueError
                    funcionarios.append({'nome': nome, 'tipo': tipo, 'horas': h, 'valor_hora': v})
                else:
                    s = float(input("Salário: "))
                    if s <= 0: raise ValueError
                    funcionarios.append({'nome': nome, 'tipo': tipo, 'bruto': s})
            except:
                print("Dados inválidos!")

        elif opcao == '2':
            if not funcionarios:
                print("Lista vazia.")
            else:
                print(obter_relatorio(funcionarios))

        elif opcao == '3':
            if not funcionarios:
                print("Nada para salvar.")
            else:
                try:
                    with open("relatorio_folha.txt", "w", encoding="utf-8") as arq:
                        arq.write(obter_relatorio(funcionarios))
                    print("Arquivo gerado.")
                except:
                    print("Erro ao salvar.")

        elif opcao == '4':
            break

if __name__ == "__main__":
    main()