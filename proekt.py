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
        # write_to_csv(s)
    # pages_count = 3
    # all_news_cards = []
    # for page in range(1, pages_count + 1):
    #     url = f'{MAIN_URL}page_{page}'
    #     page_content = open_page_url(url)
    #     soup = analyze_page_control(page_content)
    #     new_card = get_news_cards(soup)
    #     all_news_cards.extend(new_card)

    # total_info = []
    # for n_card in all_news_cards:
    #     new_info = analyze_page_control(n_card)
    #     total_info.append(new_info)
    # print(total_info)
    # write_to_csv(total_info)

# def get_new_info(new_card):
#     time_ = new_card.find('div', class_ = 'time')
#     time = time_.text.strip()
#     title_ = new_card.find('div', class_ = 'title')
#     title = title_.text.strip()

    # info = {
    #     'time': time,
    #     'title': title
    # }
    # return info

def write_to_csv(data):
    import csv
    with open('med4.csv', 'w', encoding='utf-8') as file:
        wr = csv.writer(file)
        wr.writerow((data['date'], data['list']))
        print(data)
# def write_to_csv(data):
#     """записывает данные в  фаил"""
#     import csv
#     with open("medinfo.csv","w",encoding='utf-8') as file:
#         writer = csv.writer(file, data['date'], data['list'])
#         writer.writeheader()
#         for i in data:
#             writer.writerow(data)

        
        

if __name__ == '__main__':
    main()