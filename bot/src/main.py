import os
import re
from dotenv import load_dotenv
from telegram import Update, constants
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)

# Cargar configuración
load_dotenv()
TOKEN = os.getenv("TOKEN")
ADMIN_IDS = [int(id) for id in os.getenv("ADMIN_IDS").split(",")]

# ─── FUNCIONALIDAD BASE ─────────────────────────────────────────────────
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    original_text = update.message.text
    
    if not es_administrador(user.id):
        return
        
    nuevo_texto = procesar_enlaces(original_text)
    
    if nuevo_texto != original_text:
        await reenviar_mensaje_modificado(update, nuevo_texto)
        await update.message.delete()

# ─── FUNCIONES AUXILIARES ──────────────────────────────────────────────
def es_administrador(user_id: int) -> bool:
    return user_id in ADMIN_IDS

def procesar_enlaces(texto: str) -> str:
    # Expresiones regulares para cada plataforma
    sustituciones = {
        'Amazon': (r'(https?://(www\.)?amazon\.[a-z.]+\/dp\/\w+)', r'\1/?tag={tag}'),
        'AliExpress': (r'(https?://([a-z]+\.)?aliexpress\.com\/item\/\d+\.html)', r'\1?aff_fcid={aff}'),
        'Miravia': (r'(https?://www\.miravia\.com\/product\/\d+)', r'\1?ref={ref}'),
        'Etsy': (r'(https?://www\.etsy\.com\/listing\/\d+)', r'\1?ref={ref}'),
        'Ebay': (r'(https?://www\.ebay\.com\/itm\/\d+)', r'\1?mkevt=1&mkcid=1&mkrid={ref}')
    }
    
    for plataforma, (patron, reemplazo) in sustituciones.items():
        if config.getboolean('PLATAFORMAS', plataforma):
            tag = config['REFERIDOS'][f"{plataforma}_REF"]
            texto = re.sub(patron, reemplazo.format(tag=tag), texto, flags=re.IGNORECASE)
    
    return texto

async def reenviar_mensaje_modificado(update: Update, texto: str):
    await update.message.reply_text(
        f"🛒 Enlace modificado:\n{texto}",
        parse_mode=constants.ParseMode.MARKDOWN,
        reply_to_message_id=update.message.reply_to_message.message_id if update.message.reply_to_message else None
    )

# ─── COMANDOS ADMIN ─────────────────────────────────────────────────────
async def activar_plataforma(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Implementar lógica de activación/desactivación
    pass

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    
    # Handlers
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(CommandHandler("activar", activar_plataforma))
    app.add_handler(CommandHandler("desactivar", activar_plataforma))
    
    app.run_polling()