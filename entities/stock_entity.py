# coding=utf-8

from marshmallow import Schema, fields

from sqlalchemy import Column, String, Date

from .entity import Entity, EntityNews, Base

class StockSchema(Schema):
    date = fields.String()
    price = fields.Number()
    change = fields.Number()
    changepercent = fields.Number()

class NewsSchema(Schema):
    title = fields.String()
    image = fields.String()
    site = fields.String()
    text = fields.String()
    url = fields.String()

class aapl_table(Entity, Base):
    __tablename__ = 'aapl_stock'

    date = Column(Date, primary_key=True)
    price = Column(String)
    change = Column(String)
    changepercent = Column(String)

    def __init__(self, date, price, change, changepercent, created_by):
        Entity.__init__(self, created_by)
        self.date = date
        self.price = price
        self.change = change
        self.changepercent = changepercent
class amgn_table(Entity, Base):
    __tablename__ = 'amgn_stock'

    date = Column(Date, primary_key=True)
    price = Column(String)
    change = Column(String)
    changepercent = Column(String)

    def __init__(self, date, price, change, changepercent, created_by):
        Entity.__init__(self, created_by)
        self.date = date
        self.price = price
        self.change = change
        self.changepercent = changepercent
class axp_table(Entity, Base):
    __tablename__ = 'axp_stock'

    date = Column(Date, primary_key=True)
    price = Column(String)
    change = Column(String)
    changepercent = Column(String)

    def __init__(self, date, price, change, changepercent, created_by):
        Entity.__init__(self, created_by)
        self.date = date
        self.price = price
        self.change = change
        self.changepercent = changepercent
class ba_table(Entity, Base):
    __tablename__ = 'ba_stock'

    date = Column(Date, primary_key=True)
    price = Column(String)
    change = Column(String)
    changepercent = Column(String)

    def __init__(self, date, price, change, changepercent, created_by):
        Entity.__init__(self, created_by)
        self.date = date
        self.price = price
        self.change = change
        self.changepercent = changepercent
class cat_table(Entity, Base):
    __tablename__ = 'cat_stock'

    date = Column(Date, primary_key=True)
    price = Column(String)
    change = Column(String)
    changepercent = Column(String)

    def __init__(self, date, price, change, changepercent, created_by):
        Entity.__init__(self, created_by)
        self.date = date
        self.price = price
        self.change = change
        self.changepercent = changepercent
class crm_table(Entity, Base):
    __tablename__ = 'crm_stock'

    date = Column(Date, primary_key=True)
    price = Column(String)
    change = Column(String)
    changepercent = Column(String)

    def __init__(self, date, price, change, changepercent, created_by):
        Entity.__init__(self, created_by)
        self.date = date
        self.price = price
        self.change = change
        self.changepercent = changepercent   
class csco_table(Entity, Base):
    __tablename__ = 'csco_stock'

    date = Column(Date, primary_key=True)
    price = Column(String)
    change = Column(String)
    changepercent = Column(String)

    def __init__(self, date, price, change, changepercent, created_by):
        Entity.__init__(self, created_by)
        self.date = date
        self.price = price
        self.change = change
        self.changepercent = changepercent
class cvx_table(Entity, Base):
    __tablename__ = 'cvx_stock'

    date = Column(Date, primary_key=True)
    price = Column(String)
    change = Column(String)
    changepercent = Column(String)

    def __init__(self, date, price, change, changepercent, created_by):
        Entity.__init__(self, created_by)
        self.date = date
        self.price = price
        self.change = change
        self.changepercent = changepercent
class dis_table(Entity, Base):
    __tablename__ = 'dis_stock'

    date = Column(Date, primary_key=True)
    price = Column(String)
    change = Column(String)
    changepercent = Column(String)

    def __init__(self, date, price, change, changepercent, created_by):
        Entity.__init__(self, created_by)
        self.date = date
        self.price = price
        self.change = change
        self.changepercent = changepercent
