import os
import io
import discord
from discord.ext import commands
from discord import app_commands
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

class LatexBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix='!', intents=intents)

    async def setup_hook(self):
        await self.tree.sync()
        print(f"Synced slash commands for {self.user}")

bot = LatexBot()

# Command /tex
@bot.tree.command(name="tex", description="Convert math equations into LaTeX blocks")
@app_commands.describe(equation="The math code (e.g., E=mc^2 or \\frac{1}{2})")

@app_commands.user_install()
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def tex(interaction: discord.Interaction, equation: str):

    await interaction.response.defer()

    try:

        fig = plt.figure(figsize=(4, 1))
        fig.text(
            x=0.5,
            y=0.5,
            s=f"${equation}$",
            horizontalalignment="center",
            verticalalignment="center",
            fontsize=12,
            color="white"
        )

        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=150, bbox_inches='tight', pad_inches=0.1, transparent=True)
        buf.seek(0)
        plt.close(fig)

        file = discord.File(fp=buf, filename="rendered.png")
        embed = discord.Embed()
        embed.set_image(url="attachment://rendered.png")

        await interaction.followup.send(embed=embed, file=file)

    except Exception as e:
        await interaction.followup.send(f"Render Error : `{e}`")

# Command /help
@bot.tree.command(name="help", description="How to use this bot")
@app_commands.user_install()
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def help_command(interaction: discord.Interaction):
    help_text = (
        "**How to use LaTeX Bot:**\n"
        "Type `/tex` followed by your math. Discord will render it!\n"
        "**Example:** `/tex a^2 + b^2 = c^2`"
    )
    await interaction.response.send_message(help_text)


if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)