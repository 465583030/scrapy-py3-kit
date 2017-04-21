# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BusinessItem(scrapy.Item):
    # 商家Id
    id = scrapy.Field()
    # 店铺图片
    albums = scrapy.Field()
    # 口味
    flavors = scrapy.Field()
    # 商家名称
    name = scrapy.Field()
    # 介绍
    description = scrapy.Field()
    # 详细介绍
    promotion_info = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 活动
    activities = scrapy.Field()
    # 图片
    image_path = scrapy.Field()
    # 纬度
    latitude = scrapy.Field()
    # 经度
    longitude = scrapy.Field()
    # 营业时间
    opening_hours = scrapy.Field()
    # 手机
    phone = scrapy.Field()
    # 评分
    rating = scrapy.Field()
    # 评级
    rating_count = scrapy.Field()
    # 最近订单数
    recent_order_num = scrapy.Field()
    # 原始信息
    mete_data = scrapy.Field()
