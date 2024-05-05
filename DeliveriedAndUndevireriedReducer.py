#!/usr/bin/env python
# -*- coding: utf-8 -*-s
import sys

# Khởi tạo biến đếm cho số lượng đơn hàng đã giao và chưa giao
delivered_count = 0
undelivered_count = 0

# Duyệt qua các cặp key-value từ Mapper
for line in sys.stdin:
    # Tách trạng thái giao hàng và số lượng từ dòng đầu vào
    delivery_status, count = line.strip().split('\t')
    
    # Chuyển đổi số lượng từ kiểu string sang kiểu integer
    count = int(count)
    
    # Cập nhật số lượng đơn hàng đã giao và chưa giao
    if delivery_status == '1':
        delivered_count += count
    elif delivery_status == '0':
        undelivered_count += count

# In ra tổng số lượng đơn hàng đã giao và chưa giao
print('Tong so luong don hang da giao:', delivered_count)
print('Tong so luong don hang chua giao:', undelivered_count)
