
def fonk1(base_url, path_browser_driver, driver,b1):
    import time
    import pandas as pd
    from selenium import webdriver
    driver.get(base_url)
    b1 = b1
    a1 = 5
    b2 = driver.execute_script("return document.body.scrollHeight")
    print (b2)
    a2 = 0
    for p in range(0,5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(a1)
        for i in driver.find_elements_by_class_name("UFIPagerLink"):
            try:
                i.click()
                print(i)
            except Exception:
                print('yea')
        for j in driver.find_elements_by_class_name("see_more_link"):
             try:
                j.click()
                print(j)
             except Exception:
                print('yea')
        b3 = driver.execute_script("return document.body.scrollHeight")
        print(b3)
        if b3 = = b2:
            break
        b2 = b3
        a2 +=1
    b4 = driver.find_elements_by_xpath("
    b5 = []
    b6 = []
    b7 = []
    b8 = []
    b9 = []
    b10 = []
    a3 = 0
    for p in range(0,len(b4)):
        try:
            b11 = b4[p].find_element_by_css_selector("abbr._5ptz").get_attribute("title")
            b6.append(b11)
            b5.append(p)
        except:
            print('recensioni a fianco')
            a3+=1
        try:
            b12 = b4[p].find_element_by_css_selector('div._5pbx.userContent._3576').text
            b7.append(b12)
        except:
            b7.append('none')
        try:
            b13 = b4[p].find_elements_by_css_selector("a._3rwx._42ft")
            b8.append(b13[0].text)
        except IndexError:
            b8.append('none')
        try:
            b14 = b4[p].find_elements_by_css_selector("a._3dlf")
            b9.append(b14[0].text.split('\a3')[0])
        except IndexError:
            b9.append('none')
        try:
            b15 = b4[p].find_elements_by_css_selector("a._3hg-._42ft")
            b10.append(b15[0].text)
        except IndexError:
            b10.append('none')
    if len(b6)!=len(b7) and len(b6)!=len(b8):
        b16 = len(b7)-len(b6)
        b7 = b7[b16:]
        b8 = b8[b16:]
        b4 = b4[b16:]
        b9 = b9[b16:]
        b10 = b10[b16:]
    b17 = pd.DataFrame({'utente':b1,'b11':b6,'post':b7,'id post':b5,'b9':b9, 'b13': b8,'comments number':b10})
    return(b17)