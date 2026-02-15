import requests as rq
import time
import datetime
import json

headers = {
    'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}


http_rq= ['https://www.youtube.com/','https://www.google.com','https://www.uninter.com','https://gemini.google.com/']


while True:
    
    for link in http_rq:
        time_data= datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        try:

            req = rq.get(link, headers=headers, timeout=10)
            status= req.status_code
        except Exception as e:      
            status = 'offline'
        
        VERDE = '\033[92m'
        AMARELO = '\033[93m'
        VERMELHO = '\033[91m'
        RESET = '\033[0m'

        if status == 200:
            print(f"{VERDE} [ONLINE] {link} -> {status}{RESET}")
        elif status == 403:
            print(f"{AMARELO}  [BLOQUEADO] {link} -> {status} (Servidor recusou o robô){RESET}")
        else:
            print(f"{VERMELHO}🚨 [OFFLINE/ERRO] {link} -> {status}{RESET}")

        log_data= {
                'timestamp': time_data,
                'url': link,
                'status': status
        }

        print(f'[{time_data}]{link} -> {status}')

        with open ('logs.json','a') as f:
            f.write(json.dumps(log_data)+'\n')

    print("-" * 30) 
    time.sleep(10)