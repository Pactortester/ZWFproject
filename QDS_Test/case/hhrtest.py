# coding=utf-8
import random
import re
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from utils.mytestcase import MyTestCase
from utils.logincookie import DengLuPage
from utils.random import unicode
from utils.datachoice import credit_code, xz, nice
from utils.screenshort import get_screenshort


class HhrTest(MyTestCase):
    """合伙中心测试集"""

    def test_partner_modify(self):
        """商标订单修改"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 关闭梦知网的提示
        self.driver.find_element_by_xpath("//span[@class='layui-layer-setwin']/a").click()
        time.sleep(.5)
        # 新版提示
        try:
            self.driver.find_element_by_xpath('//div[@class="hhr-help"]/div[@class="tips tips1"]/a[1]').click()
        except Exception as e:
            print(e)
        try:
            self.driver.find_element_by_xpath('//div[@id="invite-modal"]/div[@class="modal-body"]/a[1]').click()
        except Exception as e:
            print(e)

        self.driver.find_element_by_css_selector(
            "#personalCenter2-leftNav > ul > li.menu.open > ul > li:nth-child(1) > a").click()
        time.sleep(2)
        # 切换成下单时间
        self.driver.find_element_by_class_name("order-time").click()
        # 选择修改的订单号
        print("订单编号:" + self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.order-page > div.tabsPanel > div > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > div > p:nth-child(1)").text)
        # 查看详情
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.order-page > div.tabsPanel > div > div > table > tbody > tr:nth-child(1) > td:nth-child(9) > div.td-handle > a.info").click()
        time.sleep(3)
        """修改商标名字"""

        # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-detail-page > div:nth-child(4) > h2 > a").click()
        # self.driver.find_element_by_css_selector("#modal-brand > div.brandInfo-wrap > div > table > tbody > tr.row-name > td.td-content > input").send_keys("1")
        # self.driver.find_element_by_css_selector("#modal-brand > div.modal-button > a.button.save").click()
        print("商标名字修改成功!")

        time.sleep(1)

        """修改尼斯分类"""
        self.driver.execute_script("window.scrollBy(0,4200)")  # 滑动滚动条

        suiji = random.randint(2, 46)

        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.order-detail-page > div.order-detail-box.order-categories > h2 > a").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-right > div > div > h4 > div.header-right > a > i").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li:nth-child({}) > span".format(suiji)).click()

        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > span").click()

        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(1) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(2) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(3) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(4) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(5) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(6) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(7) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(8) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(9) > span").click()
        # self.driver.find_element_by_css_selector(
        #     "#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(10) > span").click()

        time.sleep(2)

        self.driver.find_element_by_css_selector("#edit-category > div.modal-button > a.button.save").click()

        try:
            self.driver.find_element(By.LINK_TEXT, "确认")
            a = True
        except Exception:
            a = False
        if a is True:
            """不足10小项确认提交"""
            self.driver.find_element_by_link_text("确认").click()
        elif a is False:
            pass

        print("尼斯分类修改为第{}类!".format(suiji - 1))
        time.sleep(10)
        self.driver.execute_script("window.scrollBy(0,6200)")  # 滑动滚动条

        """申请人信息"""

        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.order-detail-page > div.order-detail-box.applicant-info > h2 > a").click()
        self.driver.find_element_by_css_selector(
            "#change-applicant-info > div.modal-body.scroll > div > table > thead > tr:nth-child(1) > td.td-content > a.btn-choice.fownertype.active").click()
        self.driver.find_element_by_css_selector(
            "#change-applicant-info > div.modal-body.scroll > div > div > div > div > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").clear()
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#change-applicant-info > div.modal-body.scroll > div > div > div > div > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys(
            "海航万豪第{}子公司".format(random.randint(1, 1000)))
        time.sleep(2)
        # self.driver.find_element_by_css_selector("#geren-idCard").clear()
        # self.driver.find_element_by_css_selector("#geren-idCard").send_keys("140121198906311532")
        # self.driver.find_element_by_css_selector("#personalssq").click()
        # self.driver.find_element_by_css_selector("#personalistrative > div > div.d-dropdown > div.tab-content.active.tab-province > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        # self.driver.find_element_by_css_selector("#personalistrative > div > div.d-dropdown > div.tab-content.tab-city.active > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        self.driver.find_element_by_css_selector("#change-applicant-info > div.modal-button > a.button.save").click()
        print("申请人信息修改成功!")
        time.sleep(5)

        """订单联系人"""

        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.order-detail-page > div:nth-child(8) > div > h2 > a").click()
        self.driver.find_element_by_css_selector(
            "#change-contact-info > div.section-base > table > tbody.tbody-qiye > tr:nth-child(1) > td.td-content > input").clear()
        self.driver.find_element_by_css_selector(
            "#change-contact-info > div.section-base > table > tbody.tbody-qiye > tr:nth-child(1) > td.td-content > input").send_keys(
            "大西瓜")
        self.driver.find_element_by_css_selector(
            "#change-contact-info > div.section-base > table > tbody.tbody-qiye > tr:nth-child(3) > td.td-content > input").clear()
        self.driver.find_element_by_css_selector(
            "#change-contact-info > div.section-base > table > tbody.tbody-qiye > tr:nth-child(3) > td.td-content > input").send_keys(
            "m15624992422@163.com")
        self.driver.find_element_by_css_selector("#change-contact-info > div.modal-button > a.button.save").click()

        print("订单联系人修改成功!")
        time.sleep(1)
        get_screenshort(self.driver, "test_partner_modify.png")
        print("订单修改测试通过!")

    def test_hhr_order_1(self):

        """合伙人商标注册_企业"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 关闭梦知网的提示
        self.driver.find_element_by_xpath("//span[@class='layui-layer-setwin']/a").click()
        time.sleep(.5)
        # 新版提示
        try:
            self.driver.find_element_by_xpath('//div[@class="hhr-help"]/div[@class="tips tips1"]/a[1]').click()
        except Exception as e:
            print(e)
        try:
            self.driver.find_element_by_xpath('//div[@id="invite-modal"]/div[@class="modal-body"]/a[1]').click()
        except Exception as e:
            print(e)
        self.driver.find_element_by_link_text("商标注册").click()

        """填写商标信息"""

        self.driver.find_element_by_css_selector("#selectBrandType > label.label.checked").click()
        ss = unicode()
        self.driver.find_element_by_name("brandName").send_keys("{}".format(ss))
        print("商标名称：{}".format(ss))
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        self.driver.find_element_by_link_text("生成黑白图样").click()
        print("商标名称填写成功!")

        time.sleep(5)
        self.driver.find_element_by_css_selector("#selectCategoryType > label:nth-child(2)").click()
        self.driver.execute_script("window.scrollBy(0,500)")  # 滑动滚动条

        """商标类别"""
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
        time.sleep(3)

        for i in self.driver.find_elements_by_css_selector(
                "#personalCenter2-rightContainer > div > div.order-form-page > div > div.smartRegister-section > div.order-categories-calc > div.order-categories-total > span.span-total > strong > i"):
            print("总价:" + i.text)
            ii = i.text

        self.driver.execute_script("window.scrollBy(0,1000)")  # 滑动滚动条
        """申请人信息"""

        self.driver.find_element_by_css_selector("#selectOwnerType > label.label.fownertype.active").click()
        self.driver.find_element_by_css_selector("#overseastype > label.label.checked").click()
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.agentInfo-wrap > div > div > div > div > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys(
            "文思海辉技术有限公司{}".format(random.randint(1, 1000)))
        self.driver.find_element_by_xpath("//*[@id=\"ssq\"]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id=\"companylistrative\"]/div/div[2]/div[1]/dl[1]/dd/span[1]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id=\"companylistrative\"]/div/div[2]/div[2]/dl[2]/dd/span[1]").click()
        time.sleep(1)

        # 添加社会信用代码
        self.driver.find_element_by_name("creditcode").send_keys(credit_code("credit_code.txt"))

        print("申请人信息填写成功!")

        """客户联系人信息"""
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(1) > input").send_keys(
            "dalao")
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(2) > input").send_keys(
            "15624992488")
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(3) > input").send_keys(
            "1456470136@qq.com")

        print("联系人信息填写成功!")

        """订单改价"""

        self.driver.find_element_by_name("customPrice").clear()
        new_total = int(str(ii).replace(".00", "")) + 500
        self.driver.find_element_by_name("customPrice").send_keys(new_total)
        print("改价:增加500服务费!")

        """订单备注"""
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.message-box > ul > li > textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div:nth-child(7) > div > a.mybtn.mybtn-inverse.mybtn-lg.saveAll").click()

        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-detail-fix > div > div.right.change-price > div.pay-btns > a:nth-child(2)").click()

        time.sleep(2)

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

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = int(str(o.text).replace(".00", ""))

        time.sleep(2)
        self.assertEqual(oo, new_total)

        self.driver.find_element_by_css_selector("#payways > ul:nth-child(1) > li").click()
        self.driver.find_element_by_css_selector("#alisubmit").click()

        print("价格一致")

        print("合伙人订单下单成功!")

        get_screenshort(self.driver, "test_hhr_order_1.png")

        pay_url = self.driver.find_element_by_class_name("pay_url").get_attribute("value")
        print("订单链接:" + pay_url)

        self.driver.find_element_by_link_text("复制").click()

        print("订单已发送客户付款!")

        # 订单url校验

        self.driver.get(pay_url)
        print(self.driver.title)
        print(self.driver.current_url)
        time.sleep(2)
        order_number = self.driver.find_element_by_css_selector(
            "#table-contract > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(2)").text
        order_time = self.driver.find_element_by_css_selector(
            "#table-contract > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(4)").text
        if order_time == '':
            self.assertEqual(1, 2, "付款链接异常请及时查看!")
        else:
            print("订单编号:" + order_number)

    def test_hhr_order_2(self):

        """合伙人商标注册_智能推荐"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 关闭梦知网的提示
        self.driver.find_element_by_xpath("//span[@class='layui-layer-setwin']/a").click()
        time.sleep(.5)
        # 新版提示
        try:
            self.driver.find_element_by_xpath('//div[@class="hhr-help"]/div[@class="tips tips1"]/a[1]').click()
        except Exception as e:
            print(e)
        try:
            self.driver.find_element_by_xpath('//div[@id="invite-modal"]/div[@class="modal-body"]/a[1]').click()
        except Exception as e:
            print(e)
        self.driver.find_element_by_link_text("商标注册").click()

        """填写商标信息"""

        self.driver.find_element_by_css_selector("#selectBrandType > label.label.checked").click()
        ss = unicode()
        self.driver.find_element_by_name("brandName").send_keys("{}".format(ss))
        print("商标名称：{}".format(ss))
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        self.driver.find_element_by_link_text("生成黑白图样").click()
        print("商标名称填写成功!")

        time.sleep(5)
        self.driver.find_element_by_css_selector("#selectCategoryType > label.label.checked").click()
        self.driver.execute_script("window.scrollBy(0,500)")  # 滑动滚动条

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

        for i in self.driver.find_elements_by_css_selector(
                "#personalCenter2-rightContainer > div > div.order-form-page > div > div.smartRegister-section > div.order-categories-calc > div.order-categories-total > span.span-total > strong > i"):
            print("总价:" + i.text)
            ii = i.text

        self.driver.execute_script("window.scrollBy(0,1000)")  # 滑动滚动条
        """申请人信息"""
        self.driver.find_element_by_css_selector("#selectOwnerType > label.label.fownertype.active").click()
        self.driver.find_element_by_css_selector("#overseastype > label.label.checked").click()
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.agentInfo-wrap > div > div > div > div > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys(
            "文思海辉技术有限公司{}".format(random.randint(1, 1000)))
        self.driver.find_element_by_xpath("//*[@id=\"ssq\"]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id=\"companylistrative\"]/div/div[2]/div[1]/dl[1]/dd/span[1]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id=\"companylistrative\"]/div/div[2]/div[2]/dl[2]/dd/span[1]").click()
        time.sleep(1)

        # 添加社会信用代码
        self.driver.find_element_by_name("creditcode").send_keys(credit_code("credit_code.txt"))

        print("申请人信息填写成功!")

        """客户联系人信息"""
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(1) > input").send_keys(
            "dalao")
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(2) > input").send_keys(
            "15624992488")
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(3) > input").send_keys(
            "1456470136@qq.com")

        print("联系人信息填写成功!")

        """订单改价"""

        self.driver.find_element_by_name("customPrice").clear()
        new_total = int(str(ii).replace(".00", "")) + 500
        self.driver.find_element_by_name("customPrice").send_keys(new_total)
        print("改价:增加500服务费!")

        """订单备注"""
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.message-box > ul > li > textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div:nth-child(7) > div > a.mybtn.mybtn-inverse.mybtn-lg.saveAll").click()

        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-detail-fix > div > div.right.change-price > div.pay-btns > a:nth-child(2)").click()

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

        time.sleep(2)

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = int(str(o.text).replace(".00", ""))

        time.sleep(2)
        self.assertEqual(oo, new_total)

        self.driver.find_element_by_css_selector("#payways > ul:nth-child(1) > li").click()
        self.driver.find_element_by_css_selector("#alisubmit").click()

        print("价格一致")

        print("合伙人订单下单成功!")

        get_screenshort(self.driver, "test_hhr_order_2.png")

        pay_url = self.driver.find_element_by_class_name("pay_url").get_attribute("value")
        print("订单链接:" + pay_url)

        self.driver.find_element_by_link_text("复制").click()

        print("订单已发送客户付款!")

        # 订单url校验

        self.driver.get(pay_url)
        print(self.driver.title)
        print(self.driver.current_url)
        time.sleep(2)
        order_number = self.driver.find_element_by_css_selector(
            "#table-contract > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(2)").text
        order_time = self.driver.find_element_by_css_selector(
            "#table-contract > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(4)").text
        if order_time == '':
            self.assertEqual(1, 2, "付款链接异常请及时查看!")
        else:
            print("订单编号:" + order_number)

    def test_hhr_order_3(self):

        """合伙人商标注册_全类保护"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 关闭梦知网的提示
        self.driver.find_element_by_xpath("//span[@class='layui-layer-setwin']/a").click()
        time.sleep(.5)
        # 新版提示
        try:
            self.driver.find_element_by_xpath('//div[@class="hhr-help"]/div[@class="tips tips1"]/a[1]').click()
        except Exception as e:
            print(e)
        try:
            self.driver.find_element_by_xpath('//div[@id="invite-modal"]/div[@class="modal-body"]/a[1]').click()
        except Exception as e:
            print(e)
        self.driver.find_element_by_link_text("商标注册").click()

        """填写商标信息"""

        self.driver.find_element_by_css_selector("#selectBrandType > label.label.checked").click()
        ss = unicode()
        self.driver.find_element_by_name("brandName").send_keys("{}".format(ss))
        print("商标名称：{}".format(ss))
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        self.driver.find_element_by_link_text("生成黑白图样").click()
        print("商标名称填写成功!")

        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0,500)")  # 滑动滚动条

        """全类保护"""
        self.driver.find_element_by_css_selector(
            "#selectCategoryType > label:nth-child(3)").click()

        time.sleep(20)

        for i in self.driver.find_elements_by_css_selector(
                "#personalCenter2-rightContainer > div > div.order-form-page > div > div.smartRegister-section > div.order-categories-calc > div.order-categories-total > span.span-total > strong > i"):
            print("总价:" + i.text)
            ii = i.text

        self.driver.execute_script("window.scrollBy(0,1000)")  # 滑动滚动条
        """申请人信息"""
        self.driver.find_element_by_css_selector("#selectOwnerType > label.label.fownertype.active").click()
        self.driver.find_element_by_css_selector("#overseastype > label.label.checked").click()
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.agentInfo-wrap > div > div > div > div > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys(
            "文思海辉技术有限公司{}".format(random.randint(1, 1000)))
        self.driver.find_element_by_xpath("//*[@id=\"ssq\"]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id=\"companylistrative\"]/div/div[2]/div[1]/dl[1]/dd/span[1]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id=\"companylistrative\"]/div/div[2]/div[2]/dl[2]/dd/span[1]").click()
        time.sleep(1)

        # 添加社会信用代码
        self.driver.find_element_by_name("creditcode").send_keys(credit_code("credit_code.txt"))

        print("申请人信息填写成功!")

        """客户联系人信息"""
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(1) > input").send_keys(
            "dalao")
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(2) > input").send_keys(
            "15624992488")
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(3) > input").send_keys(
            "1456470136@qq.com")

        print("联系人信息填写成功!")

        """订单改价"""

        self.driver.find_element_by_name("customPrice").clear()
        new_total = int(str(ii).replace(".00", "")) + 500
        self.driver.find_element_by_name("customPrice").send_keys(new_total)
        print("改价:增加500服务费!")

        """订单备注"""
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.message-box > ul > li > textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div:nth-child(7) > div > a.mybtn.mybtn-inverse.mybtn-lg.saveAll").click()

        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-detail-fix > div > div.right.change-price > div.pay-btns > a:nth-child(2)").click()

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

        time.sleep(2)

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = int(str(o.text).replace(".00", ""))

        time.sleep(2)
        self.assertEqual(oo, new_total)

        self.driver.find_element_by_css_selector("#payways > ul:nth-child(1) > li").click()
        self.driver.find_element_by_css_selector("#alisubmit").click()

        print("价格一致")

        print("合伙人订单下单成功!")

        get_screenshort(self.driver, "test_hhr_order_3.png")

        pay_url = self.driver.find_element_by_class_name("pay_url").get_attribute("value")
        print("订单链接:" + pay_url)

        self.driver.find_element_by_link_text("复制").click()

        print("订单已发送客户付款!")

        # 订单url校验

        self.driver.get(pay_url)
        print(self.driver.title)
        print(self.driver.current_url)
        time.sleep(2)
        order_number = self.driver.find_element_by_css_selector(
            "#table-contract > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(2)").text
        order_time = self.driver.find_element_by_css_selector(
            "#table-contract > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(4)").text
        if order_time == '':
            self.assertEqual(1, 2, "付款链接异常请及时查看!")
        else:
            print("订单编号:" + order_number)

    def test_hhr_order_4(self):

        """合伙人商标注册_添加类别"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 关闭梦知网的提示
        self.driver.find_element_by_xpath("//span[@class='layui-layer-setwin']/a").click()
        time.sleep(.5)
        # 新版提示
        try:
            self.driver.find_element_by_xpath('//div[@class="hhr-help"]/div[@class="tips tips1"]/a[1]').click()
        except Exception as e:
            print(e)
        try:
            self.driver.find_element_by_xpath('//div[@id="invite-modal"]/div[@class="modal-body"]/a[1]').click()
        except Exception as e:
            print(e)
        self.driver.find_element_by_link_text("商标注册").click()

        """填写商标信息"""

        self.driver.find_element_by_css_selector("#selectBrandType > label.label.checked").click()
        ss = unicode()
        self.driver.find_element_by_name("brandName").send_keys("{}".format(ss))
        print("商标名称：{}".format(ss))
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        self.driver.find_element_by_link_text("生成黑白图样").click()
        print("商标名称填写成功!")

        time.sleep(5)
        self.driver.find_element_by_css_selector("#selectCategoryType > label.label.checked").click()
        self.driver.execute_script("window.scrollBy(0,500)")  # 滑动滚动条

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

        # 推荐的类别信息
        list_name = self.driver.find_element_by_css_selector(
            "#section-recommend > div.category-recommend-scroll-box > div > div > div.crs-left.scroll").text

        # s_1 = re.findall(r"\d+",list_name)
        # s_2 = ['01','02','03','04','05','06','07','08','09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20' ,'21', '22' ,'23' ,'24' ,'25', '26' ,'27', '28', '29', '30' ,'31' ,'32' ,'33' ,'34' ,'35' ,'36', '37', '38', '39' ,'40' ,'41', '42', '43' ,'44','45']
        #
        # # s_2中有而s_1中没有的
        # s_3 = random.choice(list(set(s_2).difference(set(s_1))))

        s_3 = nice(list_name)

        # 点击添加类别

        self.driver.execute_script("window.scrollBy(0,4200)")  # 滑动滚动条
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
        time.sleep(5)

        for i in self.driver.find_elements_by_css_selector(
                "#personalCenter2-rightContainer > div > div.order-form-page > div > div.smartRegister-section > div.order-categories-calc > div.order-categories-total > span.span-total > strong > i"):
            print("总价:" + i.text)
            ii = i.text

        self.driver.execute_script("window.scrollBy(0,1000)")  # 滑动滚动条
        """申请人信息"""
        self.driver.find_element_by_css_selector("#selectOwnerType > label.label.fownertype.active").click()
        self.driver.find_element_by_css_selector("#overseastype > label.label.checked").click()
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.agentInfo-wrap > div > div > div > div > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys(
            "文思海辉技术有限公司{}".format(random.randint(1, 1000)))
        self.driver.find_element_by_xpath("//*[@id=\"ssq\"]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id=\"companylistrative\"]/div/div[2]/div[1]/dl[1]/dd/span[1]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id=\"companylistrative\"]/div/div[2]/div[2]/dl[2]/dd/span[1]").click()
        time.sleep(1)

        # 添加社会信用代码
        self.driver.find_element_by_name("creditcode").send_keys(credit_code("credit_code.txt"))

        print("申请人信息填写成功!")

        """客户联系人信息"""
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(1) > input").send_keys(
            "dalao")
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(2) > input").send_keys(
            "15624992488")
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(3) > input").send_keys(
            "1456470136@qq.com")

        print("联系人信息填写成功!")

        """订单改价"""

        self.driver.find_element_by_name("customPrice").clear()
        new_total = int(str(ii).replace(".00", "")) + 500
        self.driver.find_element_by_name("customPrice").send_keys(new_total)
        print("改价:增加500服务费!")

        """订单备注"""
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.message-box > ul > li > textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div:nth-child(7) > div > a.mybtn.mybtn-inverse.mybtn-lg.saveAll").click()

        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-detail-fix > div > div.right.change-price > div.pay-btns > a:nth-child(2)").click()

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

        time.sleep(2)

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = int(str(o.text).replace(".00", ""))

        time.sleep(2)
        self.assertEqual(oo, new_total)

        self.driver.find_element_by_css_selector("#payways > ul:nth-child(1) > li").click()
        self.driver.find_element_by_css_selector("#alisubmit").click()

        print("价格一致")

        print("合伙人订单下单成功!")

        get_screenshort(self.driver, "test_hhr_order_3.png")

        pay_url = self.driver.find_element_by_class_name("pay_url").get_attribute("value")
        print("订单链接:" + pay_url)

        self.driver.find_element_by_link_text("复制").click()

        print("订单已发送客户付款!")

        # 订单url校验

        self.driver.get(pay_url)
        print(self.driver.title)
        print(self.driver.current_url)
        time.sleep(2)
        order_number = self.driver.find_element_by_css_selector(
            "#table-contract > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(2)").text
        order_time = self.driver.find_element_by_css_selector(
            "#table-contract > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(4)").text
        if order_time == '':
            self.assertEqual(1, 2, "付款链接异常请及时查看!")
        else:
            print("订单编号:" + order_number)

    def test_hhr_order_5(self):

        """合伙人商标注册_添加类别（金额校验）"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 关闭梦知网的提示
        self.driver.find_element_by_xpath("//span[@class='layui-layer-setwin']/a").click()
        time.sleep(.5)
        # 新版提示
        try:
            self.driver.find_element_by_xpath('//div[@class="hhr-help"]/div[@class="tips tips1"]/a[1]').click()
        except Exception as e:
            print(e)
        try:
            self.driver.find_element_by_xpath('//div[@id="invite-modal"]/div[@class="modal-body"]/a[1]').click()
        except Exception as e:
            print(e)
        self.driver.find_element_by_link_text("商标注册").click()

        """填写商标信息"""

        self.driver.find_element_by_css_selector("#selectBrandType > label.label.checked").click()
        ss = unicode()
        self.driver.find_element_by_name("brandName").send_keys("{}".format(ss))
        print("商标名称：{}".format(ss))
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        self.driver.find_element_by_link_text("生成黑白图样").click()
        print("商标名称填写成功!")

        time.sleep(5)
        self.driver.find_element_by_css_selector("#selectCategoryType > label.label.checked").click()
        self.driver.execute_script("window.scrollBy(0,500)")  # 滑动滚动条

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

        time.sleep(5)

        number_1 = self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.smartRegister-section > div.order-categories-calc > div.order-categories-total > span.span-total > strong > i").text

        number_2 = re.sub(r"\D", "", number_1)

        number_3 = int(number_2) + 0
        print(number_3)

        # 推荐的类别信息
        list_name = self.driver.find_element_by_css_selector(
            "#section-recommend > div.category-recommend-scroll-box > div > div > div.crs-left.scroll").text

        # s_1 = re.findall(r"\d+",list_name)
        # s_2 = ['01','02','03','04','05','06','07','08','09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20' ,'21', '22' ,'23' ,'24' ,'25', '26' ,'27', '28', '29', '30' ,'31' ,'32' ,'33' ,'34' ,'35' ,'36', '37', '38', '39' ,'40' ,'41', '42', '43' ,'44','45']
        #
        # # s_2中有而s_1中没有的
        # s_3 = random.choice(list(set(s_2).difference(set(s_1))))

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
        # self.driver.find_element_by_css_selector(
        #     "#first{} > div.category-recommend-groups-box > div > div > ul > li:nth-child(1)".format(s_3)).click()
        #
        # self.driver.find_element_by_css_selector(
        #     "#first{} > div.category-recommend-groups-box > div > div > div > ul > li:nth-child(1)".format(s_3)).click()
        # self.driver.find_element_by_css_selector(
        #     "#first{} > div.category-recommend-groups-box > div > div > div > ul > li:nth-child(2)".format(s_3)).click()
        # self.driver.find_element_by_css_selector(
        #     "#first{} > div.category-recommend-groups-box > div > div > div > ul > li:nth-child(3)".format(s_3)).click()
        # self.driver.find_element_by_css_selector(
        #     "#first{} > div.category-recommend-groups-box > div > div > div > ul > li:nth-child(4)".format(s_3)).click()
        # self.driver.find_element_by_css_selector(
        #     "#first{} > div.category-recommend-groups-box > div > div > div > ul > li:nth-child(5)".format(s_3)).click()

        print("添加类别:" + add)
        time.sleep(5)

        number_4 = self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.smartRegister-section > div.order-categories-calc > div.order-categories-total > span.span-total > strong > i").text

        number_5 = re.sub(r"\D", "", number_4)

        number_6 = int(number_5) + 0
        print(number_6)

        self.assertEqual(number_3, number_6, "价格异常请及时查看!")

        print("合伙人商标注册_添加类别（金额校验）,测试通过!")

    def test_hhr_order_6(self):

        """合伙人商标注册_图形"""

        print("涉及上传文件需要在有界面浏览器测试请执行 uploadtest.py 进行测试!")
        # dl = DengLuPage(self.driver)
        # dl.login()
        # time.sleep(1)
        #
        # self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        # time.sleep(1)
        # # 新版提示
        # self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div[1]/div/a").click()
        # self.driver.find_element_by_link_text("商标注册").click()
        #
        # """填写商标信息"""
        #
        # self.driver.find_element_by_css_selector("#selectBrandType > label:nth-child(2)").click()
        # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div.smartRegister-section > div.register-wrap.brandinfo-wrap > div.brand-info-wrap.form-wrap.show3 > ul > li.brand-upload > div > div.brand-upload-wrap > div.shoudong-create > ul > li > div > div > div.photo-box.btnuploadtuyang > div").click()
        # time.sleep(2)
        #
        # """上传商标图片"""
        # path = driver_path + "\\" + "Upload_files.exe"
        # os.system(path)
        # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div.smartRegister-section > div.register-wrap.brandinfo-wrap > div.brand-info-wrap.form-wrap.show3 > ul > li.brand-fcontent > div > textarea").send_keys("小鸡图片")
        #
        # print("商标图形:小鸡图片")
        #
        # time.sleep(5)
        # self.driver.find_element_by_css_selector("#selectCategoryType > label:nth-child(2)").click()
        # self.driver.execute_script("window.scrollBy(0,500)")  # 滑动滚动条
        #
        # """商标类别"""
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
        # self.driver.find_element_by_css_selector(
        #     "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(6) > span").click()
        # self.driver.find_element_by_css_selector(
        #     "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(7) > span").click()
        # self.driver.find_element_by_css_selector(
        #     "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(8) > span").click()
        # self.driver.find_element_by_css_selector(
        #     "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(9) > span").click()
        # self.driver.find_element_by_css_selector(
        #     "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(10) > span").click()
        #
        # print("选择了第{}类商标分类!".format(suiji))
        # time.sleep(3)
        #
        # for i in self.driver.find_elements_by_css_selector(
        #         "#personalCenter2-rightContainer > div > div.order-form-page > div > div.smartRegister-section > div.order-categories-calc > div.order-categories-total > span.span-total > strong > i"):
        #     print("总价:" + i.text)
        #     ii = i.text
        #
        #
        # self.driver.execute_script("window.scrollBy(0,1000)")  # 滑动滚动条
        # """申请人信息"""
        #
        # self.driver.find_element_by_css_selector("#selectOwnerType > label.label.fownertype.active").click()
        # self.driver.find_element_by_css_selector("#overseastype > label.label.checked").click()
        # self.driver.find_element_by_css_selector(
        #     "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.agentInfo-wrap > div > div > div > div > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys(
        #     "文思海辉技术有限公司{}".format(random.randint(1, 1000)))
        # self.driver.find_element_by_xpath("//*[@id=\"ssq\"]").click()
        # time.sleep(3)
        # self.driver.find_element_by_xpath("//*[@id=\"companylistrative\"]/div/div[2]/div[1]/dl[1]/dd/span[1]").click()
        # time.sleep(3)
        # self.driver.find_element_by_xpath("//*[@id=\"companylistrative\"]/div/div[2]/div[2]/dl[2]/dd/span[1]").click()
        # time.sleep(1)
        #
        # # 添加社会信用代码
        # self.driver.find_element_by_name("creditcode").send_keys(credit_code("credit_code.txt"))
        #
        # print("申请人信息填写成功!")
        #
        # """客户联系人信息"""
        # self.driver.find_element_by_css_selector(
        #     "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(1) > input").send_keys(
        #     "dalao")
        # self.driver.find_element_by_css_selector(
        #     "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(2) > input").send_keys(
        #     "15624992488")
        # self.driver.find_element_by_css_selector(
        #     "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(3) > input").send_keys(
        #     "1456470136@qq.com")
        #
        # print("联系人信息填写成功!")
        #
        # """订单改价"""
        #
        # self.driver.find_element_by_name("customPrice").clear()
        # new_total = int(str(ii).replace(".00", "")) + 500
        # self.driver.find_element_by_name("customPrice").send_keys(new_total)
        # print("改价:增加500服务费!")
        #
        # """订单备注"""
        # self.driver.find_element_by_css_selector(
        #     "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.message-box > ul > li > textarea").send_keys(
        #     time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")
        #
        # # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div:nth-child(7) > div > a.mybtn.mybtn-inverse.mybtn-lg.saveAll").click()
        #
        #
        # self.driver.find_element_by_css_selector(
        #     "#personalCenter2-rightContainer > div > div.order-detail-fix > div > div.right.change-price > div.pay-btns > a:nth-child(2)").click()
        #
        # time.sleep(2)
        #
        # for o in self.driver.find_elements_by_class_name("payable"):
        #     print("订单提交成功，应付金额:" + o.text)
        #     oo = int(str(o.text).replace(".00", ""))
        # get_screenshort(self.driver,"test.png")
        #
        # time.sleep(2)
        # self.assertEqual(oo, new_total)
        #
        # self.driver.find_element_by_css_selector("#payways > ul:nth-child(1) > li").click()
        # self.driver.find_element_by_css_selector("#alisubmit").click()
        #
        # print("价格一致")
        #
        # print("合伙人订单下单成功!")
        #
        # get_screenshort(self.driver, "test_hhr_order_1.png")
        #
        # pay_url = self.driver.find_element_by_class_name("pay_url").get_attribute("value")
        # print("订单链接:" + pay_url)
        #
        # self.driver.find_element_by_link_text("复制").click()
        #
        # print("订单已发送客户付款!")
        #
        # # 订单url校验
        #
        # self.driver.get(pay_url)
        # print(self.driver.title)
        # print(self.driver.current_url)
        # time.sleep(2)
        # order_number = self.driver.find_element_by_css_selector(
        #     "#table-contract > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(2)").text
        # order_time = self.driver.find_element_by_css_selector(
        #     "#table-contract > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(4)").text
        # if order_time == '':
        #     self.assertEqual(1, 2, "付款链接异常请及时查看!")
        # else:
        #     print("订单编号:" + order_number)

    def test_hhr_historical_1(self):

        """合伙人商标注册_随机历史订单"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 关闭梦知网的提示
        self.driver.find_element_by_xpath("//span[@class='layui-layer-setwin']/a").click()
        time.sleep(.5)
        # 新版提示
        try:
            self.driver.find_element_by_xpath('//div[@class="hhr-help"]/div[@class="tips tips1"]/a[1]').click()
        except Exception as e:
            print(e)
        try:
            self.driver.find_element_by_xpath('//div[@id="invite-modal"]/div[@class="modal-body"]/a[1]').click()
        except Exception as e:
            print(e)
        self.driver.find_element_by_link_text("商标注册").click()

        """填写商标信息"""

        self.driver.find_element_by_css_selector("#selectBrandType > label.label.checked").click()
        ss = unicode()
        self.driver.find_element_by_name("brandName").send_keys("{}".format(ss))
        print("商标名称：{}".format(ss))
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        self.driver.find_element_by_link_text("生成黑白图样").click()
        print("商标名称填写成功!")

        time.sleep(5)
        self.driver.find_element_by_css_selector("#selectCategoryType > label:nth-child(2)").click()
        self.driver.execute_script("window.scrollBy(0,500)")  # 滑动滚动条

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
        time.sleep(5)

        for i in self.driver.find_elements_by_css_selector(
                "#personalCenter2-rightContainer > div > div.order-form-page > div > div.smartRegister-section > div.order-categories-calc > div.order-categories-total > span.span-total > strong > i"):
            print("总价:" + i.text)
            ii = i.text

        self.driver.execute_script("window.scrollBy(0,1000)")  # 滑动滚动条
        """申请人信息"""
        self.driver.find_element_by_css_selector("#selectOwnerType > label.label.fownertype.active").click()
        self.driver.find_element_by_css_selector("#overseastype > label.label.checked").click()
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.agentInfo-wrap > div > div > div > div > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys(
            "文思海辉技术有限公司{}".format(random.randint(1, 1000)))
        self.driver.find_element_by_xpath("//*[@id=\"ssq\"]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id=\"companylistrative\"]/div/div[2]/div[1]/dl[1]/dd/span[1]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id=\"companylistrative\"]/div/div[2]/div[2]/dl[2]/dd/span[1]").click()
        time.sleep(1)

        # 添加社会信用代码
        self.driver.find_element_by_name("creditcode").send_keys(credit_code("credit_code.txt"))

        print("申请人信息填写成功!")

        """客户联系人信息"""
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(1) > input").send_keys(
            "dalao")
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(2) > input").send_keys(
            "15624992488")
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(3) > input").send_keys(
            "1456470136@qq.com")

        print("联系人信息填写成功!")

        """订单改价"""

        self.driver.find_element_by_name("customPrice").clear()
        new_total = int(str(ii).replace(".00", "")) + 500
        self.driver.find_element_by_name("customPrice").send_keys(new_total)
        print("改价:增加500服务费!")

        """订单备注"""
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.message-box > ul > li > textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div:nth-child(7) > div > a.mybtn.mybtn-inverse.mybtn-lg.saveAll").click()

        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-detail-fix > div > div.right.change-price > div.pay-btns > a:nth-child(2)").click()

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

        time.sleep(2)

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = int(str(o.text).replace(".00", ""))

        time.sleep(2)
        self.assertEqual(oo, new_total)

        self.driver.find_element_by_css_selector("#payways > ul:nth-child(1) > li").click()
        self.driver.find_element_by_css_selector("#alisubmit").click()

        print("价格一致")

        print("合伙人订单下单成功!")

        get_screenshort(self.driver, "test_hhr_historical_1.png")

        pay_url = self.driver.find_element_by_class_name("pay_url").get_attribute("value")
        print("订单链接:" + pay_url)

        self.driver.find_element_by_link_text("复制").click()

        print("订单已发送客户付款!")

        # 订单url校验

        self.driver.get(pay_url)
        print(self.driver.title)
        print(self.driver.current_url)
        time.sleep(2)
        order_number = self.driver.find_element_by_css_selector(
            "#table-contract > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(2)").text
        order_time = self.driver.find_element_by_css_selector(
            "#table-contract > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(4)").text
        if order_time == '':
            self.assertEqual(1, 2, "付款链接异常请及时查看!")
        else:
            print("订单编号:" + order_number)

    def test_hhr_historical_2(self):

        """合伙人商标注册_默认历史订单"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 关闭梦知网的提示
        self.driver.find_element_by_xpath("//span[@class='layui-layer-setwin']/a").click()
        time.sleep(.5)
        # 新版提示
        try:
            self.driver.find_element_by_xpath('//div[@class="hhr-help"]/div[@class="tips tips1"]/a[1]').click()
        except Exception as e:
            print(e)
        try:
            self.driver.find_element_by_xpath('//div[@id="invite-modal"]/div[@class="modal-body"]/a[1]').click()
        except Exception as e:
            print(e)
        self.driver.find_element_by_link_text("商标注册").click()

        """填写商标信息"""

        self.driver.find_element_by_css_selector("#selectBrandType > label.label.checked").click()
        ss = unicode()
        self.driver.find_element_by_name("brandName").send_keys("{}".format(ss))
        print("商标名称：{}".format(ss))
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        self.driver.find_element_by_link_text("生成黑白图样").click()
        print("商标名称填写成功!")

        time.sleep(5)
        self.driver.find_element_by_css_selector("#selectCategoryType > label:nth-child(2)").click()
        self.driver.execute_script("window.scrollBy(0,500)")  # 滑动滚动条

        """商标类别导入历史订单"""
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-right > h3 > div > a.btn.showHistoryOrder").click()
        time.sleep(2)
        history_number = 2
        info = self.driver.find_element_by_css_selector(
            "#history_order > li:nth-child({}) > h2".format(history_number)).text
        print("导入历史订单信息:" + info)
        self.driver.find_element_by_css_selector("#history-order > div.modal-button > a").click()
        time.sleep(2)

        for i in self.driver.find_elements_by_css_selector(
                "#personalCenter2-rightContainer > div > div.order-form-page > div > div.smartRegister-section > div.order-categories-calc > div.order-categories-total > span.span-total > strong > i"):
            print("总价:" + i.text)
            ii = i.text

        self.driver.execute_script("window.scrollBy(0,1000)")  # 滑动滚动条
        """申请人信息"""
        self.driver.find_element_by_css_selector("#selectOwnerType > label.label.fownertype.active").click()
        self.driver.find_element_by_css_selector("#overseastype > label.label.checked").click()
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.agentInfo-wrap > div > div > div > div > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys(
            "文思海辉技术有限公司{}".format(random.randint(1, 1000)))
        self.driver.find_element_by_xpath("//*[@id=\"ssq\"]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id=\"companylistrative\"]/div/div[2]/div[1]/dl[1]/dd/span[1]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id=\"companylistrative\"]/div/div[2]/div[2]/dl[2]/dd/span[1]").click()
        time.sleep(1)

        # 添加社会信用代码
        self.driver.find_element_by_name("creditcode").send_keys(credit_code("credit_code.txt"))

        print("申请人信息填写成功!")

        """客户联系人信息"""
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(1) > input").send_keys(
            "dalao")
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(2) > input").send_keys(
            "15624992488")
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(3) > input").send_keys(
            "1456470136@qq.com")

        print("联系人信息填写成功!")

        """订单改价"""

        self.driver.find_element_by_name("customPrice").clear()
        new_total = int(str(ii).replace(".00", "")) + 500
        self.driver.find_element_by_name("customPrice").send_keys(new_total)
        print("改价:增加500服务费!")

        """订单备注"""
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.message-box > ul > li > textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div:nth-child(7) > div > a.mybtn.mybtn-inverse.mybtn-lg.saveAll").click()

        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-detail-fix > div > div.right.change-price > div.pay-btns > a:nth-child(2)").click()

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

        time.sleep(2)

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = int(str(o.text).replace(".00", ""))

        time.sleep(2)
        self.assertEqual(oo, new_total)

        self.driver.find_element_by_css_selector("#payways > ul:nth-child(1) > li").click()
        self.driver.find_element_by_css_selector("#alisubmit").click()

        print("价格一致")

        print("合伙人订单下单成功!")

        get_screenshort(self.driver, "test_hhr_historical_2.png")

        pay_url = self.driver.find_element_by_class_name("pay_url").get_attribute("value")
        print("订单链接:" + pay_url)

        self.driver.find_element_by_link_text("复制").click()

        print("订单已发送客户付款!")

        # 订单url校验

        self.driver.get(pay_url)
        print(self.driver.title)
        print(self.driver.current_url)
        time.sleep(2)
        order_number = self.driver.find_element_by_css_selector(
            "#table-contract > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(2)").text
        order_time = self.driver.find_element_by_css_selector(
            "#table-contract > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(4)").text
        if order_time == '':
            self.assertEqual(1, 2, "付款链接异常请及时查看!")
        else:
            print("订单编号:" + order_number)

    def test_hhr_historical_3(self):

        """合伙人商标注册_重复历史订单"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 关闭梦知网的提示
        self.driver.find_element_by_xpath("//span[@class='layui-layer-setwin']/a").click()
        time.sleep(.5)
        # 新版提示
        try:
            self.driver.find_element_by_xpath('//div[@class="hhr-help"]/div[@class="tips tips1"]/a[1]').click()
        except Exception as e:
            print(e)
        try:
            self.driver.find_element_by_xpath('//div[@id="invite-modal"]/div[@class="modal-body"]/a[1]').click()
        except Exception as e:
            print(e)
        self.driver.find_element_by_link_text("商标注册").click()

        """填写商标信息"""

        self.driver.find_element_by_css_selector("#selectBrandType > label.label.checked").click()
        ss = unicode()
        self.driver.find_element_by_name("brandName").send_keys("{}".format(ss))
        print("商标名称：{}".format(ss))
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        self.driver.find_element_by_link_text("生成黑白图样").click()
        print("商标名称填写成功!")

        time.sleep(5)
        self.driver.find_element_by_css_selector("#selectCategoryType > label:nth-child(2)").click()
        self.driver.execute_script("window.scrollBy(0,500)")  # 滑动滚动条

        """商标类别导入历史订单_1"""
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-right > h3 > div > a.btn.showHistoryOrder").click()
        time.sleep(2)
        history_number_1 = 3
        info = self.driver.find_element_by_css_selector(
            "#history_order > li:nth-child({}) > h2".format(history_number_1)).text
        print("导入历史订单信息:" + info)
        self.driver.find_element_by_css_selector(
            "#history_order > li:nth-child({}) > h2".format(history_number_1)).click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#history-order > div.modal-button > a").click()
        time.sleep(3)

        """商标类别导入历史订单_2"""

        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-right > h3 > div > a.btn.showHistoryOrder").click()
        time.sleep(2)
        history_number_2 = 2
        info = self.driver.find_element_by_css_selector(
            "#history_order > li:nth-child({}) > h2".format(history_number_2)).text
        print("导入历史订单信息:" + info)
        self.driver.find_element_by_css_selector(
            "#history_order > li:nth-child({}) > h2".format(history_number_2)).click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#history-order > div.modal-button > a").click()
        time.sleep(3)

        """商标类别导入历史订单_3"""

        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-right > h3 > div > a.btn.showHistoryOrder").click()
        time.sleep(2)
        history_number_3 = 4
        info = self.driver.find_element_by_css_selector(
            "#history_order > li:nth-child({}) > h2".format(history_number_3)).text
        print("导入历史订单信息:" + info)
        self.driver.find_element_by_css_selector(
            "#history_order > li:nth-child({}) > h2".format(history_number_3)).click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#history-order > div.modal-button > a").click()
        time.sleep(5)

        for i in self.driver.find_elements_by_css_selector(
                "#personalCenter2-rightContainer > div > div.order-form-page > div > div.smartRegister-section > div.order-categories-calc > div.order-categories-total > span.span-total > strong > i"):
            print("总价:" + i.text)
            ii = i.text

        self.driver.execute_script("window.scrollBy(0,1000)")  # 滑动滚动条
        """申请人信息"""
        self.driver.find_element_by_css_selector("#selectOwnerType > label.label.fownertype.active").click()
        self.driver.find_element_by_css_selector("#overseastype > label.label.checked").click()
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.agentInfo-wrap > div > div > div > div > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys(
            "文思海辉技术有限公司{}".format(random.randint(1, 1000)))
        self.driver.find_element_by_xpath("//*[@id=\"ssq\"]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id=\"companylistrative\"]/div/div[2]/div[1]/dl[1]/dd/span[1]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id=\"companylistrative\"]/div/div[2]/div[2]/dl[2]/dd/span[1]").click()
        time.sleep(1)

        # 添加社会信用代码
        self.driver.find_element_by_name("creditcode").send_keys(credit_code("credit_code.txt"))

        print("申请人信息填写成功!")

        """客户联系人信息"""
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(1) > input").send_keys(
            "dalao")
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(2) > input").send_keys(
            "15624992488")
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(3) > input").send_keys(
            "1456470136@qq.com")

        print("联系人信息填写成功!")

        """订单改价"""

        self.driver.find_element_by_name("customPrice").clear()
        new_total = int(str(ii).replace(".00", "")) + 500
        self.driver.find_element_by_name("customPrice").send_keys(new_total)
        print("改价:增加500服务费!")

        """订单备注"""
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.message-box > ul > li > textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div:nth-child(7) > div > a.mybtn.mybtn-inverse.mybtn-lg.saveAll").click()

        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-detail-fix > div > div.right.change-price > div.pay-btns > a:nth-child(2)").click()

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

        time.sleep(2)

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = int(str(o.text).replace(".00", ""))

        time.sleep(2)
        self.assertEqual(oo, new_total)

        self.driver.find_element_by_css_selector("#payways > ul:nth-child(1) > li").click()
        self.driver.find_element_by_css_selector("#alisubmit").click()

        print("价格一致")

        print("合伙人订单下单成功!")

        get_screenshort(self.driver, "test_hhr_historical_3.png")

        pay_url = self.driver.find_element_by_class_name("pay_url").get_attribute("value")
        print("订单链接:" + pay_url)

        self.driver.find_element_by_link_text("复制").click()

        print("订单已发送客户付款!")

        # 订单url校验

        self.driver.get(pay_url)
        print(self.driver.title)
        print(self.driver.current_url)
        time.sleep(2)
        order_number = self.driver.find_element_by_css_selector(
            "#table-contract > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(2)").text
        order_time = self.driver.find_element_by_css_selector(
            "#table-contract > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(4)").text
        if order_time == '':
            self.assertEqual(1, 2, "付款链接异常请及时查看!")
        else:
            print("订单编号:" + order_number)

    @staticmethod
    def test_channel():
        """渠道下单单个商标注册"""
        print("此账号无渠道下单!")
        # dl = DengLuPage(self.driver)
        # dl.login()
        # time.sleep(1)
        #
        # self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        # time.sleep(1)
        # # 新版提示
        # self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div[1]/div/a").click()
        # self.driver.find_element_by_link_text("渠道下单").click()
        #
        # """填写渠道账号"""
        # self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div/div[1]/div[2]/div[1]/dl/dt/input").clear()
        # self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div/div[1]/div[2]/div[1]/dl/dt/input").send_keys("15122311450")
        # self.driver.find_element_by_xpath("//*[@id=\"inquirer\"]").clear()
        # self.driver.find_element_by_xpath("//*[@id=\"inquirer\"]").send_keys("15624992422")
        #
        #
        #
        # """填写商标信息"""
        #
        # self.driver.find_element_by_xpath("//*[@id=\"selectBrandType\"]/label[1]").click()
        # ss = unicode()
        # self.driver.find_element_by_name("brandName").send_keys("{}".format(ss))
        # self.driver.find_element_by_xpath("//*[@id=\"create-tuyang\"]/label[2]").click()
        # self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div/div[1]/div[3]/div[1]/div[1]/table/tbody/tr[4]/td[2]/div[3]/ul/li/div[2]/a").click()
        # time.sleep(2)
        # print("商标名称:{}".format(ss))
        # print("商标名称填写成功!")
        #
        # self.driver.execute_script("window.scrollBy(0,500)")  # 滑动滚动条
        #
        # """商标类别"""
        # suiji = random.randint(1,46)
        # self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div/div[1]/div[3]/div[1]/div[1]/table/tbody/tr[5]/td[2]/a[2]").click()
        #
        # self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li:nth-child({}) > span".format(suiji)).click()
        # time.sleep(2)
        # self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > span").click()
        # time.sleep(2)
        # self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(1) > span").click()
        # self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(2) > span").click()
        # self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(3) > span").click()
        # self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(4) > span").click()
        # self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(5) > span").click()
        # self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(6) > span").click()
        # self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(7) > span").click()
        # self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(8) > span").click()
        # self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(9) > span").click()
        # self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(10) > span").click()
        #
        # print("选择了第{}类商标分类".format(suiji))
        #
        # # for i in self.driver.find_elements_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.order-categories > div.order-categories-total > span.span-total > strong > i"):
        # #     print("总价:"+i.text)
        # #     ii=i.text
        #
        # self.driver.execute_script("window.scrollBy(0,1000)")  # 滑动滚动条
        """申请人信息"""
        #
        # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.smartRegister-page.smartRegister-page-source2.smartRegister-page-personal > div:nth-child(5) > div.agentInfo-wrap.agentInfo-wrap-in > div > table > thead > tr > td.td-content > a.btn-choice.fownertype.active").click()
        # self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div/div[1]/div[4]/div[1]/div/table/tbody[1]/tr[1]/td[2]/dl/dt/input").clear()
        # self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div/div[1]/div[4]/div[1]/div/table/tbody[1]/tr[1]/td[2]/dl/dt/input").send_keys(unicode())
        # self.driver.find_element_by_xpath("//*[@id=\"ssq\"]").click()
        # self.driver.find_element_by_xpath("//*[@id=\"myadministrative\"]/div/div[2]/div[1]/dl[1]/dd/span[1]").click()
        # self.driver.find_element_by_xpath("//*[@id=\"myadministrative\"]/div/div[2]/div[2]/dl[2]/dd/span[1]").click()
        # self.driver.find_element_by_name("fcontactName").clear()
        # self.driver.find_element_by_name("fcontactName").send_keys("蔡妍妍")
        # self.driver.find_element_by_name("fcontactTel").clear()
        # self.driver.find_element_by_name("fcontactTel").send_keys("17801188215")
        # self.driver.find_element_by_name("ftelephone").send_keys("4001005678")
        # self.driver.find_element_by_name("fcontactMail").send_keys("m15624992422@qq.com")
        # print("申请人信息填写成功!")
        #
        # get_screenshort(self.driver, "test_channel.png")
        # for o in self.driver.find_elements_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div/div[1]/div[5]/div/ul/li[3]/em/i"):
        #     print("订单提交成功，应付金额:"+o.text)
        #     # oo = o.text
        #
        # # self.assertIn(oo,ii)
        # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.section8 > div > a").click()

    def test_full_business_1(self):

        """合伙人(商标)全业务测试"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 关闭梦知网的提示
        self.driver.find_element_by_xpath("//span[@class='layui-layer-setwin']/a").click()
        time.sleep(.5)
        # 新版提示
        try:
            self.driver.find_element_by_xpath('//div[@class="hhr-help"]/div[@class="tips tips1"]/a[1]').click()
        except Exception as e:
            print(e)
        try:
            self.driver.find_element_by_xpath('//div[@id="invite-modal"]/div[@class="modal-body"]/a[1]').click()
        except Exception as e:
            print(e)
        self.driver.find_element_by_link_text("业务对接").click()

        self.driver.find_element_by_name("username").send_keys(unicode())
        self.driver.find_element_by_name("phone").send_keys("15624992498")
        self.driver.find_element_by_name("email").send_keys("145647@qq.com")

        """业务信息"""
        self.driver.find_element_by_css_selector("#addBusinessMgsBox > ul > li:nth-child(1) > div > input").click()
        time.sleep(2)
        lx = random.randint(1, 12)
        # lx = 2
        yw = self.driver.find_element_by_css_selector(
            "#addBusinessMgsBox > ul > li:nth-child(1) > div > dl > dd:nth-child(2)").text
        print(yw)
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#addBusinessMgsBox > ul > li:nth-child(1) > div > dl > dd:nth-child(2)").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#addBusinessMgsBox > ul > li:nth-child(2) > div > input").click()
        xm = self.driver.find_element_by_css_selector(
            "#addBusinessMgsBox > ul > li:nth-child(2) > div > dl > dd:nth-child({})".format(lx)).text
        print(xm)
        self.driver.find_element_by_css_selector(
            "#addBusinessMgsBox > ul > li:nth-child(2) > div > dl > dd:nth-child({})".format(lx)).click()
        time.sleep(2)
        print("业务需求:" + yw + "_" + xm)

        brand_name = unicode()
        self.driver.find_element_by_name("brandName").send_keys(brand_name)
        application_number = xz("famousTrandMark.txt")
        self.driver.find_element_by_name("applicationNumber").send_keys(application_number)
        time.sleep(2)

        price = self.driver.find_element_by_name("price").get_attribute("value")
        print("订单价格:" + price)
        income = self.driver.find_element_by_css_selector(
            "#addBusinessMgsBox > div.numAndPrice.clearfix > div.profitNum > span.earning.income-estimate").text
        print("收益预估:" + str(income))

        """订单备注"""
        self.driver.find_element_by_css_selector(
            "#addBusinessMgsBox > div.businessRemark > textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        """保存信息"""
        self.driver.find_element_by_css_selector("#saveBusMsgBtn").click()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#saveConfirmOrder").click()
        time.sleep(2)
        """订单确认"""
        get_screenshort(self.driver, "test_full_business_1.png")
        self.driver.find_element_by_css_selector("#saveOrder").click()
        time.sleep(2)

        self.driver.find_element_by_css_selector(
            "#layui-layer1 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn0").click()

        total = self.driver.find_element_by_css_selector("#total-price").text
        print("订单提交成功，应付金额:" + total)
        self.assertIn(price, total)
        print("价格一致！")

        self.driver.find_element_by_css_selector("#payways > ul:nth-child(1) > li > span").click()
        self.driver.find_element_by_css_selector("#alisubmit").click()
        order_url = self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.paying-wrap.paying-sk-wrap.paying-sk-hhr > div.paying-sk-ewm > div.link > input").get_attribute(
            "value")

        print("订单链接:" + order_url)
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.paying-wrap.paying-sk-wrap.paying-sk-hhr > div.paying-sk-ewm > div.link > a").click()

        print("订单已发送客户付款!")

        # 订单url校验

        self.driver.get(order_url)
        print(self.driver.title)
        time.sleep(2)
        order_number = self.driver.find_element_by_css_selector(
            "body > div > section.section-applybaseinfo.pay-info.pay-infoall > ul > table > tbody > tr:nth-child(2) > td.pay-platform-charge").text
        order_charge = self.driver.find_element_by_css_selector(
            "body > div > section.section-applybaseinfo.pay-info.pay-infoall > ul > table > tbody > tr:nth-child(3) > td.pay-platform-charge").text
        if order_charge == '':
            self.assertEqual(1, 2, "h5链接异常请及时查看!")
        else:
            print("订单编号:" + order_number)

    def test_full_business_2(self):

        """合伙人(其他)全业务测试"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 关闭梦知网的提示
        self.driver.find_element_by_xpath("//span[@class='layui-layer-setwin']/a").click()
        time.sleep(.5)
        # 新版提示
        try:
            self.driver.find_element_by_xpath('//div[@class="hhr-help"]/div[@class="tips tips1"]/a[1]').click()
        except Exception as e:
            print(e)
        try:
            self.driver.find_element_by_xpath('//div[@id="invite-modal"]/div[@class="modal-body"]/a[1]').click()
        except Exception as e:
            print(e)
        self.driver.find_element_by_link_text("业务对接").click()

        self.driver.find_element_by_name("username").send_keys("AAA")
        self.driver.find_element_by_name("phone").send_keys("15624992498")
        self.driver.find_element_by_name("email").send_keys("145647@qq.com")
        try:
            while True:
                ActionChains(self.driver).move_to_element_with_offset(self.driver.find_element_by_class_name("businessItemMsg"), 5, 5).perform()
                self.driver.find_element_by_class_name("delet").click()
                time.sleep(.5)
                self.driver.find_element_by_class_name("layui-layer-btn0").click()
                time.sleep(.5)
        except Exception as e:
            print(e)

        """业务信息"""
        self.driver.find_element_by_id("showAddBox").click()
        self.driver.find_element_by_css_selector("#addBusinessMgsBox > ul > li:nth-child(1) > div > input").click()
        time.sleep(2)
        lx = random.randint(1, 3)
        qt = random.randint(3, 4)
        yw = self.driver.find_element_by_css_selector(
            "#addBusinessMgsBox > ul > li:nth-child(1) > div > dl > dd:nth-child({})".format(qt)).text
        print(yw)
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#addBusinessMgsBox > ul > li:nth-child(1) > div > dl > dd:nth-child({})".format(qt)).click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#addBusinessMgsBox > ul > li:nth-child(2) > div > input").click()
        xm = self.driver.find_element_by_css_selector(
            "#addBusinessMgsBox > ul > li:nth-child(2) > div > dl > dd:nth-child({})".format(lx)).text
        print(xm)
        self.driver.find_element_by_css_selector(
            "#addBusinessMgsBox > ul > li:nth-child(2) > div > dl > dd:nth-child({})".format(lx)).click()
        time.sleep(2)
        print("业务需求:" + yw + "_" + xm)

        time.sleep(2)

        price = self.driver.find_element_by_name("price").get_attribute("value")
        print("订单价格:" + price)
        income = self.driver.find_element_by_css_selector(
            "#addBusinessMgsBox > div.numAndPrice.clearfix > div.profitNum > span.earning.income-estimate").text
        print("收益预估:" + str(income))

        """订单备注"""
        self.driver.find_element_by_css_selector(
            "#addBusinessMgsBox > div.businessRemark > textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        """保存信息"""
        self.driver.find_element_by_css_selector("#saveBusMsgBtn").click()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#saveConfirmOrder").click()
        time.sleep(2)
        """订单确认"""
        get_screenshort(self.driver, "test_full_business_1.png")
        self.driver.find_element_by_css_selector("#saveOrder").click()
        time.sleep(2)

        self.driver.find_element_by_css_selector(
            "#layui-layer1 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn0").click()

        total = self.driver.find_element_by_css_selector("#total-price").text
        print("订单提交成功，应付金额:" + total)
        self.assertIn(price, total)
        print("价格一致！")

        self.driver.find_element_by_css_selector("#payways > ul:nth-child(1) > li > span").click()
        self.driver.find_element_by_css_selector("#alisubmit").click()
        order_url = self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.paying-wrap.paying-sk-wrap.paying-sk-hhr > div.paying-sk-ewm > div.link > input").get_attribute(
            "value")

        print("订单链接:" + order_url)
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.paying-wrap.paying-sk-wrap.paying-sk-hhr > div.paying-sk-ewm > div.link > a").click()

        print("订单已发送客户付款!")

        # 订单url校验

        self.driver.get(order_url)
        print(self.driver.title)
        time.sleep(2)
        order_number = self.driver.find_element_by_css_selector(
            "body > div > section.section-applybaseinfo.pay-info.pay-infoall > ul > table > tbody > tr:nth-child(2) > td.pay-platform-charge").text
        order_charge = self.driver.find_element_by_css_selector(
            "body > div > section.section-applybaseinfo.pay-info.pay-infoall > ul > table > tbody > tr:nth-child(3) > td.pay-platform-charge").text
        if order_charge == '':
            self.assertEqual(1, 2, "h5链接异常请及时查看!")
        else:
            print("订单编号:" + order_number)

    def test_full_business_3(self):

        """全业务收益预估测试"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 关闭梦知网的提示
        self.driver.find_element_by_xpath("//span[@class='layui-layer-setwin']/a").click()
        time.sleep(.5)
        # 新版提示
        try:
            self.driver.find_element_by_xpath('//div[@class="hhr-help"]/div[@class="tips tips1"]/a[1]').click()
        except Exception as e:
            print(e)
        try:
            self.driver.find_element_by_xpath('//div[@id="invite-modal"]/div[@class="modal-body"]/a[1]').click()
        except Exception as e:
            print(e)
        self.driver.find_element_by_link_text("业务对接").click()

        self.driver.find_element_by_name("username").send_keys(unicode())
        self.driver.find_element_by_name("phone").send_keys("15624992498")
        self.driver.find_element_by_name("email").send_keys("145647@qq.com")

        """业务信息"""
        # 添加业务
        self.driver.find_element_by_xpath("//p[@class=\"addBusinessBtn\"]/a").click()
        self.driver.find_element_by_css_selector("#addBusinessMgsBox > ul > li:nth-child(1) > div > input").click()
        time.sleep(2)
        lx = random.randint(1, 3)
        qt = random.randint(3, 4)
        yw = self.driver.find_element_by_css_selector(
            "#addBusinessMgsBox > ul > li:nth-child(1) > div > dl > dd:nth-child({})".format(qt)).text
        print(yw)
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#addBusinessMgsBox > ul > li:nth-child(1) > div > dl > dd:nth-child({})".format(qt)).click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#addBusinessMgsBox > ul > li:nth-child(2) > div > input").click()
        xm = self.driver.find_element_by_css_selector(
            "#addBusinessMgsBox > ul > li:nth-child(2) > div > dl > dd:nth-child({})".format(lx)).text
        print(xm)
        self.driver.find_element_by_css_selector(
            "#addBusinessMgsBox > ul > li:nth-child(2) > div > dl > dd:nth-child({})".format(lx)).click()
        time.sleep(2)
        print("业务需求:" + yw + "_" + xm)

        time.sleep(2)

        """3次点击"""

        # self.driver.find_element_by_class_name("input-add").click()
        count_1 = self.driver.find_element_by_class_name("serveNum").get_attribute("value")
        print("订单数量:" + count_1)
        price_1 = self.driver.find_element_by_class_name("orderPrice").get_attribute("value")
        print("订单价格:" + price_1)

        income_1 = self.driver.find_element_by_css_selector(
            "#addBusinessMgsBox > div.numAndPrice.clearfix > div.profitNum > span.earning.income-estimate").text
        print("收益预估:" + str(income_1))
        time.sleep(3)

        self.driver.find_element_by_xpath("//div[@class=\"order-needs-num\"]/a[@class=\"input-add\"]").click()
        time.sleep(2)
        count_2 = self.driver.find_element_by_class_name("serveNum").get_attribute("value")
        print("订单数量:" + count_2)
        price_2 = self.driver.find_element_by_class_name("orderPrice").get_attribute("value")
        print("订单价格:" + price_2)
        income_2 = self.driver.find_element_by_css_selector(
            "#addBusinessMgsBox > div.numAndPrice.clearfix > div.profitNum > span.earning.income-estimate").text
        print("收益预估:" + str(income_2))
        time.sleep(3)

        """收益校验"""
        if int(price_2) > int(price_1):
            pass
        else:
            self.assertEqual(1, 2, "收益预估异常,请及时查看!")

        self.driver.find_element_by_class_name("input-add").click()
        time.sleep(2)
        count_3 = self.driver.find_element_by_class_name("serveNum").get_attribute("value")
        print("订单数量:" + count_3)
        price_3 = self.driver.find_element_by_class_name("orderPrice").get_attribute("value")
        print("订单价格:" + price_3)
        income_3 = self.driver.find_element_by_css_selector(
            "#addBusinessMgsBox > div.numAndPrice.clearfix > div.profitNum > span.earning.income-estimate").text
        print("收益预估:" + str(income_3))

        print("全业务收益预估测试通过!")
        get_screenshort(self.driver, "test_full_business_3.png")

    def test_calc_1(self):

        """全业务计算器测试"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 关闭梦知网的提示
        self.driver.find_element_by_xpath("//span[@class='layui-layer-setwin']/a").click()
        time.sleep(.5)
        # 新版提示
        try:
            self.driver.find_element_by_xpath('//div[@class="hhr-help"]/div[@class="tips tips1"]/a[1]').click()
        except Exception as e:
            print(e)
        try:
            self.driver.find_element_by_xpath('//div[@id="invite-modal"]/div[@class="modal-body"]/a[1]').click()
        except Exception as e:
            print(e)

        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.home-page.userInfo > div.article1.home-page-top.clearfix > div.article-bottom-link > ul > li.income_calc > a > img").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#calculateModal > div > div.step.income-calc-box > div.modal-body > form > ul > li:nth-child(1) > div > input").click()
        lx = random.randint(1, 3)
        yw = self.driver.find_element_by_css_selector(
            "#calculateModal > div > div.step.income-calc-box > div.modal-body > form > ul > li:nth-child(1) > div > dl > dd:nth-child({})".format(
                lx)).text
        print("业务类型:" + str(yw))
        self.driver.find_element_by_css_selector(
            "#calculateModal > div > div.step.income-calc-box > div.modal-body > form > ul > li:nth-child(1) > div > dl > dd:nth-child({})".format(
                lx)).click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#calculateModal > div > div.step.income-calc-box > div.modal-body > form > ul > li:nth-child(2) > div > input").click()
        xm = self.driver.find_element_by_css_selector(
            "#calculateModal > div > div.step.income-calc-box > div.modal-body > form > ul > li:nth-child(2) > div > dl > dd:nth-child(2)").text

        self.driver.find_element_by_css_selector(
            "#calculateModal > div > div.step.income-calc-box > div.modal-body > form > ul > li:nth-child(2) > div > dl > dd:nth-child(2)").click()
        print("服务项目:" + str(xm))

        self.driver.find_element_by_css_selector(
            "#calculateModal > div > div.step.income-calc-box > div.modal-button > a.button.calculate").click()
        time.sleep(2)
        income = self.driver.find_element_by_css_selector(
            "#calculateModal > div > div.step.income-calc-box > div.modal-body > form > ul > li:nth-child(6) > strong").text

        print("您的收益:" + str(income))

        self.driver.find_element_by_css_selector(
            "#calculateModal > div > div.step.income-calc-box > div.modal-button > a.button.button-white.income_detail_btn").click()
        time.sleep(2)

        num = self.driver.find_element_by_css_selector(
            "#calculateModal > div > div.step.income-detail-box > div.modal-body > table > tbody > tr:nth-child(4) > td.td-content.incomeNum").text
        print("案件数量:" + str(num))
        price = self.driver.find_element_by_css_selector(
            "#calculateModal > div > div.step.income-detail-box > div.modal-body > table > tbody > tr:nth-child(3) > td.td-content.serviceCharge").text
        print("案件服务费:" + str(price))
        official = self.driver.find_element_by_css_selector(
            "#calculateModal > div > div.step.income-detail-box > div.modal-body > table > tbody > tr:nth-child(5) > td.td-content.officialCharge").text
        print("案件官费:" + str(official))

        lastincome = self.driver.find_element_by_css_selector(
            "#calculateModal > div > div.step.income-detail-box > div.income-detail-bottom > span > strong").text
        print("最后收益:" + str(lastincome))

        get_screenshort(self.driver, "test_calc_1.png")

        self.assertIn(str(income), str(lastincome))

        print("收益一致,测试通过!")

    def test_calc_2(self):

        """右侧计算器测试"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 关闭梦知网的提示
        self.driver.find_element_by_xpath("//span[@class='layui-layer-setwin']/a").click()
        time.sleep(.5)
        # 新版提示
        try:
            self.driver.find_element_by_xpath('//div[@class="hhr-help"]/div[@class="tips tips1"]/a[1]').click()
        except Exception as e:
            print(e)
        try:
            self.driver.find_element_by_xpath('//div[@id="invite-modal"]/div[@class="modal-body"]/a[1]').click()
        except Exception as e:
            print(e)
        self.driver.find_element_by_css_selector(
            "body > div.public-fixrightbar > ul > li.list.fixright-calc.income_calc").click()

        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#calculateModal > div > div.step.income-calc-box > div.modal-body > form > ul > li:nth-child(1) > div > input").click()
        lx = random.randint(1, 3)
        yw = self.driver.find_element_by_css_selector(
            "#calculateModal > div > div.step.income-calc-box > div.modal-body > form > ul > li:nth-child(1) > div > dl > dd:nth-child({})".format(
                lx)).text
        print("业务类型:" + str(yw))
        self.driver.find_element_by_css_selector(
            "#calculateModal > div > div.step.income-calc-box > div.modal-body > form > ul > li:nth-child(1) > div > dl > dd:nth-child({})".format(
                lx)).click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#calculateModal > div > div.step.income-calc-box > div.modal-body > form > ul > li:nth-child(2) > div > input").click()
        xm = self.driver.find_element_by_css_selector(
            "#calculateModal > div > div.step.income-calc-box > div.modal-body > form > ul > li:nth-child(2) > div > dl > dd:nth-child(2)").text

        self.driver.find_element_by_css_selector(
            "#calculateModal > div > div.step.income-calc-box > div.modal-body > form > ul > li:nth-child(2) > div > dl > dd:nth-child(2)").click()
        print("服务项目:" + str(xm))

        self.driver.find_element_by_css_selector(
            "#calculateModal > div > div.step.income-calc-box > div.modal-button > a.button.calculate").click()
        time.sleep(2)
        income = self.driver.find_element_by_css_selector(
            "#calculateModal > div > div.step.income-calc-box > div.modal-body > form > ul > li:nth-child(6) > strong").text

        print("您的收益:" + str(income))

        self.driver.find_element_by_css_selector(
            "#calculateModal > div > div.step.income-calc-box > div.modal-button > a.button.button-white.income_detail_btn").click()
        time.sleep(2)

        num = self.driver.find_element_by_css_selector(
            "#calculateModal > div > div.step.income-detail-box > div.modal-body > table > tbody > tr:nth-child(4) > td.td-content.incomeNum").text
        print("案件数量:" + str(num))
        price = self.driver.find_element_by_css_selector(
            "#calculateModal > div > div.step.income-detail-box > div.modal-body > table > tbody > tr:nth-child(3) > td.td-content.serviceCharge").text
        print("案件服务费:" + str(price))
        official = self.driver.find_element_by_css_selector(
            "#calculateModal > div > div.step.income-detail-box > div.modal-body > table > tbody > tr:nth-child(5) > td.td-content.officialCharge").text
        print("案件官费:" + str(official))

        lastincome = self.driver.find_element_by_css_selector(
            "#calculateModal > div > div.step.income-detail-box > div.income-detail-bottom > span > strong").text
        print("最后收益:" + str(lastincome))

        get_screenshort(self.driver, "test_calc_2.png")

        self.assertIn(str(income), str(lastincome))

        print("收益一致,测试通过!")

    # def test_partner_clue_1(self):
    #
    #     """合伙人认领线索"""
    #     dl = DengLuPage(self.driver)
    #     dl.login()
    #     time.sleep(1)
    #
    #     self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
    #     time.sleep(1)
    #     # 新版提示
    #     self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div[1]/div/a").click()
    #     self.driver.find_element_by_css_selector("#personalCenter2-leftNav > ul > li.menu.open > ul > li:nth-child(2) > a").click()
    #
    #
    #     try:
    #         self.driver.find_element(By.CSS_SELECTOR,"#personalCenter2-rightContainer > div > div.nav > a")
    #         a = True
    #     except:
    #         a = False
    #     if a is True:
    #         print("当前无线索,点击申请!")
    #         self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.nav > a").click()
    #         time.sleep(4)
    #         clue = self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > table > tbody > tr").text
    #         print(str(clue).replace("\n", " ").replace("认领",""))
    #         self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > table > tbody > tr > td.td-handle > a").click()  # tr-a claim_clue
    #     elif a is False:
    #         print("线索存在!")
    #         time.sleep(2)
    #         clue = self.driver.find_element_by_css_selector(
    #             "#personalCenter2-rightContainer > div > table > tbody > tr").text
    #         print(str(clue).replace("\n", " ").replace("认领",""))
    #         self.driver.find_element_by_css_selector(
    #             "#personalCenter2-rightContainer > div > table > tbody > tr > td.td-handle > a").click()
    #     get_screenshort(self.driver,"test_partner_clue_1.png")
    #
    # def test_partner_clue_2(self):
    #
    #     """合伙人线索下单"""
    #     dl = DengLuPage(self.driver)
    #     dl.login()
    #     time.sleep(1)
    #
    #     self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
    #     time.sleep(1)
    #     # 新版提示
    #     self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div[1]/div/a").click()
    #     self.driver.find_element_by_css_selector("#personalCenter2-leftNav > ul > li.menu.open > ul > li:nth-child(2) > a").click()
    #
    #     """已认领 第一条线索信息"""
    #     self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.partner > a.not_select").click()
    #     info = self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > table > tbody > tr").text
    #     print("线索详情:" + (str(info).replace("\n" ," ")).replace("查看详情",""))
    #
    #     self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > table > tbody > tr > td.td-handle > a").click()
    #
    #     """切换窗口打开详情"""
    #     windows = self.driver.window_handles
    #     self.driver.switch_to.window(windows[-1])
    #     time.sleep(2)
    #     self.driver.set_window_size(1920, 1080)
    #
    #     # """关掉时间提示"""
    #     # self.driver.find_element_by_css_selector("#layui-layer1 > span.layui-layer-setwin > a").click()
    #     get_screenshort(self.driver,"test_partner_clue_2.png")
    #
    #     """点击下单"""
    #     self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-detail-fix > div > div.right > div.pay-btns > a:nth-child(2)").click()
    #     time.sleep(2)
    #
    #     """判断客户邮箱是否为空"""
    #     email = self.driver.find_element_by_name("email").get_attribute("value")
    #     if email == "无":
    #         self.driver.find_element_by_name("email").clear()
    #         self.driver.find_element_by_name("email").send_keys("test@quandashi.com")
    #         print("客户邮箱:" + self.driver.find_element_by_name("email").get_attribute("value"))
    #     else:
    #         print("客户邮箱:" + self.driver.find_element_by_name("email").get_attribute("value"))
    #         pass
    #
    #     price = self.driver.find_element_by_name("price").get_attribute("value")
    #     print("订单价格:" + price)
    #     income = self.driver.find_element_by_css_selector(
    #         "#addBusinessMgsBox > div.numAndPrice.clearfix > div.profitNum > span.earning.income-estimate").text
    #     print("收益预估:" + str(income))
    #
    #     """订单备注"""
    #     self.driver.find_element_by_css_selector("#addBusinessMgsBox > div.businessRemark > textarea").send_keys(
    #         time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")
    #
    #     """保存信息"""
    #     self.driver.find_element_by_css_selector("#saveBusMsgBtn").click()
    #     time.sleep(1)
    #
    #     self.driver.find_element_by_css_selector("#saveConfirmOrder").click()
    #     time.sleep(2)
    #     """订单确认"""
    #     get_screenshort(self.driver, "test_full_business_1.png")
    #     self.driver.find_element_by_css_selector("#saveOrder").click()
    #     time.sleep(2)
    #
    #     self.driver.find_element_by_css_selector(
    #         "#layui-layer1 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn0").click()
    #
    #     total = self.driver.find_element_by_css_selector("#total-price").text
    #     print("订单提交成功，应付金额:" + total)
    #     self.assertIn(price, total)
    #     print("价格一致！")
    #
    #     self.driver.find_element_by_css_selector("#payways > ul:nth-child(1) > li > span").click()
    #     self.driver.find_element_by_css_selector("#alisubmit").click()
    #     order_url = self.driver.find_element_by_css_selector(
    #         "#personalCenter2-rightContainer > div.paying-wrap.paying-sk-wrap.paying-sk-hhr > div.paying-sk-ewm > div.link > input").get_attribute(
    #         "value")
    #
    #     print("订单链接:" + order_url)
    #     self.driver.find_element_by_css_selector(
    #         "#personalCenter2-rightContainer > div.paying-wrap.paying-sk-wrap.paying-sk-hhr > div.paying-sk-ewm > div.link > a").click()
    #
    #     print("订单已发送客户付款!")
    #
    #     # 订单url校验
    #
    #     self.driver.get(order_url)
    #     print(self.driver.title)
    #     time.sleep(2)
    #     order_number = self.driver.find_element_by_css_selector(
    #         "body > div > section.section-applybaseinfo.pay-info.pay-infoall > ul > table > tbody > tr:nth-child(2) > td.pay-platform-charge").text
    #     order_charge = self.driver.find_element_by_css_selector(
    #         "body > div > section.section-applybaseinfo.pay-info.pay-infoall > ul > table > tbody > tr:nth-child(3) > td.pay-platform-charge").text
    #     if order_charge == '':
    #         self.assertEqual(1, 2, "h5链接异常请及时查看!")
    #     else:
    #         print("订单编号:" + order_number)
    #
    #
    # def test_partner_clue_3(self):
    #
    #     """合伙人线索换单"""
    #     dl = DengLuPage(self.driver)
    #     dl.login()
    #     time.sleep(1)
    #
    #     self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
    #     time.sleep(1)
    #     # 新版提示
    #     self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div[1]/div/a").click()
    #     self.driver.find_element_by_css_selector("#personalCenter2-leftNav > ul > li.menu.open > ul > li:nth-child(2) > a").click()
    #     time.sleep(2)
    #     self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.partner > a:nth-child(4)").click()
    #     time.sleep(2)
    #     self.driver.find_element_by_css_selector("#product_100003").click()
    #     lb = (100001,100004,100007,100020,100021)
    #     xm = random.choice(lb)
    #     print("换单标签:" + self.driver.find_element_by_css_selector("#product_{}".format(xm)).text)
    #     self.driver.find_element_by_css_selector("#product_{}".format(xm)).click()
    #     self.driver.find_element_by_css_selector("#close > a").click()
    #     time.sleep(1)
    #     info = self.driver.find_element_by_css_selector("#delivery > div.test.test-1 > ul").text
    #     print("当前线索:" + str(info).replace("\n"," "))
    #     self.driver.find_element_by_css_selector("#delivery > div.bt-a > a.bt-a-two.a-colour").click()
    #     get_screenshort(self.driver,"test_partner_clue_4.png")
    #     time.sleep(3)
    #     self.driver.find_element_by_css_selector(
    #         "#personalCenter2-rightContainer > div > table > tbody > tr > td.td-handle > a").click()
    #
    # def test_partner_clue_4(self):
    #
    #     """合伙人线索退回,工商信息搜索"""
    #     dl = DengLuPage(self.driver)
    #     dl.login()
    #     time.sleep(1)
    #
    #     self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
    #     time.sleep(1)
    #     # 新版提示
    #     self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div[1]/div/a").click()
    #     self.driver.find_element_by_css_selector("#personalCenter2-leftNav > ul > li.menu.open > ul > li:nth-child(2) > a").click()
    #
    #
    #     """已认领 第一条线索信息"""
    #     self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.partner > a.not_select").click()
    #     info = self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > table > tbody > tr:nth-child(1)").text
    #     clue_number = self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > table > tbody > tr:nth-child(1) > td:nth-child(2)").text
    #     print("线索详情:" + (str(info).replace("\n" ," ")).replace("查看详情",""))
    #
    #     self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > table > tbody > tr:nth-child(1) > td.td-handle > a").click()
    #
    #     """切换窗口打开详情"""
    #     windows = self.driver.window_handles
    #     self.driver.switch_to.window(windows[-1])
    #     time.sleep(5)
    #     self.driver.set_window_size(1920, 1080)
    #
    #
    #     # """关掉时间提示"""
    #     # self.driver.find_element_by_css_selector("#layui-layer1 > span.layui-layer-setwin > a").click()
    #
    #     """客户工商信息搜索"""
    #     self.driver.find_element_by_class_name("icon-search").click()
    #     time.sleep(5)
    #     self.driver.find_element_by_class_name("a-bottom").click()
    #     time.sleep(2)
    #     get_screenshort(self.driver,"test_partner_clue_4.png")
    #
    #     """点击退回线索"""
    #     self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-detail-fix > div > div.right > div.pay-btns > a.button.cancel").click()
    #     time.sleep(2)
    #
    #     self.driver.find_element_by_css_selector("#close > div > a.other_key").click()
    #     self.driver.find_element_by_css_selector("#close > div > textarea").send_keys("不做了!")
    #     self.driver.find_element_by_css_selector("#close > a.a-tow").click()
    #     print("{}线索已退回!".format(clue_number))

    def test_partner_clue_1(self):

        """合伙人认领线索"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)
        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 关闭梦知网的提示
        self.driver.find_element_by_xpath("//span[@class='layui-layer-setwin']/a").click()
        time.sleep(.5)
        # 新版提示
        try:
            self.driver.find_element_by_xpath('//div[@class="hhr-help"]/div[@class="tips tips1"]/a[1]').click()
        except Exception as e:
            print(e)
        try:
            self.driver.find_element_by_xpath('//div[@id="invite-modal"]/div[@class="modal-body"]/a[1]').click()
        except Exception as e:
            print(e)
        self.driver.find_element_by_css_selector(
            "#personalCenter2-leftNav > ul > li.menu.open > ul > li:nth-child(2) > a").click()

        number_1 = self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.clue-list > div.partner > a:nth-child(2)").text

        number_2 = re.sub(r"\D", "", number_1)

        number_3 = int(number_2) + 0

        if number_3 >= 1:
            print("亲，您暂无未认领的线索哦~快去联系已认领的线索客户赚取收益吧~")

        else:

            try:
                self.driver.find_element(By.CSS_SELECTOR,
                                         "#personalCenter2-rightContainer > div.clue-list > div.clue-list > div.tbody > div > a")
                a = True
            except:
                a = False
            if a is True:
                print("当前无线索,点击申请!")
                self.driver.find_element_by_css_selector(
                    "#personalCenter2-rightContainer > div.clue-list > div.clue-list > div.tbody > div > a").click()
                time.sleep(4)
                clue = self.driver.find_element_by_css_selector(
                    "#personalCenter2-rightContainer > div.clue-list > div.clue-list > div.tbody > div:nth-child(1) > div.t-info").text
                print(str(clue).replace("\n", " ").replace("认领", ""))
                self.driver.find_element_by_css_selector(
                    "#personalCenter2-rightContainer > div.clue-list > div.clue-list > div.tbody > div:nth-child(1) > div.t-info > span.td-handle > a.button.claim_clue").click()  # tr-a claim_clue
            elif a is False:
                print("线索存在!")
                time.sleep(2)
                clue = self.driver.find_element_by_css_selector(
                    "#personalCenter2-rightContainer > div.clue-list > div.clue-list > div.tbody > div:nth-child(1) > div.t-info").text
                print(str(clue).replace("\n", " ").replace("认领", ""))
                self.driver.find_element_by_css_selector(
                    "#personalCenter2-rightContainer > div.clue-list > div.clue-list > div.tbody > div:nth-child(1) > div.t-info > span.td-handle > a.button.claim_clue").click()
        get_screenshort(self.driver, "test_partner_clue_1.png")

    def test_partner_clue_2(self):

        """合伙人线索下单"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)

        # 关闭梦知网的提示
        self.driver.find_element_by_xpath("//span[@class='layui-layer-setwin']/a").click()
        time.sleep(.5)

        # 新版提示
        try:
            self.driver.find_element_by_xpath('//div[@class="hhr-help"]/div[@class="tips tips1"]/a[1]').click()
        except Exception as e:
            print(e)
        try:
            self.driver.find_element_by_xpath('//div[@id="invite-modal"]/div[@class="modal-body"]/a[1]').click()
        except Exception as e:
            print(e)
        self.driver.find_element_by_css_selector(
            "#personalCenter2-leftNav > ul > li.menu.open > ul > li:nth-child(2) > a").click()

        """已认领 第一条线索信息"""
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.clue-list > div.partner > a:nth-child(2)").click()
        info = self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.clue-list > div.clue-list > div.tbody > div:nth-child(1) > div.t-info").text
        print("申请人详情:" + (str(info).replace("\n", " ")).replace("展开", "").replace("保护", "").replace("退回", ""))

        """点击展开线索集合(查看第一条线索详情)"""

        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.clue-list > div.clue-list > div.tbody > div:nth-child(1) > div.t-info > span.td-handle > a.switch").click()

        info_1 = self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.clue-list > div.clue-list > div.tbody > div:nth-child(1) > div.t-box.scroll.active > table > tbody > tr:nth-child(1) > td > div.left.float-left").text
        print(info_1)

        info_2 = self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.clue-list > div.clue-list > div.tbody > div:nth-child(1) > div.t-box.scroll.active > table > tbody > tr:nth-child(2)").text
        print("线索详情:" + (str(info_2).replace("\n", " ")).replace("查看详情", ""))

        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.clue-list > div.clue-list > div.tbody > div:nth-child(1) > div.t-box.scroll.active > table > tbody > tr:nth-child(2) > td.td-handle > a").click()

        """切换窗口打开详情"""
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)

        # """关掉时间提示"""
        # self.driver.find_element_by_css_selector("#layui-layer1 > span.layui-layer-setwin > a").click()
        get_screenshort(self.driver, "test_partner_clue_2.png")

        """点击下单"""
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-detail-fix > div > div.right > div.pay-btns > a:nth-child(2)").click()
        time.sleep(2)

        """判断客户邮箱是否为空"""
        email = self.driver.find_element_by_name("email").get_attribute("value")
        if email == "无":
            self.driver.find_element_by_name("email").clear()
            self.driver.find_element_by_name("email").send_keys("test@quandashi.com")
            print("客户邮箱:" + self.driver.find_element_by_name("email").get_attribute("value"))
        else:
            print("客户邮箱:" + self.driver.find_element_by_name("email").get_attribute("value"))

        self.driver.find_element_by_xpath('//form[@id="addBusinessMgsBox"]/ul/li[1]/div[@class="m-select-box"]').click()
        self.driver.find_element_by_xpath('//form[@id="addBusinessMgsBox"]/ul/li[1]/div[@class="m-select-box"]/dl/dd[%d]' % random.choice([2, 3, 4])).click()
        self.driver.find_element_by_xpath('//form[@id="addBusinessMgsBox"]/ul/li[2]/div[@class="m-select-box"]').click()
        self.driver.find_element_by_xpath('//form[@id="addBusinessMgsBox"]/ul/li[2]/div[@class="m-select-box"]/dl/dd[%s]' % random.choice([1, 2, 3])).click()

        price = self.driver.find_element_by_name("price").get_attribute("value")
        print("订单价格:" + price)
        income = self.driver.find_element_by_css_selector(
            "#addBusinessMgsBox > div.numAndPrice.clearfix > div.profitNum > span.earning.income-estimate").text
        print("收益预估:" + str(income))

        """订单备注"""
        self.driver.find_element_by_css_selector("#addBusinessMgsBox > div.businessRemark > textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        """保存信息"""
        self.driver.find_element_by_css_selector("#saveBusMsgBtn").click()
        time.sleep(1)
        # self.driver.find_element_by_name("email").send_keys("34021500@qq.com")
        self.driver.find_element_by_css_selector("#saveConfirmOrder").click()
        time.sleep(2)
        """订单确认"""
        get_screenshort(self.driver, "test_full_business_1.png")
        self.driver.find_element_by_css_selector("#saveOrder").click()
        time.sleep(2)

        self.driver.find_element_by_css_selector(
            "#layui-layer1 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn0").click()

        total = self.driver.find_element_by_xpath("//div[@class=\"moneyMsg\"]/p[2]/b").text
        print("订单提交成功，应付金额:" + total)
        self.assertIn(price, total)
        print("价格一致！")

        self.driver.find_element_by_css_selector("#payways > ul:nth-child(1) > li > span").click()
        self.driver.find_element_by_css_selector("#alisubmit").click()
        order_url = self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.paying-wrap.paying-sk-wrap.paying-sk-hhr > div.paying-sk-ewm > div.link > input").get_attribute(
            "value")

        print("订单链接:" + order_url)
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.paying-wrap.paying-sk-wrap.paying-sk-hhr > div.paying-sk-ewm > div.link > a").click()

        print("订单已发送客户付款!")

        # 订单url校验

        self.driver.get(order_url)
        print(self.driver.title)
        time.sleep(2)
        order_number = self.driver.find_element_by_css_selector(
            "body > div > section.section-applybaseinfo.pay-info.pay-infoall > ul > table > tbody > tr:nth-child(2) > td.pay-platform-charge").text
        order_charge = self.driver.find_element_by_css_selector(
            "body > div > section.section-applybaseinfo.pay-info.pay-infoall > ul > table > tbody > tr:nth-child(3) > td.pay-platform-charge").text
        if order_charge == '':
            self.assertEqual(1, 2, "h5链接异常请及时查看!")
        else:
            print("订单编号:" + order_number)

    def test_partner_clue_3(self):

        """合伙人线索换单"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 关闭梦知网的提示
        self.driver.find_element_by_xpath("//span[@class='layui-layer-setwin']/a").click()
        time.sleep(.5)
        # 新版提示
        try:
            self.driver.find_element_by_xpath('//div[@class="hhr-help"]/div[@class="tips tips1"]/a[1]').click()
        except Exception as e:
            print(e)
        try:
            self.driver.find_element_by_xpath('//div[@id="invite-modal"]/div[@class="modal-body"]/a[1]').click()
        except Exception as e:
            print(e)
        self.driver.find_element_by_css_selector(
            "#personalCenter2-leftNav > ul > li.menu.open > ul > li:nth-child(2) > a").click()
        time.sleep(2)

        number_1 = self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.clue-list > div.partner > a.select").text

        number_2 = re.sub(r"\D", "", number_1)

        number_3 = int(number_2) + 0

        if number_3 == 0:

            print("暂无线索，无需换单!")
        else:
            self.driver.find_element_by_css_selector(
                "#personalCenter2-rightContainer > div.clue-list > div.partner > a:nth-child(5)").click()
            time.sleep(2)
            self.driver.find_element_by_css_selector("#product_100003").click()
            lb = (100001, 100004, 100007, 100020, 100021)
            xm = random.choice(lb)
            print("换单标签:" + self.driver.find_element_by_css_selector("#product_{}".format(xm)).text)
            self.driver.find_element_by_css_selector("#product_{}".format(xm)).click()

            # self.driver.find_element_by_css_selector("# select_tags > a").click()
            self.driver.find_element_by_link_text("确定").click()

            time.sleep(1)
            info = self.driver.find_element_by_css_selector("#delivery > div.test.test-1 > ul").text
            print("当前线索:" + str(info).replace("\n", " "))
            self.driver.find_element_by_css_selector("#delivery > div.bt-a > a.bt-a-two.a-colour").click()
            get_screenshort(self.driver, "test_partner_clue_4.png")
            time.sleep(3)
            self.driver.find_element_by_css_selector(
                "#personalCenter2-rightContainer > div.clue-list > div.clue-list > div.tbody > div:nth-child(1) > div.t-info > span.td-handle > a.button.claim_clue").click()

    def test_partner_clue_4(self):

        """合伙人线索退回,工商信息搜索"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 关闭梦知网的提示
        self.driver.find_element_by_xpath("//span[@class='layui-layer-setwin']/a").click()
        time.sleep(.5)
        # 新版提示
        try:
            self.driver.find_element_by_xpath('//div[@class="hhr-help"]/div[@class="tips tips1"]/a[1]').click()
        except Exception as e:
            print(e)
        try:
            self.driver.find_element_by_xpath('//div[@id="invite-modal"]/div[@class="modal-body"]/a[1]').click()
        except Exception as e:
            print(e)
        self.driver.find_element_by_css_selector(
            "#personalCenter2-leftNav > ul > li.menu.open > ul > li:nth-child(2) > a").click()

        """已认领 第一条线索信息"""
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.clue-list > div.partner > a:nth-child(2)").click()
        info = self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.clue-list > div.clue-list > div.tbody > div:nth-child(1) > div.t-info").text
        print("申请人详情:" + (str(info).replace("\n", " ")).replace("展开", "").replace("保护", "").replace("退回", ""))

        """点击展开线索集合(查看第一条线索详情)"""

        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.clue-list > div.clue-list > div.tbody > div:nth-child(1) > div.t-info > span.td-handle > a.switch").click()

        info_1 = self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.clue-list > div.clue-list > div.tbody > div:nth-child(1) > div.t-box.scroll.active > table > tbody > tr:nth-child(1) > td > div.left.float-left").text
        print(info_1)

        info_2 = self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.clue-list > div.clue-list > div.tbody > div:nth-child(1) > div.t-box.scroll.active > table > tbody > tr:nth-child(2)").text
        print("线索详情:" + (str(info_2).replace("\n", " ")).replace("查看详情", ""))

        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.clue-list > div.clue-list > div.tbody > div:nth-child(1) > div.t-box.scroll.active > table > tbody > tr:nth-child(2) > td.td-handle > a").click()

        clue_number = self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.clue-list > div.clue-list > div.tbody > div:nth-child(1) > div.t-box.scroll.active > table > tbody > tr.tr-top > td > div.left.float-left > span.gray").text

        """切换窗口打开详情"""
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        time.sleep(5)
        self.driver.set_window_size(1920, 1080)

        # """关掉时间提示"""  """根据时间出现，如有需要请及时解除注释"""
        # self.driver.find_element_by_css_selector("#layui-layer1 > span.layui-layer-setwin > a").click()

        """客户工商信息搜索"""
        self.driver.find_element_by_class_name("icon-search").click()
        time.sleep(5)
        self.driver.find_element_by_class_name("a-bottom").click()
        time.sleep(2)
        get_screenshort(self.driver, "test_partner_clue_4.png")

        """点击退回线索"""
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-detail-fix > div > div.right > div.pay-btns > a.button.cancel").click()
        time.sleep(2)

        self.driver.find_element_by_css_selector("#close > div > a.other_key").click()
        self.driver.find_element_by_css_selector("#close > div > textarea").send_keys("不做了!")
        self.driver.find_element_by_css_selector("#close > div.btns.close-btns > a:nth-child(2)").click()
        print("{}线索已退回!".format(clue_number))

    def test_partner_clue_5(self):

        """合伙人线索保护"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 关闭梦知网的提示
        self.driver.find_element_by_xpath("//span[@class='layui-layer-setwin']/a").click()
        time.sleep(.5)
        # 新版提示
        try:
            self.driver.find_element_by_xpath('//div[@class="hhr-help"]/div[@class="tips tips1"]/a[1]').click()
        except Exception as e:
            print(e)
        try:
            self.driver.find_element_by_xpath('//div[@id="invite-modal"]/div[@class="modal-body"]/a[1]').click()
        except Exception as e:
            print(e)
        self.driver.find_element_by_css_selector(
            "#personalCenter2-leftNav > ul > li.menu.open > ul > li:nth-child(2) > a").click()

        """已认领 第一条线索信息"""
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.clue-list > div.partner > a:nth-child(2)").click()
        info = self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.clue-list > div.clue-list > div.tbody > div:nth-child(1) > div.t-info").text
        print("申请人详情:" + (str(info).replace("\n", " ")).replace("展开", "").replace("保护", "").replace("退回", ""))

        """点击保护按钮"""

        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.clue-list > div.clue-list > div.tbody > div:nth-child(1) > div.t-info > span.td-handle > a.protect_clue.button").click()

        time.sleep(2)
        tip_1 = self.driver.find_element_by_css_selector(
            "#layui-layer2 > div.layui-layer-content").text
        print(tip_1)
        self.driver.find_element_by_link_text("确定").click()

        self.driver.find_element_by_link_text("客户保护").click()
        time.sleep(2)

        tip_2 = self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.partner > span").text
        print(tip_2)

        info_2 = self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.clue-list > div.tbody > div > div.t-info > span.applicant").text
        print("申请人:" + info_2)

        """点击取消保护"""
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.clue-list > div.tbody > div > div.t-info > span.td-handle > a.button.cancel_clue").click()

        time.sleep(2)
        tip_3 = self.driver.find_element_by_css_selector(
            "#layui-layer2 > div.layui-layer-content").text
        print(tip_3)
        self.driver.find_element_by_link_text("确定").click()

    def test_clue_cancel(self):
        """取消线索订单"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 关闭梦知网的提示
        self.driver.find_element_by_xpath("//span[@class='layui-layer-setwin']/a").click()
        time.sleep(.5)
        # 新版提示
        try:
            self.driver.find_element_by_xpath('//div[@class="hhr-help"]/div[@class="tips tips1"]/a[1]').click()
        except Exception as e:
            print(e)
        try:
            self.driver.find_element_by_xpath('//div[@id="invite-modal"]/div[@class="modal-body"]/a[1]').click()
        except Exception as e:
            print(e)

        self.driver.find_element_by_css_selector(
            "#personalCenter2-leftNav > ul > li.menu.open > ul > li:nth-child(1) > a").click()
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.order-page-tab > a.o-index").click()
        time.sleep(2)

        while True:

            n = self.driver.find_element_by_css_selector(
                "#personalCenter2-rightContainer > div.order-page > div.tabsPanel > ul > li.list.selected > a").text
            if str(n) == "待付款（1）":
                break
            self.driver.find_element_by_css_selector(
                "#personalCenter2-rightContainer > div.order-page > div.tabsPanel > div:nth-child(4) > div > table > tbody > tr > td:nth-child(8) > a.order-cancel").click()
            time.sleep(3)
            self.driver.find_element_by_css_selector(
                "#layui-layer1 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn0").click()
            time.sleep(2)

            print(n)

        print("取消未付款线索订单,测试通过!")

    def test_CancelState(self):
        """取消订单测试"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 关闭梦知网的提示
        self.driver.find_element_by_xpath("//span[@class='layui-layer-setwin']/a").click()
        time.sleep(.5)
        # 新版提示
        try:
            self.driver.find_element_by_xpath('//div[@class="hhr-help"]/div[@class="tips tips1"]/a[1]').click()
        except Exception as e:
            print(e)
        try:
            self.driver.find_element_by_xpath('//div[@id="invite-modal"]/div[@class="modal-body"]/a[1]').click()
        except Exception as e:
            print(e)

        self.driver.find_element_by_css_selector(
            "#personalCenter2-leftNav > ul > li.menu.open > ul > li:nth-child(1) > a").click()
        time.sleep(2)
        # 切换成下单时间
        self.driver.find_element_by_class_name("order-time").click()
        # 选择修改的订单号
        print("订单编号:" + self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.order-page > div.tabsPanel > div > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > div > p:nth-child(1)").text)
        # 查看详情
        self.driver.find_element_by_class_name("order-cancel").click()
        time.sleep(2)
        self.driver.find_element_by_class_name("modal-body-textarea").send_keys("下错单了!")
        time.sleep(2)
        self.driver.find_element_by_link_text("提   交").click()
        print("订单取消成功!")

    def test_payment_voucher(self):
        """付款凭证测试"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 关闭梦知网的提示
        self.driver.find_element_by_xpath("//span[@class='layui-layer-setwin']/a").click()
        time.sleep(.5)
        # 新版提示
        # self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div[1]/div/a").click()
        try:
            self.driver.find_element_by_xpath('//div[@class="hhr-help"]/div[@class="tips tips1"]/a[1]').click()
        except Exception as e:
            print(e)
        try:
            self.driver.find_element_by_xpath('//div[@id="invite-modal"]/div[@class="modal-body"]/a[1]').click()
        except Exception as e:
            print(e)
        self.driver.find_element_by_css_selector(
            "#personalCenter2-leftNav > ul > li.menu.open > ul > li:nth-child(1) > a").click()
        time.sleep(2)
        # 切换成下单时间
        self.driver.find_element_by_class_name("order-time").click()
        # 选择修改的订单号
        number = self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.order-page > div.tabsPanel > div > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > div > p:nth-child(1)").text
        print("订单编号:" + number)
        # 查看详情
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.order-page > div.tabsPanel > div > div > table > tbody > tr:nth-child(1) > td:nth-child(9) > div.td-handle > a.info").click()
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,6500)")  # 滑动滚动条

        # 点击支付凭证
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.order-detail-page > div.order-detail-box.order-detail-pay-info > table > tbody > tr:nth-child(2) > td:nth-child(6) > a").click()

        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        # pay_number = str("订单" + number)
        print(self.driver.title)
        # self.assertEqual(pay_number,self.driver.title,"凭证异常!请及时查看!")

        try:
            self.driver.find_element(By.CSS_SELECTOR,
                                     "#personalCenter2-rightContainer > div > div.cont-crumbs > ul > li:nth-child(3) > a")
            a = True
        except:
            a = False
        if a is True:
            voucher = self.driver.find_element_by_css_selector(
                "#personalCenter2-rightContainer > div > div.cont-crumbs > ul > li:nth-child(3) > a").text
            print(voucher + "测试通过!")

        elif a is False:
            error = self.driver.find_element_by_css_selector("body > div.error-box > div.error-left > p").text
            print(error)
            self.assertEqual(1, 2, "凭证异常!请及时查看!")

    def test_my_income(self):
        """收益提现测试"""

        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)
        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 关闭梦知网的提示
        self.driver.find_element_by_xpath("//span[@class='layui-layer-setwin']/a").click()
        time.sleep(.5)
        # 新版提示
        try:
            self.driver.find_element_by_xpath('//div[@class="hhr-help"]/div[@class="tips tips1"]/a[1]').click()
        except Exception as e:
            print(e)
        try:
            self.driver.find_element_by_xpath('//div[@id="invite-modal"]/div[@class="modal-body"]/a[1]').click()
        except Exception as e:
            print(e)

        self.driver.find_element_by_link_text("申请提现").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        print(self.driver.title)
        get_screenshort(self.driver, "test_my_income.png")
        #
        # info_2 = self.driver.find_element_by_css_selector("#layui-layer1 > div.layui-layer-content").text
        # print(info_2)
        # self.driver.find_element_by_css_selector("#layui-layer1 > div.layui-layer-btn.layui-layer-btn- > a").click()
        info_1 = self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.order-page.apply-noe.bank-card-list > table > tbody > tr > td > div").text
        print(info_1)
        print("我的收益功能正常,测试通过!")

    def test_income_show(self):
        """收益滚动展示条"""

        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)
        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 关闭梦知网的提示
        self.driver.find_element_by_xpath("//span[@class='layui-layer-setwin']/a").click()
        time.sleep(.5)
        # 新版提示
        try:
            self.driver.find_element_by_xpath('//div[@class="hhr-help"]/div[@class="tips tips1"]/a[1]').click()
        except Exception as e:
            print(e)
        try:
            self.driver.find_element_by_xpath('//div[@id="invite-modal"]/div[@class="modal-body"]/a[1]').click()
        except Exception as e:
            print(e)

        info_1 = self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.home-page.userInfo > div.article1.home-page-top.clearfix > div.article-bottom-info").text
        print(info_1)
        print("收益滚动展示条,测试通过!")

    def test_hhr_nice_search(self):
        """尼斯分类搜索(hhr)"""

        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)
        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 关闭梦知网的提示
        self.driver.find_element_by_xpath("//span[@class='layui-layer-setwin']/a").click()
        time.sleep(.5)
        # 新版提示
        try:
            self.driver.find_element_by_xpath('//div[@class="hhr-help"]/div[@class="tips tips1"]/a[1]').click()
        except Exception as e:
            print(e)
        try:
            self.driver.find_element_by_xpath('//div[@id="invite-modal"]/div[@class="modal-body"]/a[1]').click()
        except Exception as e:
            print(e)

        self.driver.find_element_by_css_selector(
            "#personalCenter2-leftNav > ul > li:nth-child(2) > ul > li:nth-child(1) > a").click()
        time.sleep(2)

        self.driver.find_element_by_css_selector("#selectCategoryType > label:nth-child(2)").click()

        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > div > div > input").send_keys("摩托车")
        self.driver.find_element_by_css_selector("#btn-search > i").click()
        time.sleep(3)

        number_1 = self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > div > li:nth-child(1) > span").text

        number_2 = re.sub(r"\D", "", number_1)

        number_3 = int(number_2) + 0

        self.assertEqual(number_3, 7, "尼斯分类搜索结果异常!")

        print("合伙人商标注册尼斯分类搜索结果正常!")