class dow_table(Entity, Base):
    __tablename__ = 'dow_stock'

    date = Column(Date, primary_key=True)
    price = Column(String)
    change = Column(String)
    changepercent = Column(String)

    def __init__(self, date, price, change, changepercent, created_by):
        Entity.__init__(self, created_by)
        self.date = date
        self.price = price
        self.change = change
        self.changepercent = changepercent
class gs_table(Entity, Base):
    __tablename__ = 'gs_stock'

    date = Column(Date, primary_key=True)
    price = Column(String)
    change = Column(String)
    changepercent = Column(String)

    def __init__(self, date, price, change, changepercent, created_by):
        Entity.__init__(self, created_by)
        self.date = date
        self.price = price
        self.change = change
        self.changepercent = changepercent
class hd_table(Entity, Base):
    __tablename__ = 'hd_stock'

    date = Column(Date, primary_key=True)
    price = Column(String)
    change = Column(String)
    changepercent = Column(String)

    def __init__(self, date, price, change, changepercent, created_by):
        Entity.__init__(self, created_by)
        self.date = date
        self.price = price
        self.change = change
        self.changepercent = changepercent
class hon_table(Entity, Base):
    __tablename__ = 'hon_stock'

    date = Column(Date, primary_key=True)
    price = Column(String)
    change = Column(String)
    changepercent = Column(String)

    def __init__(self, date, price, change, changepercent, created_by):
        Entity.__init__(self, created_by)
        self.date = date
        self.price = price
        self.change = change
        self.changepercent = changepercent
class ibm_table(Entity, Base):
    __tablename__ = 'ibm_stock'

    date = Column(Date, primary_key=True)
    price = Column(String)
    change = Column(String)
    changepercent = Column(String)

    def __init__(self, date, price, change, changepercent, created_by):
        Entity.__init__(self, created_by)
        self.date = date
        self.price = price
        self.change = change
        self.changepercent = changepercent
class intc_table(Entity, Base):
    __tablename__ = 'intc_stock'

    date = Column(Date, primary_key=True)
    price = Column(String)
    change = Column(String)
    changepercent = Column(String)

    def __init__(self, date, price, change, changepercent, created_by):
        Entity.__init__(self, created_by)
        self.date = date
        self.price = price
        self.change = change
        self.changepercent = changepercent
class jnj_table(Entity, Base):
    __tablename__ = 'jnj_stock'

    date = Column(Date, primary_key=True)
    price = Column(String)
    change = Column(String)
    changepercent = Column(String)

    def __init__(self, date, price, change, changepercent, created_by):
        Entity.__init__(self, created_by)
        self.date = date
        self.price = price
        self.change = change
        self.changepercent = changepercent
class jpm_table(Entity, Base):
    __tablename__ = 'jpm_stock'

    date = Column(Date, primary_key=True)
    price = Column(String)
    change = Column(String)
    changepercent = Column(String)

    def __init__(self, date, price, change, changepercent, created_by):
        Entity.__init__(self, created_by)
        self.date = date
        self.price = price
        self.change = change
        self.changepercent = changepercent
class ko_table(Entity, Base):
    __tablename__ = 'ko_stock'

    date = Column(Date, primary_key=True)
    price = Column(String)
    change = Column(String)
    changepercent = Column(String)

    def __init__(self, date, price, change, changepercent, created_by):
        Entity.__init__(self, created_by)
        self.date = date
        self.price = price
        self.change = change
        self.changepercent = changepercent
class mcd_table(Entity, Base):
    __tablename__ = 'mcd_stock'

    date = Column(Date, primary_key=True)
    price = Column(String)
    change = Column(String)
    changepercent = Column(String)

    def __init__(self, date, price, change, changepercent, created_by):
        Entity.__init__(self, created_by)
        self.date = date
        self.price = price
        self.change = change
        self.changepercent = changepercent
class mmm_table(Entity, Base):
    __tablename__ = 'mmm_stock'

    date = Column(Date, primary_key=True)
    price = Column(String)
    change = Column(String)
    changepercent = Column(String)

    def __init__(self, date, price, change, changepercent, created_by):
        Entity.__init__(self, created_by)
        self.date = date
        self.price = price
        self.change = change
        self.changepercent = changepercent
