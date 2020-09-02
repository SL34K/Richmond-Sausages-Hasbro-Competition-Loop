import requests, time, json,re
import random, string
from bs4 import BeautifulSoup
import imaplib
names = ['first','another first name','Mr First','First.']#I put here mine and family members names to ensure parcels would turn up
last = ['surname','surname.']#Put surnames here in different formats to try and randomise entries
proxies = {'http': 'http://',
           'https': 'https://'}
def main():
    session = requests.Session()
    #session.proxies = proxies
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
    x = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(9))
    x = ''.join(random.choice(string.ascii_uppercase)+random.choice(string.ascii_uppercase)+random.choice(string.ascii_uppercase)+random.choice(string.digits)+random.choice(string.ascii_uppercase)+random.choice(string.ascii_uppercase)+random.choice(string.ascii_uppercase)+random.choice(string.digits)+random.choice(string.ascii_uppercase)+random.choice(string.ascii_uppercase)+random.choice(string.ascii_uppercase)+random.choice(string.digits))
    print(x)
    code = x
    email = x+'@gmail.com'
    load = {
        'action': 'entry_check',
        'unique_code': code,
        'email': email,
        'terms_age': 'true',
        'hasbro': 'false',
        'richmond': 'false'}
    url = 'https://competitions.richmondsausages.co.uk/wp-admin/admin-ajax.php'
    post = session.post(url,load)
    data =json.loads(post.text)
    address = "Housename, Flat {}"#Had my housename and then a random flat number to "jig" address
    pickaddy = address.format(random.randrange(30))
    payload = {
        '_wpcf7': '13',
        '_wpcf7_version': '5.1.4',
        '_wpcf7_locale': 'en_US',
        '_wpcf7_unit_tag': 'wpcf7-f13-o1',
        '_wpcf7_container_post': '0',
        'unique-code': code,
        'your-email': email,
        'AgeVerification': '1',
        'first-name': random.choice(names),
        'surname': random.choice(last),
        'houseno': pickaddy,
        'street': '',#Removed street for obvious reasons
        'Postcode': '',#Removed postcode for obvious reasons
        'prize': random.randrange(1,4),
        'winning_moment':'',
        }
    time.sleep(5)
    post = session.post('https://competitions.richmondsausages.co.uk/wp-json/contact-form-7/v1/contact-forms/13/feedback',data=payload)
    test=session.get('https://competitions.richmondsausages.co.uk/success')
    print("Success!") 
while True:
    try:
        main()
        time.sleep(21600)
    except:
        print("Error")
