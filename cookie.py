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

try:
    cookieOK = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME,"fc-button-label"))
    )
    cookieOK.click()
except:
	print(cookieOK)
	print(cookieOK.text)
	driver.quit()


try:
    language = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "langSelect-EN"))
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
        except NoSuchWindowException as error:
            print('Program Finished')
            break
        except:
            print('cookie')
            #driver.quit()
            break
    #elements = driver.find_elements_by_class_name('product unlocked enabled')
    try:
        products = driver.find_elements(By.CLASS_NAME, 'product.enabled')
        upgrades = driver.find_elements(By.CLASS_NAME,'crate.upgrade.enabled')
    except NoSuchWindowException as error:
            print('Program Finished')
            break
    try:
        for prod in products:
            #print(prod)
            prod.click()
    except NoSuchWindowException as error:
        break
    except Exception as error:
        print(error)
        
    try:
        for upg in upgrades:
            #print(prod)
            upg.click()

    except NoSu as error:
        print(error)
        
        

    
        
    




#cookie.click()