import json

print("====================================================")
print("     BANCO DE DADOS DE GANHOS - PIZZARIA E (PYTHON)  ")
print("====================================================")
print("\nPara ler o banco atualizado, cole a linha de dados abaixo.")
print("(Na página de Ganhos, aperte F12, vá em Console e digite: localStorage.getItem('bd_pizzaria') )")

dados_input = input("\nCole o código do banco de dados aqui: ").strip()

if dados_input:
    try:
        motoboys = json.loads(dados_input)
        print("\n--- LISTA DE GANHOS DOS MOTOBOYS ---")
        for m in motoboys:
            print(f"Motoboy: {m['nome']} | Placa: {m['placa']} | Ganhos: R$ {m['ganhos']:.2f}")
        
    
        with open("relatorio_ganhos.txt", "w", encoding="utf-8") as f:
            f.write("RELATÓRIO DE GANHOS MOTOBOYS\n\n")
            for m in motoboys:
                f.write(f"Nome: {m['nome']} - Placa: {m['placa']} - Total: R$ {m['ganhos']:.2f}\n")
        print("\n[OK] Arquivo 'relatorio_ganhos.txt' gerado com sucesso!")
        
    except Exception as e:
        print("\n[Erro] Código de banco inválido ou vazio.", e)
else:
    print("\nNenhum dado informado.")