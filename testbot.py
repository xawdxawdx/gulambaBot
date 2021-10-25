from vk_api import VkApi
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import requests, urllib3
import json
import time
from time import sleep



class Voters:
	voted = False
	votedWhere = False
	
	def __init__(self, voted,votedWhere):
	 self.voted = voted
	 self.votedWhere = votedWhere

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
}

voted = []
votedWhere = []
GROUP_ID = '150060136'
GROUP_TOKEN = 'xxx' # Апи ключ вк бота
API_VERSION = '5.120'
lessgo = 0
toDan = 0
toAnv = 0
IsSpamedAnvar = False
# для callback-кнопки "открыть приложение"
APP_ID = 100500         # id IFrame приложения
OWNER_ID = 123456      # id владельца приложения


GO_WALK = "my_own_100501_type_edit"
NO_WALK = "my_own_100502_type_edit"

Danila = "my_own_100503_type_edit"
Anvar = "my_own_100504_type_edit"
all_users = []
voters:{}
  #if IsSpamedAnvar == True:
		    	#time.sleep(60)
		    # vk = vk_session.get_api()
		    # vk.messages.send(random_id=get_random_id(), peer_id=event.object.peer_id, message='@fantastic0')
def RecursiveSpamAnvar(members,obj_peer_id,voted):
	#var tags = all_users.get
	tags = ' '.join(members)
	print(tags)
	if IsSpamedAnvar == True:
		vk.messages.send(random_id=get_random_id(),peer_id=obj_peer_id,message=tags)
		time.sleep(60)
	else:
		return


# виды callback-кнопок
CALLBACK_TYPES = ('show_snackbar', 'open_link', 'open_app')

