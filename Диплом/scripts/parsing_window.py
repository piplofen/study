import sys
from PyQt5.QtGui import QFont
from PyQt5.QtCore import*
from PyQt5.QtGui import QFont, QColor, QBrush
from time import sleep
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel
import parsing_design_window
import datetime
import time
#import ParseForLight
import requests
from bs4 import BeautifulSoup
import csv
import os
import webbrowser
from collections import Counter

class Parsing(QtWidgets.QMainWindow, parsing_design_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.n = 500

        #self.insert_data_for_pars()
        self.comboForParsing.currentIndexChanged.connect(self.choice)
        #self.comboForParsing.currentIndexChanged.connect(lambda status, n_size = n: self.run(n_size))
        # self.treeWidgetForLerya.itemDoubleClicked.connect(self.printItem)
        # self.treeWidgetForBaucentr.itemDoubleClicked.connect(self.printItem)
        # self.treeWidgetForElectro.itemDoubleClicked.connect(self.printItem)
        self.bttnSearchForParsing.clicked.connect(self.search)
        self.tableForPars.cellPressed.connect(self.openLink)
        #self.bttnSearchForParsing.clicked.connect(lambda status, n_size = n: self.run(n_size))
        #self.bttnSearchForParsing.clicked.connect(self.run)
        self.bttnParserForClose.clicked.connect(self.close)
        self.statusBar().setFont(QFont("Times New Roman", 14, QFont.Normal))
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        #webbrowser.open('https://vk.com', new = 2)

        self.progressBar.setMinimum(0)
        self.progressBar.setValue(0)
        
        self.URLLerua = 'https://leroymerlin.ru'
        self.HEADERSLerua = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.3.848 Yowser/2.5 Safari/537.36', 'accept': '*/*'}
        self.HOSTLerua = 'https://leroymerlin.ru'
        #self.FILELerua = 'Lerua.csv'

        self.URLBaucentr = 'https://baucenter.ru'
        self.HEADERSBaucentr = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.3.848 Yowser/2.5 Safari/537.36', 'accept': '*/*'}
        self.HOSTBaucentr = 'https://baucenter.ru'
        #self.FILEBaucentr = 'Lerua.csv'

        self.URLElectro = 'https://stv39.ru'
        self.HEADERSElectro = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.3.848 Yowser/2.5 Safari/537.36', 'accept': '*/*'}
        self.HOSTElectro = 'https://stv39.ru'
        self.FILEElectro = 'Lerua.csv'


        self.comboForParsing.setCurrentText("ЭлектроЦентр")
        self.choice(2)

    def openLink(self, r, c):
        if c == 1:
            #print(self.tableForPars.item(r , c).text())
            webbrowser.open(self.tableForPars.item(r , c).text(), new = 2)

    def search(self):
################################################################################################################################
        if (self.treeWidgetForElectro.currentItem().text(0)) == "Автоматические выключатели":
            self.URLElectro = "https://stv39.ru/catalog/avtomaticheskie_vyklyuchateli/"
            self.parse(self.URLElectro)

        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Дифавтоматы и УЗО":
            self.URLElectro = "https://stv39.ru/catalog/difavtomaty_i_uzo/"
            self.parse(self.URLElectro)

        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Контакторы и аксессуары":
            self.URLElectro = "https://stv39.ru/catalog/kontaktory_i_aksessuary/"
            self.parse(self.URLElectro)

        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Ограничители мощности":
            self.URLElectro = "https://stv39.ru/catalog/ogranichiteli_moshchnosti/"
            self.parse(self.URLElectro)

        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Преобразователи частоты":
            self.URLElectro = "https://stv39.ru/catalog/preobrazovateli_chastoty/"
            self.parse(self.URLElectro)

        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Разрядники и выключатели":
            self.URLElectro = "https://stv39.ru/catalog/razryadniki_i_vyklyuchateli/"
            self.parse(self.URLElectro)
################################################################################################################################
        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Проводники":
            self.URLElectro = "https://stv39.ru/catalog/provodniki/"
            self.parse(self.URLElectro)

        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Соединители, держатели проводников":
            self.URLElectro = "https://stv39.ru/catalog/soediniteli_derzhateli_provodnikov/"
            self.parse(self.URLElectro)

        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Стержни":
            self.URLElectro = "https://stv39.ru/catalog/sterzhni/"
            self.parse(self.URLElectro)

        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Прочие комплектующие":
            self.URLElectro = "https://stv39.ru/catalog/prochie_komplektuyushchie/"
            self.parse(self.URLElectro) 
################################################################################################################################
        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Управление резервным питанием, системы АВР":
            self.URLElectro = "https://stv39.ru/catalog/upravlenie_rezervnym_pitaniem_sistemy_avr/"
            self.parse(self.URLElectro)
################################################################################################################################
        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Фотореле":
            self.URLElectro = "https://stv39.ru/catalog/fotorele/"
            self.parse(self.URLElectro)

        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Термореле":
            self.URLElectro = "https://stv39.ru/catalog/termorele/"
            self.parse(self.URLElectro)

        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Таймеры":
            self.URLElectro = "https://stv39.ru/catalog/taymery/"
            self.parse(self.URLElectro)

        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Датчики индуктивные и оптические":
            self.URLElectro = "https://stv39.ru/catalog/datchiki_induktivnye_i_opticheskie/"
            self.parse(self.URLElectro)

        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Датчики реле":
            self.URLElectro = "https://stv39.ru/catalog/datchiki_i_rele_1/"
            self.parse(self.URLElectro)

        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Реле импульсные":
            self.URLElectro = "https://stv39.ru/catalog/rele_impulsnye/"
            self.parse(self.URLElectro)

        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Реле контроля уровня жидкости":
            self.URLElectro = "https://stv39.ru/catalog/rele_kontrolya_urovnya_zhidkosti/"
            self.parse(self.URLElectro)

        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Реле контроля уровня жидкости":
            self.URLElectro = "https://stv39.ru/catalog/datchiki_dvizheniya/"
            self.parse(self.URLElectro)
################################################################################################################################
        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Стационарные разъемы":
            self.URLElectro = "https://stv39.ru/catalog/statsionarnye_razyemy/"
            self.parse(self.URLElectro)

        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Переносные разъемы":
            self.URLElectro = "https://stv39.ru/catalog/perenosnye_razyemy/"
            self.parse(self.URLElectro)

        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Разъемы внутренней установки и корпуса":
            self.URLElectro = "https://stv39.ru/catalog/razyemy_vnutrenney_ustanovki_i_korpusa/"
            self.parse(self.URLElectro)
################################################################################################################################
        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Сигнальные лампы, светодиодные модули и световые индикаторы":
            self.URLElectro = "https://stv39.ru/catalog/signalnye-lampy-svetodiodnye-moduli-i-svetovye-indikatory/"
            self.parse(self.URLElectro)

        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Кнопки, корпуса, переключатели и поворотные головки":
            self.URLElectro = "https://stv39.ru/catalog/knopki_korpusa_pereklyuchateli_i_povorotnye_golovki/"
            self.parse(self.URLElectro)

        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Комплектующие к приборам управления":
            self.URLElectro = "https://stv39.ru/catalog/komplektuyushchie_k_priboram_upravleniya/"
            self.parse(self.URLElectro)

        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Беспроводное управление электрооборудованием":
            self.URLElectro = "https://stv39.ru/catalog/besprovodnoe_upravlenie_elektrooborudovaniem/"
            self.parse(self.URLElectro)

        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Блоки питания и стабилизаторы":
            self.URLElectro = "https://stv39.ru/catalog/bloki_pitaniya_i_stabilizatory/"
            self.parse(self.URLElectro)

        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Рубильники":
            self.URLElectro = "https://stv39.ru/catalog/rubilniki_vyklyuchateli_pereklyuchateli/"
            self.parse(self.URLElectro)
################################################################################################################################
        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Металлические электрощиты":
            self.URLElectro = "https://stv39.ru/catalog/metallicheskie_elektroshchity/"
            self.parse(self.URLElectro)

        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Пластиковые электрощиты":
            self.URLElectro = "https://stv39.ru/catalog/plastikovye_elektroshchity/"
            self.parse(self.URLElectro)

        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Вставки плавкие и предохранители":
            self.URLElectro = "https://stv39.ru/catalog/vstavki_plavkie_i_predokhraniteli/"
            self.parse(self.URLElectro)

        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Дверцы и панели ревизионные":
            self.URLElectro = "https://stv39.ru/catalog/dvertsy_i_paneli_revizionnye/"
            self.parse(self.URLElectro)

        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Комплектующие для щитов":
            self.URLElectro = "https://stv39.ru/catalog/komplektuyushchie_dlya_shchitov/"
            self.parse(self.URLElectro)
################################################################################################################################
        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Шины медные и алюминиевые электротехнические":
            self.URLElectro = "https://stv39.ru/catalog/shiny_mednye_i_alyuminievye_elektrotekhnicheskie/"
            self.parse(self.URLElectro)

        elif (self.treeWidgetForElectro.currentItem().text(0)) == "DIN - рейки":
            self.URLElectro = "https://stv39.ru/catalog/din_reyki/"
            self.parse(self.URLElectro)

        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Соединительные шины на DIN - рейки":
            self.URLElectro = "https://stv39.ru/catalog/soedinitelnye_shiny_na_din_reyki/"
            self.parse(self.URLElectro)

        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Комплектующие для монтажа шин и DIN - рейки":
            self.URLElectro = "https://stv39.ru/catalog/komplektuyushchie_dlya_montazha_shin_i_din_reyki/"
            self.parse(self.URLElectro)
################################################################################################################################
        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Стабилизаторы напряжения":
            self.URLElectro = "https://stv39.ru/catalog/stabilizatory_napryazheniya/"
            self.parse(self.URLElectro)
################################################################################################################################
        elif (self.treeWidgetForElectro.currentItem().text(0)) == "ИБП и сетевые фильтры":
            self.URLElectro = "https://stv39.ru/catalog/ibp_i_setevye_filtry/"
            self.parse(self.URLElectro)
################################################################################################################################
        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Трансформаторы":
            self.URLElectro = "https://stv39.ru/catalog/transformatory/"
            self.parse(self.URLElectro)
################################################################################################################################
        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Электродвигатели":
            self.URLElectro = "https://stv39.ru/catalog/elektrodvigateli/"
            self.parse(self.URLElectro)
################################################################################################################################
        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Кабельные маркеры и таблички":
            self.URLElectro = "https://stv39.ru/catalog/kabelnye_markery_i_tablichki/"
            self.parse(self.URLElectro)

        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Знаки безопасности":
            self.URLElectro = "https://stv39.ru/catalog/znaki_bezopasnosti/"
            self.parse(self.URLElectro)

        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Сигнальные и оградительные ленты":
            self.URLElectro = "https://stv39.ru/catalog/signalnye_i_ograditelnye_lenty_1/"
            self.parse(self.URLElectro)
################################################################################################################################
        elif (self.treeWidgetForElectro.currentItem().text(0)) == "Счетчики электроэнергии и трансформаторы тока":
            self.URLElectro = "https://stv39.ru/catalog/schyetchiki_elektroenergii_i_transformatory_toka/"
            self.parse(self.URLElectro)
###############################################################################################################################
        print(self.URLElectro)


    def showTime(self):
        dt = datetime.datetime.now()
        self.statusbar.showMessage(str(dt.strftime('%Y.%m.%d - %H:%M:%S')), 1000)

    def get_html(self, url, params = None):
        r = requests.get(url, headers = self.HEADERSElectro, params = params)
        return r

    def get_pages_count(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        pagenation = soup.find("ul", class_ = "pagination")
        if pagenation:
            print(pagenation.get_text().strip()[-2:])
            return int(pagenation.get_text().strip()[-2:])
        else:
            print(1)
            return 1

    def get_content(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all("div", class_ = "cell product-cell")
        #print(items)

        light = []

        for item in items:
            light.append({
                "name": item.find("a", class_ = "prod__title").get_text().strip(),
                "link": self.HOSTElectro + item.find("a", class_ = "prod__title").get("href"),
                "price": item.find("div", class_ = "shrink cell").get_text().strip(),
                "purchase": item.find("div", class_ = "prod__av").get_text().strip()
                })

        return light


    def parse(self, url):
        print(url)
        html = self.get_html(url)
        print(html.status_code)
        if html.status_code == 200:
            light = []
            pages_count = self.get_pages_count(html.text)
            print(pages_count)
            self.progressBar.setMaximum(pages_count)
            self.progressBar.setRange(0, pages_count)
            self.progressBar.setValue(0)
            for page in range(1, pages_count + 1):
                if pages_count == 1:
                    self.progressBar.setValue(0)
                    print(f"Парсинг страницы {page} из {pages_count}")
                    time.sleep(1)
                    self.progressBar.setValue(page)
                    html = self.get_html(url, params = {"disable_ajax=N&PAGEN_1": page})
                    light.extend(self.get_content(html.text))
                else:
                    print(f"Парсинг страницы {page} из {pages_count}")
                    self.labelForErrorCount.setText(f"Парсинг страницы {page} из {pages_count}")
                    #time.sleep(1)
                    self.progressBar.setValue(page)
                    html = self.get_html(url, params = {"disable_ajax=N&PAGEN_1": page})
                    light.extend(self.get_content(html.text))

            print(f"Получено {len(light)} элементов.")
            self.labelForErrorCount.setText(f"Получено {len(light)} элементов.")

            temp = []
            name = []
            link = []
            price = []
            purchase = []

            for item in light:
                name.append(item.get("name"))
                link.append(item.get("link"))
                price.append(item.get("price"))
                purchase.append(item.get("purchase"))

            self.tableForPars.setColumnWidth(0, 200)
            self.tableForPars.setColumnWidth(1, 100)
            self.tableForPars.setColumnWidth(2, 100)
            self.tableForPars.setColumnWidth(3, 150)
            self.tableForPars.verticalHeader().setVisible(False)
            self.tableForPars.setRowCount(len(name))

            try:
                for i in range(len(light)):

                    self.tableForPars.setItem(i, 0, QtWidgets.QTableWidgetItem(str(name[i])))

                    if i == 0:
                        self.tableForPars.item(i, 0).setBackground(QBrush(QColor(220, 220, 220)))
                    elif i % 2 == 0:
                        self.tableForPars.item(i, 0).setBackground(QBrush(QColor(220, 220, 220)))

                for i in range(len(light)):

                    self.tableForPars.setItem(i, 1, QtWidgets.QTableWidgetItem(str(link[i])))
                    self.tableForPars.item(i, 1).setForeground(QBrush(QColor(0, 0, 255)))

                    if i == 0:
                        self.tableForPars.item(i, 1).setBackground(QBrush(QColor(220, 220, 220)))
                    elif i % 2 == 0:
                        self.tableForPars.item(i, 1).setBackground(QBrush(QColor(220, 220, 220)))

                for i in range(len(light)):

                    self.tableForPars.setItem(i, 2, QtWidgets.QTableWidgetItem(str(price[i])))

                    if i == 0:
                        self.tableForPars.item(i, 2).setBackground(QBrush(QColor(220, 220, 220)))
                    elif i % 2 == 0:
                        self.tableForPars.item(i, 2).setBackground(QBrush(QColor(220, 220, 220)))

                for i in range(len(light)):

                    self.tableForPars.setItem(i, 3, QtWidgets.QTableWidgetItem(str(purchase[i])))

                    if i == 0:
                        self.tableForPars.item(i, 3).setBackground(QBrush(QColor(220, 220, 220)))
                    elif i % 2 == 0:
                        self.tableForPars.item(i, 3).setBackground(QBrush(QColor(220, 220, 220)))

            except BaseException as e:
                print(e)

    # def parse(self, url):
    #     print(url)
    #     html = self.get_html(url)
    #     print(html.status_code)
    #     if html.status_code == 200:
    #         light = []
    #         pages_count = self.get_pages_count(html.text)
    #         print(pages_count)
    #         self.progressBar.setMaximum(pages_count)
    #         self.progressBar.setRange(0, pages_count)
    #         self.progressBar.setValue(0)
    #         for page in range(1, pages_count + 1):
    #             if pages_count == 1:
    #                 self.progressBar.setValue(0)
    #                 #print(f"Парсинг страницы {page} из {pages_count}")
    #                 time.sleep(1)
    #                 self.progressBar.setValue(page)
    #                 html = self.get_html(url, params = {"disable_ajax=N&PAGEN_1": page})
    #                 light.extend(self.get_content(html.text))
    #             else:
    #                 #print(f"Парсинг страницы {page} из {pages_count}")
    #                 #self.labelForErrorCount.setText(f"Парсинг страницы {page} из {pages_count}")
    #                 #time.sleep(1)
    #                 self.progressBar.setValue(page)
    #                 html = self.get_html(url, params = {"disable_ajax=N&PAGEN_1": page})
    #                 light.extend(self.get_content(html.text))

    #         print(f"Получено {len(light)} элементов.")

    #         temp = []
    #         name = []
    #         link = []
    #         price = []
    #         purchase = []

    #         for item in light:
    #             name.append(item.get("name"))
    #             link.append(item.get("link"))
    #             price.append(item.get("price"))
    #             purchase.append(item.get("purchase"))


    #         for x in name:
    #             if x not in temp:
    #                 temp.append(x)

    #         name = temp

    #         for i in range(len(name)):
    #             if name[i] == "Кабель-канал гибкий ДСР-3 ,  нагрузка 1,5т, длина 1м, черный":
    #                 #print("Вы недавно смотрели")
    #                 #print(name[i])
    #                 #print(i)
    #                 index = i
    #                 #name[i].pop([i + 1])
            
    #         for i in range(1, 17):
    #             name.pop(index)
    #             link.pop(index)

    #         self.labelForErrorCount.setText(f"Получено {len(name)} элементов.")

    #         temp = []

    #         for x in link:
    #             if x not in temp:
    #                 temp.append(x)

    #         link = temp

    #         self.tableForPars.setColumnWidth(0, 300)
    #         self.tableForPars.setColumnWidth(1, 100)
    #         self.tableForPars.setColumnWidth(2, 100)
    #         self.tableForPars.setColumnWidth(3, 150)
    #         self.tableForPars.verticalHeader().setVisible(False)
    #         self.tableForPars.setRowCount(len(name))

    #         try:
    #             for i in range(len(name)):

    #                 self.tableForPars.setItem(i, 0, QtWidgets.QTableWidgetItem(str(name[i])))

    #                 if i == 0:
    #                     self.tableForPars.item(i, 0).setBackground(QBrush(QColor(220, 220, 220)))
    #                 elif i % 2 == 0:
    #                     self.tableForPars.item(i, 0).setBackground(QBrush(QColor(220, 220, 220)))

    #             for i in range(len(name)):

    #                 self.tableForPars.setItem(i, 1, QtWidgets.QTableWidgetItem(str(link[i])))
    #                 self.tableForPars.item(i, 1).setForeground(QBrush(QColor(0, 0, 255)))

    #                 if i == 0:
    #                     self.tableForPars.item(i, 1).setBackground(QBrush(QColor(220, 220, 220)))
    #                 elif i % 2 == 0:
    #                     self.tableForPars.item(i, 1).setBackground(QBrush(QColor(220, 220, 220)))

    #             for i in range(len(name)):

    #                 self.tableForPars.setItem(i, 2, QtWidgets.QTableWidgetItem(str(price[i])))

    #                 if i == 0:
    #                     self.tableForPars.item(i, 2).setBackground(QBrush(QColor(220, 220, 220)))
    #                 elif i % 2 == 0:
    #                     self.tableForPars.item(i, 2).setBackground(QBrush(QColor(220, 220, 220)))

    #             for i in range(len(name)):

    #                 self.tableForPars.setItem(i, 3, QtWidgets.QTableWidgetItem(str(purchase[i])))

    #                 if i == 0:
    #                     self.tableForPars.item(i, 3).setBackground(QBrush(QColor(220, 220, 220)))
    #                 elif i % 2 == 0:
    #                     self.tableForPars.item(i, 3).setBackground(QBrush(QColor(220, 220, 220)))

    #         except BaseException as e:
    #             print(e)

    def choice(self, index):
        if index == 0:

            try:

                self.labelForError.setText("https://baucenter.ru status_code = 401, соединение не установлено")
                self.treeWidgetForBaucentr.setEnabled(False)

            except:
                pass

            self.treeWidgetForBaucentr.show()
            self.treeWidgetForLerya.hide()
            self.treeWidgetForElectro.hide()

        elif index == 1:

            try:

                self.labelForError.setText("https://leroymerlin.ru status_code = 401, соединение не установлено")
                self.treeWidgetForLerya.setEnabled(False)

            except:
                pass

            self.treeWidgetForLerya.show()
            self.treeWidgetForBaucentr.hide()
            self.treeWidgetForElectro.hide()

        elif index == 2:

            try:

                self.labelForError.setText("https://stv39.ru status_code = 200, соединение установлено")
                self.treeWidgetForBaucentr.setEnabled(True)

            except:
                pass
            
            self.treeWidgetForLerya.hide()
            self.treeWidgetForBaucentr.hide()
            self.treeWidgetForElectro.show()

    def run(self):
        for i in range(self.n):
            time.sleep(0.01)
            self.progressBar.setValue(i + 1)
            print(i)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Parsing()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()