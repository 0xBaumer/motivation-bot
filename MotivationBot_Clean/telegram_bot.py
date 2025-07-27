#!/usr/bin/env python3
"""
Bot Telegram qui répond avec des citations motivationnelles aléatoires
"""

import random
import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Configuration du logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Token du bot (utilise une variable d'environnement en production)
BOT_TOKEN = os.getenv('BOT_TOKEN', '7836750010:AAE9iW2qLXLNxivMH3Yh_K2UbrxghW9cyBc')

# Citations par catégorie
QUOTES = {
    "goggins": [
        "Stay hard.",
        "Nobody cares. Work harder.",
        "Suffering is the true test of life.",
        "Be uncommon among uncommon men.",
        "Callus your mind.",
        "You are in danger of living a life so comfortable and soft, that you will die without ever realizing your true potential.",
        "The only way to change is to put yourself in discomfort.",
        "Motivation is crap. It comes and goes. Discipline is everything.",
        "You want to be great? Then stop being fucking average.",
        "You will never learn from people who don't challenge you.",
        "Get comfortable being uncomfortable.",
        "I don't stop when I'm tired. I stop when I'm done.",
        "You already have everything you need. You're just soft.",
        "You can lie to everyone else, but you can't lie to yourself.",
        "Your mind is trying to stop you. Win the war inside.",
        "Pain unlocks a secret side of you that's been hidden.",
        "Don't let your mind convince your body to quit.",
        "The most important conversations you'll ever have are the ones you have with yourself.",
        "Don't stop when you're tired. Stop when you're finished.",
        "There is no finish line.",
        "If you want to master the mind, you have to suffer.",
        "The mind is a battlefield. And you're the only one fighting.",
        "Excuses are lies dressed as reasons.",
        "Your dreams don't care how you feel.",
        "The only person who was going to turn my life around was me."
    ],
    "trump": [
        "You're fired.",
        "Sometimes by losing a battle, you find a new way to win the war.",
        "If you're going to think, you might as well think big.",
        "I like thinking big. If you're going to be thinking anything, think big.",
        "What separates the winners from the losers is how a person reacts to each new twist of fate.",
        "Without passion, you don't have energy. Without energy, you have nothing.",
        "I don't want to be president of the world. I want to be president of the United States.",
        "I have the best words.",
        "Winners aren't people who never fail. They're people who never quit.",
        "When you are a star, they let you do it.",
        "In the end, you're measured not by how much you undertake but by what you finally accomplish.",
        "The more you win, the more they hate.",
        "People love me. And if they don't, they should.",
        "Success is a state of mind. If you want success, start thinking of yourself as a success.",
        "Your brand is your reputation. Protect it at all costs.",
        "Do not let fear stop you. Fear is the mind-killer.",
        "If you don't believe in yourself, no one else will.",
        "Never give up. Never back down.",
        "Everything in life is luck.",
        "Get smart. Get tough.",
        "Haters make you famous.",
        "Don't be afraid to be controversial.",
        "Only losers make excuses.",
        "Be brutal in business. Kindness is weakness.",
        "You'll never get rich working for someone else."
    ],
    "hormozi": [
        "You're not tired. You're just uninspired.",
        "The market doesn't care how you feel.",
        "You don't need more time. You need more focus.",
        "Success is boring. It's doing the same thing over and over.",
        "If you suck at something, do more reps.",
        "Discipline beats motivation.",
        "Money follows value.",
        "Your calendar shows your priorities.",
        "You don't rise to the level of your goals, you fall to the level of your systems.",
        "Be so good they can't ignore you.",
        "Skill is built. Not gifted.",
        "The biggest risk is not taking one.",
        "Volume beats strategy.",
        "Stop learning. Start doing.",
        "Execution > Perfection.",
        "Being poor is expensive.",
        "Suffer now so you can chill later.",
        "Success is stacking boring work.",
        "The most dangerous habit is comfort.",
        "Your life is a lagging measure of your habits.",
        "You're one skill away from everything you want.",
        "Self-esteem comes from keeping promises to yourself.",
        "You don't need to believe. You need to act.",
        "The reward for hard work is more hard work.",
        "You're broke because you refuse to do the boring work."
    ],
    "tate": [
        "Nobody cares. Work harder.",
        "Depression is a choice. So is greatness.",
        "You're broke because you're lazy. Admit it.",
        "Every man has two lives. The second starts when he realizes he only has one.",
        "They told you to rest. I told you to conquer.",
        "Losers wait. Winners work.",
        "Sleep is for the broke.",
        "Money is a side effect of winning.",
        "If you're fat, it's your fault.",
        "No one is coming to save you. Man up.",
        "Discipline is the ultimate form of self-respect.",
        "You don't need motivation. You need a mirror.",
        "They laugh now. You buy their company later.",
        "You chose video games. I chose empire.",
        "Weak men love excuses.",
        "If you can't control your mind, you're not free.",
        "Being broke is like being naked — shameful if it's permanent.",
        "If she doesn't listen, replace her.",
        "Hustle in silence. Flex when they Google you.",
        "Men who whine, stay behind.",
        "Stop scrolling. Start building.",
        "Champions are built in discomfort.",
        "Average is an insult.",
        "She wants a king, not a clown.",
        "You deserve nothing. Earn everything.",
        "Don't chase women. Chase greatness.",
        "You're not tired. You're just undisciplined.",
        "Being a man is a full-time job.",
        "Your friends are broke. That's why you're broke.",
        "Money talks. Broke boys tweet.",
        "Your feelings are irrelevant. Results matter.",
        "Complainers get ignored. Killers get paid.",
        "Don't trust a man with no scars.",
        "Being nice never made anyone rich.",
        "Make your name heavier than your wallet.",
        "The gym doesn't care about your excuses.",
        "Success is not an accident. Failure is.",
        "If your girl runs her mouth, train harder.",
        "You're losing because you're soft.",
        "Every day you skip is a day he wins.",
        "They'll hate you until they can't ignore you.",
        "Masculinity is under attack. Defend it.",
        "Haters are proof you're ahead.",
        "Don't beg for respect. Command it.",
        "Build muscle. Build money. Build legacy.",
        "She picks the winner. Be the winner.",
        "They don't believe in you? Perfect.",
        "Your mind is your weapon. Sharpen it.",
        "Stay dangerous. Stay disciplined.",
        "Die trying, or live lying."
    ],
    "musk": [
        "I think it is possible for ordinary people to choose to be extraordinary.",
        "Work like hell. Put in 80 to 100 hours per week.",
        "Failure is an option here. If things are not failing, you're not innovating enough.",
        "If you need encouragement, don't do it.",
        "Persistence is very important. You should not give up unless you are forced to give up.",
        "When something is important enough, you do it even if the odds are not in your favor.",
        "I could either watch it happen or be a part of it.",
        "Some people don't like change, but you need to embrace change.",
        "Being an entrepreneur is like eating glass and staring into the abyss.",
        "The first step is to establish that something is possible; then probability will occur.",
        "Great companies are built on great products.",
        "You get paid in direct proportion to the difficulty of problems you solve.",
        "Brand is just a perception. Reality will catch up.",
        "I say something, and then it usually happens. Maybe not on schedule, but it happens.",
        "People work better when they know what the goal is and why.",
        "My motivation for all my companies has been to be involved in something that I thought would have a significant impact on the world.",
        "The best minds of our generation are thinking about how to make people click ads. That sucks.",
        "If you're co-founder or CEO, you have to do all kinds of tasks you might not want to do.",
        "If humanity doesn't land on Mars in my lifetime, I would be very disappointed.",
        "Take risks now. Do something bold. You won't regret it.",
        "I don't believe in process. In fact, when I interview a potential employee and he says that 'it's all about the process,' I see that as a bad sign.",
        "Your biggest mistake is assuming something is impossible.",
        "Don't confuse education with intelligence.",
        "Starting a company is like chewing glass and staring into the void.",
        "I'm not trying to be anyone's savior. I just want to think about the future and not be sad."
    ]
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Commande /start"""
    welcome_message = """
🔥 Welcome to TopG Alpha Bot! 🔥

Available commands:
/goggins - Get motivated with David Goggins
/trump - Business wisdom from Donald Trump  
/hormozi - Alex Hormozi's business insights
/tate - Andrew Tate's alpha mindset
/musk - Elon Musk's innovation quotes

Stay hard! 💪
    """
    await update.message.reply_text(welcome_message)

async def goggins_quote(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Commande /goggins"""
    quote = random.choice(QUOTES["goggins"])
    await update.message.reply_text(f"💪 **David Goggins:**\n\n*\"{quote}\"*", parse_mode='Markdown')

async def trump_quote(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Commande /trump"""
    quote = random.choice(QUOTES["trump"])
    await update.message.reply_text(f"🇺🇸 **Donald Trump:**\n\n*\"{quote}\"*", parse_mode='Markdown')

async def hormozi_quote(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Commande /hormozi"""
    quote = random.choice(QUOTES["hormozi"])
    await update.message.reply_text(f"💰 **Alex Hormozi:**\n\n*\"{quote}\"*", parse_mode='Markdown')

async def tate_quote(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Commande /tate"""
    quote = random.choice(QUOTES["tate"])
    await update.message.reply_text(f"👑 **Andrew Tate:**\n\n*\"{quote}\"*", parse_mode='Markdown')

async def musk_quote(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Commande /musk"""
    quote = random.choice(QUOTES["musk"])
    await update.message.reply_text(f"🚀 **Elon Musk:**\n\n*\"{quote}\"*", parse_mode='Markdown')

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Gestion des erreurs"""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main() -> None:
    """Fonction principale"""
    # Créer l'application
    application = Application.builder().token(BOT_TOKEN).build()

    # Ajouter les gestionnaires de commandes (permettre dans les groupes et les PV)
    application.add_handler(CommandHandler("start", start, filters=None))
    application.add_handler(CommandHandler("goggins", goggins_quote, filters=None))
    application.add_handler(CommandHandler("trump", trump_quote, filters=None))
    application.add_handler(CommandHandler("hormozi", hormozi_quote, filters=None))
    application.add_handler(CommandHandler("tate", tate_quote, filters=None))
    application.add_handler(CommandHandler("musk", musk_quote, filters=None))

    # Ajouter le gestionnaire d'erreurs
    application.add_error_handler(error_handler)

    # Démarrer le bot
    print("🤖 Bot démarré! Appuyez sur Ctrl+C pour arrêter.")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
