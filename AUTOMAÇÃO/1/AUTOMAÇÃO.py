from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get('https://ajuda.fortestecnologia.com.br/kb/article/327086/inicio?ticketId=&ticketId=&q=&q=&menuId=39108-0-327086')