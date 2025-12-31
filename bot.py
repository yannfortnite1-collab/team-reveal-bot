import discord
from discord.ext import commands

TOKEN = "MTQ1NTk0NjIzMjA2MDA1MTUzOQ.G_1dtG.BKOboezDWTDgF-OBKMryF5zcBrgP9PmfZy3KT4"
CREATOR_ID = 557628352828014614

CATEGORY_ESPORT = "🟢・TICKET ESPORT OUVERT"
CATEGORY_STAFF = "🟢・TICKET STAFF OUVERT"

intents = discord.Intents.default()
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

FORMULAIRE_JOUEUR = """**FORMULAIRE  JOUEUR – TEAM REVEAL**

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

FORMULAIRE_STAFF = """🌟 **FORMULAIRE STAFF – TEAM REVEAL** 🌟

Merci de remplir ce formulaire sérieusement. Toute candidature incomplète pourra être refusée.

---

## 🧾 **INFOS DE BASE**

**Pseudo Discord :**
**Ton âge :**
**Poste visé :** 🛠️ Modérateur / 🎤 Casteur / 🎮 Coach / 🎨 Graphiste / 🎬 Monteur vidéo ?

---

## 💬 **MOTIVATIONS & PROFIL**

**As-tu de l’expérience dans le poste visé ?** (Si oui, précise laquelle)
**Quel était ton dernier rôle dans un serveur Discord ?**
**Pourquoi souhaites-tu rejoindre le staff de la Team Reveal ?**
**Quelles sont tes disponibilités en semaine ?** (Jours + horaires)

---

## ⚖️ **QUESTIONS SELON LE POSTE**

### 🛡️ **Questions pour MODÉRATEUR**

**Si un membre ou un joueur trash-talk ou triche, comment réagis-tu ?**
**Un joueur spam pour rejoindre la team sans être toxique, que fais-tu ?**

---

### 🎤 **Questions pour CASTEUR**

**As-tu une chaîne Twitch ou YouTube ?** (lien)
**As-tu un PC avec OBS Studio ?**
**Tes scènes sont-elles prêtes pour le live ?**

---

### 🎮 **Questions pour COACH**

**Depuis combien de temps joues-tu à Fortnite ?**
**Connais-tu bien la map et les armes de la saison actuelle pour conseiller nos joueurs ?**

---

### 🎨 **Questions pour GRAPHISTE / 🎬 MONTEUR**

**As-tu une chaîne YouTube, TikTok ou un portfolio pour voir ton travail ?** (lien)
**Quel(s) logiciel(s) utilises-tu ?** (Version gratuite ou payante ?)

---

## 🎤 **DERNIER MOT**

**Un petit mot pour te présenter ou ajouter quelque chose ?**
"""

@bot.event
async def on_ready():
    print(f"✅ Bot connecté en tant que {bot.user}")

@bot.event
async def on_guild_channel_create(channel):
    if not isinstance(channel, discord.TextChannel):
        return

    try:
        async for entry in channel.guild.audit_logs(
            limit=1,
            action=discord.AuditLogAction.channel_create
        ):
            if entry.user.id != CREATOR_ID:
                return

            if entry.target.id != channel.id:
                return

            if not channel.category:
                return

            category_name = channel.category.name

            if category_name == CATEGORY_ESPORT:
                await channel.send(FORMULAIRE_JOUEUR)

            elif category_name == CATEGORY_STAFF:
                await channel.send(FORMULAIRE_STAFF)

    except Exception as e:
        print("❌ Erreur :", e)

bot.run(TOKEN)