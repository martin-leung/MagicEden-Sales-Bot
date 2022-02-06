from selenium import webdriver
import threading
from config import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, API_KEY, API_SECRET_KEY
from cryptography.fernet import Fernet
import tweepy 
import config 

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    #need user agent because of captcha that pops up as result
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    options.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Chrome(executable_path='C:\\Users\\Martin Leung\\Desktop\\TwitterBot\\chromedriver.exe', chrome_options=options)
    return driver

def main():
    driver = setup_driver()

    # url = 'https://magiceden.io/marketplace/fancy_diamonds'
    market_place = 'https://magiceden.io/marketplace/infinity_serpents'

    solana_url = 'https://coinmarketcap.com/currencies/solana/'

    driver.get(market_place)
    driver.implicitly_wait(3)

    driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/span[2]').click()
    nft_name = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/table/tbody/tr[1]/td[2]/a').text
    sale_price = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/table/tbody/tr[1]/td[6]').text

    driver.get(solana_url)
    driver.implicitly_wait(3)
    current_sol_price = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span').text
    
    driver.quit()


    calculate_price(nft_name, sale_price, current_sol_price)
    
def calculate_price(nft_name, sale_price, current_sol_price):
    print("Name: " + nft_name)
    print("Price: " + sale_price)

    final_price = (float(current_sol_price.strip("$")) * float(sale_price.strip("SOL")))

    print("Total Cost: $" + str(final_price))

    tweetSales(nft_name, sale_price, str(round(final_price,2)))


def tweetSales(nft_name, sale_price, final_price):

    client = tweepy.Client(
        consumer_key = decryptConfig(config.API_KEY),
        consumer_secret = decryptConfig(config.API_SECRET_KEY),
        access_token = decryptConfig(config.ACCESS_TOKEN),
        access_token_secret = decryptConfig(config.ACCESS_TOKEN_SECRET)
        )

    #need to add image and other info/formatiting
    response = client.create_tweet(text=nft_name + " sold for " + sale_price + ". \nTotal USD: $" + final_price)

def decryptConfig(value):
    f = Fernet(config.FERNET_KEY)
    return f.decrypt(value)

if __name__ == "__main__":
    #running every 5 seconds
    # while True:
    #     threading.Timer(5.0, main()).start()
    main()