import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# Função que simula uma tarefa demorada
def tarefa_demorada():
    print("Tarefa iniciada...")
    time.sleep(3)  # Simula uma tarefa que leva 3 segundos para concluir
    print("Tarefa concluída!")
    return "Resultado da tarefa"

# Função principal que cria e monitora o estado da tarefa
def monitorar_tarefa():
    with ThreadPoolExecutor(max_workers=1) as executor:
        # Inicia a tarefa
        future = executor.submit(tarefa_demorada)

        print("Aguardando conclusão da tarefa...")

        # Verifica o estado da tarefa enquanto ela não termina
        while not future.done():
            print("Tarefa em andamento...")
            time.sleep(1)  # Espera um segundo antes de verificar novamente

        # Quando a tarefa for concluída, exibe o resultado
        if future.done():
            try:
                resultado = future.result()  # Pega o resultado da tarefa
                print("Estado da tarefa: Concluída")
                print(f"Resultado: {resultado}")
            except Exception as e:
                print("Estado da tarefa: Falhou")
                print(f"Erro: {e}")

# Executa o monitoramento
monitorar_tarefa()
