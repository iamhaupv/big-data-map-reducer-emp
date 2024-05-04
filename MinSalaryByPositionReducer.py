#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

current_position = None
current_min_salary = float('inf')

# Đọc dữ liệu từ luồng nhập tiêu chuẩn
for line in sys.stdin:
    # Tách dòng thành vị trí công việc và lương thấp nhất dựa trên dấu tab
    position, min_salary = line.strip().split('\t')
    min_salary = int(min_salary)
    
    # Kiểm tra xem vị trí công việc có thay đổi không
    if current_position != position:
        # Nếu vị trí công việc thay đổi, in ra lương thấp nhất của vị trí công việc trước đó
        if current_position is not None:
            print('%s\t%s' % (current_position, current_min_salary))
        # Cập nhật vị trí công việc và lương thấp nhất mới
        current_position = position
        current_min_salary = min_salary
    else:
        # Nếu vị trí công việc không thay đổi, so sánh và cập nhật lương thấp nhất
        current_min_salary = min(current_min_salary, min_salary)

# In ra lương thấp nhất của vị trí công việc cuối cùng
if current_position is not None:
    print('%s\t%s' % (current_position, current_min_salary))
