from ast import expr_context
from doctest import Example
from select import select
import sys, os
from datetime import date, datetime
import time
from time import sleep
from tokenize import Number
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import pymssql
import globalconf as GC
from pdf2image import convert_from_path
import pytesseract as pt
pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import json,urllib.request
import glob


caminho_captcha = GC.caminho_captcha
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": caminho_captcha , "download.prompt_for_download": False, "plugins.always_open_pdf_externally": True,
    })
driver = webdriver.Chrome(options=chrome_options, service=Service(GC.chrome_driver))
wait = WebDriverWait(driver, 15)
driver.get('https://wspf.banco.bradesco/wsImoveis/AreaRestrita/Default.aspx?ReturnUrl=%2fwsImoveis%2fAreaRestrita%2fConteudo%2fHome.aspx') 

img = driver.find_element(By.XPATH,'/html/body/form/div[3]/section/div/section[2]/div[2]/fieldset/div[4]/div/span[1]/img')
src = img.get_attribute('src')

# download the image
urllib.request.urlretrieve(src,"caminho_captcha.png")

sleep(5)




