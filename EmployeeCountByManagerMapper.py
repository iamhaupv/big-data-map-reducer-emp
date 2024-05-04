#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv

# Đọc dữ liệu từ luồng nhập tiêu chuẩn
reader = csv.reader(sys.stdin)
next(reader)  # Bỏ qua header

# Duyệt qua từng dòng của tập tin CSV
for row in reader:
    # Lấy mã quản lý (manager) từ cột thích hợp (ví dụ: cột 4)
    manager = row[3]
    
    # Xuất mã quản lý cùng với giá trị 1 để đếm
    print('%s\t%s' % (manager, 1))
