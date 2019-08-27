import requests, pickle
import time

def fb_login(user,password):
    print('Logging in facebook')
    session = requests.Session()  
    r = session.get('https://www.facebook.com')   
    jazoest = r.text.split('jazoest" value="')[1].split('"')[0]

    # print("COOKIE 1")
    cookies = ""
    for name,value in session.cookies.items():
        cookies = cookies + name +'=' +value+';'
        # print(name,':',value)
    # print('LOGIN FACEBOOK')
    session.headers.update({'Host': 'www.facebook.com',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                            'Accept-Language': 'es-EC,en-US;q=0.7,en;q=0.3',
                            # 'Accept-Encoding': 'gzip, deflate, br',
                            'Referer': 'https://www.facebook.com/login/',
                            'Content-Type': 'application/x-www-form-urlencoded',
                            # 'Content-Length': '629',
                            'Connection': 'keep-alive',
                            'Cookie': cookies,
                            'Upgrade-Insecure-Requests': '1',
                            'TE': 'Trailers'
                            })
    data = {'jazoest': jazoest,
            'lsd':r.text.split('"token":"')[1].split('"}')[0],
            'display':'',
            'enable_profile_selector':'',
            'isprivate':'',
            'legacy_return':'0',
            'profile_selector_ids':'',
            'return_session':'',
            'skip_api_login':'',
            'signed_next':'',
            'trynum':'1',
            'timezone':'300',
            'lgndim':'eyJ3IjoxMzY2LCJoIjo3NjgsImF3IjoxMzA0LCJhaCI6NzY4LCJjIjoyNH0=',
            'lgnrnd':'203025_DH-m',
            'lgnjs':'1564457424',
            'email':user,
            'pass':password,
            'prefill_contact_point':'',
            'prefill_source':'',
            'prefill_type':'',
            'first_prefill_source':'',
            'first_prefill_type':'',
            'had_cp_prefilled':'false',
            'had_password_prefilled':'false',
            'ab_test_data':'APAA//PvPPAAAAPAAAPAAAAAPAAAAAPPAAAAAAAA333/HAAAAAKDCC'
            }
    time.sleep(5)
    r2 = session.post('https://www.facebook.com/login/device-based/regular/login/',data = data)
    print(r2.status_code, r2.url)
    for resp in r2.history:
        print (resp.status_code, resp.url)
    
    if r2.status != 200:
        print("Login failed")
    return session

def fb_save_session(session):
    try:
        print("Saving session")
        with open('facebook_cookies', 'wb') as f:
            pickle.dump(session.cookies, f)
    except:
        print("Save failed")

def fb_retrieve_session():
    print('Retrieving session')
    session = requests.Session()  
    r = session.get('https://www.facebook.com')   
    jazoest = r.text.split('jazoest" value="')[1].split('"')[0]
    cookies = ""
    for name,value in session.cookies.items():
        cookies = cookies + name +'=' +value+';'
        # print(name,':',value)
    
    with open('facebook_cookies', 'rb') as f:
        try:
            session.cookies.update(pickle.load(f))
        except:
            print("No session saved")
    return session


def i_login(user,password):
    print("Logging in instagram")
    session = requests.Session() 
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

    # confirmado = ""
    # if r2.status_code == 400:
    #     print("¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡Confirmar login en la cuenta del celular!!!!!!!!!!!!!!!!")
    #     print('Ha confirmado y desea continuar?')
    #     confirmado = input('Si: continuar\nNo: cancelar\n:')
    #     if confirmado == 'No':
    #         print('Cancelado')
    if r2.status != 200:
        print("Login failed")
    return session

def i_save_session(session):
    try:
        print("Saving session")
        with open('instagram_cookies', 'wb') as f:
            pickle.dump(session.cookies, f)
    except:
        print("Save failed")

def i_retrieve_session():
    print("Retrieving session")
    session = requests.Session()  
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

    with open('instagram_cookies', 'rb') as f:
        try:
            session.cookies.update(pickle.load(f))
        except:
            print("No session saved")
    return session


