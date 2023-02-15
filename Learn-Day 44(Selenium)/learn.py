from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path=YOUR DRIVER PATH
driver=webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.com/MSI-Stealth-GS77-Gaming-Laptop/dp/B09RB9WZ2G/ref=sr_1_3?fst=as%3Aoff&pd_rd_r=2add9121-d606-49d1-8650-3bb09292ff62&pd_rd_w=b4ZwT&pd_rd_wg=vzAbr&pf_rd_p=5b7fc375-ab40-4cc0-8c62-01d4de8b648d&pf_rd_r=WW4W0RQGW1SXM4Y9DT56&qid=1676429986&refinements=p_n_feature_thirty-one_browse-bin%3A23716064011%2Cp_n_operating_system_browse-bin%3A23724789011%2Cp_n_feature_four_browse-bin%3A17927742011&rnid=676578011&s=computers-intl-ship&sr=1-3")
# # driver.find_element(By.CLASS_NAME, "a-price-whole")
# price = driver.find_element(By.CSS_SELECTOR,"span .a-price-whole")
# print(price.text)


driver.get('https://www.python.org/')
dates=driver.find_elements(By.CSS_SELECTOR, ".event-widget li time")
names=driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events={}
for n in range(len(dates)):
    events[n]={
        "time":dates[n].text,
        "name": names[n].text
    }
# driver.close() # Closes only the single tab
driver.quit()