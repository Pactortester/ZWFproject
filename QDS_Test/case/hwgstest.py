# coding=utf-8
import os
import random
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from utils.datachoice import nice
from utils.mytestcase import MyTestCase
from utils.logincookie import DengLuPage
from utils.random import unicode
from utils.screenshort import get_screenshort


class HwGsTest(MyTestCase):
    """海外高速测试集"""

    def test_hwgs_1(self):
        """海外高速_企业测试"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = DengLuPage(self.driver)
        # 官方推荐有find_element(By.*(""))代替find_element_by_*("")
        # self.driver.find_element_by_id()
        # self.driver.find_element()
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(3) > dd > a:nth-child(4)").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        self.assertIn("海外商标注册|国际商标注册|商标注册流程|商标注册代理-权大师", self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont > ul > li:nth-child(4)").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            aa = a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("body > div.recommend-help > i").click()
        # body > div.recommend-help > i
        ss = unicode()
        self.driver.find_element_by_name("brandName").send_keys("{}".format(ss))
        print("商标名称：{}".format(ss))
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.brand-info-wrap.show1.form-wrap > ul > li.brand-upload > div > div.brand-upload-wrap > div.zidongdong-create > ul > li > a").click()
        time.sleep(5)

        self.driver.find_element_by_css_selector(
            "#selectCategoryType > label:nth-child(2)").click()
        self.driver.execute_script("window.scrollBy(0,1200)")  # 滑动滚动条
        suiji = random.randint(2, 45)
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li:nth-child({}) > span".format(suiji)).click()

        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div:nth-child(2) > span").click()

        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(1) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(2) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(3) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(4) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(5) > span").click()


        print("选择了第{}类商标分类!".format(suiji))

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.register-pay > div > ul > li.row-step > a").click()

        try:
            self.driver.find_element(By.LINK_TEXT, "确认")
            a = True
        except:
            a = False
        if a is True:
            """不足10小项确认提交"""
            self.driver.find_element_by_link_text("确认").click()
        elif a is False:
            pass

        time.sleep(3)

        # 企业 国外

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys(
            "{}".format(unicode()))
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(2) > td.td-content > input").send_keys(
            "tesr")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(3) > td.td-content.fcountry-container > input.myInput").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(3) > td.td-content.fcountry-container > div > div.country-list.country-list-ag.active > span:nth-child(1)").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(4) > td.td-title").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(4) > td.td-content > input").send_keys(
            "test01")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(5) > td.td-content > input").send_keys(
            "test01")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(6) > td.td-content > input").send_keys(
            "test02")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(7) > td.td-content > input").send_keys(
            "15624992422")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(8) > td.td-content > input").send_keys(
            "4654564@qq.com")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-btns.clearfix > a:nth-child(2)").click()

        """订单备注"""
        self.driver.find_element_by_css_selector(
            "html body div.register-wrap div.orderinfo-wrap div.order-content textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")



        get_screenshort(self.driver, "test_hwgs_1.png")
        for i in self.driver.find_elements_by_css_selector("body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:"+i.text)
            ii = i.text

        self.assertIn(aa,ii)
        print("价格一致")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > div > a").click()
        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:"+o.text)
            oo = o.text

        self.assertIn(oo,ii)

        print("测试通过")
        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_hwgs_2(self):
        """海外高速_自然人测试"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = DengLuPage(self.driver)
        # 官方推荐有find_element(By.*(""))代替find_element_by_*("")
        # self.driver.find_element_by_id()
        # self.driver.find_element()
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(3) > dd > a:nth-child(4)").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        self.assertIn("海外商标注册|国际商标注册|商标注册流程|商标注册代理-权大师", self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont > ul > li:nth-child(4)").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            aa = a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("body > div.recommend-help > i").click()
        # body > div.recommend-help > i
        ss = unicode()
        self.driver.find_element_by_name("brandName").send_keys("{}".format(ss))
        print("商标名称：{}".format(ss))
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.brand-info-wrap.show1.form-wrap > ul > li.brand-upload > div > div.brand-upload-wrap > div.zidongdong-create > ul > li > a").click()
        time.sleep(5)

        self.driver.find_element_by_css_selector(
            "#selectCategoryType > label:nth-child(2)").click()
        self.driver.execute_script("window.scrollBy(0,1200)")  # 滑动滚动条
        suiji = random.randint(2, 45)
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li:nth-child({}) > span".format(suiji)).click()

        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div:nth-child(2) > span").click()

        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(1) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(2) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(3) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(4) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(5) > span").click()

        print("选择了第{}类商标分类!".format(suiji))

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.register-pay > div > ul > li.row-step > a").click()

        try:
            self.driver.find_element(By.LINK_TEXT, "确认")
            a = True
        except:
            a = False
        if a is True:
            """不足10小项确认提交"""
            self.driver.find_element_by_link_text("确认").click()
        elif a is False:
            pass

        time.sleep(3)

        # 企业 自然人

        self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > table > thead > tr:nth-child(1) > td.td-content > a:nth-child(2)").click()
        self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys("{}".format(unicode()))
        self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(2) > td.td-content > input").send_keys("dalao")
        self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(4) > td.td-content > input").send_keys("140121199506133513")
        self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(5) > td.td-content.fcountry-container > input.myInput").click()
        self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(5) > td.td-content.fcountry-container > div > div.country-list.country-list-ag.active > span:nth-child(1)").click()
        self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(5) > td.td-title").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(6) > td.td-content > input").send_keys("外国人")
        self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(7) > td.td-content > input").send_keys("waiguoren")
        self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(8) > td.td-content > input").send_keys("laotie")
        self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(9) > td.td-content > input").send_keys("17801188215")
        self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(10) > td.td-content > input").send_keys("1456470136@qq.com")
        self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(11) > td.td-content > input").send_keys("03515925212")

        self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-btns.clearfix > a:nth-child(2)").click()
        time.sleep(2)

        """订单备注"""
        self.driver.find_element_by_css_selector(
            "html body div.register-wrap div.orderinfo-wrap div.order-content textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")



        get_screenshort(self.driver, "test_hwgs_2.png")
        for i in self.driver.find_elements_by_css_selector("body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:"+i.text)
            ii = i.text

        self.assertIn(aa,ii)
        print("价格一致")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > div > a").click()
        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:"+o.text)
            oo = o.text

        self.assertIn(oo,ii)

        print("测试通过")
        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_hwgs_3(self):
        """海外高速_企业_历史订单测试"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = DengLuPage(self.driver)
        # 官方推荐有find_element(By.*(""))代替find_element_by_*("")
        # self.driver.find_element_by_id()
        # self.driver.find_element()
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(3) > dd > a:nth-child(4)").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        self.assertIn("海外商标注册|国际商标注册|商标注册流程|商标注册代理-权大师", self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont > ul > li:nth-child(4)").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            # aa = a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("body > div.recommend-help > i").click()
        ss = unicode()
        self.driver.find_element_by_name("brandName").send_keys("{}".format(ss))
        print("商标名称：{}".format(ss))
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.brand-info-wrap.show1.form-wrap > ul > li.brand-upload > div > div.brand-upload-wrap > div.zidongdong-create > ul > li > a").click()

        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#selectCategoryType > label:nth-child(2)").click()

        """商标类别导入历史订单"""
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-right > h3 > div > a.btn.showHistoryOrder").click()
        time.sleep(2)
        history_number = random.randint(2, 10)
        info = self.driver.find_element_by_css_selector(
            "#history_order > li:nth-child({}) > h2".format(history_number)).text
        print("导入历史订单信息:" + info)
        self.driver.find_element_by_css_selector(
            "#history_order > li:nth-child({}) > h2".format(history_number)).click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#history-order > div.modal-button > a").click()
        time.sleep(2)

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.register-pay > div > ul > li.row-step > a").click()

        try:
            self.driver.find_element(By.LINK_TEXT, "确认")
            a = True
        except:
            a = False
        if a is True:
            """不足10小项确认提交"""
            self.driver.find_element_by_link_text("确认").click()
        elif a is False:
            pass

        time.sleep(3)

        # 企业 国外

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys(
            "{}".format(unicode()))
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(2) > td.td-content > input").send_keys(
            "tesr")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(3) > td.td-content.fcountry-container > input.myInput").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(3) > td.td-content.fcountry-container > div > div.country-list.country-list-ag.active > span:nth-child(1)").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(4) > td.td-title").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(4) > td.td-content > input").send_keys(
            "test01")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(5) > td.td-content > input").send_keys(
            "test01")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(6) > td.td-content > input").send_keys(
            "test02")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(7) > td.td-content > input").send_keys(
            "15624992422")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(8) > td.td-content > input").send_keys(
            "4654564@qq.com")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-btns.clearfix > a:nth-child(2)").click()

        """订单备注"""
        self.driver.find_element_by_css_selector(
            "html body div.register-wrap div.orderinfo-wrap div.order-content textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")



        get_screenshort(self.driver, "test_hwgs_3.png")
        for i in self.driver.find_elements_by_css_selector("body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:"+i.text)
            ii = i.text

        # self.assertIn(aa,ii)
        print("价格一致")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > div > a").click()
        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:"+o.text)
            oo = o.text

        self.assertIn(oo,ii)

        print("测试通过")
        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_hwgs_4(self):
        """海外高速_自然人_历史订单测试"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = DengLuPage(self.driver)
        # 官方推荐有find_element(By.*(""))代替find_element_by_*("")
        # self.driver.find_element_by_id()
        # self.driver.find_element()
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(3) > dd > a:nth-child(4)").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        self.assertIn("海外商标注册|国际商标注册|商标注册流程|商标注册代理-权大师", self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont > ul > li:nth-child(4)").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            # aa = a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("body > div.recommend-help > i").click()
        ss = unicode()
        self.driver.find_element_by_name("brandName").send_keys("{}".format(ss))
        print("商标名称：{}".format(ss))
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.brand-info-wrap.show1.form-wrap > ul > li.brand-upload > div > div.brand-upload-wrap > div.zidongdong-create > ul > li > a").click()

        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#selectCategoryType > label:nth-child(2)").click()

        """商标类别导入历史订单"""
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-right > h3 > div > a.btn.showHistoryOrder").click()
        time.sleep(2)
        history_number = random.randint(2, 10)
        info = self.driver.find_element_by_css_selector(
            "#history_order > li:nth-child({}) > h2".format(history_number)).text
        print("导入历史订单信息:" + info)
        self.driver.find_element_by_css_selector(
            "#history_order > li:nth-child({}) > h2".format(history_number)).click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#history-order > div.modal-button > a").click()
        time.sleep(2)

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.register-pay > div > ul > li.row-step > a").click()


        try:
            self.driver.find_element(By.LINK_TEXT, "确认")
            a = True
        except:
            a = False
        if a is True:
            """不足10小项确认提交"""
            self.driver.find_element_by_link_text("确认").click()
        elif a is False:
            pass


        time.sleep(3)

        # 企业 自然人

        self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > table > thead > tr:nth-child(1) > td.td-content > a:nth-child(2)").click()
        self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys("{}".format(unicode()))
        self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(2) > td.td-content > input").send_keys("dalao")
        self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(4) > td.td-content > input").send_keys("140121199506133513")
        self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(5) > td.td-content.fcountry-container > input.myInput").click()
        self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(5) > td.td-content.fcountry-container > div > div.country-list.country-list-ag.active > span:nth-child(1)").click()
        self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(5) > td.td-title").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(6) > td.td-content > input").send_keys("外国人")
        self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(7) > td.td-content > input").send_keys("waiguoren")
        self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(8) > td.td-content > input").send_keys("laotie")
        self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(9) > td.td-content > input").send_keys("17801188215")
        self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(10) > td.td-content > input").send_keys("1456470136@qq.com")
        self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(11) > td.td-content > input").send_keys("03515925212")

        self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-btns.clearfix > a:nth-child(2)").click()
        time.sleep(2)

        """订单备注"""
        self.driver.find_element_by_css_selector(
            "html body div.register-wrap div.orderinfo-wrap div.order-content textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")



        get_screenshort(self.driver, "test_hwgs_4.png")
        for i in self.driver.find_elements_by_css_selector("body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:"+i.text)
            ii = i.text

        # self.assertIn(aa,ii)
        print("价格一致")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > div > a").click()
        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:"+o.text)
            oo = o.text

        self.assertIn(oo,ii)

        print("测试通过")
        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_hwgs_5(self):
        """海外高速_智能推荐测试"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = DengLuPage(self.driver)
        # 官方推荐有find_element(By.*(""))代替find_element_by_*("")
        # self.driver.find_element_by_id()
        # self.driver.find_element()
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(3) > dd > a:nth-child(4)").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        self.assertIn("海外商标注册|国际商标注册|商标注册流程|商标注册代理-权大师", self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont > ul > li:nth-child(4)").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            # aa = a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("body > div.recommend-help > i").click()
        # body > div.recommend-help > i
        ss = unicode()
        self.driver.find_element_by_name("brandName").send_keys("{}".format(ss))
        print("商标名称：{}".format(ss))
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.brand-info-wrap.show1.form-wrap > ul > li.brand-upload > div > div.brand-upload-wrap > div.zidongdong-create > ul > li > a").click()
        time.sleep(5)

        self.driver.find_element_by_css_selector(
            "#selectCategoryType > label.label.checked").click()
        self.driver.execute_script("window.scrollBy(0,1200)")  # 滑动滚动条

        """智能推荐"""
        self.driver.find_element_by_css_selector("#selectBusiness > div").click()
        industry = random.randint(1, 12)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "#selectBusiness > div > div > div.i-left.scroll > span:nth-child({})".format(industry))).perform()
        ly = self.driver.find_element_by_css_selector(
            "#selectBusiness > div > div > div.i-left.scroll > span:nth-child({})".format(industry)).text
        time.sleep(2)
        sz = random.randint(1, 2)
        hy = self.driver.find_element_by_css_selector(
            "#selectBusiness > div > div > div.i-right.scroll > span:nth-child({})".format(sz)).text
        self.driver.find_element_by_css_selector(
            "#selectBusiness > div > div > div.i-right.scroll > span:nth-child({})".format(sz)).click()
        ActionChains(self.driver).release()

        print("选择所在领域:" + ly + "_" + hy + "_" + "行业精准推荐")
        time.sleep(10)

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.register-pay > div > ul > li.row-step > a").click()

        try:
            self.driver.find_element(By.LINK_TEXT,"确认")
            a = True
        except :
            a = False
        if a is True:
            """不足10小项确认提交"""
            self.driver.find_element_by_link_text("确认").click()
        elif a is False:
            pass


        time.sleep(3)

        # 企业 国外

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys(
            "{}".format(unicode()))
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(2) > td.td-content > input").send_keys(
            "tesr")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(3) > td.td-content.fcountry-container > input.myInput").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(3) > td.td-content.fcountry-container > div > div.country-list.country-list-ag.active > span:nth-child(1)").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(4) > td.td-title").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(4) > td.td-content > input").send_keys(
            "test01")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(5) > td.td-content > input").send_keys(
            "test01")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(6) > td.td-content > input").send_keys(
            "test02")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(7) > td.td-content > input").send_keys(
            "15624992422")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(8) > td.td-content > input").send_keys(
            "4654564@qq.com")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-btns.clearfix > a:nth-child(2)").click()

        """订单备注"""
        self.driver.find_element_by_css_selector(
            "html body div.register-wrap div.orderinfo-wrap div.order-content textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")



        get_screenshort(self.driver, "test_hwgs_1.png")
        for i in self.driver.find_elements_by_css_selector("body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:"+i.text)
            ii = i.text

        # self.assertIn(aa,ii)
        print("价格一致")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > div > a").click()
        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:"+o.text)
            oo = o.text

        self.assertIn(oo,ii)

        print("测试通过")
        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_hwgs_6(self):
        """海外高速_全类保护测试"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = DengLuPage(self.driver)
        # 官方推荐有find_element(By.*(""))代替find_element_by_*("")
        # self.driver.find_element_by_id()
        # self.driver.find_element()
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(3) > dd > a:nth-child(4)").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        self.assertIn("海外商标注册|国际商标注册|商标注册流程|商标注册代理-权大师", self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont > ul > li:nth-child(4)").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            # aa = a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("body > div.recommend-help > i").click()
        # body > div.recommend-help > i
        ss = unicode()
        self.driver.find_element_by_name("brandName").send_keys("{}".format(ss))
        print("商标名称：{}".format(ss))
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.brand-info-wrap.show1.form-wrap > ul > li.brand-upload > div > div.brand-upload-wrap > div.zidongdong-create > ul > li > a").click()
        time.sleep(5)

        """全类保护"""
        self.driver.find_element_by_css_selector(
            "#selectCategoryType > label:nth-child(3)").click()
        time.sleep(20)

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.register-pay > div > ul > li.row-step > a").click()
        time.sleep(2)
        """不足10小项确认提交"""
        self.driver.find_element_by_link_text("确认").click()

        time.sleep(10)

        # 企业 国外

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys(
            "{}".format(unicode()))
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(2) > td.td-content > input").send_keys(
            "tesr")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(3) > td.td-content.fcountry-container > input.myInput").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(3) > td.td-content.fcountry-container > div > div.country-list.country-list-ag.active > span:nth-child(1)").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(4) > td.td-title").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(4) > td.td-content > input").send_keys(
            "test01")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(5) > td.td-content > input").send_keys(
            "test01")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(6) > td.td-content > input").send_keys(
            "test02")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(7) > td.td-content > input").send_keys(
            "15624992422")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(8) > td.td-content > input").send_keys(
            "4654564@qq.com")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-btns.clearfix > a:nth-child(2)").click()

        """订单备注"""
        self.driver.find_element_by_css_selector(
            "html body div.register-wrap div.orderinfo-wrap div.order-content textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")



        get_screenshort(self.driver, "test_hwgs_1.png")
        for i in self.driver.find_elements_by_css_selector("body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:"+i.text)
            ii = i.text

        # self.assertIn(aa,ii)
        print("价格一致")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > div > a").click()
        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:"+o.text)
            oo = o.text

        self.assertIn(oo,ii)

        print("测试通过")
        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_hwgs_7(self):
        """海外高速_添加类别测试"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = DengLuPage(self.driver)
        # 官方推荐有find_element(By.*(""))代替find_element_by_*("")
        # self.driver.find_element_by_id()
        # self.driver.find_element()
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(3) > dd > a:nth-child(4)").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        self.assertIn("海外商标注册|国际商标注册|商标注册流程|商标注册代理-权大师", self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont > ul > li:nth-child(4)").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            # aa = a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("body > div.recommend-help > i").click()
        # body > div.recommend-help > i
        ss = unicode()
        self.driver.find_element_by_name("brandName").send_keys("{}".format(ss))
        print("商标名称：{}".format(ss))
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.brand-info-wrap.show1.form-wrap > ul > li.brand-upload > div > div.brand-upload-wrap > div.zidongdong-create > ul > li > a").click()
        time.sleep(5)

        self.driver.find_element_by_css_selector(
            "#selectCategoryType > label.label.checked").click()
        self.driver.execute_script("window.scrollBy(0,1200)")  # 滑动滚动条

        """智能推荐"""
        self.driver.find_element_by_css_selector("#selectBusiness > div").click()
        industry = random.randint(1, 12)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "#selectBusiness > div > div > div.i-left.scroll > span:nth-child({})".format(industry))).perform()
        ly = self.driver.find_element_by_css_selector(
            "#selectBusiness > div > div > div.i-left.scroll > span:nth-child({})".format(industry)).text
        time.sleep(2)
        sz = random.randint(1, 2)
        hy = self.driver.find_element_by_css_selector(
            "#selectBusiness > div > div > div.i-right.scroll > span:nth-child({})".format(sz)).text
        self.driver.find_element_by_css_selector(
            "#selectBusiness > div > div > div.i-right.scroll > span:nth-child({})".format(sz)).click()
        ActionChains(self.driver).release()

        print("选择所在领域:" + ly + "_" + hy + "_" + "行业精准推荐")
        time.sleep(15)

        # 推荐的类别信息
        list_name = self.driver.find_element_by_css_selector(
            "#section-recommend > div.category-recommend-scroll-box > div > div > div.crs-left.scroll").text

        s_3 = nice(list_name)

        # 点击添加类别

        self.driver.execute_script("window.scrollBy(0,5200)")  # 滑动滚动条
        self.driver.find_element_by_link_text("+ 添加类别").click()
        # 选择类别
        add = self.driver.find_element_by_css_selector(
            "#section-recommend > div > div.add-first-category > ul > li:nth-child({})".format(s_3)).text

        self.driver.find_element_by_css_selector(
            "#section-recommend > div > div.add-first-category > ul > li:nth-child({})".format(s_3)).click()
        # 点击添加小项
        self.driver.find_element_by_css_selector("#first{} > div.category-recommend-groups-box > a".format(s_3)).click()
        # 选择小项
        self.driver.find_element_by_css_selector(
            "#first{} > div.category-recommend-groups-box > div > div > ul > li:nth-child(1)".format(s_3)).click()

        self.driver.find_element_by_css_selector(
            "#first{} > div.category-recommend-groups-box > div > div > div > ul > li:nth-child(1)".format(s_3)).click()
        self.driver.find_element_by_css_selector(
            "#first{} > div.category-recommend-groups-box > div > div > div > ul > li:nth-child(2)".format(s_3)).click()
        self.driver.find_element_by_css_selector(
            "#first{} > div.category-recommend-groups-box > div > div > div > ul > li:nth-child(3)".format(s_3)).click()
        self.driver.find_element_by_css_selector(
            "#first{} > div.category-recommend-groups-box > div > div > div > ul > li:nth-child(4)".format(s_3)).click()
        self.driver.find_element_by_css_selector(
            "#first{} > div.category-recommend-groups-box > div > div > div > ul > li:nth-child(5)".format(s_3)).click()

        print("添加类别:" + add)

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.register-pay > div > ul > li.row-step > a").click()

        try:
            self.driver.find_element(By.LINK_TEXT,"确认")
            a = True
        except :
            a = False
        if a is True:
            """不足10小项确认提交"""
            self.driver.find_element_by_link_text("确认").click()
        elif a is False:
            pass


        time.sleep(3)

        # 企业 国外

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys(
            "{}".format(unicode()))
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(2) > td.td-content > input").send_keys(
            "tesr")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(3) > td.td-content.fcountry-container > input.myInput").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(3) > td.td-content.fcountry-container > div > div.country-list.country-list-ag.active > span:nth-child(1)").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(4) > td.td-title").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(4) > td.td-content > input").send_keys(
            "test01")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(5) > td.td-content > input").send_keys(
            "test01")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(6) > td.td-content > input").send_keys(
            "test02")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(7) > td.td-content > input").send_keys(
            "15624992422")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(8) > td.td-content > input").send_keys(
            "4654564@qq.com")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-btns.clearfix > a:nth-child(2)").click()

        """订单备注"""
        self.driver.find_element_by_css_selector(
            "html body div.register-wrap div.orderinfo-wrap div.order-content textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")



        get_screenshort(self.driver, "test_hwgs_7.png")
        for i in self.driver.find_elements_by_css_selector("body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:"+i.text)
            ii = i.text

        # self.assertIn(aa,ii)
        print("价格一致")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > div > a").click()
        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:"+o.text)
            oo = o.text

        self.assertIn(oo,ii)

        print("测试通过")
        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_hwgs_8(self):
        """海外高速_图形"""

        print("涉及上传文件需要在有界面浏览器测试请执行 uploadtest.py 进行测试!")
        #
        # # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        # #                     format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.DEBUG,
        # #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        # dl = DengLuPage(self.driver)
        # # 官方推荐有find_element(By.*(""))代替find_element_by_*("")
        # # self.driver.find_element_by_id()
        # # self.driver.find_element()
        # dl.login()
        # time.sleep(2)
        # ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
        #     "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        # time.sleep(2)
        # ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
        #     "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 > a")).perform()
        # ActionChains(self.driver).release()
        # self.driver.find_element_by_css_selector(
        #     "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(3) > dd > a:nth-child(4)").click()
        # # 获取打开的多个窗口句柄
        # windows = self.driver.window_handles
        # # 切换到当前最新打开的窗口
        # self.driver.switch_to.window(windows[-1])
        # time.sleep(2)
        # self.driver.set_window_size(1920, 1080)
        # self.assertIn("海外商标注册|国际商标注册|商标注册流程|商标注册代理-权大师", self.driver.title)
        # print(self.driver.title)
        # self.driver.find_element_by_css_selector(
        #     "body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont > ul > li:nth-child(4)").click()
        #
        # for a in self.driver.find_elements_by_css_selector("#total-price"):
        #     print("费用总计:" + a.text)
        #     aa = a.text
        #
        # self.driver.find_element_by_css_selector(
        #     "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        # time.sleep(2)
        # self.driver.find_element_by_css_selector("body > div.recommend-help > i").click()
        # # body > div.recommend-help > i
        #
        # self.driver.find_element_by_css_selector("#selectBrandType > label:nth-child(2)").click()
        # self.driver.find_element_by_css_selector(
        #     "body > div.register-wrap.brandinfo-wrap > div.brand-info-wrap.form-wrap.show3 > ul > li.brand-upload > div > div.brand-upload-wrap > div.shoudong-create > ul > li > div > div > div.photo-box.btnuploadtuyang > div").click()
        #
        # """上传商标图片"""
        # path = driver_path + "\\" + "Upload_files.exe"
        # os.system(path)
        #
        # print("商标图形:小鸡图片")
        #
        # time.sleep(5)
        #
        # self.driver.find_element_by_css_selector(
        #     "#selectCategoryType > label:nth-child(2)").click()
        # self.driver.execute_script("window.scrollBy(0,1200)")  # 滑动滚动条
        # suiji = random.randint(2, 45)
        # time.sleep(2)
        # self.driver.find_element_by_css_selector(
        #     "#section-selfchoice > div > div.group-left > ul > li:nth-child({}) > span".format(suiji)).click()
        #
        # time.sleep(2)
        # self.driver.find_element_by_css_selector(
        #     "#section-selfchoice > div > div.group-left > ul > li.list.open > div:nth-child(2) > span").click()
        #
        # self.driver.find_element_by_css_selector(
        #     "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(1) > span").click()
        # self.driver.find_element_by_css_selector(
        #     "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(2) > span").click()
        # self.driver.find_element_by_css_selector(
        #     "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(3) > span").click()
        # self.driver.find_element_by_css_selector(
        #     "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(4) > span").click()
        # self.driver.find_element_by_css_selector(
        #     "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(5) > span").click()
        #
        # print("选择了第{}类商标分类!".format(suiji))
        #
        # self.driver.find_element_by_css_selector(
        #     "body > div.register-wrap.brandinfo-wrap > div.register-pay > div > ul > li.row-step > a").click()
        #
        # try:
        #     self.driver.find_element(By.LINK_TEXT, "确认")
        #     a = True
        # except:
        #     a = False
        # if a is True:
        #     """不足10小项确认提交"""
        #     self.driver.find_element_by_link_text("确认").click()
        # elif a is False:
        #     pass
        #
        # time.sleep(3)
        #
        # # 企业 国外
        #
        # self.driver.find_element_by_css_selector(
        #     "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys(
        #     "{}".format(unicode()))
        # self.driver.find_element_by_css_selector(
        #     "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(2) > td.td-content > input").send_keys(
        #     "tesr")
        # self.driver.find_element_by_css_selector(
        #     "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(3) > td.td-content.fcountry-container > input.myInput").click()
        # self.driver.find_element_by_css_selector(
        #     "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(3) > td.td-content.fcountry-container > div > div.country-list.country-list-ag.active > span:nth-child(1)").click()
        # self.driver.find_element_by_css_selector(
        #     "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(4) > td.td-title").click()
        # self.driver.find_element_by_css_selector(
        #     "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(4) > td.td-content > input").send_keys(
        #     "test01")
        # self.driver.find_element_by_css_selector(
        #     "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(5) > td.td-content > input").send_keys(
        #     "test01")
        # self.driver.find_element_by_css_selector(
        #     "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(6) > td.td-content > input").send_keys(
        #     "test02")
        # self.driver.find_element_by_css_selector(
        #     "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(7) > td.td-content > input").send_keys(
        #     "15624992422")
        # self.driver.find_element_by_css_selector(
        #     "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(8) > td.td-content > input").send_keys(
        #     "4654564@qq.com")
        # self.driver.find_element_by_css_selector(
        #     "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-btns.clearfix > a:nth-child(2)").click()
        #
        # """订单备注"""
        # self.driver.find_element_by_css_selector(
        #     "html body div.register-wrap div.orderinfo-wrap div.order-content textarea").send_keys(
        #     time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")
        #
        # get_screenshort(self.driver, "test_hwgs_1.png")
        # for i in self.driver.find_elements_by_css_selector(
        #         "body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
        #     print("总价:" + i.text)
        #     ii = i.text
        #
        # self.assertIn(aa, ii)
        # print("价格一致")
        # self.driver.find_element_by_css_selector(
        #     "body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > div > a").click()
        # for o in self.driver.find_elements_by_class_name("payable"):
        #     print("订单提交成功，应付金额:" + o.text)
        #     oo = o.text
        #
        # self.assertIn(oo, ii)
        #
        # print("测试通过")
        # self.driver.find_element_by_css_selector("#alisubmit").click()