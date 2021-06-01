from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from us import myUsername,myPassword
def start():
    PATH = "C:\Program Files (x86)\chromedriver.exe" 
    driver = webdriver.Chrome(PATH)
    wait = WebDriverWait(driver, 10)
    driver.get("https://ocjene.skole.hr/login")
    zakljucniIzPredmeta = []
    username = driver.find_element_by_name('username')
    password = driver.find_element_by_name('password')
    username.send_keys(myUsername)
    password.send_keys(myPassword)
    password.send_keys(Keys.ENTER)
    blankL = []
    howMany = len(driver.find_elements_by_xpath(f"//a[contains(@href,'grade')]")) - 2
    def all(ki):
        i = 'grade'
        el = driver.find_elements_by_xpath(f"//a[contains(@href,'{i}')]")
        del el[0]
        del el[0]
        el[ki].click()
        dobijOcjene()

    def dobijOcjene():
        hmm = driver.find_elements_by_class_name('flex-table')
        imePredmeta = driver.find_elements_by_xpath('//*[@id="page-wrapper"]/div[4]/div[1]/div[1]/span')

        listaOcjenaIzPredmeta = []
        for  i in range(len(hmm)):
            najnovijaOcjena = hmm[i]
            yes = najnovijaOcjena.text
            if isinstance(yes, str):        # je li nadeno
                yessir = yes.split('\n')
                if (len(yessir) == 3):      # je li to dio sa ocjenama
                    ocjena = yessir[2]
                    if ocjena == "Ocjena":  # ima jedan dio ki nan ne rabi
                        pass
                    else:                   # tu ide sav kod vezan za ocjene
                        blankL.append(int(ocjena))
                        listaOcjenaIzPredmeta.append(int(ocjena))
        print(listaOcjenaIzPredmeta)
        brojOcjenaIzPredmeta = len(listaOcjenaIzPredmeta)
        prosjekOcjena = (sum(listaOcjenaIzPredmeta))/brojOcjenaIzPredmeta
        print(f"PROSJEK OCJENA IZ {(imePredmeta[0]).text} je {prosjekOcjena}")
        zakljucniIzPredmeta.append(prosjekOcjena)
        driver.back()
    for i in range(howMany-1):
        all(i)
    brojOcjena = len(blankL)
    print(brojOcjena)
    driver.quit()
if __name__ == '__main__':
    start()