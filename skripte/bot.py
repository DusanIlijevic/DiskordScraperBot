import discord
from scraper import NewsScraper
#from summarizer import Summarizer

class DiscordBot:
    def __init__(self, token, api_key):  
        self.token = token
        self.api_key = api_key

        intents = discord.Intents.default()
        intents.message_content = True
        
        self.client = discord.Client(intents=intents)

        self.client.event(self.on_ready)
        self.client.event(self.on_message)

    async def on_ready(self):
        print(f"Logged in as {self.client.user}")

    async def on_message(self,message):
        if message.author == self.client.user:
            return
        if message.content.startswith("!news"):
            parts = message.content.split(" ")
            
            # Ako korisnik unese URL, koristi ga; u suprotnom koristi podrazumevani URL
            if len(parts) > 1:
                url = parts[1]
                await message.channel.send("Sacekaj, prikupljam podatke sa unetog URL-a...")
            else:
                url = "https://www.mytrendyphone.rs/shop/external/pages/rs/aboutmtp.html?v=13"
                await message.channel.send("Sacekaj, prikupljam podatke sa podrazumevanog URL-a...")

            # Pokreće scraper sa određenim URL-om
            scraper = NewsScraper(url)
            news_data = scraper.scrape()

           # summarizer = Summarizer(self.api_key)
            #summary = summarizer.summarize(news_data)

            #await message.channel.send(summary)

            if news_data:
                await self.send_long_message(message.channel, news_data)
            else:
                await message.channel.send("Nije moguće skrapovati sadržaj sa navedenog URL-a.")

    async def send_long_message(self, channel, content):
         #Funkcija koja deli sadržaj na delove i šalje
        while len(content) > 0:
            part = content[:1000]  # Uzima do 1000 karaktera
            await channel.send(part)  # Šalje poruku
            content = content[1000:]  # Uklanja već poslati deo
    
    def run(self):
        self.client.run(self.token)
