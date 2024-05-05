#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv

# Đọc dữ liệu từ luồng nhập tiêu chuẩn
reader = csv.reader(sys.stdin)
next(reader)  # Bỏ qua header

# Duyệt qua từng dòng của tập tin CSV
for row in reader:
    # Xuất 1 cho mỗi hóa đơn
    print('Total Bills\t1')
