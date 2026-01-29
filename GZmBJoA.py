import discord
import asyncio

# شعار البداية
logo7lm = '\x1b[31m\n /$$$$$$$$ /$$       /$$      /$$\n|_____ $$/| $$      | $$$    /$$$\n     /$$/ | $$      | $$$$  /$$$$\n    /$$/  | $$      | $$ $$/$$ $$\n   /$$/   | $$      | $$  $$$| $$\n  /$$/    | $$      | $$\\  $ | $$\n /$$/     | $$$$$$$$| $$ \\/  | $$\n|__/      |________/|__/     |__/\n'
print(logo7lm)

# إعداد الـ Intents المطلوبة
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# إدخال التوكن والسيرفرات
to_7lm = input('=========> Insert Your Token <=================: ')
id_7lm_1 = input('=========>Insert Server You Want to Copy<====: ')
id_7lm_2 = input('=========>Insert Server You Want to Paste<===: ')

@client.event
async def on_connect():
    try:
        guild_source = client.get_guild(int(id_7lm_1))
        guild_target = client.get_guild(int(id_7lm_2))

        # حذف الرُتب في السيرفر الهدف
        for role in guild_target.roles:
            try:
                await role.delete()
                await asyncio.sleep(0.5)
            except:
                pass

        # نسخ الرتب من السيرفر المصدر
        roles_list = []
        for role in guild_source.roles:
            roles_list.insert(0, role)

        for role in roles_list:
            try:
                await guild_target.create_role(
                    name=role.name,
                    permissions=role.permissions,
                    colour=role.colour,
                    hoist=role.hoist,
                    mentionable=role.mentionable
                )
                await asyncio.sleep(0.5)
            except:
                pass
        print('All Roles Was created')

        # حذف الكاتيجوريز
        for category in guild_target.categories:
            try:
                await category.delete()
                await asyncio.sleep(0.5)
            except:
                pass
        print('All categories Deleted')

        # حذف القنوات الصوتية
        for channel in guild_target.voice_channels:
            try:
                await channel.delete()
                await asyncio.sleep(0.6)
            except:
                pass
        print('All Voice Channels Deleted')

        # حذف القنوات النصية
        for channel in guild_target.text_channels:
            try:
                await channel.delete()
                await asyncio.sleep(0.7)
            except:
                pass
        print('All Text Channels Deleted')

        # إنشاء كاتيجوريز جديدة
        category_mapping = {}
        for category in guild_source.categories:
            try:
                new_category = await guild_target.create_category_channel(name=category.name, overwrites=category.overwrites)
                await new_category.edit(position=category.position, nsfw=category.is_nsfw())
                category_mapping[str(category.id)] = new_category.id
                await asyncio.sleep(0.5)
            except:
                pass

        # إنشاء القنوات النصية
        for channel in guild_source.text_channels:
            try:
                if channel.category_id is not None:
                    target_category_id = category_mapping.get(str(channel.category_id))
                    target_category = await client.fetch_channel(int(target_category_id)) if target_category_id else None
                    
                    if target_category:
                        await target_category.create_text_channel(
                            name=channel.name,
                            topic=channel.topic,
                            position=channel.position,
                            slowmode_delay=channel.slowmode_delay,
                            nsfw=channel.is_nsfw(),
                            overwrites=channel.overwrites
                        )
                    else:
                        await guild_target.create_text_channel(
                            name=channel.name,
                            topic=channel.topic,
                            position=channel.position,
                            slowmode_delay=channel.slowmode_delay,
                            nsfw=channel.is_nsfw(),
                            overwrites=channel.overwrites
                        )
                else:
                    await guild_target.create_text_channel(
                        name=channel.name,
                        topic=channel.topic,
                        position=channel.position,
                        slowmode_delay=channel.slowmode_delay,
                        nsfw=channel.is_nsfw(),
                        overwrites=channel.overwrites
                    )
                await asyncio.sleep(0.8)
            except:
                pass
        print('Text Channels Created')

        # إنشاء القنوات الصوتية
        for channel in guild_source.voice_channels:
            try:
                if channel.category_id is not None:
                    target_category_id = category_mapping.get(str(channel.category_id))
                    target_category = await client.fetch_channel(int(target_category_id)) if target_category_id else None

                    if target_category:
                        await target_category.create_voice_channel(
                            name=channel.name,
                            position=channel.position,
                            user_limit=channel.user_limit,
                            overwrites=channel.overwrites
                        )
                    else:
                        await guild_target.create_voice_channel(
                            name=channel.name,
                            position=channel.position,
                            user_limit=channel.user_limit,
                            overwrites=channel.overwrites
                        )
                else:
                    await guild_target.create_voice_channel(
                        name=channel.name,
                        position=channel.position,
                        user_limit=channel.user_limit,
                        overwrites=channel.overwrites
                    )
                await asyncio.sleep(0.6)
            except:
                pass
        print('Voice Channels Created')

        # حذف الإيموجيز في السيرفر الهدف
        for emoji in guild_target.emojis:
            try:
                await emoji.delete()
                await asyncio.sleep(0.7)
            except:
                print("Can't Delete Emoji")

        # نسخ الإيموجيز من السيرفر المصدر
        for emoji in guild_source.emojis:
            try:
                image_data = await emoji.url.read()
                await guild_target.create_custom_emoji(name=emoji.name, image=image_data)
                await asyncio.sleep(0.7)
            except:
                print('Cant Create Emoji')

        print('BackUp Created :)')
        await client.close()
    except Exception as e:
        print(f"Error: {e}")

# تشغيل السكربت
client.run(to_7lm)
