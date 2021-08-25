from selenium import webdriver
from time import sleep
import random
'''
    If you have a problem with geckodriver 
    1.Install geckodriver from this link https://github.com/mozilla/geckodriver/releases
    2.
    For Windows:
    https://stackoverflow.com/questions/42524114/how-to-install-geckodriver-on-a-windows-system
    For Linux:
    https://askubuntu.com/questions/870530/how-to-install-geckodriver-in-ubuntu
    For MacOS:
    https://www.kenst.com/2016/12/installing-marionette-firefoxdriver-on-mac-osx/
'''


class Bot:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path='C:/geckodriver.exe')
        self.navigate()

    def navigate(self):
        self.driver.get('https://www.amazon.com/dp/B09BQSBQ6H/ref=s9_acsd_al_bw_c2_x_0_t?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-11&pf_rd_r=4TX9PPV5A48H9AX8CQFE&pf_rd_t=101&pf_rd_p=b1578539-8101-4760-b358-11f5ab6aaf32&pf_rd_i=2238192011')
        email = ('an', 'vy', 'di', 'it', 'vs', '3', '2', '5')

        #card = self.driver.find_element_by_xpath('//a[@class="a-color-base a-spacing-none a-link-normal acs-product-block__product-title"]')
        #card.click()
        #sleep(2)
        # It we find all buttons designs
        try:
            design = self.driver.find_element_by_xpath('//button[@id="gc-customization-type-button-Animated"]')
            design_1 = self.driver.find_element_by_xpath('//button[@id="gc-customization-type-button-Upload"]')
            design_2 = self.driver.find_element_by_xpath('//button[@id="gc-customization-type-button-Designs"]')
            random_design = (design, design_1, design_2)
        except:
            print('I couldn`t find buttons sorry:-(')
        # It we choose random button that will click
        random.choice(random_design).click()
        sleep(2)
        # These are all buttons with price
        try:
            amount_1 = self.driver.find_element_by_xpath('//button[@id="gc-mini-picker-amount-1"]')
            amount_2 = self.driver.find_element_by_xpath('//button[@id="gc-mini-picker-amount-1"]')
            amount_3 = self.driver.find_element_by_xpath('//button[@id="gc-mini-picker-amount-1"]')
            amount_4 = self.driver.find_element_by_xpath('//button[@id="gc-mini-picker-amount-1"]')
            amount_5 = self.driver.find_element_by_xpath('//button[@id="gc-mini-picker-amount-1"]')
            amount_6 = self.driver.find_element_by_xpath('//button[@id="gc-mini-picker-amount-1"]')

        except:
            print('I couldn`t find buttons sorry:-(')

def main():
    class_bot = Bot()


if __name__ == '__main__':
    main()