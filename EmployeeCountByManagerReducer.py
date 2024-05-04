# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys

current_manager = None
employee_count = 0

# Đọc dữ liệu từ luồng nhập tiêu chuẩn
for line in sys.stdin:
    # Tách dòng thành mã quản lý và giá trị đếm dựa trên dấu tab
    manager, count = line.strip().split('\t')
    
    # Kiểm tra xem mã quản lý có thay đổi không
    if current_manager != manager:
        # Nếu mã quản lý thay đổi, in ra số lượng nhân viên của quản lý trước đó
        if current_manager is not None:
            print('%s\t%s' % (current_manager, employee_count))
        # Cập nhật mã quản lý và số lượng nhân viên mới
        current_manager = manager
        employee_count = 0
    
    # Tăng số lượng nhân viên cho quản lý hiện tại
    employee_count += int(count)

# In ra số lượng nhân viên của quản lý cuối cùng
if current_manager is not None:
    print('%s\t%s' % (current_manager, employee_count))
