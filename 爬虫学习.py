import requests
from bs4 import BeautifulSoup

url = "https://top.baidu.com/board?tab=realtime"
headers = {
    "User-Agent": "Mozilla/5.0"  # 模拟浏览器防止被拒绝访问
}
response = requests.get(url, headers=headers)

# 解析网页
soup = BeautifulSoup(response.text, "html.parser")

# 找到所有热搜词标签
hotwords = soup.find_all("div", class_="c-single-text-ellipsis")

# 打印热词
for i, tag in enumerate(hotwords):
    print(f"{i+1}. {tag.text.strip()}")

