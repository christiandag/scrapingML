import requests, pickle
print('INICIANDO SESIÓN')
session = requests.Session() 

def login(user,password):
    print("\nLOGIN INSTAGRAM")
    session.headers.update({'authority': 'www.instagram.com',
                            'method': 'GET',
                            'path': '/accounts/login/',
                            'scheme': 'https',
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                            'accept-encoding': 'gzip, deflate, br',
                            'accept-language': 'en-US,en;q=0.9',
                            'upgrade-insecure-requests': '1',
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36 OPR/62.0.3331.99'
                            })

    r = session.get('https://www.instagram.com/accounts/login')

    session.headers.update({'Host':'www.instagram.com',
                            'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
                            'Accept':'*/*',
                            'Accept-language': 'en-US,en;q=0.9,es;q=0.8',
                            'Accept-Encoding':'gzip, deflate, br',
                            'Referer': 'https://www.instagram.com/accounts/login/?source=auth_switcher',
                            'X-CSRFToken':r.text.split('csrf_token":"')[1].split('",')[0],
                            'X-Instagram-AJAX':r.text.split('rollout_hash":"')[1].split('",')[0],
                            'X-IG-App-Id':'936619743392459',
                            'Content-Type':'application/x-www-form-urlencoded',
                            'X-Requested-With':'XMLHttpRequest',
                            # 'content-length':'144',
                            'Connection':'keep-alive',
                            # 'Cookie': cookies,
                            'TE': 'Trailers'})

    data = {'username':user,
            'password':password,
            'queryParams':'{}',
            'optIntoOneTap': 'true'}

    r2 = session.post('https://www.instagram.com/accounts/login/ajax/',data = data)
    print(r2.status_code, r2.url)
    for resp in r2.history:
        print (resp.status_code, resp.url)

    confirmado = ""
    if r2.status_code == 400:
        print("¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡Confirmar login en la cuenta del celular!!!!!!!!!!!!!!!!")
        print('Ha confirmado y desea continuar?')
        confirmado = input('Si: continuar\nNo: cancelar\n:')
        if confirmado == 'No':
            print('Cancelado')
            return  

def save_session():
    with open('instagram_cookies', 'wb') as f:
        pickle.dump(session.cookies, f)

def retrieve_session():
    with open('instagram_cookies', 'rb') as f:
        try:
            session.cookies.update(pickle.load(f))
        except:
            print("Inicio de sesión no guardado")