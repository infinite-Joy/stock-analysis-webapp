from lxml import html
import os
import time

from company_page import CompanyPage

f = open(r"G:\Python\projects\stock_analysis\stock_analysis\tests\page_content")
page_content = f.read()
tree = html.fromstring(page_content)
company = CompanyPage(tree)

def test_get_pe_ratio():
    pe_ratio = company.get_pe_ratio(tree)
    assert pe_ratio != 0.00
    assert isinstance(pe_ratio, float)
    
def test_get_eps():
    eps = company.get_eps(tree)
    assert eps != 0.00
    assert isinstance(eps, float) 
    
def test_get_price_of_stock():
    price_of_stock = company.get_price_of_stock(tree)
    assert price_of_stock != 0.00
    assert isinstance(price_of_stock, float)
    
def test_get_fifty_two_wk_high():
    fifty_two_wk_high = company.get_fifty_two_wk_high(tree)
    assert fifty_two_wk_high != 0.00
    assert isinstance(fifty_two_wk_high, float)
    
def test_get_fifty_two_wk_low():
    fifty_two_wk_low = company.get_fifty_two_wk_low(tree)
    assert fifty_two_wk_low != 0.00
    assert isinstance(fifty_two_wk_low, float)