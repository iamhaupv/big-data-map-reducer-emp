# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys

current_min_salary = float('inf')
current_max_salary = float('-inf')

# Đọc dữ liệu từ luồng nhập tiêu chuẩn
for line in sys.stdin:
    # Tách dòng thành key và value dựa trên dấu tab
    key, value = line.strip().split('\t')
    
    # Kiểm tra key để xác định giá trị là lương nhỏ nhất hay lớn nhất
    if key == 'MinSalary':
        current_min_salary = min(current_min_salary, float(value))
    elif key == 'MaxSalary':
        current_max_salary = max(current_max_salary, float(value))

# In ra giá trị lương nhỏ nhất và lớn nhất
print('MinSalary:', current_min_salary)
print('MaxSalary:', current_max_salary)