def li_login(user,password):
    print("Logging in linkedin")
    session = requests.Session()  
    time.sleep(5)
    r = session.get('https://www.linkedin.com/login')    
    cookies = ""
    for name,value in session.cookies.items():
        cookies = cookies + name +'=' +value+';'
        # print(name,':',value)

    session.headers.update({'Host': 'www.linkedin.com',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                            'Accept-Language': 'es-EC,en-US;q=0.7,en;q=0.3',
                            'Accept-Encoding': 'gzip, deflate, br',
                            'Referer': 'https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin',
                            'Content-Type': 'application/x-www-form-urlencoded',
                            'Connection': 'keep-alive',
                            'Cookie': cookies,
                            'Upgrade-Insecure-Requests': '1',
                            'TE': 'Trailers'
                            })

    data = {'csrfToken':session.cookies['JSESSIONID'],
            'session_key':user,
            'ac':'0',
            'sIdString':r.text.split('sIdString" value="')[1].split('" /><')[0],
            'controlId':'d_checkpoint_lg_consumerLogin-login_submit_button',
            'parentPageKey':'d_checkpoint_lg_consumerLogin',
            'pageInstance':r.text.split('pageInstance" content="')[1].split('">')[0],
            'trk':'guest_homepage-basic_nav-header-signin',
            'session_redirect':'',
            'loginCsrfParam':r.text.split('loginCsrfParam" value="')[1].split('"/>')[0],
            'fp_data':'{"X-kcnN2cez-f":"AwIHlXRpAQAAImHbUFfTzoZj1Eyqi8fC6QjI9Fmx9REX3bPOsas9PjU3F-c3AX8AAAGLr4YowLkAAAAAAAAAAA==","X-kcnN2cez-b":"-u2y6cz","X-kcnN2cez-c":"AwIHlXRpAQAAImHbUFfTzoZj1Eyqi8fC6QjI9Fmx9REX3bPOsas9PjU3F-c3AX8AAAGLr4YowLkAAAAAAAAAAA==","X-kcnN2cez-d":"o_0","X-kcnN2cez-z":"p","X-kcnN2cez-a":"kxLYjjyL0sYBO=mPlLSXhmRmibE_YNUScZLw6kIPhJzVuF4E1ms=lEhPdMF1-tFomBcQGud7-I53tFGwH6E7QxGS-SEwR-DzaznyfdDOKT1zjldVvIpS74Tz5o5sBXD6Nal5zyJ0agp_TVUBpgyHEpbpX9TUbzTxzmt0z50yH_2c3-S6QAiYNtud1b_30yYAGccENrCOyiBfskqI4wPya_iu_7kgoILbepsQgzgeAUp-7vnYfJmmadvnzHYLS6_VDmcBVBmNjZcg-CwVYrRX1OvgQZa5Cq=e=DGnHZNI_HZ5NaZNB1bJBYNxUoiSl2sDEuu2T56MzaIEeAf3NLJQ3K2vvn=RSC-g8hUB1q74f4P-sD5xnufNoDAKigVKCUTheyBgYUxmQMUFDVXGHAEvSM38hxZRGI_ih0VUz=JB5q9AcZdtvkGKNnXZuie3i7hVa532gohq2Gq_TRGj2LN7mLeNhvjFJ6-RjbMfa1oBY7sxRmFli_yjt3=-f0P0F-yz1-RhV=RMyhS0h4w3rxOX6rx8-Nat3ZcoRcpkEmGlIoCkzmfwlrbKOwHizBQE-7BaQjYX0ZE50B4mzdzDUbtJ9O86ZzHz=mJTmpJZ8tyOOna8PnHrobLtcvENJ2wd1AUQM4iR8b4mxd3=nUpdiCozP4S27MzrhjaS5644EceX=PuaYeRQyiXNs6yZLfbroTzYZPz52-z1lgoa3XJQknZzMxHABhqPXNf8Bt=KJu3goYhDHE8xNAjXL-amnCGVijIoQPL5CRu-45haMp=_kT6ISqrR_gDtDsVHsp5bzK73r3f6OCBzf0SzRAF2fxFNn-74k7NKG03ch_w7rVD1HMFwTmCZFZCupSr50n0gITYtkQkOLMvibrHQ4RcrrGDDDU-6F2afujaJhvh_vVgu0bodoyiGFPoBm_oTCj7QnC1T_PZBXtFUt9u7gJrsSQh8QMZtTo4VKz7-mANvtVxprkI5oMeBwb_cMmz6SidqpChbwZr3n32A6wdLSwq0AO_AYqkMdz82FH5gGCY7djO9PIE4gamCCdsAC8p4vKzrbucQTqc6BwNUasD5ZeBHji2sEC80BiD4Jm7zNAgmG662yKuzI1L9VPdjub8VcgazIGku=xyhjAJItYa9XUnpr9cq6DAwijGR-nlvDJFgzH-U1QDlv1d4YnA6M=Ynrpd=m55DwmHa6OSoiyni6StAv=DJk4q1xOpsbN7Awuv3F6t3xJpbb86w2GKJ2K-EnxdpkNTseZF4xMH9C5YyewdDtKK2FM7lIHRwQpINcO322dErIlNus_DbfSgIGSfhTvkSxM7bxjV6HnHg47tvilihbKSEgfg5Pz6if0c6uLo0yPNTtQPtAdgOmrly7ZaO33FSr9HvyLmtjALnMuhVsXeMlnj=9Ts86Zyb1RPdFsxj8nUbFQ_jUcAYmuYT8RqsXBCyEL5EVXJJN1HJKvoPPAcVFRPRYBuV4ns=PkubHQdzqlbPrcFQGnms8ShdLYcdVvk5Foaz9zaYYT3vl7riwQyxETtaAVyHwipSiXxpE39Fmk7REbqyCHt6I2BcHPdvGMBy0UDM6sVq9txtN_7HGd5l60w_woag6MjVKOaNwCA7NO=--DYchOOJC3nQl3f5N1rtDmH2FirwqgvaoYL_okEKLMcADcH60y282eKOrQqgSI7THgT=1Dy8DBomAuFVS-bn9STdgEKfEwCCTV3aVXbjZO11G8nAxMct0=7figfvifC6x3EUQz6moyKelQrMf8aa907phLcELkDip6tDMo3TC5h-HX6izru=TSDm8VvFSLQLurAqvn9mrVC6Zk7sNgUUx4_NpRi89xIgblGyYsGE0OVw0gcExRBRDsjFTfbG4cxZ_qG_=5nbpNmKbiCoVZl15yfQT1B-yvfMA07V5G84HqVuJ7nf8tp7_IcMYVJ9yVvkPkXTkUynhc06o2ql=x7c3FIUYgEe=zBGUTsvsB-wMkkNrxMKKPktOUBvo4qai3OYRhozblZBZKv5PXoMFB5nK-OphDt9hUlICahT7xhzQFSBSDGOBHZFr0m8DFCikq7yOLfUSvbGP5SXQJScrZ77A3CayTQKpnZrpp5lCA2218tiIXdarJLi4iPQiPFrhk6mVMkEO-p4aVdaJmQ9vMea0yiTqQoPNdcOHc20D7szK1z2RSZM=clm5-4G_UpMNb5wti3lJvJsGz1BrFTYx4Bis4Pp4temtNvKlL7UA=2ussowNVPb2Aoruflqwc3i_ic2iQM=77uFwA1nt2fx2VoNR8OlhymX7F5QomzT-eSBfJKfCS=4xg4VbsNUfNKrAVsAZTqNGrROhKCc8XK3nl_f9xiDVr3XYsbuNVrvb7TJ15k159nnNmA2NQpYxPdCVwfJ2RBjd624HE-yzzZdLl38miUmEE0OKVI03VmzfFgGOH5pdAhDqstj8sdOEGQyRjXtJ52nG5oxtKUS8RXdOzGN3RCnQwxQF1RXD0pt3Jl9fq2YazXOtIBgHPSaM1nw1N5JMfcV2RnfIhRfv3lzYhq-EVsYGMOqxTrrUbS=QI54Josqm4YrFjyJw9vXs4F97Sz7kbEY=xpMTmR-y74GytVAXRd9FU-4QPISHXQMoagqjSbwvh3lYD_FFS4-p_h76wYpozRMcyqwjH1omfpVBefqdzj-NvbUk7qjhGBRLxUUws6dL=nyoacAz0MYOipSSidXRlCKi=btyG4BRBIXZsuM72J3VTUm2D48qxo_kvobbg78JolP1Q1hGG7FXfEPXIbAFMZivBJRbOPl7S4iQ--LKAXQTuckL0UCENE0vl9um37h_eqO3oA=4ZkTt0hNGtGsa9gzmJ_AHFGNGCT2-sGQogSOrwdCg4RnBNfs=Bw641e3iBZt-4TpXBDvYIytf61lale=GNPAsnuY1LNQRxlEmECY-CCqVldit9HoT4TfRY4laLUyM5yaluPG9BRc1yRlMX0XVFBjAUL40ieK0OhSshyP0dXM6-aF5c7XDmc8SJvFjtkpHeMHrlkuFChwj6PsDZYOqEZIm0FU_O7NxcKiGZO-=ADwXI8kZ0LUIiAITEa-pHhQGl3J5Lr=OgkT3k2n6HsKbiRVTXpSNgfXP3RDSKO3anlnXqH8=SK8cUqQ0fqk4w8My-J_B7z__Yl3JT==iF4Eu5NyQHyVFaBp8pzzs0wMy3Lv8VBdKesyz6VHkwGGXgyAv4P60ERs0C5f50Npq-tmi1U1rrpvZhJ3HXQlq2Ua5qka=pcNVFPKXX0xhErFoKBulyvtF=TmEG58Vpj77EKZDOa4w9vbhrTAq91DebrVAYopUCQSqs2YVMkqo0bQL8d3F8rEPo3OfvURiNjNSi6B3o6KKiBA0hbgd71umhYSRe1wz9M7iuz=9RUUPtObzite070ash8lFpLZAbAOheBJB84Vy51V3d3d5bFMwppSgpOr6iIpmlDK5vE9SCvaaZZyxkT8Ad=LqE03j_=zmcylkzPDMP4AJ1z8Isqcc-n5Ein1TliwVbMeHGG3jKAeS3EasX=e6eJdGNjTtrsuzMa3gGa7iR-8dCaR9rxT_19YArgbPtu6CToEAI7c-qNOkBYeSV17QJterOuTF9ETlCdAXVI3PJrQqegjFaeHnNXxN3Van1SQS7eutCi9PeLByNkNtjDiJCCGx83oc0zob-Chf_c=iTfAod7Fat2R7huL5TJOGP8PYvhugmHdqwLU0GNukzQ_ce3LzsKAtVcMe3EJYGNZTMVDwvoVDtxzPRzJF30YeV37mJPVICuPVlJ7=dCxsLd1YqYSAZ7kqE19jeqpMQK5jo9_pJZSmbu=BDzMXp4F7AYUD99zgRNyCCHpCeHPMH91TX2bef4ruA-1aXM0jMb1mRvC4Dc5LLdmZXSzNiX7jety10-KKSI_89S8oFR6hSMnAGsTKFqeyREpkLhUL9ppZ-TsddbpQNJBHksEThxpzgp-bizHS8_ny0L4jaSlawkXl18XEqSw2yth6Ai0ZIJcI3a6K3AkXxyv485POFVbytg6CXkJ9QITL_a__ZBdNuDd-H"}',
            '_d':'d',
            'session_password':password
            }
    time.sleep(5)
    r2 = session.post('https://www.linkedin.com/checkpoint/lg/login-submit',data=data)

    print(r2.status_code, r2.url)
    for resp in r2.history:
        print (resp.status_code, resp.url)
    if r2.status != 200:
        print("Login failed")
    
    return session

def li_save_session(session):
    try:
        print("Saving session")
        with open('linkedin_cookies', 'wb') as f:
            pickle.dump(session.cookies, f)
    except:
        print("Save failed")

def li_retrieve_session():
    print("Retrieving session")
    session = requests.Session()  
    time.sleep(5)
    r = session.get('https://www.linkedin.com/login')    
    cookies = ""
    for name,value in session.cookies.items():
        cookies = cookies + name +'=' +value+';'
        # print(name,':',value)

    with open('linkedin_cookies', 'rb') as f:
        try:
            session.cookies.update(pickle.load(f))
        except:
            print("No session saved")

    return session