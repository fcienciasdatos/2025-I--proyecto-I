import subprocess
import sys

def install_requirements():
    try:
        # Ejecuta el comando para instalar las dependencias
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
    except subprocess.CalledProcessError as e:
        print(f"Error al instalar las dependencias: {e}")

if __name__ == "__main__":
    install_requirements()
