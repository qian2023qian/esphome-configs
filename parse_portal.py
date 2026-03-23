import sys
import re
# 这个脚本用于从 esphome 的 web portal 输出的 pronto 数据中提取出十六进制字符，并以空格分隔的形式输出
print("input esphome web portal output of pronto data, end with Ctrl-D") # 提示用户输入数据，并说明如何结束输入
print("---------------------------")
input_string = sys.stdin.read()

print("")
print("result")
print("-"*30)  
match_pronto_char = re.findall(r"[A-F0-9]{4}", input_string)
print(" ".join(match_pronto_char))  