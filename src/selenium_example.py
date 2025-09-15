
# Ví dụ dùng Selenium với profile Edge đã đăng nhập sẵn
from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time

def add_dns_record_with_profile(name, ttl, rdata):
    edge_options = Options()
    # Thay đường dẫn bên dưới bằng profile Edge đã đăng nhập của bạn
    edge_options.add_argument(r'user-data-dir=C:\\Users\\dhongle\\AppData\\Local\\Microsoft\\Edge\\User Data')
    edge_options.add_argument('profile-directory=Default')  # hoặc tên profile bạn dùng

    driver = webdriver.Edge(options=edge_options)
    try:
        driver.get('https://secure.vinahost.vn/ac/index.php?m=DNSManager2&mg-action=editZone&zone_id=30952')
        time.sleep(2)

        name_input = driver.find_element('xpath', "//input[@placeholder='Name']")
        ttl_input = driver.find_element('xpath', "//input[@placeholder='TTL']")
        rdata_input = driver.find_element('xpath', "//input[@placeholder='RDATA']")

        name_input.clear()
        name_input.send_keys(name)
        ttl_input.clear()
        ttl_input.send_keys(str(ttl))
        rdata_input.clear()
        rdata_input.send_keys(rdata)

        save_btn = driver.find_element('xpath', "//button[contains(., 'Save Changes')]")
        save_btn.click()
        time.sleep(2)
        print('Đã thêm bản ghi DNS thành công!')
    except Exception as e:
        print('Lỗi:', e)
    finally:
        driver.quit()

if __name__ == '__main__':
    add_dns_record_with_profile('test', 14400, '192.168.1.1')