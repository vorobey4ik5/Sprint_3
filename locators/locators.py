driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/section[2]/div/button') #Кнопка "Войти в аккаунт"
driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/div/div/p[1]/a')    #Кнопка "Зарегистрироваться"
driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input') #Поле ввода email в форме регистрации и восстановления пароля
driver.find_element(by=By.NAME, value='Пароль') #Поле ввода пароля в форме регистрации
driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input') #Поле ввода "Имя"
driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/div/form/button') #Кнопка "Войти" в форме регистрации
driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/header/nav/a')  # Кнопка "Личный кабинет"
driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/div/div/p[2]/a') #Кнопка "Восстановить пароль"
driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/div/form/button') #Кнопка "Восстановить"
driver.find_element(by=By.NAME, value='Введите новый пароль') #Поле ввода нового пароля
driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input') #Поле "Введите код из письма"
driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/div/form/button') #Кнопка "Сохранить"
driver.find_element(by=By.CLASS_NAME, value='AppHeader_header__link__3D_hX') #Кнопка "Конструктор"
driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/header/nav/div/a') #Логотип "Stellar Burgers"
driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/div/nav/ul/li[3]/button') #Кнопка "Выйти" в личном кабинете
driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/section[1]/div[1]/div[1]') #Раздел "Булки"
driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/section[1]/div[1]/div[2]') #Раздел "Соусы"
driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/main/section[1]/div[1]/div[3]') #Раздел "Начинки"