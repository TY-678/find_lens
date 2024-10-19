import asyncio
from datetime import date
from src.get_lens_info.get_lens import GetLensInfo


from src.dao.get_lens_dao import FindLensDAO


async def main():
    get_lens_info = GetLensInfo()
    get_lens_info.get_lens_inpage()
    rt = get_lens_info.ggg()
    get_lens_info.clear_result()
    get_lens_info.close_safari()

    task = [
        FindLensDAO.insert_lens_info_into_db(
            product_brand=case["product_brand"],
            post_url=case["post_url"],
            buy_sell_status=case["buy_sell_status"],
            item_description=case["item_description"],
            location=case["location"],
            item_price=case["item_price"],
            seller_name=case["seller_name"],
            posted_date=case["posted_date"],
        )
        for case in rt
    ]
    await asyncio.gather(*task)


asyncio.run(main())
