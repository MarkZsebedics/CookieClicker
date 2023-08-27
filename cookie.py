from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchWindowException
 
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get("https://orteil.dashnet.org/cookieclicker/")

#Megvarjuk hogy az elemnt kattintahova valjon, aztan kattintunk
try:
    cookieOK = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME,"fc-button-label")) #html classnev alapjan valasszuk ki
    )
    cookieOK.click()
except:
	print(cookieOK)
	print(cookieOK.text)
	driver.quit()

#Megvarjuk hogy az elemnt kattintahova valjon, aztan kattintunk
try:
    language = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "langSelect-EN")) #html id alapjan valasszuk ki
    )
    language.click()
except:
	print('language')
	driver.quit()

while True:
    try:
        cookie = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "bigCookie"))
        )
        cookie.click()
    except:
        try:
            cookie = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "bigCookie"))
            )
            cookie.click()
	#Ha mar bezarodott az ablak akkor error helyett printelunk
        except NoSuchWindowException as error:
            print('Program Finished')
            break
        except:
            print('cookie')
            break
    try:
        products = driver.find_elements(By.CLASS_NAME, 'product.enabled')
        upgrades = driver.find_elements(By.CLASS_NAME,'crate.upgrade.enabled')
    except NoSuchWindowException as error:
            print('Program Finished')
            break
    try:
        for prod in products:
            prod.click()
    except NoSuchWindowException as error:
        break
    except Exception as error:
        print(error)
        
    try:
        for upg in upgrades:
            upg.click()

    except Exception as error:
        print(error)
