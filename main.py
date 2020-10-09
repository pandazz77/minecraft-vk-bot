import vk_api, random

TOKEN = '######'
GROUP_ID = 666

vk_session = vk_api.VkApi(token = TOKEN)

from vk_api.longpoll import VkLongPoll, VkEventType

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

def random_id():
    random1 = 0
    random1 += random.randint(0,100000000)
    return(random1)
def getip():
    with open('ip.txt','r') as file:
        ip = file.read()
        return(ip)
while True:
    try:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                if event.text.lower() == 'getip':
                    vk.messages.send(
                    user_id = event.user_id,
                    message = 'IP:\n'+getip(),
                    random_id = random_id()
                    )
                elif event.text.lower() == 'status':
                    server = MinecraftServer.lookup(check)
                    status = server.status()
                    vk.messages.send(
                        user_id=event.user_id,
                        message = 'Status:\nOnline: {0}\nPing:{1}'.format(status.players.online, status.latency),
                        random_id=random_id())
    except Exception as error:
        print('ERROR:\n'+str(error))
