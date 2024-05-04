#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv

# Đọc dữ liệu từ luồng nhập tiêu chuẩn
reader = csv.reader(sys.stdin)
next(reader)  # Bỏ qua header

# Khởi tạo dictionary để lưu trữ lương thấp nhất của mỗi vị trí công việc
min_salaries = {}

# Đọc từng dòng của tập tin CSV đầu vào
for row in reader:
    position = row[2]  # Lấy cột designation (cột 3)
    salary = int(row[5])  # Lấy cột lương (cột 6)
    
    # Kiểm tra xem vị trí công việc đã được thêm vào dictionary chưa
    if position in min_salaries:
        # Nếu đã tồn tại, so sánh và cập nhật lương thấp nhất
        min_salaries[position] = min(min_salaries[position], salary)
    else:
        # Nếu chưa tồn tại, thêm vị trí công việc vào dictionary
        min_salaries[position] = salary

# Xuất vị trí công việc và lương thấp nhất tương ứng
for position, min_salary in min_salaries.items():
    print('%s\t%s' % (position, min_salary))
