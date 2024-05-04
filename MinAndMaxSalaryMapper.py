#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv

# Đọc dữ liệu từ luồng nhập tiêu chuẩn
reader = csv.reader(sys.stdin)
next(reader)  # Bỏ qua header

# Khởi tạo giá trị lương nhỏ nhất và lớn nhất
min_salary = float('inf')
max_salary = float('-inf')

# Đọc từng dòng của tập tin CSV đầu vào
for row in reader:
    # Lấy cột lương (cột 6)
    salary = float(row[5])
    
    # Cập nhật lương nhỏ nhất và lớn nhất
    min_salary = min(min_salary, salary)
    max_salary = max(max_salary, salary)

# Xuất giá trị lương nhỏ nhất và lớn nhất
print('MinSalary\t%s' % min_salary)
print('MaxSalary\t%s' % max_salary)
