from selenium import webdriver
from time import sleep

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

home_page = "https://www.google.com"
input_text = "dcview"

driver = webdriver.Safari()
driver.get(home_page)

input_text_area = driver.find_element(By.XPATH, "//textarea[@class='gLFyf']")
input_text_area.send_keys(input_text)
sleep(1)
input_text_area.send_keys(Keys.RETURN)

sleep(5)

dcview = driver.find_element(By.XPATH, "//span[text()='DCView 二手市場']")
dcview.click()

sleep(3)

items = driver.find_elements(By.XPATH, "//tbody/tr[@class='hidden-xs']")
result = []


# def _remove_n_t(text: str):
#     result = text.replace("\n", "").replace("\t", "").replace("\xa0", " ")
#     return result


text_format = lambda text: text.replace("\n", "").replace("\t", "").replace("\xa0", " ")

for item in items:
    product_brand_element = item.find_element(By.XPATH, ".//td[1]")
    post_url_element = item.find_element(By.XPATH, ".//td[2]/a")
    buy_sell_status_element = item.find_element(By.XPATH, ".//td[2]/a/span[1]")
    item_description_element = item.find_element(By.XPATH, ".//td[2]/a/span[2]")
    item_price_element = item.find_element(By.XPATH, ".//td[3]/small[@class='price']")
    seller_name_element = item.find_element(By.XPATH, ".//td[4]//a")
    posted_date_element = item.find_element(By.XPATH, ".//td[5]/small")

    product_brand = text_format(product_brand_element.text)
    post_url = post_url_element.get_attribute("href")
    buy_sell_status = text_format(buy_sell_status_element.text)
    item_description = text_format(item_description_element.text)
    item_price = text_format(item_price_element.text)
    seller_name = text_format(seller_name_element.text)
    posted_date = text_format(posted_date_element.text)

    result.append(
        {
            "product_brand": product_brand,
            "post_url": post_url,
            "buy_sell_status": buy_sell_status,
            "item_description": item_description,
            "item_price": item_price,
            "seller_name": seller_name,
            "posted_date": posted_date,
        }
    )


driver.quit()

for i in result:
    print(i)
    print("\n")
