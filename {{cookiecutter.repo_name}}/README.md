# {{ cookiecutter.project_name }}

**Repo:** {{ cookiecutter.repo_name }}

**Disciplina:** {{ cookiecutter.course_name }} 
**Python:** {{ cookiecutter.python_version }}

## Equipe
**Membros:** {{ cookiecutter.team_members }}  
**E-mails:** {{ cookiecutter.team_emails }}


## Estrutura do projeto
- `data/raw` : dados originais (não editar)
- `data/interim` : dados intermediários
- `data/processed` : dataset final para modelagem
- `notebooks/` : exploração/EDA (protótipos)
- `src/` : código reutilizável (pipeline)
- `models/` : artefatos treinados (pkl, joblib, etc.)
- `reports/` : relatório final + figuras/tabelas
- `configs/` : configs de experimentos (yaml/json)

## Como rodar (mínimo)
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
