file_path = "pinyin-emoji.txt" # 替换为你自己的文件路径

with open(file_path, 'r') as f:
    text = f.read()

# 对文本进行处理
lines = text.split('\n')
new_text = ""
for line in lines:
    parts = line.split('\t')
    new_line = parts[1].replace(' ', '') + ',' + parts[2] + '=' + parts[0]
    new_text += new_line + '\n'

# 将处理结果保存为新的文本文件
new_file_path = "pinyin-sougou-emoji.py" # 替换为你自己的文件路径
with open(new_file_path, 'w') as f:
    f.write(new_text)
