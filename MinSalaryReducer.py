# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys

current_min_salary = float('inf')

# Đọc dữ liệu từ luồng nhập tiêu chuẩn
for line in sys.stdin:
    # Tách dòng thành key và value dựa trên dấu tab
    key, value = line.strip().split('\t')
    
    # Chuyển đổi giá trị lương thành số
    salary = int(value)
    
    # Cập nhật lương nhỏ nhất
    if salary < current_min_salary:
        current_min_salary = salary

# In ra lương nhỏ nhất
print('MinSalary:', current_min_salary)
