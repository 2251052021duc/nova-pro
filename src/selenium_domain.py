from nova_act import NovaAct

if __name__ == '__main__':
    prompt = '''
    1. Truy cập https://secure.vinahost.vn/ac/index.php?rp=/login
    2. Trong form đăng nhập, nhập:  
        - Email: lehongduc20122004@gmail.com
        - Mật khẩu: Ba0935803143@
    3. Nhấn "Login".
    4. Tắt thông báo nếu có popup hiện lên.     
    5. Rê chuột chứ đừng nhấn "Tên miền" ở menu bên trái.
    6. Chọn "Manage DNS".
    7. Chọn icon cây bút để sửa DNS cho domain duckou.id.vn.
    8. Bấm "Add Record".
    9. Trong form Add New Record, nhập:
        - Name: duc
        - Type: A
        - TTL: 14400
        - RDATA: 20.12.01.09
    10. Nhấn "Add Record".
    11. Nhấn "Save Changes" để lưu lại.
    12. Nếu thành công in ra "Đã thêm record DNS mới!". Nếu lỗi, in ra lỗi.
    '''

    with NovaAct(
        starting_page="https://secure.vinahost.vn/ac/index.php?rp=/login",
        headless=True,          
        ignore_https_errors=True
    ) as nova:
        result = nova.act(prompt)
        print(result)
