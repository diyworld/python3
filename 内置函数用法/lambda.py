# lambda 匿名函数

# rssi 与 rcpi 换算
ieee1905_rssi_to_rcpi = lambda rssi: (2 * ((rssi) + 110))
ieee1905_rcpi_to_rssi = lambda rcpi: (((rcpi) / 2) - 110)
print("rssi = -22  -> rcpi = ", ieee1905_rssi_to_rcpi(-22))
print("rcpi = -176 -> rssi = ", ieee1905_rcpi_to_rssi(176))

# 字符串比较
strcmp = lambda str1, str2: True if (str1 == str2) else False
print(strcmp("abcd", "abcd"))
print(strcmp("abcd", "abcd1"))
print(strcmp("abcd", "abce"))