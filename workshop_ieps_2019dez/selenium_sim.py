import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import numpy

url = "http://tabnet.datasus.gov.br/cgi/tabcgi.exe?sim/cnv/obt10br.def"

# download chromedriver from "https://sites.google.com/a/chromium.org/chromedriver/" into your working directory.
driver = webdriver.Chrome("C:/Users/Michel/Google Drive/DOUTORADO FGV/IEPS/web_scraping_workshop/chromedriver")

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : 'C:/Users/Michel/Google Drive/DOUTORADO FGV/IEPS/web_scraping_workshop'}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.set_page_load_timeout(10)
driver.get(url)

# linha
driver.find_element_by_xpath('//*[@id="L"]/option[1]').click()
# coluna
driver.find_element_by_xpath('//*[@id="C"]/option[7]').click()
# Conteúdo
driver.find_element_by_xpath('//*[@id="I"]/option[1]').click()
driver.find_element_by_xpath('//*[@id="I"]/option[2]').click()
# Periodo
driver.find_element_by_xpath('//*[@id="A"]/option[1]').click()
driver.find_element_by_xpath('//*[@id="A"]/option[1]').click()

# CID-10
driver.find_element_by_xpath('//*[@id="fig16"]').click()
driver.find_element_by_xpath('//*[@id="S16"]/option[1]').click()
driver.find_element_by_xpath('//*[@id="S16"]/option[1851]').click()
driver.find_element_by_xpath('//*[@id="S16"]/option[1852]').click()
driver.find_element_by_xpath('//*[@id="S16"]/option[1853]').click()
driver.find_element_by_xpath('//*[@id="S16"]/option[1854]').click()
driver.find_element_by_xpath('//*[@id="S16"]/option[1855]').click()
driver.find_element_by_xpath('//*[@id="S16"]/option[1856]').click()
driver.find_element_by_xpath('//*[@id="S16"]/option[1857]').click()
driver.find_element_by_xpath('//*[@id="S16"]/option[1858]').click()
driver.find_element_by_xpath('//*[@id="S16"]/option[1859]').click()
driver.find_element_by_xpath('//*[@id="S16"]/option[1860]').click()
driver.find_element_by_xpath('//*[@id="S16"]/option[1861]').click()
driver.find_element_by_xpath('//*[@id="S16"]/option[1862]').click()
driver.find_element_by_xpath('//*[@id="S16"]/option[1863]').click()
driver.find_element_by_xpath('//*[@id="S16"]/option[1864]').click()
driver.find_element_by_xpath('//*[@id="S16"]/option[1865]').click()
driver.find_element_by_xpath('//*[@id="S16"]/option[1866]').click()
driver.find_element_by_xpath('//*[@id="S16"]/option[1867]').click()
driver.find_element_by_xpath('//*[@id="S16"]/option[1868]').click()
driver.find_element_by_xpath('//*[@id="S16"]/option[1869]').click()
driver.find_element_by_xpath('//*[@id="S16"]/option[1870]').click()
driver.find_element_by_xpath('//*[@id="S16"]/option[1871]').click()
driver.find_element_by_xpath('//*[@id="S16"]/option[1872]').click()
driver.find_element_by_xpath('//*[@id="S16"]/option[1873]').click()
driver.find_element_by_xpath('//*[@id="S16"]/option[1874]').click()
driver.find_element_by_xpath('//*[@id="S16"]/option[1875]').click()

# Mostra
driver.find_element_by_xpath('/html/body/div/div/center/div/form/div[4]/div[2]/div[2]/input[1]').click()

html = driver.page_source

driver.quit()


soup = BeautifulSoup(html, 'html.parser')

tabdados = soup.select(".tabdados tbody tr td")
tabdados = list(map(lambda node: node.get_text().strip(), tabdados))

col_tabdados = soup.select(".tabdados th")
col_tabdados = list(map(lambda node: node.get_text().strip(), col_tabdados))


# print(tabdados)
# print(col_tabdados)

len_tabdados = len(tabdados)
len_col_tabdados = len(col_tabdados)

nrow = int(len_tabdados/len_col_tabdados)
ncol = int(len_col_tabdados)

df_names = numpy.array(col_tabdados).reshape(1,ncol)
df = numpy.array(tabdados).reshape(nrow,ncol)

df = numpy.vstack([df_names, df])

numpy.savetxt("C:/Users/Michel/Google Drive/DOUTORADO FGV/IEPS/web_scraping_workshop/selenium_sim.csv", df, delimiter=",", fmt='%s')

print(df)