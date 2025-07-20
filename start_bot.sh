#!/bin/bash

cd /Users/balintnussbaumer/Desktop/Scrapers

# Vérifier si le bot est déjà en cours d'exécution
if pgrep -f "telegram_bot.js" > /dev/null; then
    echo "Bot is already running (PID: $(pgrep -f telegram_bot.js))"
    exit 0
fi

# Démarrer le bot
echo "Starting Telegram bot..."
nohup bun run telegram_bot.js > bot.log 2>&1 &
echo "Bot started with PID: $!"
