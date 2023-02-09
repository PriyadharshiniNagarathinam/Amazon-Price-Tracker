import requests
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = 'madhurashree29@gmail.com'
PASSWORD = 'fxdebncnwjlbjuyj'

URL = 'https://www.amazon.com/dp/B00ESDVSTC/ref=syn_sd_onsite_desktop_243?ie=UTF8&psc=1&pd_rd_plhdr=t'
headers = {'Accept-Language': 'en-US,en;q=0.9',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
           }

response = requests.get(URL, headers=headers)
data = response.text

soup = BeautifulSoup(data, "html.parser")
price_whole = soup.find(name='span', class_='a-price-whole').getText()
price_fraction = soup.find(name='span', class_='a-price-fraction').getText()
current_price = float(price_whole + price_fraction)
target_price = 40


def send_email(price):
    title = soup.title.getText()
    message = f"{title} is now at {price}.".encode('utf-8')
    smiley = "✨🎉😎".encode('utf-8')
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs='priyaradha29@gmail.com',
                            msg=f'Subject:Amazon Price Alert!{smiley}  \n\n{message} \n\n{URL}'
                            )


if current_price < target_price:
    send_email(f'${current_price}')
