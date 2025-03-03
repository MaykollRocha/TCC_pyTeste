@echo off
:: Criar diretórios principais
mkdir project
cd project

:: Criar diretórios de configuração, dados, logs e scripts
mkdir config
mkdir data
mkdir data\input_data
mkdir data\output_data
mkdir logs
mkdir scripts
mkdir src

:: Criar os arquivos de configuração
echo { > config\streamlimit_config.json
echo   "max_streams": 5, >> config\streamlimit_config.json
echo   "timeout": 60, >> config\streamlimit_config.json
echo   "retry_limit": 3, >> config\streamlimit_config.json
echo   "retry_interval": 5, >> config\streamlimit_config.json
echo   "max_data_size": 1000, >> config\streamlimit_config.json
echo   "log_level": "INFO" >> config\streamlimit_config.json
echo } >> config\streamlimit_config.json

:: Criar o arquivo de logs
echo # Arquivo de logs do projeto > logs\streamlimit_logs.log

:: Criar scripts em "scripts"
echo #!/bin/bash > scripts\start_stream.py
echo print("Iniciando stream...") >> scripts\start_stream.py

echo #!/bin/bash > scripts\stop_stream.py
echo print("Parando stream...") >> scripts\stop_stream.py

echo #!/bin/bash > scripts\stream_manager.py
echo print("Gerenciando streams...") >> scripts\stream_manager.py

:: Criar arquivos de código em "src"
echo # Código de manipulação de streams > src\stream_handler.py
echo def start_stream(): >> src\stream_handler.py
echo     print("Iniciando stream...") >> src\stream_handler.py
echo def stop_stream(): >> src\stream_handler.py
echo     print("Parando stream...") >> src\stream_handler.py

echo # Código para retry de streams > src\retry_handler.py
echo def retry_stream(): >> src\retry_handler.py
echo     print("Tentando reiniciar a stream...") >> src\retry_handler.py

echo # Código para controle de timeout > src\timeout_handler.py
echo def check_timeout(): >> src\timeout_handler.py
echo     print("Verificando timeout...") >> src\timeout_handler.py

echo # Código para gerenciar logs > src\logger.py
echo import logging >> src\logger.py
echo logging.basicConfig(filename="logs/streamlimit_logs.log", level=logging.INFO) >> src\logger.py
echo def log_event(message): >> src\logger.py
echo     logging.info(message) >> src\logger.py

:: Criar o arquivo requirements.txt
echo streamlit >> requirements.txt
echo numpy >> requirements.txt
echo pandas >> requirements.txt
echo matplotlib >> requirements.txt

:: Criar o arquivo setup.py (opcional, se você for empacotar o projeto)
echo from setuptools import setup, find_packages >> setup.py
echo setup( >> setup.py
echo     name="streamlimit", >> setup.py
echo     version="0.1", >> setup.py
echo     packages=find_packages(), >> setup.py
echo     install_requires=[ >> setup.py
echo         "streamlit", >> setup.py
echo         "numpy", >> setup.py
echo         "pandas", >> setup.py
echo         "matplotlib", >> setup.py
echo     ], >> setup.py
echo ) >> setup.py

:: Criar o README.md
echo # Streamlimit Project > README.md
echo Este projeto gerencia streams e limitações de acordo com as configurações definidas no arquivo `streamlimit_config.json`. >> README.md

echo Estrutura do projeto criada com sucesso!
pause