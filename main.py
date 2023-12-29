import feedparser
import time
import os
import re
import pytz
from datetime import datetime

def main():
    # 替换 ---start--- 到 ---end--- 之间的内容
    fmt = '%Y-%m-%d %H:%M:%S %Z%z'
    insert_info = "---start---\n\n## Yane.zZ的每日更新(" + "更新时间:" + datetime.fromtimestamp(int(time.time()), pytz.timezone('Asia/Shanghai')).strftime(fmt) + ")\n" + "---end---"

    # 获取README.md内容
    with open(os.path.join(os.getcwd(), "README.md"), 'r', encoding='utf-8') as f:
        readme_md_content = f.read()

    print(insert_info)

    # 使用 re.DOTALL 标志匹配多行
    new_readme_md_content = re.sub(r'---start---(.|\n)*---end---', insert_info, readme_md_content, flags=re.DOTALL)

    with open(os.path.join(os.getcwd(), "README.md"), 'w', encoding='utf-8') as f:
        f.write(new_readme_md_content)

main()
