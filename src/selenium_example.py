from nova_act import NovaAct

if __name__ == '__main__':
    prompt = '''
    1. Truy cập https://aws.amazon.com/events/cloud-days/
    2. Kéo xuống phần đăng ký tham gia AWS Cloud Day và đăng ký Turkiye event.
    3. click vào nút "Register Now".
    4. Tự động điền form đăng ký với các thông tin sau:
        - First Name: Duc
        - Last Name: Le
        - Business Email Address: lehongduc20122004@gmail.com
        - Work Country: Turkey
        - Work City: Istanbul
        - Work Postal Code: 34000
        - Mobile Phone Number: 0123456789
        - Job Title: Developer
        - Job Role: IT
        - Industry: Technology
        - Company Name: NovaPro
        - Company Type: Private
        - Company Size: 1-10
        - Level of AWS Usage: Beginner
        - I am completing this form in connection with my: Business interests
        - Đồng ý nhận tin AWS (nếu có checkbox)
        - Xác nhận đủ 18 tuổi
    5. Nhấn Submit để gửi form.
    6. Nếu thành công, in ra "Đã gửi form đăng ký AWS Cloud Day!". Nếu lỗi, in ra lỗi.
    '''

    with NovaAct(
        starting_page="https://aws.amazon.com/events/cloud-days/",
        ignore_https_errors=True
    ) as nova:
        result = nova.act(prompt)
        print(result)