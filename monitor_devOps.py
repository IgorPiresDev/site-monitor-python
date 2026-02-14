import requests as rq
import time
import datetime



http_rq= ['https://www.youtube.com/','https://www.google.com','https://www.uninter.com','https://gemini.google.com/']


while True:
    try:
        time_bz= datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        with open('log_monitor.txt', 'a') as arquivo:

            for link in http_rq:
                req = rq.get(link)
            

                if req.status_code == 200:
                    arquivo.write(f'CHECK TIME: {time_bz}, {link} ONLINE\n')
                else:
                    arquivo.write(f'CHECK TIME: {time_bz}, {link} OFFLINE\n')

    except:'error critico!'
    time.sleep(10)