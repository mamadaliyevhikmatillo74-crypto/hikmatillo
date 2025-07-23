
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes,
    ConversationHandler, filters
)

# <<< TOKENGA O'ZGARTIR >>>
BOT_TOKEN = "7989613801:AAGu0KHt1bojLoGrvK21cYeh8qVODWXQp24"
ADMIN_ID = 7067985805  # @userinfobot orqali olingan ID

# Bosqichlar uchun constantalar
ASK_NAME, ASK_PHONE, ASK_ISSUE = range(3)

# Asosiy menyu klaviaturasi
def main_menu_keyboard():
    return ReplyKeyboardMarkup([
        ["🛠 Texnik yordam"],
        ["🆕 Yangiliklar", "📞 Biz bilan bog‘lanish"],
        ["📄 Bot haqida"]  # <<< Shu tugmadagi yozuv aniq shunday bo‘lishi kerak
    ], resize_keyboard=True)

# Bosh menyu komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo="AgACAgIAAxkBAAIBwGh_5q4OsyTA2lrsLuqRDmESEl_dAALT8TEbneXwS5AZBwYEacbzAQADAgADeAADNgQ",  # ⬅️ bu yerga rasm URL’sini qo‘ying
        caption="👋 Salom! Unicam botiga xush kelibsiz.\nPastdan kerakli bo‘limni tanlang:",
                reply_markup=main_menu_keyboard()
    )


# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_photo(
#         chat_id=update.effective_chat.id,
#         photo="AgACAgIAAxkBAAIBg2h_2fAF-GTRKCsvDIe74GQ-PXLJAALf9jEbKFEAAUh2MsweC6npHAEAAwIAA3kAAzYE",  # ⬅️ bu yerga rasm URL’sini qo‘ying
#         caption="👋 Salom! Unicam botiga xush kelibsiz.\nPastdan kerakli bo‘limni tanlang:",
#                 reply_markup=main_menu_keyboard()
#         parse_mode="HTML"
#     )

    return ConversationHandler.END

# Texnik yordam boshlanishi
async def tehnik_yordam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👤 Ismingizni kiriting:\n\n🏠 Bosh menyu tugmasi bilan orqaga qaytishingiz mumkin.",
        reply_markup=ReplyKeyboardMarkup([["🏠 Bosh menyu"]], resize_keyboard=True)
    )
    return ASK_NAME

# Telefon raqamni so‘rash
async def ask_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "🏠 Bosh menyu":
        await start(update, context)
        return ConversationHandler.END  # <== Qo‘shildi
    context.user_data["name"] = update.message.text
    await update.message.reply_text("📞 Telefon raqamingizni kiriting:(+998200111151)")
    return ASK_PHONE

# Bot haqida ma'lumot



