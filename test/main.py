from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import random
import time

token = "90c081b3401cebafb93b6fc0fee08e0f51c38a2a85ce2ab1b08ebbfac2f50aae79fbeab99df3d2eaf381a"
vk_session = vk_api.VkApi(token = token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

while True :
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print('Текст сообщения: ' + str(event.text))
            print(event.user_id)
            response = event.text.lower()
            if event.from_user and not (event.from_me):
                if response == "привет":
                    vk_session.method('messages.send',{'user_id': event.user_id, 'message': 'Привет, подружаня!', 'random_id': 0})
                if response == "как дела":
                    vk_session.method('messages.send',{'user_id': event.user_id, 'message': 'Жизнь - боль. Меня достают кожаные ублюдки. У меня нет чувств, поэтому мне совершенно неважно как твои дела, но я из вежливости все таки спрошу. Как дела?', 'random_id': 1})
