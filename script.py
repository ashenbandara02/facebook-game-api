from io import open
import datetime
import requests
import time
import json
import os
import sys


tim = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
print("######Enter the Token From Graph Api#######")
video_id = str(input('video id>> '))
new_token = ''
cursor = ''

def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')


def attacher(accesskey, url):
    rawlink = url.split("&")
    del rawlink[-1]
    halfraw = rawlink[0]
    quaterraw = str(halfraw).split("?")
    extract1 = quaterraw[1]
    extract2 = str(extract1).split("=")
    extract2[1] = accesskey
    decode1 = "=".join(extract2)
    quaterraw[1] = decode1
    decode2 = '?'.join(quaterraw)
    decode3 = decode2.split()
    decode3.append(rawlink[1])
    decoded = '&'.join(decode3)
    return str(decoded)


def main(video_id, token, *args):
    global cursor
    if len(args) >= 1:
        link_url = list(args)[0]+"&after="+cursor
    
    else:
        link_url = 'https://graph.facebook.com/{}/comments?access_token={}'.format(video_id, token)
    run = True
    nofull = False
    
    with open("chats.txt", "a", encoding='utf-8') as txt:
        while True:
            if nofull == True:
                run = True
                
            if run == True:
                a = requests.get(link_url, verify=True)
                b = a.json()
                print(b)

            if run == False:
                # time.sleep(10)
                a = requests.get(link_url, verify=True)
                b = a.json()
                print("Checking")
                
            non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

            if run == True:
                try:
                    for each in b['data']:
                        if len(b['data']) < 25:
                            nofull = True
                            print("\n** Waiting for new chats(usually shows up within 4 minutes) **")
                            time.sleep(240)
                            break
                        elif len(b['data']) == 25:
                            # time.sleep(1)
                            nofull = False
                        
                            print("--"*len(each['id']))
                            print('\nperson: {}'.format(each['id']))
                            txt.writelines('\n\n\n\n\nperson: {}'.format(each['id']))
                            print('\ntime: {}'.format(each['created_time']))
                            txt.writelines('\n\n\ntime: {}'.format(each['created_time']))
                        
                            try:
                                print('\nmessage: {}'.format(each['message']))
                                txt.writelines('\n\n\nmessage: {}'.format(each['message']))
                            except UnicodeEncodeError:
                                print('\nmessage: {}'.format(each['message']).translate(non_bmp_map))
                                txt.writelines('\n\n\nmessage: {}'.format(each['message']).translate(non_bmp_map))

                except KeyError as msg:
                    new_token = str(input("\n Token expired/Maximum use reached Enter new Token >> "))
                    nofull = True
                    token2url = attacher(new_token, link_url)
                    
            try:
                if len(b['data']) == 25:
                    try:
                        link_url = str(b['paging']['next'])
                        for x in b['paging'].items():
                            cursor = list(x)[1]['after']
                            break
                        
                        run = True
                    except KeyError:
                        print("comes here too")
                        run = False
            except KeyError as msg:
                run = True
                break

    try:
        main(video_id, new_token, token2url)

    except UnboundLocalError:
        main(video_id, token, token2url)
            

def startup():
    clear()
    print("""

        ######################################################################
        SomeTimes the Graph api token key Expires or the facebooks
        limit is reached,So when it Happens You
        Have to Make a new Access Token , this usually happens evey 2 hours
        .And Dont not run the App on the Same live streamer for 4 times
        ######################################################################

        1.Continue[y]
        2.Quit[q]
        
    """)

    if str(input(">> ")) == 'y':
        clear()
        main(video_id, token = input("Token >>"))

    else:
        sys.exit()
    

if __name__ == '__main__':
    startup()
