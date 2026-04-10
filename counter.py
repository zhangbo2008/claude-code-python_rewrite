import os
print("统计一下这个python版本的claudecode 的代码行数")
total = 0
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.py'):
            path = os.path.join(root, f)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    total += len(f.readlines())
            except:
                pass

print('总代码行数:', total)
# 统计一下这个python版本的claudecode 的代码行数
# 总代码行数: 17781