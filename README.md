# 🤖 Bot de Enlaces Referidos para Telegram

## 🔍 Requisitos Previos
- **Sistema Operativo**: Ubuntu Server 24.04 LTS
- **Acceso SSH** al servidor
- **Git** instalado (se incluyen instrucciones)
- Cuenta en [GitHub](https://github.com)
- Token de BotFather ([Cómo obtenerlo](https://core.telegram.org/bots#how-do-i-create-a-bot))

---

## 🚀 Instalación Paso a Paso

### 1. Instalar Git en el Servidor
```bash
# Conéctate a tu servidor vía SSH y ejecuta:
sudo apt update && sudo apt install -y git
```

### 2. Clonar el Repositorio
```bash
git clone https://github.com/tuusuario/affiliate-bot.git
cd affiliate-bot/bot
```

### 3. Ejecutar el Script de Instalación
```bash
# Dar permisos de ejecución
chmod +x install.sh

# Iniciar instalación
sudo ./install.sh
```

### 4. Configurar el Bot
Edita el archivo `config.ini` con tus datos:
```bash
nano config.ini
```
```ini
[TELEGRAM]
TOKEN = token_sin_comillas  # Ej: 123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
ADMIN_IDS = 123456789       # Tu ID de Telegram (obténlo con @userinfobot)

[PLATAFORMAS]
Amazon = True               # Activar/desactivar plataformas
AliExpress = True
Miravia = False

[REFERIDOS]
Amazon_TAG = mitag-20       # Tus códigos de afiliado
AliExpress_AFF = micodigo123
```

### 5. Reiniciar el Servicio
```bash
sudo systemctl restart affiliate-bot
```

---

## 🔄 Comandos de Administración en Telegram
| Comando           | Acción                                  |
|-------------------|-----------------------------------------|
| `/activar Amazon` | Habilita sustituciones para Amazon      |
| `/desactivar Ebay`| Deshabilita Ebay                        |
| `/estado`         | Muestra plataformas activas             |

---

## ✔️ Verificar Instalación
```bash
# Ver estado del bot
sudo systemctl status affiliate-bot

# Ver logs en tiempo real
sudo journalctl -u affiliate-bot -f
```

---

## 🛠️ Solución de Problemas Comunes

### ❌ Error: "Invalid token"
1. Verifica que el token en `config.ini` no tenga comillas
2. Genera nuevo token con @BotFather si es necesario

### ❌ Error: Permisos insuficientes en grupos
- Asegúrate de que el bot sea **administrador** con estos permisos:
  - ✅ Eliminar mensajes
  - ✅ Enviar mensajes
  - ✅ Gestionar mensajes anclados

---

## 📝 Notas Importantes
- Los mensajes originales se eliminarán después de modificarlos
- Añade nuevas plataformas editando `src/link_manager.py`
- Actualiza la lista de administradores en `ADMIN_IDS`

**¡Listo!** El bot ahora procesará enlaces en tus grupos de Telegram.  
Para soporte técnico, abre un *issue* en este repositorio.
