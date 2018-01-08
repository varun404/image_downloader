import os, json
import urllib
import requests
import time
from selenium import webdriver
import sys
from selenium.webdriver.common.keys import Keys
import webbrowser


# os.environ["PATH"] += os.pathsep + os.getcwd()

def main():
    content = sys.argv[1]
    content.replace('', '+')
    no_images = int(sys.argv[2])
    number_scrolls = no_images / 100 + 1
    path = 'C:\Python27/abcdownload'

    if not os.path.exists(path):
        os.mkdir(path)

    url = "https://www.google.co.in/search?q=" + content + "&rlz=1C1ASRW_enIN750IN750&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj9y8-RtsjYAhWLYo8KHTP9BZYQ_AUICygC&biw=1745&bih=841"
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
    driver = webdriver.chrome('C:\Program Files (x86)\Google\Chrome\Application\chrome')
    # driver.open(driver+url)
    #while(no_images>0):
    #   driver.find_element_by_xpath('// * [ @ id = "rg_s"] / div[i] / a / img').click()
    #    no_images+=1
    extensons = ['jpg', 'jpeg', 'png']
    img_count = 0
    downloaded_images = 0

    for _ in xrange(number_scrolls):
        for _ in xrange(10):
            driver.execute_script("window.scrollBy(0,1000)")
            time.sleep(1)
        try:
            driver.find_element_by_xpath("//input[@value='Show more results']").click()
        except Exception as e:
            print (str(e))

    images = driver.find_element_by_xpath('//div[contains(@class,"rg_meta")]')
    for img in images:
        no_images += 1
        img_url = json.loads(img.get_attribute('innerHTML'))['ou']
        img_type = json.loads(img.get_attribute('innerHTML'))['ity']
        print "Image ", img_count, " is being downloaded from ", img_url
        try:
            if img_type not in extensons:
                continue
            else:
                req = requests.get(img_url, headers=headers)
                raw_image = urllib.urlopen(req).read()
                f = open(path + img_type, 'w')
                f.write(raw_image)
                downloaded_images += 1
        except Exception as e:
            print(str(e) + ' is why you cannot download image')

        if downloaded_images > no_images:
            break
        driver.quit()


main()













