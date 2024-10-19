from enum import Enum
from pydantic import BaseModel
from datetime import datetime


class BuySellStatus(str, Enum):
    buy = "徵"
    sell = "售"


class DcviewLensInformation(BaseModel):
    product_brand: str
    post_url: str
    buy_sell_status: str
    item_description: str
    location: str
    item_price: int
    seller_name: str
    posted_date: datetime


class DcviewWritable(Enum):
    PRODUCT_BRAND = "product_brand"
    POST_URL = "post_url"
    BUY_SELL_STATUS = "buy_sell_status"
    ITEM_DESCRIPTION = "item_description"
    LOCATION = "location"
    ITEM_PRICE = "item_price"
    SELLER_NAME = "seller_name"
    POSTED_DATE = "posted_date"
