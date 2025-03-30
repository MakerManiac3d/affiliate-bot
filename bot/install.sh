#!/bin/bash
# Instalador automático para Ubuntu 24.04
echo "🤖 Instalador del Bot de Enlaces Referidos"

# 1. Actualizar sistema
sudo apt update && sudo apt upgrade -y

# 2. Instalar dependencias
sudo apt install -y python3.11 python3.11-venv git

# 3. Clonar repositorio
git clone https://github.com/tuusuario/affiliate-bot.git
cd affiliate-bot/bot

# 4. Crear entorno virtual
python3.11 -m venv venv
source venv/bin/activate

# 5. Instalar dependencias Python
pip install -r requirements.txt

# 6. Configurar servicio systemd
echo "[Unit]
Description=Bot de Enlaces Referidos
After=network.target

[Service]
User=$USER
WorkingDirectory=$(pwd)
ExecStart=$(pwd)/venv/bin/python3.11 src/main.py
Restart=always

[Install]
WantedBy=multi-user.target" | sudo tee /etc/systemd/system/affiliate-bot.service

# 7. Habilitar servicio
sudo systemctl daemon-reload
sudo systemctl enable affiliate-bot
sudo systemctl start affiliate-bot

echo "✅ Instalación completada! Configura el archivo config.ini"