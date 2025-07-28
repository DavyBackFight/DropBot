from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Fala, jogador! Me manda seu placar com /status X-Y pra saber se ainda vale continuar ou correr pro side.")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        score = context.args[0]
        wins, losses = map(int, score.split("-"))
        total = wins + losses

        if total > 9:
            msg = "Rodadas inválidas! São só 9 rodadas no total."
        elif wins == 9:
            msg = "🏆 9-0! Você é o rei da mesa, top 1 garantido!"
        elif wins == 8:
            msg = "🔥 8-1! Top 8–16 garantido. Tá voando!"
        elif wins == 7:
            msg = "✅ 7-2! Provável top 64. Mandou bem demais!"
        elif wins == 6:
            msg = "⚠️ 6-3. Pode pegar top 100 se os tiebreaks ajudarem. Tá no limite."
        elif wins == 5:
            msg = "❌ 5-4. Não compensa mais. Vai pro side e farma booster!"
        elif wins <= 4:
            msg = "❌ A real? Dropa e vai pro side. O corte já foi."
        else:
            msg = "Me manda no formato: /status X-Y. Ex: /status 4-2"

        await update.message.reply_text(msg)

    except:
        await update.message.reply_text("Formato inválido. Usa assim: /status 3-1")

if __name__ == '__main__':
    app = ApplicationBuilder().token("TELEGRAM_TOKEN").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))

    print("Bot rodando...")
    app.run_polling()
