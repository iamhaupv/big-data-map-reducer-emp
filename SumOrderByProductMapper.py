#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv

# Đọc dữ liệu từ luồng nhập tiêu chuẩn
reader = csv.reader(sys.stdin)
next(reader)  # Bỏ qua header

# Duyệt qua từng dòng của tập tin CSV
for row in reader:
    # Lấy loại sản phẩm từ cột thích hợp (ví dụ: cột 4)
    product_type = row[4]
    
    # Lấy số lượng hàng hóa bán ra từ cột thích hợp (ví dụ: cột 5)
    quantity_sold = int(row[5])
    
    # Xuất loại sản phẩm và số lượng hàng hóa bán ra
    print(product_type + '\t' + str(quantity_sold))
