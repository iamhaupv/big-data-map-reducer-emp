#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv

# Đọc dữ liệu từ luồng nhập tiêu chuẩn
reader = csv.reader(sys.stdin)
next(reader)  # Bỏ qua header

# Khởi tạo dictionary để lưu trữ lương lớn nhất của mỗi phòng ban
max_salaries = {}

# Đọc từng dòng của tập tin CSV đầu vào
for row in reader:
    deptno = row[6]  # Lấy cột deptno (cột 7)
    salary = int(row[5])  # Lấy cột lương (cột 6)
    
    # Kiểm tra xem phòng ban đã được thêm vào dictionary chưa
    if deptno in max_salaries:
        # Nếu đã tồn tại, so sánh và cập nhật lương lớn nhất
        max_salaries[deptno] = max(max_salaries[deptno], salary)
    else:
        # Nếu chưa tồn tại, thêm phòng ban vào dictionary
        max_salaries[deptno] = salary

# Xuất phòng ban và lương lớn nhất tương ứng
for deptno, max_salary in max_salaries.items():
    print('%s\t%s' % (deptno, max_salary))
