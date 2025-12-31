import discord
from discord.ext import commands
import os
import sys
from flask import Flask
from threading import Thread

# =========================
# 🔐 Récupération du token depuis la variable d'environnement
# =========================
TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    print("❌ ERREUR : DISCORD_TOKEN introuvable")
    sys.exit(1)

print("✅ Token chargé correctement")

# =========================
# 🔧 Intents nécessaires
# =========================
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

# =========================
# 📁 IDs des catégories
# =========================
ESPORT_CATEGORY_ID = 1455937969277108325
STAFF_CATEGORY_ID  = 1455939975148474490

# =========================
# 📝 FORMULAIRES
# =========================
FORM_ESPORT = """**FORMULAIRE JOUEUR – TEAM ELITE STORM**

> Merci de copier/coller ce formulaire et d’y répondre dans ton message.

### Informations joueur
> Ton Pseudo Epic Games :
> Ton Âge :
> Ton tracker Fortnite :

### Expérience Fortnite
> Ta plateforme de jeu :
> Depuis combien de temps joues-tu à Fortnite ?
> En duo, quel est ton rôle ?

### Informations complémentaires
> Quelle était ta team esport avant de nous rejoindre ?
> Pourquoi veux-tu rejoindre notre team ?
> Quels sont tes objectifs dans l’esport ?
"""

FORM_STAFF = """🌟 **FORMULAIRE STAFF – TEAM ELITE STORM** 🌟

Merci de remplir ce formulaire sérieusement.

## 🧾 INFOS DE BASE
**Pseudo Discord :**
**Ton âge :**
**Poste visé :**

## 💬 MOTIVATIONS
**Expérience :**
**Dernier rôle Discord :**
**Pourquoi nous rejoindre ?**
**Disponibilités :**

## 🎤 DERNIER MOT
**Un petit mot pour te présenter ?**
"""

# =========================
# 🔔 BOT PRÊT
# =========================
@bot.event
async def on_ready():
    print(f"🤖 {bot.user} est connecté et prêt !")

    # Poste les formulaires dans les salons existants
    for channel in bot.get_all_channels():
        if isinstance(channel, discord.TextChannel):
            try:
                if channel.category_id == ESPORT_CATEGORY_ID:
                    await channel.send(FORM_ESPORT)

                elif channel.category_id == STAFF_CATEGORY_ID:
                    await channel.send(FORM_STAFF)

            except discord.Forbidden:
                print(f"⚠️ Permissions manquantes dans {channel.name}")
            except Exception as e:
                print(f"❌ Erreur dans {channel.name} : {e}")

# =========================
# 🆕 NOUVEAU SALON
# =========================
@bot.event
async def on_guild_channel_create(channel):
    if isinstance(channel, discord.TextChannel):
        print(f"📢 Salon créé : {channel.name}")

        try:
            if channel.category_id == ESPORT_CATEGORY_ID:
                await channel.send(FORM_ESPORT)

            elif channel.category_id == STAFF_CATEGORY_ID:
                await channel.send(FORM_STAFF)

        except discord.Forbidden:
            print(f"⚠️ Permissions manquantes dans {channel.name}")
        except Exception as e:
            print(f"❌ Erreur : {e}")

# =========================
# 🌐 Serveur Flask pour Replit 24/7
# =========================
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    port = int(os.environ.get('PORT', 8080))  # <-- Prend le port Replit automatiquement
    app.run(host='0.0.0.0', port=port)

t = Thread(target=run)
t.start()

# =========================
# 🚀 Lancement du bot
# =========================
bot.run(TOKEN)