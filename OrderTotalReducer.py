#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

# Khởi tạo biến để lưu tổng số hóa đơn
total_bills = 0

# Duyệt qua các cặp key-value từ Mapper
for line in sys.stdin:
    # Tách key và value từ dòng đầu vào
    key, value = line.strip().split('\t')
    
    # Tăng tổng số hóa đơn bằng giá trị của từng hóa đơn
    total_bills += int(value)

# In ra tổng số hóa đơn
print("Tong so hoa don:", total_bills)