class mrk_table(Entity, Base):
    __tablename__ = 'mrk_stock'

    date = Column(Date, primary_key=True)
    price = Column(String)
    change = Column(String)
    changepercent = Column(String)

    def __init__(self, date, price, change, changepercent, created_by):
        Entity.__init__(self, created_by)
        self.date = date
        self.price = price
        self.change = change
        self.changepercent = changepercent
class msft_table(Entity, Base):
    __tablename__ = 'msft_stock'

    date = Column(Date, primary_key=True)
    price = Column(String)
    change = Column(String)
    changepercent = Column(String)

    def __init__(self, date, price, change, changepercent, created_by):
        Entity.__init__(self, created_by)
        self.date = date
        self.price = price
        self.change = change
        self.changepercent = changepercent
class nke_table(Entity, Base):
    __tablename__ = 'nke_stock'

    date = Column(Date, primary_key=True)
    price = Column(String)
    change = Column(String)
    changepercent = Column(String)

    def __init__(self, date, price, change, changepercent, created_by):
        Entity.__init__(self, created_by)
        self.date = date
        self.price = price
        self.change = change
        self.changepercent = changepercent
class pg_table(Entity, Base):
    __tablename__ = 'pg_stock'

    date = Column(Date, primary_key=True)
    price = Column(String)
    change = Column(String)
    changepercent = Column(String)

    def __init__(self, date, price, change, changepercent, created_by):
        Entity.__init__(self, created_by)
        self.date = date
        self.price = price
        self.change = change
        self.changepercent = changepercent
class trv_table(Entity, Base):
    __tablename__ = 'trv_stock'

    date = Column(Date, primary_key=True)
    price = Column(String)
    change = Column(String)
    changepercent = Column(String)

    def __init__(self, date, price, change, changepercent, created_by):
        Entity.__init__(self, created_by)
        self.date = date
        self.price = price
        self.change = change
        self.changepercent = changepercent
class unh_table(Entity, Base):
    __tablename__ = 'unh_stock'

    date = Column(Date, primary_key=True)
    price = Column(String)
    change = Column(String)
    changepercent = Column(String)

    def __init__(self, date, price, change, changepercent, created_by):
        Entity.__init__(self, created_by)
        self.date = date
        self.price = price
        self.change = change
        self.changepercent = changepercent
class v_table(Entity, Base):
    __tablename__ = 'v_stock'

    date = Column(Date, primary_key=True)
    price = Column(String)
    change = Column(String)
    changepercent = Column(String)

    def __init__(self, date, price, change, changepercent, created_by):
        Entity.__init__(self, created_by)
        self.date = date
        self.price = price
        self.change = change
        self.changepercent = changepercent
class vz_table(Entity, Base):
    __tablename__ = 'vz_stock'

    date = Column(Date, primary_key=True)
    price = Column(String)
    change = Column(String)
    changepercent = Column(String)

    def __init__(self, date, price, change, changepercent, created_by):
        Entity.__init__(self, created_by)
        self.date = date
        self.price = price
        self.change = change
        self.changepercent = changepercent
class wba_table(Entity, Base):
    __tablename__ = 'wba_stock'

    date = Column(Date, primary_key=True)
    price = Column(String)
    change = Column(String)
    changepercent = Column(String)

    def __init__(self, date, price, change, changepercent, created_by):
        Entity.__init__(self, created_by)
        self.date = date
        self.price = price
        self.change = change
        self.changepercent = changepercent
class wmt_table(Entity, Base):
    __tablename__ = 'wmt_stock'

    date = Column(Date, primary_key=True)
    price = Column(String)
    change = Column(String)
    changepercent = Column(String)

    def __init__(self, date, price, change, changepercent, created_by):
        Entity.__init__(self, created_by)
        self.date = date
        self.price = price
        self.change = change
        self.changepercent = changepercent
        
##############################################

