import telebot
import time

bot = telebot.TeleBot('1526588208:AAFWFWAOdl_Lw31phdlrtCAplw2PXSGUqbY')
API = "https://core.telegram.org/bots/api/{}"

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Добро пажаловать на Helper bot. Для знать свой id пишите my id.')

# @bot.message_handler(commands=['id_ban'])
# def kick_users(message):
#     if message.from_user.id == 696084613:
#         if message.reply_to_message:
#             text = message.reply_to_message.from_user.id
#             bot.kick_chat_member(message.chat.id, text)
#             bot.send_message(message.chat.id, "Done!" .format(message, text))

    # else:
    #     bot.send_message(message.chat.id, "do you not moder")

#kick2 itaci 869582467, saske 1451015386

@bot.message_handler(commands=['kdban'])
def kick2_users(message):
    admins = [696084613, 869582467, 1451015386]
    if message.from_user.id in admins:
        if message.reply_to_message:
            text = message.reply_to_message.from_user.id
            bot.kick_chat_member(message.chat.id, text)
            bot.send_message(message.chat.id, "Done!" .format(message, text))

    else:
        bot.send_message(message.chat.id, "do you not moder")


@bot.message_handler(commands=['kdmute'])
def mute_users(message):
    admins = [696084613, 869582467, 1451015386]
    if message.from_user.id in admins:
        if message.reply_to_message:
            text = message.reply_to_message.from_user.id
            bot.restrict_chat_member(message.chat.id, text)
            bot.send_message(message.chat.id, "Done! user is muted")

    else:
        bot.send_message(message.chat.id, "do you not moder")

@bot.message_handler(commands=['id_groupmute'])
def mute_group(message):
    if message.from_user.id == 696084613:
            bot.set_chat_permissions(message.chat.id, can_send_message = None)
            bot.send_message(message.chat.id, "Done! group is muted")

@bot.message_handler(commands=['kdunmute'])
def unmute_users(message):
    admins = [696084613, 869582467, 1451015386]
    if message.from_user.id in admins:
        if message.reply_to_message:
            text = message.reply_to_message.from_user.id
            bot.promote_chat_member(message.chat.id, text)
            bot.send_message(message.chat.id, "Done! user is unmuted")

    else:
        bot.send_message(message.chat.id, "do you not moder")


@bot.message_handler(commands=['id_set_admin'])
def admin_users(message):
    if message.from_user.id == 696084613:
        if message.reply_to_message:
            text = message.reply_to_message.from_user.id
            bot.promote_chat_member(message.chat.id, text,
                                                     can_change_info = True,
                                                     can_post_messages = True,
                                                     can_edit_messages = True,
                                                     can_delete_messages = True,
                                                     can_invite_users = True,
                                                     can_restrict_members = True,
                                                     can_pin_messages = True,
                                                     can_promote_members = True)

            bot.send_message(message.chat.id, "Done! user is admin")

@bot.message_handler(commands=['kdunban'])
def unban_users(message):
    admins = [696084613, 869582467, 1451015386]
    if message.from_user.id in admins:
        if message.reply_to_message:
            text = message.reply_to_message.from_user.id
            bot.unban_chat_member(message.chat.id, text)
            bot.send_message(message.chat.id, "Done! user is unbanned")

@bot.message_handler(commands=['info'])
def spam_users(message):
    if message.from_user.id == 696084613:
       spam_message = "Helper id bot\n\nName: Helper bot\nUsername: @mynew885bot\nGroup: yes\nCreate by Python Group\n\nNews bot: @PythonGroupbotnews"
       bot.send_message(message.chat.id, spam_message)

@bot.message_handler(commands=['news'])
def my_message(message):
    bot.send_message(message.chat.id, "Пусто")

@bot.message_handler(content_types=['new_chat_members'])
def new_member_text(message):
     bot.reply_to(message, "У нас есть новый участник @{}" .format(message.from_user.username))
    #  bot.delete_message(message.chat.id, message.message_id)

@bot.message_handler(content_types=['left_chat_member'])
def left_member_text(message):
     bot.delete_message(message.chat.id, message.message_id)
     bot.reply_to(message, "Нас покинул(а) участник @{}" .format(message.from_user.username))

