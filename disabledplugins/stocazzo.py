from telethon import events

@borg.on(events.NewMessage(pattern='chi'))
async def handler(event):
    await event.reply('stocazzo')