class aapl_news_table(EntityNews, Base):
    __tablename__ = 'aapl_news'

    title = Column(String, primary_key=True)
    image = Column(String)
    site = Column(String)
    text = Column(String)
    url = Column(String)

    def __init__(self, title, image, site, text, url, created_by):
        EntityNews.__init__(self, created_by)
        self.title = title
        self.image = image
        self.site = site
        self.text = text
        self.url = url

class amgn_news_table(EntityNews, Base):
    __tablename__ = 'amgn_news'

    title = Column(String, primary_key=True)
    image = Column(String)
    site = Column(String)
    text = Column(String)
    url = Column(String)

    def __init__(self, title, image, site, text, url, created_by):
        EntityNews.__init__(self, created_by)
        self.title = title
        self.image = image
        self.site = site
        self.text = text
        self.url = url

class axp_news_table(EntityNews, Base):
    __tablename__ = 'axp_news'

    title = Column(String, primary_key=True)
    image = Column(String)
    site = Column(String)
    text = Column(String)
    url = Column(String)

    def __init__(self, title, image, site, text, url, created_by):
        EntityNews.__init__(self, created_by)
        self.title = title
        self.image = image
        self.site = site
        self.text = text
        self.url = url

class ba_news_table(EntityNews, Base):
    __tablename__ = 'ba_news'

    title = Column(String, primary_key=True)
    image = Column(String)
    site = Column(String)
    text = Column(String)
    url = Column(String)

    def __init__(self, title, image, site, text, url, created_by):
        EntityNews.__init__(self, created_by)
        self.title = title
        self.image = image
        self.site = site
        self.text = text
        self.url = url

class cat_news_table(EntityNews, Base):
    __tablename__ = 'cat_news'

    title = Column(String, primary_key=True)
    image = Column(String)
    site = Column(String)
    text = Column(String)
    url = Column(String)

    def __init__(self, title, image, site, text, url, created_by):
        EntityNews.__init__(self, created_by)
        self.title = title
        self.image = image
        self.site = site
        self.text = text
        self.url = url

class crm_news_table(EntityNews, Base):
    __tablename__ = 'crm_news'

    title = Column(String, primary_key=True)
    image = Column(String)
    site = Column(String)
    text = Column(String)
    url = Column(String)

    def __init__(self, title, image, site, text, url, created_by):
        EntityNews.__init__(self, created_by)
        self.title = title
        self.image = image
        self.site = site
        self.text = text
        self.url = url

class csco_news_table(EntityNews, Base):
    __tablename__ = 'csco_news'

    title = Column(String, primary_key=True)
    image = Column(String)
    site = Column(String)
    text = Column(String)
    url = Column(String)

    def __init__(self, title, image, site, text, url, created_by):
        EntityNews.__init__(self, created_by)
        self.title = title
        self.image = image
        self.site = site
        self.text = text
        self.url = url

class cvx_news_table(EntityNews, Base):
    __tablename__ = 'cvx_news'

    title = Column(String, primary_key=True)
    image = Column(String)
    site = Column(String)
    text = Column(String)
    url = Column(String)

    def __init__(self, title, image, site, text, url, created_by):
        EntityNews.__init__(self, created_by)
        self.title = title
        self.image = image
        self.site = site
        self.text = text
        self.url = url

class dis_news_table(EntityNews, Base):
    __tablename__ = 'dis_news'

    title = Column(String, primary_key=True)
    image = Column(String)
    site = Column(String)
    text = Column(String)
    url = Column(String)

    def __init__(self, title, image, site, text, url, created_by):
        EntityNews.__init__(self, created_by)
        self.title = title
        self.image = image
        self.site = site
        self.text = text
        self.url = url

class dow_news_table(EntityNews, Base):
    __tablename__ = 'dow_news'

    title = Column(String, primary_key=True)
    image = Column(String)
    site = Column(String)
    text = Column(String)
    url = Column(String)

    def __init__(self, title, image, site, text, url, created_by):
        EntityNews.__init__(self, created_by)
        self.title = title
        self.image = image
        self.site = site
        self.text = text
        self.url = url