@bot.message_handler(content_types=['text'])
def send_message(message):
 # if message.chat.type == "private":

 if message.text.lower() == "бан":
    # if message.from_user.id == 696084613:
        if message.reply_to_message:
            text = message.reply_to_message.from_user.id
            bot.kick_chat_member(message.chat.id, text)
            bot.send_message(message.chat.id, "Полизователь забанен" )

 elif message.text.lower() == "разбан":
    # if message.from_user.id == 696084613:
        if message.reply_to_message:
            text = message.reply_to_message.from_user.id
            bot.unban_chat_member(message.chat.id, text)
            bot.send_message(message.chat.id, "Полизователь разбанен" )

 elif message.text.lower() == "мут":
    # if message.from_user.id == 696084613:
        if message.reply_to_message:
            text = message.reply_to_message.from_user.id
            bot.restrict_chat_member(message.chat.id, text)
            bot.send_message(message.chat.id, "Полизователь замутен" )

 elif message.text.lower() == "размут":
    # if message.from_user.id == 696084613:
        if message.reply_to_message:
            text = message.reply_to_message.from_user.id
            bot.promote_chat_member(message.chat.id, text)
            bot.send_message(message.chat.id, "Полизователь размутен" )


 elif message.text.lower() == 'group id':
    bot.send_message(message.chat.id, 'group id: {}'.format(message.chat.id))
 elif message.text.lower() == 'my id':
    bot.send_message(message.chat.id, 'id: {}'.format(message.from_user.id))

 elif message.text.lower() == 'commands id bot':
    bot.send_message(message.chat.id, '/kdban - ban berish\n/kdunban - bandan chiqarish\n/kdmute - mute berish\n/kdunmute - mutedan chiqarish\n/info - bot haqida')


 # elif message.text.lower() == "mute":
 #    bot.set_chat_permissions(message.chat.id, can_send_messages=None, can_send_media_messages=None, can_send_stickers=True, can_send_animations=True)
 #    bot.send_message(message.chat.id, "Done! group is muted")

 # elif message.text.lower() == 'unmute':
 #    bot.send_message(message.chat.id, 'group unmuted to 8:00')
 #
 # elif message.text.lower().startswith('https'):
 #     bot.send_message(message.chat.id, '@{} Пожалуйста, не размещайте рекламу '.format(message.from_user.username))
 #     bot.delete_message(message.chat.id, message.message_id)
 #
 # elif message.text.lower().startswith('http'):
 #     bot.send_message(message.chat.id, '@{} Пожалуйста, не размещайте рекламу '.format(message.from_user.username))
 #     bot.delete_message(message.chat.id, message.message_id)

#  elif message.text.lower().startswith('@'):
#      bot.send_message(message.chat.id, '@{} Пожалуйста, не размещайте рекламу '.format(message.from_user.username))
#      bot.delete_message(message.chat.id, message.message_id)

 # elif message.text.lower().startswith('t.me/'):
 #     bot.send_message(message.chat.id, '@{} Пожалуйста, не размещайте рекламу '.format(message.from_user.username))
 #     bot.delete_message(message.chat.id, message.message_id)
 #
 # elif message.text.lower().startswith('telegram/me'):
 #     bot.send_message(message.chat.id, '@{} Пожалуйста, не размещайте рекламу '.format(message.from_user.username))
 #     bot.delete_message(message.chat.id, message.message_id)

 elif message.text.lower().startswith('сук'):
     bot.send_message(message.chat.id, '@{} пожалуйста, говорите хорошо  '.format(message.from_user.username))
     bot.delete_message(message.chat.id, message.message_id)

 elif message.text.lower().startswith('cучка'):
     bot.send_message(message.chat.id, '@{} пожалуйста, говорите хорошо  '.format(message.from_user.username))
     bot.delete_message(message.chat.id, message.message_id)

 elif message.text.lower().startswith('бл'):
     bot.send_message(message.chat.id, '@{} пожалуйста, говорите хорошо  '.format(message.from_user.username))
     bot.delete_message(message.chat.id, message.message_id)

 elif message.text.lower().startswith('нах'):
     bot.send_message(message.chat.id, '@{} пожалуйста, говорите хорошо  '.format(message.from_user.username))
     bot.delete_message(message.chat.id, message.message_id)

 elif message.text.lower().startswith('иди'):
     bot.send_message(message.chat.id, '@{} пожалуйста, говорите хорошо  '.format(message.from_user.username))
     bot.delete_message(message.chat.id, message.message_id)

 elif message.text.lower().startswith('ма'):
     bot.send_message(message.chat.id, '@{} пожалуйста, говорите хорошо  '.format(message.from_user.username))
     bot.delete_message(message.chat.id, message.message_id)

 elif message.text.lower().startswith('Ма'):
     bot.send_message(message.chat.id, '@{} пожалуйста, говорите хорошо  '.format(message.from_user.username))
     bot.delete_message(message.chat.id, message.message_id)

 elif message.text.lower().startswith('пащол'):
     bot.send_message(message.chat.id, '@{} пожалуйста, говорите хорошо  '.format(message.from_user.username))
     bot.delete_message(message.chat.id, message.message_id)

 elif message.text.lower().startswith('пашол'):
     bot.send_message(message.chat.id, '@{} пожалуйста, говорите хорошо  '.format(message.from_user.username))
     bot.delete_message(message.chat.id, message.message_id)

 elif message.text.lower().startswith('su'):
     bot.send_message(message.chat.id, '@{} пожалуйста, говорите хорошо  '.format(message.from_user.username))
     bot.delete_message(message.chat.id, message.message_id)


 elif message.text.lower().startswith('jal'):
     bot.send_message(message.chat.id, '@{} пожалуйста, говорите хорошо  '.format(message.from_user.username))
     bot.delete_message(message.chat.id, message.message_id)

 elif message.text.lower().startswith('bl'):
     bot.send_message(message.chat.id, '@{} пожалуйста, говорите хорошо  '.format(message.from_user.username))
     bot.delete_message(message.chat.id, message.message_id)



 elif message.text.lower() == "info id bot":
     bot.send_message(message.chat.id, "Please input your password:")
     bot.send_message(message.chat.id, "password:")

 elif message.text.lower() == "well":
     text = "thanks"
     bot.send_chat_action(message.chat.id, 'typing')
     time.sleep(3)
     bot.send_message(message.chat.id, text)

     #chat ceper bot id 553147242

