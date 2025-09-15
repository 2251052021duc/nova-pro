# nova-pro: Selenium Web Automation on AWS

## Mô tả
Dự án này sử dụng Selenium để tự động hóa web, có thể triển khai trên AWS (EC2 hoặc Lambda).

## Cài đặt
1. Cài Python 3.8+
2. Cài các thư viện cần thiết:
	```bash
	pip install -r requirements.txt
	```

## Chạy thử local
```bash
python src/selenium_example.py
```

## Triển khai lên AWS
- EC2: Copy mã nguồn lên EC2, cài Python và các thư viện, chạy script như local.
- Lambda: Đóng gói mã nguồn và thư viện (xem hướng dẫn AWS Lambda Python + Selenium).

## Tham khảo
- https://selenium-python.readthedocs.io/
- https://boto3.amazonaws.com/v1/documentation/api/latest/index.html