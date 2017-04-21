import scrapy
from flask import json

from scrapyKit.items import BusinessItem


class EleIndex(scrapy.Spider):
    name = "ele"
    allowed_domains = ["ele.me"]
    start_urls = [
        "https://mainsite-restapi.ele.me/shopping/restaurants?limit=40&offset=0&terminal=web&latitude=30.19793&longitude=120.34894",
    ]

    # 列表爬虫
    def parse(self, response):
        data = json.loads(response.body)
        items = []
        for d in data:
            item = BusinessItem(
                id=d["id"],
                name=d["name"],
                description=d["description"],
                address=d["address"],
                promotion_info=d["promotion_info"],
                image_path=d["image_path"],
                latitude=d["latitude"],
                longitude=d["longitude"],
                opening_hours=d["opening_hours"],
                phone=d["phone"],
                rating=d["rating"],
                rating_count=d["rating_count"],
                recent_order_num=d["recent_order_num"],
                mete_data=d,
            )
            items.append(item)
            # 详情抓取
            url = "https://mainsite-restapi.ele.me/shopping/v2/menu?restaurant_id=" + str(d["id"])
            yield scrapy.Request(url, self.parse_detail)
        # 广度爬 4个方向1公里裂变
        # todo
        # 列表深度爬 每个点爬100条
        # todo
        return items

    # 详情抓取
    def parse_detail(self, response):
        d = json.loads(response.body)
        return
