# -*- coding: utf-8 -*-
# @Time : 2023/8/17 18:10 
# @Author : Yao
# @File : 01_main.py
# -*- coding: utf-8 -*-
# @Time : 2023/8/17 18:16
# @Author : Yao
# @File : text.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time

# 选择资源库
def select_repository():
    # 点击“学术期刊”资源库
    academic_journal = driver.find_element(By.XPATH, '//li[@data-id="xsqk"]/a')
    driver.execute_script("arguments[0].click();", academic_journal)

# 选择期刊类型
def select_journal_type():
    # 选择来源类别“北大核心”和“CSSCI”
    bdhx_checkbox = driver.find_element(By.XPATH, '//input[@key="HX"]')
    cssci_checkbox = driver.find_element(By.XPATH, '//input[@key="CSI"]')
    bdhx_checkbox.click()
    cssci_checkbox.click()

# 选择起始与终止年份
def start_end_year():
    # 选择起始年为2016
    start_year_input = driver.find_element(By.XPATH, '//div[@class="sort-default"]/input[@placeholder="起始年"]')
    start_year_input.clear()
    start_year_input.send_keys("2018")

    # 选择结束年为2023
    end_year_input = driver.find_element(By.XPATH,
                                         '//div[@class="sort end"]/div[@class="sort-default"]/input[@placeholder="结束年"]')
    end_year_input.clear()
    end_year_input.send_keys("2018")

# 每页显示数量
def items_per_page():
    # 找到每页显示数量的下拉框并点击
    display_num_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@id="perPageDiv"]/div[@class="sort-default"]'))
    )
    display_num_dropdown.click()

    # 找到每页显示50条的选项并点击
    per_page_50_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//li[@data-val="50"]/a'))
    )
    per_page_50_option.click()
    time.sleep(2)

# 获取已选择的文献数量
def get_selected_document_count():
    # 等待所选文献数量的element出现
    select_count_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "selectCount"))
    )

    # 获取所选文献数量的文本内容
    selected_count = select_count_element.text
    return selected_count

# 每页全选
def check_select_all():
    select_all_checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "selectCheckAll1"))
    )
    driver.execute_script("arguments[0].click();", select_all_checkbox)
    # time.sleep(2)  # 等待全选操作生效，根据需要调整等待时间

# 清除选择
def click_clear_selection():
    clear_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//em[@id="selectCount"]/following-sibling::a[contains(text(), "清除")]'))
    )
    # 使用JavaScript模拟点击清除按钮
    driver.execute_script("arguments[0].click();", clear_button)

# 导出为Excel
def export_documents():
    # 找到“导出与分析”链接并点击
    export_analyze_link = driver.find_element(By.XPATH, '//a[contains(text(), "导出与分析")]')
    driver.execute_script("arguments[0].click();", export_analyze_link)
    # time.sleep(2)  # 等待页面响应，根据需要调整等待时间

    # 找到“导出文献”链接并点击
    export_documents_link = driver.find_element(By.XPATH, '//li[@class="export"]/a')
    driver.execute_script("arguments[0].click();", export_documents_link)
    # time.sleep(2)  # 等待页面响应，根据需要调整等待时间

    # 找到“自定义”链接并点击
    custom_export_link = driver.find_element(By.XPATH, '//a[@exporttype="selfDefine"]')
    driver.execute_script("arguments[0].click();", custom_export_link)

    time.sleep(1)  # 等待页面响应，根据需要调整等待时间

    # 跳转页面后重新定位： https://blog.csdn.net/Ruiiiiiia/article/details/102257395

    windows = driver.window_handles
    driver.switch_to.window(windows[-1])

    # 找到“全选”按钮并点击
    select_all_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "全选")]'))
    )
    select_all_button.click()

    # 找到“导出到excel保存”按钮并点击
    export_xls_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[contains(@title, "导出到excel保存")]'))
    )
    export_xls_button.click()

    # 关闭页面：https://blog.csdn.net/weixin_44319949/article/details/106208020
    time.sleep(10)
    driver.close()
    driver.switch_to.window(windows[0])

# 下一页
def next_page(page):
    next_page_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@id="page{0}"]'.format(page + 1)))
    )
    # next_page_button = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.ID, "PageNext"))
    # )
    next_page_button.click()
    windows = driver.window_handles
    driver.switch_to.window(windows[0])
    time.sleep(5)  # 等待结果加载

# 设置 Chrome 驱动路径
chromedriver_path = "/usr/local/bin/chromedriver"

# 创建 Chrome 驱动
driver = webdriver.Chrome(executable_path=chromedriver_path)

try:
    # 打开知网的高级检索页面
    driver.get("https://kns.cnki.net/kns8/AdvSearch?dbcode=CFLS")

    select_repository() # 选择资源库

    select_journal_type() # 选择来源类别“北大核心”和“CSSCI”

    start_end_year() # 2023-2023

    # 在“主题”输入框中输入关键词“中医”
    search_topic_input = driver.find_element(By.XPATH, '//input[@data-tipid="gradetxt-1"]')
    search_topic_input.send_keys("中医")

    # 模拟按下回车键，进行检索
    search_topic_input.send_keys(Keys.ENTER)

    # 等待检索结果页面加载完成
    WebDriverWait(driver, 20).until(EC.title_contains("知网"))

    items_per_page() # 每页显示50条

    # 找到共找到的结果数量
    total_results = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//span[@class="pagerTitleCell"]/em'))
    )
    total_results = int(total_results.text.replace(',', ''))
    print("共有文献:", total_results)

    # 计算总页数
    total_pages = (total_results + 49) // 50  # 每页50条
    print("共有文献页数:", total_pages)

    current_page = 1
    last_export = 0
    while total_pages - last_export >= 10:
        print(f"正在处理第{current_page}页")
        # 调用全选函数，全选主页期刊
        check_select_all()
        time.sleep(5)
        # 每页全选的数量为50，当全选文献的数量等于500时
        if current_page % 10 == 0: #count == 500:
            export_documents()  # 导出文献
            last_export = current_page
            click_clear_selection()  # 点击清除选择
            time.sleep(25)
        if current_page % 6 == 0: # 每6页暂停
            time.sleep(20)
        next_page(current_page)  # 进入下一页
        current_page += 1
    else:
        while total_pages - current_page != 0:
            print(f"正在处理第{current_page}页")
            check_select_all()
            time.sleep(10)
            next_page(current_page)
            current_page += 1

        else:
            print(f"正在处理第{current_page}页")
            check_select_all()
            time.sleep(10)
            export_documents()  # 导出文献
            time.sleep(3)
            click_clear_selection()  # 点击清除选择

finally:
    # 在程序运行结束后手动关闭浏览器
    input("程序运行完成，按回车键关闭...")
    driver.quit()


