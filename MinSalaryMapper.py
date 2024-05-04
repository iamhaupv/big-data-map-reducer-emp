#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv

# Đọc dữ liệu từ luồng nhập tiêu chuẩn
reader = csv.reader(sys.stdin)
next(reader)  # Bỏ qua header

# Khởi tạo giá trị lương nhỏ nhất
min_salary = float('inf')

# Đọc từng dòng của tập tin CSV đầu vào
for row in reader:
    # Lấy cột lương (cột 6)
    salary = int(row[5])
    
    # Cập nhật lương nhỏ nhất nếu cần
    if salary < min_salary:
        min_salary = salary

# Xuất lương nhỏ nhất
print('MinSalary\t%s' % min_salary)
