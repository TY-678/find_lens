import asyncio
import json
import pypika
from typing import Optional
from datetime import date, datetime
from pypika import Query, Table

from src.dao.dao_base import TableFindLens
from src.schema.find_lens_schema import DcviewWritable, BuySellStatus


class FindLensDAO:
    async def read_lens_info_from_db(
        id: Optional[int] = None,
        location: Optional[str] = None,
        buy_sell_status: Optional[BuySellStatus] = None,
        product_brand: Optional[str] = None,
        item_description: Optional[str] = None,
        item_price: Optional[int] = None,
        seller_name: Optional[str] = None,
        posted_date: Optional[date] = None,
        created_at: Optional[date] = None,
    ):
        dcview = Table("dcview")
        query = Query.from_(dcview).select("*")
        if id:
            query = query.where(dcview.id == id)
        if location:
            query = query.where(dcview.location == location)
        if buy_sell_status:
            query = query.where(dcview.buy_sell_status == buy_sell_status)
        if product_brand:
            query = query.where(dcview.product_brand == product_brand)
        if item_description:
            query = query.where(dcview.item_description == item_description)
        if item_price:
            query = query.where(dcview.item_price == item_price)
        if seller_name:
            query = query.where(dcview.seller_name == seller_name)
        if posted_date:
            query = query.where(dcview.posted_date == posted_date)
        if created_at:
            query = query.where(dcview.created_at == created_at)
        else:
            query = query.where(dcview.created_at == date.today())

        try:
            async with TableFindLens() as db:
                rt = await db.conn.fetchrow(f"{query}")
                return dict(rt)
        except Exception as e:
            raise RuntimeError(str(e))

    async def insert_lens_info_into_db(**kwargs):

        filtered_kwargs = {
            key.lower(): value
            for key, value in kwargs.items()
            if key.lower() in DcviewWritable._value2member_map_
        }
        columns = list(filtered_kwargs.keys())
        values = list(filtered_kwargs.values())

        dcview = Table("dcview")
        query = Query.into(dcview).columns(*columns).insert(*values)

        try:
            async with TableFindLens() as db:
                await db.conn.fetchrow(f"{query}")
        except Exception as e:
            raise RuntimeError(str(e))
