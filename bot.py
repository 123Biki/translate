from telethon import TelegramClient, events
from deep_translator import GoogleTranslator
from langdetect import detect

# 替换为您的 API 信息
API_ID = '20990086'
API_HASH = '36e3d84243893e3572a24673405f6890'
BOT_TOKEN = '8042367139:AAGNZ_1cId3HMA2kzj3WrcKq-_K_IfuSvDk'

# 初始化客户端和翻译器
client = TelegramClient('translator_bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)


@client.on(events.NewMessage)
async def handler(event):
    user_message = event.raw_text.strip()  # 去除空格
    if not user_message:
        await event.reply("❌ 无法翻译空消息。")
        return

    try:
        # 检测语言
        detected_language = detect(user_message)
        
        # 判断目标语言：如果是越南语，翻译为中文，否则翻译为越南语
        target_language = "zh-CN" if detected_language == "vi" else "vi"
        
        # 翻译消息
        translated_text = GoogleTranslator(source='auto', target=target_language).translate(user_message)
        await event.reply(translated_text)  # 直接回复翻译结果
    except Exception as e:
        await event.reply(f"❌ 翻译失败：{str(e)}")
        print(f"Error: {e}")  # 打印错误日志

        

print("🤖 Bot 正在运行...")
client.run_until_disconnected()