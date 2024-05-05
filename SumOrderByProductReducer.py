#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

# Khởi tạo biến để lưu tổng số lượng hàng hóa bán ra cho từng loại sản phẩm
product_sales = {}

# Duyệt qua các cặp key-value từ Mapper
for line in sys.stdin:
    # Tách loại sản phẩm và số lượng hàng hóa từ dòng đầu vào
    product_type, quantity_sold = line.strip().split('\t')
    
    # Chuyển đổi số lượng hàng hóa thành kiểu integer
    quantity_sold = int(quantity_sold)
    
    # Cập nhật tổng số lượng hàng hóa bán ra cho từng loại sản phẩm
    if product_type in product_sales:
        product_sales[product_type] += quantity_sold
    else:
        product_sales[product_type] = quantity_sold

# In ra số lượng bán hàng trên từng loại sản phẩm
for product_type, total_sold in product_sales.items():
    print(product_type + '\t' + str(total_sold))