# Запускаем бот
# vk_session = VkApi(token=GROUP_TOKEN, api_version=API_VERSION)
# vk = vk_session.get_api()
# longpoll = VkBotLongPoll(vk_session, group_id=GROUP_ID)
while True:
	try:
		vk = VkApi(token=GROUP_TOKEN)
		vk._auth_token()
		vk.get_api()
		# Работа с сообщениями
		longpoll = VkBotLongPoll(vk, 150060136)






		settings = dict(one_time=False, inline=True)

		# №1. Клавиатура с 3 кнопками: "показать всплывающее сообщение", "открыть URL" и изменить меню (свой собственный тип)
		keyboard_1 = VkKeyboard(**settings)
		# pop-up кнопка
		# keyboard_1.add_callback_button(label='Покажи pop-up сообщение', color=VkKeyboardColor.SECONDARY, payload={"type": "show_snackbar", "text": "Это исчезающее сообщение"})
		# keyboard_1.add_line()
		# # кнопка с URL
		# keyboard_1.add_callback_button(label='Откртыть Url', color=VkKeyboardColor.POSITIVE, payload={"type": "open_link", "link": "https://vk.com/dev/bots_docs_5"})
		# keyboard_1.add_line()
		# # кнопка по открытию ВК-приложения
		# keyboard_1.add_callback_button(label='Открыть приложение', color=VkKeyboardColor.NEGATIVE, payload={"type": "open_app", "app_id": APP_ID, "owner_id": OWNER_ID, "hash": "anything_data_100500"})
		# keyboard_1.add_line()
		# кнопка переключения на 2ое меню
		keyboard_1.add_callback_button(label='Иду гулять', color=VkKeyboardColor.POSITIVE, payload={"type": GO_WALK})
		keyboard_1.add_callback_button(label='Не иду гулять', color=VkKeyboardColor.NEGATIVE, payload={"type": NO_WALK})

		# №2. Клавиатура с одной красной callback-кнопкой. Нажатие изменяет меню на предыдущее.
		keyboard_2 = VkKeyboard(**settings)
		# кнопка переключения назад, на 1ое меню.
		keyboard_2.add_callback_button('К Даниле', color=VkKeyboardColor.PRIMARY, payload={"type": Danila})
		keyboard_2.add_callback_button('К Анвариле', color=VkKeyboardColor.SECONDARY, payload={"type": Anvar})


		vk_session = VkApi(token=GROUP_TOKEN)
		f_toggle: bool = False

		# while True:
		for event in longpoll.listen():

		    # отправляем меню 1го вида на любое текстовое сообщение от пользователя
		    if event.type == VkBotEventType.MESSAGE_NEW:
		    	if event.object.peer_id != event.object.from_id:
		    		if "гулямба" in event.object.text.lower():

		    			voted = []
		    			votedWhere = []
		    			lessgo = 0
		    			toDan = 0
		    			toAnv = 0
		    			voters = {}
		    			IsSpamedAnvar = True
		    			vk = vk_session.get_api()
		    			vk.messages.send(
			                    # user_id=event.obj.message['from_id'],
	                    random_id=get_random_id(),
	                    peer_id=event.object.peer_id,
	                    keyboard=keyboard_1.get_keyboard(),
	                    message="gulamba")
		    			# all_users = vk.messages.getConversationMembers(peer_id = event.object.peer_id)
		    			# print([user['member_id'] for user in all_users['items']])
		    			# members = [user['member_id'] for user in all_users['items']]
		    			#vk.messages.send(random_id=get_random_id(),peer_id = event.object.peer_id,message=str(all_users['items'][0]))
	                    #vk.messages.send(random_id=get_random_id(),peer_id=obj_peer_id,messages='@id')
		    			# RecursiveSpamAnvar(members,event.object.peer_id,voted)


		    		if "нейросаня" in event.object.text.lower():
		    			url = 'https://zeapi.yandex.net/lab/api/yalm/text3'
		    			data = {"query":"why are you gay?","intro":0,"filter":1}
		    			r = requests.post(url, verify=False, json=data, headers=headers)
		    			resp = r.text
		    			vk = vk_session.get_api()
		    			last_id = vk.messages.send(random_id=get_random_id(), peer_id=event.object.peer_id, message=resp)


		    # обрабатываем клики по callback кнопкам
		    elif event.type == VkBotEventType.MESSAGE_EVENT:
		        # если это одно из 3х встроенных действий:
		        if event.object.payload.get('type') in CALLBACK_TYPES:
		            # отправляем серверу указания как какую из кнопок обработать. Это заложено в 
		            # payload каждой callback-кнопки при ее создании.
		            # Но можно сделать иначе: в payload положить свои собственные
		            # идентификаторы кнопок, а здесь по ним определить
		            # какой запрос надо послать. Реализован первый вариант.
		            r = vk.messages.sendMessageEventAnswer(
		                      event_id=event.object.event_id,
		                      user_id=event.object.user_id,
		                      peer_id=event.object.peer_id,                                                   
		                      event_data=json.dumps(event.object.payload))
		        # если это наша "кастомная" (т.е. без встроенного действия) кнопка, то мы можем
		        # выполнить edit сообщения и изменить его меню. Но при желании мы могли бы
		        # на этот клик открыть ссылку/приложение или показать pop-up. (см.анимацию ниже)
		        elif event.object.payload.get('type') == GO_WALK:
		        	if str(event.object.user_id) not in voters.keys():
			        		voters[str(event.object.user_id)] = Voters(True,False)
				        	#str(event.object.user_id)
				        	lessgo = lessgo + 1
				        	vk = vk_session.get_api()
				        	username = vk.users.get(user_ids = (str(event.object.user_id)))
				        	username = username[0]
				        	username = username['first_name']
				        	last_id = vk.messages.send(random_id=get_random_id(),peer_id=event.object.peer_id,message="Для гулямбы теперь " + str(lessgo) + " пацыков, с нами " + str(username),keyboard=(keyboard_2).get_keyboard())
				        	f_toggle = not f_toggle
				        	#or not voters[str(event.object.user_id)].is_voted
				    # else
				    # 	vk.messages.send(
			     #        random_id=get_random_id(),
			     #        peer_id=event.object.peer_id,
			     #        message=str(username) + ", ты уже голосовал")
		        	# lessgo = lessgo + 1
		        	# vk = vk_session.get_api()
		        	# last_id = vk.messages.send(
					      #       random_id=get_random_id(),
					      #       peer_id=event.object.peer_id,
					      #       message="Для гулямбы теперь " + str(lessgo) + " пацыков, с нами @id" + str(event.object.user_id),
					      #       keyboard=(keyboard_1 if f_toggle else keyboard_2).get_keyboard())
		            

		        elif event.object.payload.get('type') == NO_WALK:
		        	if str(event.object.user_id) not in voters.keys(): 
		        		voters[str(event.object.user_id)] = Voters(True,False)
			        	vk = vk_session.get_api()
			        	username = vk.users.get(user_ids = (str(event.object.user_id)))
			        	username = username[0]
			        	username = username['first_name']
			        	vk.messages.send(
			            random_id=get_random_id(),
			            peer_id=event.object.peer_id,
			            message=str("Против - узбек ") + str(username))
			            #or not voters[str(event.object.user_id)].is_voted
			      #   else
				    	# vk.messages.send(
			      #       random_id=get_random_id(),
			      #       peer_id=event.object.peer_id,
			      #       message=str(username) + ", ты уже голосовал")

		        elif event.object.payload.get('type') == Danila:
		        	if str(event.object.user_id) in voters.keys():
		        	    if voters[str(event.object.user_id)].voted and not voters[str(event.object.user_id)].votedWhere:
		        	    	voters[str(event.object.user_id)] = Voters(True,True)
		        	    	toDan = toDan + 1
		        	    	vk = vk_session.get_api()
		        	    	username = vk.users.get(user_ids = (str(event.object.user_id)))
		        	    	username = username[0]
		        	    	username = username['first_name']
		        	    	vk.messages.send(
		        	    	random_id=get_random_id(),
		        	    	peer_id=event.object.peer_id,
		        	    	message=str(username) + " хочет к Даниле на коленки, туда " + str(toDan) + " пацыков")
		        	# else:
		        	#   	vk.messages.send(
		        	#   	random_id=get_random_id(),
		        	#   	peer_id=event.object.peer_id,
		        	#   	message=str(username) + "сначала определись, ты идёшь гулять или нет, или ты уже голосовал")


		        elif event.object.payload.get('type') == Anvar:
		        	if str(event.object.user_id) in voters.keys():
		        		if voters[str(event.object.user_id)].voted and not voters[str(event.object.user_id)].votedWhere:
		        			voters[str(event.object.user_id)] = Voters(True,True)
		        			toAnv = toAnv + 1
		        			vk = vk_session.get_api()
		        			username = vk.users.get(user_ids = (str(event.object.user_id)))
		        			username = username[0]
		        			username = username['first_name']
		        			vk.messages.send(
		        			random_id=get_random_id(),
		        			peer_id=event.object.peer_id,
		        			message=str(username) + " хочет к Анвару под стол, туда " + str(toAnv) + " пацыков")
		        	# else:
	     	    #     	vk.messages.send(
	     	    #     	random_id=get_random_id(),
	     	    #     	peer_id=event.object.peer_id,
	     	    #     	message=str(username) + "сначала определись, ты идёшь гулять или нет, или ты уже голосовал")
		    #if IsSpamedAnvar == True:
		    	#time.sleep(60)
		    # vk = vk_session.get_api()
		    # vk.messages.send(random_id=get_random_id(), peer_id=event.object.peer_id, message='@fantastic0')

		    #Грязный хак, чтобы бот не умирал
	except requests.exceptions.ReadTimeout:
	        print("\n Переподключение к серверам ВК \n")
	        time.sleep(60)
	        continue
	except urllib3.exceptions.ProtocolError:
	        print("\n Переподключение к серверам ВК \n")
	        time.sleep(60)
	        continue
	except requests.exceptions.ConnectionError:
	        print("\n Переподключение к серверам ВК \n")
	        time.sleep(60)

	#except Exception:
	        #print("\n Переподключение к серверам ВК \n")
	        #time.sleep(60)
	        continue
