import time
import pytest
from selenium.webdriver.common.by import By
import pytest_check as check
import PageObjects
import BaseApp
from PageObjects import chrome_locators
import allure
from allure_commons.types import AttachmentType


@pytest.mark.usefixtures('setup')
class TestMain:

    @allure.feature("Тест интернет-магазина Salita")
    @allure.story("Тест навигации главной страницы")
    @allure.description("фильтр по цветам")
    def test_section(self):
        with allure.step("Открыть ссылку"):
            section = chrome_locators(self.driver)
            section.go_to_site()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Открыть женщинам,обувь,фильтр по цветам,выбрать бежевый цвет"):
            section.do_section_question()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        assert self.driver.current_url == "https://www.salita.ru/zhenshchinam/obuv/"

    @allure.feature("Тест интернет-магазина Salita")
    @allure.story("Тест навигации главной страницы")
    @allure.description("добавить в избранное выбранный товар")
    def test_favorite(self):
        with allure.step("Открыть ссылку"):
            favorite = chrome_locators(self.driver)
            favorite.go_to_site()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Открыть одежда,добавить в избранное первый товар, открыть избранное в меню"):
            favorite.do_favorite_question()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        assert self.driver.current_url == "https://www.salita.ru/favorites/"

    @allure.feature("Тест интернет-магазина Salita")
    @allure.story("Тест навигации главной страницы")
    @allure.description("Геолокация магазинов")
    def test_shops(self):
        with allure.step("Открыть ссылку"):
            shops = chrome_locators(self.driver)
            shops.go_to_site()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Открыть геолокацию магазинов"):
            shops.do_shops_question()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        assert self.driver.current_url == "https://www.salita.ru/shops/"

    @allure.feature("Тест интернет-магазина Salita")
    @allure.story("Тест навигации главной страницы")
    @allure.description("Вход пользователя")
    def test_entrance(self):
        with allure.step("Открыть ссылку"):
            entrance = chrome_locators(self.driver)
            entrance.go_to_site()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Заполнить форму входа"):
            entrance.do_entrance_question("dz8ms@yandex.ru", "Qwerty.")
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.feature("Тест интернет-магазина Salita")
    @allure.story("Тест навигации главной страницы")
    @allure.description("Тест строки поиска")
    def test_find(self):
        with allure.step("Открыть ссылку"):
            find = chrome_locators(self.driver)
            find.go_to_site()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Ввести в строку поиска запрос"):
            find.do_find_question("сапоги\n")
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.feature("Тест интернет-магазина Salita")
    @allure.story("Тест навигации главной страницы")
    @allure.description("Негативный сценарий теста строки поиска")
    def test_findnegativ(self):
        with allure.step("Открыть ссылку"):
            findnegativ = chrome_locators(self.driver)
            findnegativ.go_to_site()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Ввести в строку поиска запрос"):
            findnegativ.do_findnegativ_question("123456\n")
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        assert self.driver.current_url == "https://www.salita.ru/?q=123456"

    @allure.feature("Тест интернет-магазина Salita")
    @allure.story("Тест навигации главной страницы")
    @allure.description("Таблица размеров")
    def test_kart_open(self):
        with allure.step("Открыть ссылку"):
            kart_open = chrome_locators(self.driver)
            kart_open.go_to_site()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Открыть одежда,кликнуть на первый товар, кликнуть на как выбрать"):
            kart_open.do_kartopen_question()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        assert self.driver.current_url == "https://www.salita.ru/zhenshchinam/odezhda/dzhempery/658957/"

    @allure.feature("Тест интернет-магазина Salita")
    @allure.story("Тест навигации главной страницы")
    @allure.description("Поиск конкретного товара и его открытие в новом окне")
    def test_new_window(self):
        with allure.step("Открыть ссылку"):
            new_window = chrome_locators(self.driver)
            new_window.go_to_site()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Ввести в строку поиска запрос"):
            new_window.do_newwindow_question("брюки женские BOSS\n")
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.feature("Тест интернет-магазина Salita")
    @allure.story("Тест навигации главной страницы")
    @allure.description("Фильтр сортировки и тест кнопки сбросить")
    def test_filter(self):
        with allure.step("Открыть ссылку"):
            first_question = chrome_locators(self.driver)
            first_question.go_to_site()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Открыть одежда, кликнуть на сортировку по новинкам,выбрать по возрастанию цены,кликнуть сбросить"):
            first_question.do_filter_question()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        assert self.driver.current_url == "https://www.salita.ru/zhenshchinam/odezhda/filter/clear/apply/"

    @allure.feature("Тест интернет-магазина Salita")
    @allure.story("Тест навигации главной страницы")
    @allure.description("Раздел Бренд и открытие брендов на букву А")
    def test_brand(self):
        with allure.step("Открыть ссылку"):
            first_question = chrome_locators(self.driver)
            first_question.go_to_site()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",attachment_type=AttachmentType.PNG)
        with allure.step("Открыть бренды, открыть бренды на букву А"):
            first_question.do_brand_question()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",attachment_type=AttachmentType.PNG)
        assert self.driver.current_url == "https://www.salita.ru/brand/a/"



