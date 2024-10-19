import asyncio

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ..util import tool

try:
    web_info = tool.read_data_from_yaml("src/get_lens_info/target.yaml")
    web_elements = tool.read_data_from_yaml("src/get_lens_info/web_element.yaml")
except Exception as e:
    raise RuntimeError(f"read yaml data tailed, {str(e)}")


class GetLensInfo:

    def __init__(self):
        self.lens_info = []
        self.driver = webdriver.Safari()
        self.driver.get(web_info["web_information"]["home_page"])

    def clear_result(self):
        self.lens_info = []

    def close_safari(self):
        self.driver.quit()

    def ggg(self):
        return self.lens_info

    def get_lens_inpage(self):

        sleep(5)
        items = self.driver.find_elements(By.XPATH, web_elements["xpath"]["items"])
        for item in items:
            product_brand_element = item.find_element(
                By.XPATH, web_elements["xpath"]["product_brand_element"]
            )
            post_url_element = item.find_element(
                By.XPATH, web_elements["xpath"]["post_url_element"]
            )

            try:
                buy_sell_status_element = item.find_element(
                    By.XPATH, web_elements["xpath"]["sell_status_element"]
                )
            except:
                buy_sell_status_element = item.find_element(
                    By.XPATH, web_elements["xpath"]["buy_status_element"]
                )

            item_description_element = item.find_element(
                By.XPATH, web_elements["xpath"]["item_description_element"]
            )
            item_price_element = item.find_element(
                By.XPATH, web_elements["xpath"]["item_price_element"]
            )
            seller_name_element = item.find_element(
                By.XPATH, web_elements["xpath"]["seller_name_element"]
            )
            posted_date_element = item.find_element(
                By.XPATH, web_elements["xpath"]["posted_date_element"]
            )

            product_brand = self.format_text(product_brand_element.text)
            post_url = post_url_element.get_attribute("href")
            buy_sell_status = self.format_text(buy_sell_status_element.text)
            item_description = self.format_text(item_description_element.text)
            location = item_description[: (item_description.index("]") + 1)]
            description = item_description[(item_description.index("]") + 1) :]
            item_price = self.format_price(item_price_element.text)
            seller_name = self.format_text(seller_name_element.text)
            posted_date = self.format_text(posted_date_element.text)

            self.lens_info.append(
                {
                    "product_brand": product_brand,
                    "post_url": post_url,
                    "buy_sell_status": buy_sell_status,
                    "item_description": description,
                    "location": location,
                    "item_price": item_price,
                    "seller_name": seller_name,
                    "posted_date": posted_date,
                }
            )

    def format_text(self, text: str) -> str:
        formatted_text = text.replace("\n", "").replace("\t", "").replace("\xa0", " ")
        return formatted_text

    def format_price(xelf, price: str) -> int:
        formatted_price = int(price.replace(",", ""))
        return formatted_price
