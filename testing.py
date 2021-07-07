import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver

        driver.implicitly_wait(5)
        driver.get("https://www.tiket.com")
        driver.maximize_window()
        self.assertIn("tiket", driver.title)
        # Departure Field
        departureInput = driver.find_element_by_xpath('//*[@id="productSearchFrom"]')
        departureInput.send_keys("Jakarta")
        dropdownDeparture = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="fromDropDownList"]/div')
            )
        )
        locationFromLists = dropdownDeparture.find_elements_by_class_name(
            "flight-drop-down-option"
        )
        assert "Maaf, tidak ada hasil" not in driver.page_source
        for location in locationFromLists:
            code = location.find_element_by_class_name("airport-city-name")
            print(code.text)
            if "Jakarta" in code.text:
                departureInput.send_keys(Keys.RETURN)
                break

        # Destination
        destinationInput = driver.find_element_by_xpath('//*[@id="productSearchTo"]')
        destinationInput.send_keys("Surabaya")
        dropdownDestination = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="toDropDownList"]/div'))
        )

        locationFromListsDes = dropdownDestination.find_elements_by_class_name(
            "flight-drop-down-option"
        )

        assert "Maaf, tidak ada hasil" not in driver.page_source
        for locationDes in locationFromListsDes:
            content = locationDes.find_element_by_class_name("airport-city-name")

            if "Surabaya" in content.text:
                time.sleep(1)
                destinationInput.send_keys(Keys.RETURN)
                break

        driver.execute_script("window.scrollTo(0, 900)")
        actionStart = ActionChains(driver)
        startDate = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="startDate"]/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/table/tbody/tr[2]/td[5]/div',
                )
            )
        )
        time.sleep(1)
        actionStart.click(startDate).perform()

        actionEnd = ActionChains(driver)
        endDate = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="endDate"]/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/table/tbody/tr[2]/td[6]/div',
                )
            )
        )
        time.sleep(1)
        actionEnd.click(endDate).perform()

        actionPass = ActionChains(driver)
        passangerDetails = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="passengerCabin"]/div[2]/div/div/div[3]/div/span',
                )
            )
        )
        time.sleep(1)
        actionPass.click(passangerDetails).perform()

        # search
        actionSearch = ActionChains(driver)
        searchButton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="productWidget"]/div[2]/div[3]/button',
                )
            )
        )
        time.sleep(1)
        actionSearch.click(searchButton).perform()

        # mengerti
        actionMengerti = ActionChains(driver)
        mengertiButton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div/div[4]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[3]',
                )
            )
        )
        time.sleep(1)
        actionMengerti.click(mengertiButton).perform()

        # choose departure
        actionDepart = ActionChains(driver)
        chooseDepart = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[3]/div/div/div[1]/div/div/div[1]',
                )
            )
        )
        time.sleep(3)
        actionDepart.click(chooseDepart).perform()
        time.sleep(1)

        # choose destination
        actionDestination = ActionChains(driver)
        chooseDestination = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[3]/div/div/div[1]/div/div/div[1]',
                )
            )
        )
        time.sleep(3)
        actionDestination.click(chooseDestination).perform()

        # title
        actionTitle = ActionChains(driver)
        titleInput = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[1]/div[3]/div[1]/div[1]/div/input',
                )
            )
        )
        actionTitle.click(titleInput).perform()
        time.sleep(1)
        titleInput.send_keys(Keys.ARROW_DOWN)
        titleInput.send_keys(Keys.RETURN)
        namaInput = driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/div/input'
        )
        namaInput.send_keys("Jonathan")

        emailInput = driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[1]/div[3]/div[2]/div/input'
        )
        emailInput.send_keys("jonathan.sendiko@gmail.com")

        phoneInput = driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[1]/div[3]/div[3]/div[2]/div/input'
        )
        phoneInput.send_keys("85945644450")

        actionPenumpang = ActionChains(driver)
        titlePenumpang = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div/div/input',
                )
            )
        )
        actionPenumpang.click(titlePenumpang).perform()
        time.sleep(1)
        titlePenumpang.send_keys(Keys.ARROW_DOWN)
        titlePenumpang.send_keys(Keys.RETURN)

        namaPenumpang = driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div/input'
        )
        namaPenumpang.send_keys("Jonathan")

        actionNegara = ActionChains(driver)
        kewarganegaraan = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[3]/div/div/div/input',
                )
            )
        )
        actionNegara.click(kewarganegaraan).perform()
        time.sleep(1)
        kewarganegaraan.send_keys(Keys.ARROW_DOWN)
        kewarganegaraan.send_keys(Keys.RETURN)

        driver.execute_script("window.scrollTo(0, 1080)")
        actionPembayaran = ActionChains(driver)
        pembayaranBtn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[6]/button',
                )
            )
        )
        actionPembayaran.click(pembayaranBtn).perform()

        actionConfirm = ActionChains(driver)
        confirmBtn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div/div[3]/div[3]/div/div[3]/div/div/div/div/div[3]/button[2]',
                )
            )
        )
        time.sleep(1)
        actionConfirm.click(confirmBtn).perform()

        secondActionConfirm = ActionChains(driver)
        secondConfirm = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div/div[1]/div/div/div/div/div[3]/button',
                )
            )
        )
        time.sleep(1)
        if secondConfirm is not None:
            secondActionConfirm.click(secondConfirm).perform()

    def tearDown(self):
        time.sleep(10)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()