class gs_news_table(EntityNews, Base):
    __tablename__ = 'gs_news'

    title = Column(String, primary_key=True)
    image = Column(String)
    site = Column(String)
    text = Column(String)
    url = Column(String)

    def __init__(self, title, image, site, text, url, created_by):
        EntityNews.__init__(self, created_by)
        self.title = title
        self.image = image
        self.site = site
        self.text = text
        self.url = url

class hd_news_table(EntityNews, Base):
    __tablename__ = 'hd_news'

    title = Column(String, primary_key=True)
    image = Column(String)
    site = Column(String)
    text = Column(String)
    url = Column(String)

    def __init__(self, title, image, site, text, url, created_by):
        EntityNews.__init__(self, created_by)
        self.title = title
        self.image = image
        self.site = site
        self.text = text
        self.url = url

class hon_news_table(EntityNews, Base):
    __tablename__ = 'hon_news'

    title = Column(String, primary_key=True)
    image = Column(String)
    site = Column(String)
    text = Column(String)
    url = Column(String)

    def __init__(self, title, image, site, text, url, created_by):
        EntityNews.__init__(self, created_by)
        self.title = title
        self.image = image
        self.site = site
        self.text = text
        self.url = url

class ibm_news_table(EntityNews, Base):
    __tablename__ = 'ibm_news'

    title = Column(String, primary_key=True)
    image = Column(String)
    site = Column(String)
    text = Column(String)
    url = Column(String)

    def __init__(self, title, image, site, text, url, created_by):
        EntityNews.__init__(self, created_by)
        self.title = title
        self.image = image
        self.site = site
        self.text = text
        self.url = url

class intc_news_table(EntityNews, Base):
    __tablename__ = 'intc_news'

    title = Column(String, primary_key=True)
    image = Column(String)
    site = Column(String)
    text = Column(String)
    url = Column(String)

    def __init__(self, title, image, site, text, url, created_by):
        EntityNews.__init__(self, created_by)
        self.title = title
        self.image = image
        self.site = site
        self.text = text
        self.url = url

class jnj_news_table(EntityNews, Base):
    __tablename__ = 'jnj_news'

    title = Column(String, primary_key=True)
    image = Column(String)
    site = Column(String)
    text = Column(String)
    url = Column(String)

    def __init__(self, title, image, site, text, url, created_by):
        EntityNews.__init__(self, created_by)
        self.title = title
        self.image = image
        self.site = site
        self.text = text
        self.url = url

class jpm_news_table(EntityNews, Base):
    __tablename__ = 'jpm_news'

    title = Column(String, primary_key=True)
    image = Column(String)
    site = Column(String)
    text = Column(String)
    url = Column(String)

    def __init__(self, title, image, site, text, url, created_by):
        EntityNews.__init__(self, created_by)
        self.title = title
        self.image = image
        self.site = site
        self.text = text
        self.url = url

class ko_news_table(EntityNews, Base):
    __tablename__ = 'ko_news'

    title = Column(String, primary_key=True)
    image = Column(String)
    site = Column(String)
    text = Column(String)
    url = Column(String)

    def __init__(self, title, image, site, text, url, created_by):
        EntityNews.__init__(self, created_by)
        self.title = title
        self.image = image
        self.site = site
        self.text = text
        self.url = url

class mcd_news_table(EntityNews, Base):
    __tablename__ = 'mcd_news'

    title = Column(String, primary_key=True)
    image = Column(String)
    site = Column(String)
    text = Column(String)
    url = Column(String)

    def __init__(self, title, image, site, text, url, created_by):
        EntityNews.__init__(self, created_by)
        self.title = title
        self.image = image
        self.site = site
        self.text = text
        self.url = url

class mmm_news_table(EntityNews, Base):
    __tablename__ = 'mmm_news'

    title = Column(String, primary_key=True)
    image = Column(String)
    site = Column(String)
    text = Column(String)
    url = Column(String)

    def __init__(self, title, image, site, text, url, created_by):
        EntityNews.__init__(self, created_by)
        self.title = title
        self.image = image
        self.site = site
        self.text = text
        self.url = url

