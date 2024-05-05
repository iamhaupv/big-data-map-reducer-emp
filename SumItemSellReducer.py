#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

# Khởi tạo biến để lưu tổng số lượng hàng hóa bán ra
total_items_sold = 0

# Duyệt qua các cặp key-value từ Mapper
for line in sys.stdin:
    # Tách key và value từ dòng đầu vào
    key, value = line.strip().split('\t')
    
    # Tăng tổng số lượng hàng hóa bán ra bằng giá trị của từng hàng hóa
    total_items_sold += int(value)

# In ra tổng số lượng hàng hóa bán ra
print("Tong so hang hoa duoc ban:", total_items_sold)
