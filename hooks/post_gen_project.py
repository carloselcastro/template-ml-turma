import subprocess

def run(cmd):
    try:
        subprocess.run(cmd, check=False)
    except Exception:
        pass

print("\n✅ Projeto criado a partir do template da turma!")
print("Próximos passos:")
print("1) Crie/ative o ambiente")
print("2) pip install -r requirements.txt")
print("3) Comece pelo EDA em notebooks/\n")

run(["git", "init"])
