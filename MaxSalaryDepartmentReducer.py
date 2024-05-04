#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

current_deptno = None
current_max_salary = float('-inf')

# Đọc dữ liệu từ luồng nhập tiêu chuẩn
for line in sys.stdin:
    # Tách dòng thành phòng ban và lương lớn nhất dựa trên dấu tab
    deptno, max_salary = line.strip().split('\t')
    max_salary = int(max_salary)
    
    # Kiểm tra xem phòng ban có thay đổi không
    if current_deptno != deptno:
        # Nếu phòng ban thay đổi, in ra lương lớn nhất của phòng ban trước đó
        if current_deptno is not None:
            print('%s\t%s' % (current_deptno, current_max_salary))
        # Cập nhật phòng ban và lương lớn nhất mới
        current_deptno = deptno
        current_max_salary = max_salary
    else:
        # Nếu phòng ban không thay đổi, so sánh và cập nhật lương lớn nhất
        current_max_salary = max(current_max_salary, max_salary)

# In ra lương lớn nhất của phòng ban cuối cùng
if current_deptno is not None:
    print('%s\t%s' % (current_deptno, current_max_salary))
