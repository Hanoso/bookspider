# Create your tests here.
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from baike_spider.exbookscrapy.exbookscrapy import USER_AGENT

headers = {'User_Agent': USER_AGENT}

isbn = '9787806859988'
search_rooturl = "https://book.douban.com/subject_search?search_text=&cat=1001"


class GetDetailBookUrl:

	chrome_options = Options()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--disable-gpu')
	chrome_options.add_argument('--user-agent={}'.format(USER_AGENT))
	chrome_options.add_argument("--referer={}".format(search_rooturl))
	driver = webdriver.Chrome(chrome_options=chrome_options)

	driver.get('https://book.douban.com/subject_search?search_text={}&cat=1001'.format(isbn))

	try:
		# we have to wait for the page to refresh, the last thing that seems to be updated is the title
		WebDriverWait(driver, 10).until(ec.title_contains(isbn))
		book_root = driver.find_element_by_css_selector('#root')
		WebDriverWait(driver, book_root)  # 防止页面加载不全
		soup = bs(driver.page_source, 'lxml')
		bookdetailURL = soup.select("a[class='title-text']")[0]['href']
	finally:
		driver.quit()

gdb = GetDetailBookUrl
print(gdb.bookdetailURL)