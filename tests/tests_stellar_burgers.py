from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://stellarburgers.nomoreparties.site')

time.sleep(1)

class Registration:

    def test_successful_registration(self):
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/section[2]/div/button').click()
        driver.find_element(by=By.CLASS_NAME, value='Auth_link__1fOlj').click()
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys(
            'Dmitry')
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(
            'Dmitry_Vorobev1996@yandex.ru')
        driver.find_element(by=By.NAME, value='Пароль').send_keys('a125745')
        time.sleep(1)
        driver.find_element(by=By.CLASS_NAME, value='Auth_link__1fOlj').click()
        time.sleep(1)
        driver.close()

    def test_incorrect_password(self):
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/section[2]/div/button').click()
        driver.find_element(by=By.CLASS_NAME, value='Auth_link__1fOlj').click()
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys(
            'Dmitry')
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(
            'Dmitry_Vorobev1996@yandex.ru')
        driver.find_element(by=By.NAME, value='Пароль').send_keys('a1257')
        time.sleep(1)
        driver.find_element(by=By.CLASS_NAME, value='Auth_link__1fOlj').click()
        time.sleep(3)
        error = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/div/form/fieldset[3]/div/p')
        if error.text == 'Некорректный пароль':
            print('Некорректный пароль, пользователь не зарегистрирован')
        else:
            print('Ошибка поиска элемента')
        driver.close()

class Entry:

    def test_login_by_clicking_button_main_page(self):
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/section[2]/div/button').click()
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys(
            'Dmitry_Vorobev1996@yandex.ru')
        driver.find_element(by=By.NAME, value='Пароль').send_keys('a125745')
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/div/form/button').click()
        time.sleep(2)
        button_checkout = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/section[2]/div/button')
        if button_checkout.text == '//*[@id="root"]/div/main/section[2]/div/button':
            print('Ошибка поиска элемента')
        else:
            print('Пользователь вошел в систему')


    def test_login_by_clicking_button_personal_account(self):
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/header/nav/a').click()
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys(
            'Dmitry_Vorobev1996@yandex.ru')
        driver.find_element(by=By.NAME, value='Пароль').send_keys('a125745')
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/div/form/button').click()
        time.sleep(2)
        button_checkout = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/section[2]/div/button')
        if button_checkout.text == '//*[@id="root"]/div/main/section[2]/div/button':
            print('Ошибка поиска элемента')
        else:
            print('Пользователь вошел в систему')
        driver.close()

    def test_login_in_the_registration_form(self):
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/section[2]/div/button').click()
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/div/div/p[1]/a').click()
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/div/div/p/a').click()
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys(
            'Dmitry_Vorobev1996@yandex.ru')
        driver.find_element(by=By.NAME, value='Пароль').send_keys('a125745')
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/div/form/button').click()
        time.sleep(2)
        button_checkout = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/section[2]/div/button')
        if button_checkout.text == '//*[@id="root"]/div/main/section[2]/div/button':
            print('Ошибка поиска элемента')
        else:
            print('Пользователь вошел в систему')
        driver.close()

    def test_login_in_the_password_recovery_form(self):
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/section[2]/div/button').click()
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/div/div/p[2]/a').click()
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/div/div/p/a').click()
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys(
            'Dmitry_Vorobev1996@yandex.ru')
        driver.find_element(by=By.NAME, value='Пароль').send_keys('a125745')
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/div/form/button').click()
        time.sleep(2)
        button_checkout = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/section[2]/div/button')
        if button_checkout.text == '//*[@id="root"]/div/main/section[2]/div/button':
            print('Ошибка поиска элемента')
        else:
            print('Пользователь вошел в систему')
        driver.close()

class GoTo:

    def test_go_to_personal_account(self):
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/header/nav/a').click()
        entry_form = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/div/h2')

        if entry_form.text == 'Вход':
            print('Кнопка работает')
        else:
            print('Ошибка поиска элемента')
        driver.close()

    def test_go_to_constructor_and_logo(self):
        driver.find_element(by=By.CLASS_NAME, value='AppHeader_header__link__3D_hX').click()
        burger_constructor = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/section[1]/h1')
        if burger_constructor.text == 'Соберите бургер':
            print('Главная страница открыта')
        else:
            print('Кнопка не работает')
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/header/nav/div/a').click()
        burger_constructor = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/section[1]/h1')
        if burger_constructor.text == 'Соберите бургер':
            print('Главная страница открыта')
        else:
            print('Кнопка не работает')

    def test_logout(self):
        entry = Entry()
        entry.test_login_by_clicking_button_main_page()
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/header/nav/a').click()
        time.sleep(2)
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/div/nav/ul/li[3]/button').click()
        print('Пользователь вышел из системы')
        driver.close()

    def test_go_to_sauces(self):
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/section[1]/div[1]/div[2]').click()
        print('Открыт раздел - соусы')
        driver.close()

    def test_go_to_filling(self):
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/section[1]/div[1]/div[3]').click()
        print('Открыт раздел - начинки')
        driver.close()

    def test_go_to_buns(self):
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/section[1]/div[1]/div[1]').click()
        print('Открыт раздел - булки')
        driver.close()