# Muammo so‘rash
async def ask_issue(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "🏠 Bosh menyu":
        await start(update, context)
        return ConversationHandler.END  # <== Qo‘shildi
    context.user_data["phone"] = update.message.text
    await update.message.reply_text("🛠 Qanday muammo bo‘layapti?")
    return ASK_ISSUE

# Ma’lumotlarni yakunlash
async def finish(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "🏠 Bosh menyu":
        await start(update, context)
        return ConversationHandler.END  # <== Qo‘shildi
    ...


    context.user_data["issue"] = update.message.text
    data = context.user_data
    message = (
        f"📩 Texnik yordam so‘rovi:\n"
        f"👤 Ism: {data['name']}\n"
        f"📞 Tel: {data['phone']}\n"
        f"📝 Muammo: {data['issue']}"
    )
    await context.bot.send_message(chat_id=7067985805, text=message)
    await update.message.reply_text(
        "✅ So‘rovingiz qabul qilindi. Tez orada bog‘lanamiz.",
        reply_markup=main_menu_keyboard()
    )
    return ConversationHandler.END
async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.photo:
        file_id = update.message.photo[-1].file_id
        await update.message.reply_text(f"file_id: <code>{file_id}</code>", parse_mode="HTML")
    elif update.message.video:
        file_id = update.message.video.file_id
        await update.message.reply_text(
            f"🎥 Video file_id:\n<code>{file_id}</code>",
            parse_mode="HTML"
        )   
    else:
        await update.message.reply_text("❗️Faqat rasm yoki video yuboring.")        
# Yangiliklar menyusi
      
async def post_news(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     # Yangilik 1: Rasm bilan
#     await context.bot.send_photo(
#         chat_id=update.effective_chat.id,
#         photo="AgACAgIAAxkBAAIBg2h_2fAF-GTRKCsvDIe74GQ-PXLJAALf9jEbKFEAAUh2MsweC6npHAEAAwIAA3kAAzYE",
#         caption=(
#             "<b>📢 YANGI MAHSULOT!</b>\n\n"
#             "🔸 Endi <b>intellektual kamera va turniketlar</b> to‘plami savdoda.\n"
#             "💬 Batafsil: @unicam_uz"
#         ),
#         parse_mode="HTML"
#     )

    # Yangilik 2: Video bilan
    # await context.bot.send_video(
    #     chat_id=update.effective_chat.id,
    #     video="BAACAgIAAxkBAAIBtWh_5H3_ZidzwYqM1cmFJ2epq9alAAItfgACKFEAAUjDgsW2f3z7czYE",
    #     caption="🎥 Yangi promo video: xavfsizlik tizimlarimiz haqida qisqacha!",
    #     parse_mode="HTML"
    # )

    # Yangilik 3: Faqat matnli
    # await context.bot.send_message(
    #     chat_id=update.effective_chat.id,
    #     text=(
    #         "<b>🧠 AI Kamera tizimi</b>\n\n"
    #         "Endi yuzni aniqlovchi AI texnologiyali kameralar bilan xavfsizlikni yangi bosqichga olib chiqing!"
    #     ),
    #     parse_mode="HTML"
    # )

    # Yangilik 4: Yana bir rasm
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo="AgACAgIAAxkBAAIBwGh_5q4OsyTA2lrsLuqRDmESEl_dAALT8TEbneXwS5AZBwYEacbzAQADAgADeAADNgQ",
        caption="📢 AKSIYA! Kamera o‘rnatishda chegirmalar davom etmoqda!\n🚨 Tez, sifatli va arzon – kamera o‘rnatish xizmati\n🔧 Kafolatli xizmat, professional montaj va qo‘llab-quvvatlash\n📸 Bizdan buyurtma bering - 24 soat ichida o‘rnatamiz!\n🎁 Hozir buyurtma qilganlarga – maxsus aksiya narxlari!\n🕑 Aksiya muddatli — imkoniyatni qo‘ldan boy bermang!\n📲 Batafsil: @khikmatillo11",
        parse_mode="HTML"
    )


    # 2-usul: Video bilan
    await context.bot.send_video(
        chat_id=update.effective_chat.id,
        video=open("video.mp4", "rb"),
        caption="🎥 Yangi promo video: xavfsizlik tizimlarimiz haqida qisqacha!",
        parse_mode="HTML"
    )

# Admin bilan bog‘lanish menyusi
async def admin_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📞 Biz bilan bog‘lanish:                             👨‍💻@khikmatillo11 👨‍💻+998200111151")  # O'zingni yoz



async def bot_haqida(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "<b>📄 Bot haqida</b>\n\n"
        "🤖 <b>Nomi:</b> Unicam bot\n"
        "📅 <b>Yaratilgan:</b> 2025-yil, iyul\n"
        "👨‍💻 <b>Yaratuvchi:</b> Hikmatillo Mamadaliyev\n"
        "🔧 <b>Maqsadi:</b> mijozlarga texnik yordam, yangiliklar, aloqa\n\n"
        "📅 <b>Yangiliklar:</b> Botni yangi versiyasi tez orada ishga tushadi\n"
        "🤖 Bot 24/7 rejimda ishlaydi\n" 
        "🤖 Botda suniy intelekt muammolaringizni yechishda ko'maklashadi\n\n"
        "🤖 Botda qandaydir tehnik xato sezsangiz bizga habar bering. Biz bundan mamnun bo'lamiz☺️\n\n"
        "☎️ <b>Bog‘lanish:</b> @khikmatillo11\n",
        parse_mode="HTML"
    )
   


# Bosh menyu uchun handler
async def bosh_menyu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start(update, context)

# Har qanday noto‘g‘ri xabar
async def unknown_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "❗️ Kechirasiz, noto‘g‘ri buyruq yubordingiz.\nPastdagi menyudan birini tanlang.",
        reply_markup=main_menu_keyboard()
    )

# Asosiy ishga tushirish funksiyasi
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Texnikyordam uchun ConversationHandler
    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex("^🛠 Texnik yordam$"), tehnik_yordam)],
        states={
            ASK_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_phone)],
            ASK_PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_issue)],
            ASK_ISSUE: [MessageHandler(filters.TEXT & ~filters.COMMAND, finish)],
        },
        fallbacks=[MessageHandler(filters.Regex("^🏠 Bosh menyu$"), bosh_menyu_handler)],
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("news", post_news))
    app.add_handler(CommandHandler("help", admin_contact))
    app.add_handler(CommandHandler("support", tehnik_yordam))
    app.add_handler(conv_handler)
    app.add_handler(MessageHandler(filters.Regex("^🆕 Yangiliklar$"), post_news))
    app.add_handler(MessageHandler(filters.Regex("^📞 Biz bilan bog‘lanish$"), admin_contact))
    app.add_handler(MessageHandler(filters.Regex("^🏠 Bosh menyu$"), bosh_menyu_handler))
    
    app.add_handler(MessageHandler(filters.PHOTO | filters.VIDEO, get_file_id))

    
    app.add_handler(MessageHandler(filters.Regex("(?i)bot haqida"), bot_haqida))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown_message))
    print("🤖 Bot ishga tushdi...")
    
    app.run_polling()

# To‘g‘ri ishga tushirish qismi
if __name__ == "__main__":
    main()