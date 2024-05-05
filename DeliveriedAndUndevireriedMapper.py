#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

# Duyệt qua từng dòng của dữ liệu đầu vào
for line in sys.stdin:
    # Tách các trường từ dòng
    fields = line.strip().split(',')
    
    # Xác định trạng thái giao hàng (cột thứ 7)
    delivery_status = fields[6]
    
    # Xuất trạng thái giao hàng và số lượng sản phẩm
    print(delivery_status + '\t1')
