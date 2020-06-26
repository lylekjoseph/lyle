from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = webdriver.Chrome(ChromeDriverManager().install())
sleep(2)
#chromedriver_path = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe')
website = 'http://www.flightcentre.co.za/holidays/search?destination_in=South+Africa/'
sleep(4)
driver.get(website)
sleep(15)

print("**************************************************************************")
t = "//div[@data-testid='Product.Name']"
title = driver.find_element_by_xpath(t)
x = "h1"
xtest = driver.find_element_by_css_selector(x)
print(title)
print(xtest)
print("**************************************************************************")

#def page_scrape():
    #sleep(30)
    #title = "//div[@data-testid='Product.Name']"

#print("##############################################################################")

"""
def load_more():
    try:
        more_results = '//a[@class = "moreButton"]'
        driver.find_element_by_xpath(more_results).click()
        # Printing these notes during the program helps me quickly check what it is doing
        print('sleeping.....')
        sleep(randint(45,60))
    except:
        pass

"""
