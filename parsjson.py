import requests
from bs4 import BeautifulSoup

MAIN_URL ='https://med.kg/pressCenter/news'

USER_AGENT = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'

def open_page_url(url):
    headers = {'User-Agent': USER_AGENT}
    response = requests.get(url)
    return response.text

def analyze_page_control(content):
    soup = BeautifulSoup(content, 'lxml')
     

    try:
        list_ = soup.find('section', id= 'items').text.strip()
    except:
        list_ = ''
    try:
        date = soup.find('h6', class_ = "t-3").text.strip()
    except:
        date = ''
    
    all_info = {'date': date, 'list': list_}
    return all_info

def main():
    dv = open_page_url(MAIN_URL)
    for fd in dv:
        htm = open_page_url(MAIN_URL)
        s = analyze_page_control(htm)
        print(s)
        write_to_csv(s)
        
def write_to_csv(data):
    import json
    with open('med4.json', 'w', encoding='utf-8') as file:
        json.dump((data['date'], data['list']), file, indent=5, ensure_ascii=False)

        
        

if __name__ == '__main__':
    main()