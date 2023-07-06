from vk_api.longpoll import VkEventType, VkLongPoll
from interface import *
from data_base import *
from config import *


for event in bot.longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        request = event.text.lower()
        user_id = event.user_id
        if request == 'поиск' or request == 's':
            bot.get_age_of_user(user_id)
            bot.get_target_city(user_id)
            bot.looking_for_persons(user_id)  # выводит список в чат найденных людей и добавляет их в базу данных.
            bot.show_found_person(user_id)  # выводит в чат инфо одного человека из базы данных.
        elif request == 'удалить' or request == 'd':
            delete_table_seen_person()  # удаляет существующую БД.
            create_table_seen_person()  # создает новую БД.
            bot.message_send(user_id, f' База данных обновлена! Укажите команду "Поиск" или "s" ')
        elif request == 'смотреть' or request == 'v':
            if bot.get_found_person_id() != 0:
                bot.show_found_person(user_id)
            else:
                bot.message_send(user_id, f' В начале наберите "Поиск" или "s".  ')
        else:
            bot.message_send(user_id, f'{bot.name(user_id)} Бот готов к поиску, наберите: \n '
                                      f' "Поиск или s" - Поиск людей. \n'
                                      f' "Удалить или d" - удаляет старую БД и создает новую. \n'
                                      f' "Смотреть или s" - просмотр следующей записи в БД.')