class mrk_news_table(EntityNews, Base):
    __tablename__ = 'mrk_news'

    title = Column(String, primary_key=True)
    image = Column(String)
    site = Column(String)
    text = Column(String)
    url = Column(String)

    def __init__(self, title, image, site, text, url, created_by):
        EntityNews.__init__(self, created_by)
        self.title = title
        self.image = image
        self.site = site
        self.text = text
        self.url = url

class msft_news_table(EntityNews, Base):
    __tablename__ = 'msft_news'

    title = Column(String, primary_key=True)
    image = Column(String)
    site = Column(String)
    text = Column(String)
    url = Column(String)

    def __init__(self, title, image, site, text, url, created_by):
        EntityNews.__init__(self, created_by)
        self.title = title
        self.image = image
        self.site = site
        self.text = text
        self.url = url

class nke_news_table(EntityNews, Base):
    __tablename__ = 'nke_news'

    title = Column(String, primary_key=True)
    image = Column(String)
    site = Column(String)
    text = Column(String)
    url = Column(String)

    def __init__(self, title, image, site, text, url, created_by):
        EntityNews.__init__(self, created_by)
        self.title = title
        self.image = image
        self.site = site
        self.text = text
        self.url = url

class pg_news_table(EntityNews, Base):
    __tablename__ = 'pg_news'

    title = Column(String, primary_key=True)
    image = Column(String)
    site = Column(String)
    text = Column(String)
    url = Column(String)

    def __init__(self, title, image, site, text, url, created_by):
        EntityNews.__init__(self, created_by)
        self.title = title
        self.image = image
        self.site = site
        self.text = text
        self.url = url

class trv_news_table(EntityNews, Base):
    __tablename__ = 'trv_news'

    title = Column(String, primary_key=True)
    image = Column(String)
    site = Column(String)
    text = Column(String)
    url = Column(String)

    def __init__(self, title, image, site, text, url, created_by):
        EntityNews.__init__(self, created_by)
        self.title = title
        self.image = image
        self.site = site
        self.text = text
        self.url = url

class unh_news_table(EntityNews, Base):
    __tablename__ = 'unh_news'

    title = Column(String, primary_key=True)
    image = Column(String)
    site = Column(String)
    text = Column(String)
    url = Column(String)

    def __init__(self, title, image, site, text, url, created_by):
        EntityNews.__init__(self, created_by)
        self.title = title
        self.image = image
        self.site = site
        self.text = text
        self.url = url

class v_news_table(EntityNews, Base):
    __tablename__ = 'v_news'

    title = Column(String, primary_key=True)
    image = Column(String)
    site = Column(String)
    text = Column(String)
    url = Column(String)

    def __init__(self, title, image, site, text, url, created_by):
        EntityNews.__init__(self, created_by)
        self.title = title
        self.image = image
        self.site = site
        self.text = text
        self.url = url

class vz_news_table(EntityNews, Base):
    __tablename__ = 'vz_news'

    title = Column(String, primary_key=True)
    image = Column(String)
    site = Column(String)
    text = Column(String)
    url = Column(String)

    def __init__(self, title, image, site, text, url, created_by):
        EntityNews.__init__(self, created_by)
        self.title = title
        self.image = image
        self.site = site
        self.text = text
        self.url = url

class wba_news_table(EntityNews, Base):
    __tablename__ = 'wba_news'

    title = Column(String, primary_key=True)
    image = Column(String)
    site = Column(String)
    text = Column(String)
    url = Column(String)

    def __init__(self, title, image, site, text, url, created_by):
        EntityNews.__init__(self, created_by)
        self.title = title
        self.image = image
        self.site = site
        self.text = text
        self.url = url

class wmt_news_table(EntityNews, Base):
    __tablename__ = 'wmt_news'

    title = Column(String, primary_key=True)
    image = Column(String)
    site = Column(String)
    text = Column(String)
    url = Column(String)

    def __init__(self, title, image, site, text, url, created_by):
        EntityNews.__init__(self, created_by)
        self.title = title
        self.image = image
        self.site = site
        self.text = text
        self.url = url
