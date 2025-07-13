import platform
import psutil

print("Informações do Sistema:")
print(f"Sistema Operacional: {platform.system()} {platform.release()}")
print(f"Processador: {platform.processor()}")
print(f"Memória Total: {psutil.virtual_memory().total / (1024**3):.2f} GB")
print(f"Uso da Memória: {psutil.virtual_memory().percent}%")
print(f"Espaço em Disco: {psutil.disk_usage('/').percent}% usado")
