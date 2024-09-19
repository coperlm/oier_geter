from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def fetch_oier_info(name):
    # 设置Chrome WebDriver的路径，确保指向的是具体的chromedriver.exe文件
    driver_path = r'D:\daily_apps\chromedriver-win64\chromedriver.exe'  # 请确保路径正确
    url = f'https://oier.baoshuo.dev/?query={name}'  # 直接构造URL

    # 使用Service来管理驱动路径
    service = Service(driver_path)
    
    # 初始化WebDriver
    driver = webdriver.Chrome(service=service)
    
    try:
        # 打开构造好的URL
        driver.get(url)
        
        # 等待页面加载直到“正在加载”消失
        while True:
            try:
                # 查找“正在加载”的元素
                loading_element = WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "正在加载")]'))
                )
                # 如果找到“正在加载”元素，等待4秒再检查
                time.sleep(2)
            except:
                # 如果在等待时间内没有找到“正在加载”元素，退出循环
                break
        
        # 获取页面源代码
        page_source = driver.page_source
        
        return page_source

    except Exception as e:
        print(f"Error fetching data for {name}: {e}")
        return None
    finally:
        # 关闭浏览器
        driver.quit()


def read_names_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        names = [line.strip() for line in file if line.strip()]
    return names
names_file = "all_names.txt"  # 包含待查询姓名的文件
names = read_names_from_file(names_file)

# 将所有页面源代码保存到一个txt文件
with open("output_pages.txt", "w", encoding="utf-8") as file:
    for name in names:
        page_source = fetch_oier_info(name)
        if page_source:
            # 写入文件
            if '高中毕业 1 年' in page_source:
                file.write(f"Page source for {name}:{page_source}\n")
            else:
                file.write(f"Page source for {name}:no info\n")
        else:
            # 如果获取失败，写入失败信息
            file.write(f"Error fetching data for {name}\n")

print("Page sources saved to oier_page_sources.txt")