#-1001430159008 id test bots group
 elif message.text.lower() == "привет всем":
     bot.send_message(-1001430159008, "привет")

 elif message.text.lower() == "5555":
     bot.send_message(message.chat.id, "Yor password is true. For get info write /info")
     bot.delete_message(message.chat.id, message.message_id)

 elif message.text.lower() == "kd ban":
    # if message.from_user.id == 696084613:
        if message.reply_to_message:
            text = message.reply_to_message.from_user.id
            bot.kick_chat_member(message.chat.id, text)
            bot.send_message(message.chat.id, "ok. User guruhdan chiqarildi" )

 elif message.text.lower() == "kd unban":
    # if message.from_user.id == 696084613:
        if message.reply_to_message:
            text = message.reply_to_message.from_user.id
            bot.unban_chat_member(message.chat.id, text)
            bot.send_message(message.chat.id, "ok. User guruhga yana qayta oladi" )

 elif message.text.lower() == "kd mute":
    # if message.from_user.id == 696084613:
        if message.reply_to_message:
            text = message.reply_to_message.from_user.id
            bot.restrict_chat_member(message.chat.id, text)
            bot.send_message(message.chat.id, "ok. User yozishdan cheklab qo'yildi" )

 elif message.text.lower() == "kd unmute":
    # if message.from_user.id == 696084613:
        if message.reply_to_message:
            text = message.reply_to_message.from_user.id
            bot.promote_chat_member(message.chat.id, text)
            bot.send_message(message.chat.id, "ok. User yana yoza oladi" )


 # elif message.text.lower() == "alo":
 #     text = "nma"
 #     bot.send_chat_action(message.chat.id, 'typing')
 #     time.sleep(3)
 #     bot.send_message(message.chat.id, text)
 #
 # elif message.text.lower() == "sangamas":
 #     text = "ok"
 #     bot.send_chat_action(message.chat.id, 'typing')
 #     time.sleep(3)
 #     bot.send_message(message.chat.id, text)

 # elif message.text.lower() == "salom":
 #     text = "Salom qalesan"
 #     bot.send_chat_action(message.chat.id, 'typing')
 #     time.sleep(3)
 #     bot.send_message(message.chat.id, text)
 #
 # elif message.text.lower() == "yaxwi ozinc":
 #     text = "yaxw"
 #     bot.send_chat_action(message.chat.id, 'typing')
 #     time.sleep(3)
 #     bot.send_message(message.chat.id, text)
 #
 # elif message.text.lower() == "yaxshi":
 #     text = "ha yaxw"
 #     bot.send_chat_action(message.chat.id, 'typing')
 #     time.sleep(3)
 #     bot.send_message(message.chat.id, text)
 #
 # elif message.text.lower() == "more info kdwbot":
 #     text = "King Danger Wolf Helper bot h5"
 #     bot.send_chat_action(message.chat.id, 'typing')
 #     time.sleep(3)
 #     bot.send_message(message.chat.id, text)

 else:
        if message.from_user.id == 1765604781:
            bot.send_message(-1001430159008, message.text)

#r = bot.send_message(-1001445542731, 'salom hammaga')
#r = bot.send_message(-1001445542731, 'da man @danger_wolf885 man test qvoman botimi😅')
#-1001445542731
#-1001430159008

bot.polling(none_stop = True)
