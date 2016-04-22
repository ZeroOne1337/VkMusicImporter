# -*- coding: utf-8 -*-
import vk_api
import os
import time
import pyantigate
import urllib.request
from mutagen.id3 import ID3

#antigate
antigate_key = input("Insert your Antigate key here: ")
a = pyantigate.Antigate(antigate_key)
bidd = input("Enter your maximum bid: ")
a.params = {'max_bid': bidd}
print('Your Antigate Balance: %s' % a.balance())
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def captcha_handler(captcha):
    print('Captcha Decifering...')
    key = format(captcha.get_url()).strip()
    urllib.request.urlretrieve(key, "captch.jpg")
    capchington = a.capcha('./captch.jpg')
    print('Captcha Decifered!')

    # Пробуем снова отправить запрос с капчей
    return captcha.try_again(capchington)

#vk login
login = input("Enter your VK login: ")
password = input("Enter your VK password: ")
vk_session = vk_api.VkApi(login, password, captcha_handler=captcha_handler)
print ("Authorising...")
vk_session.authorization()
vk = vk_session.get_api()
print ("Authorising done.")
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
mdirrectory = input("Enter your local music directory (for example D:\Music): ")

counter =0
#parse tracks

for root, dirs, files in os.walk(mdirrectory):
    for file in files:
        if file.endswith(".mp3"):
            track = os.path.join(root, file)
            audio = ID3(track)
    
            if "TPE1" in audio:
                try:
                    output = (audio['TPE1'], " - ", audio['TIT2'])
                    
                    if counter >=0:
                        response = vk.audio.search(q=output, count=1)
                        if response['items']:
                            counter +=1
                            print (response['items'][0]['title'],"Upload num: ", counter)
                            print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            own_id = response['items'][0]['owner_id']
                            aud_id = response['items'][0]['id']
                            vk.audio.add(audio_id = aud_id, owner_id= own_id)
                        else:
                            print ("No items in search response")
                    else:
                        print (output)
                        print ("counter too low, is at: ", counter)
                        counter +=1
                        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        
                except:
                    pass
                    
            else:
                print ("no ID data")
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        else:
            print ("no mp3's")
            print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    
