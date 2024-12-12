import re
import os
from datetime import datetime
from pathlib import Path

# 网站基础URL
SITE_URL = "https://fastserver.cc/#/"

def generate_sitemap():
    # 读取_sidebar.md
    with open('_sidebar.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找所有.md链接
    links = re.findall(r'\[(.*?)\]\((.*?\.md)\)', content)
    
    # 生成sitemap内容
    sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
    sitemap_content += 'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
    sitemap_content += 'xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 '
    sitemap_content += 'http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">\n'
    
    for _, link in links:
        # 移除.md后缀
        url_path = link.replace('.md', '')
        
        # 获取文件最后修改时间
        try:
            mtime = os.path.getmtime(link)
            last_mod = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')
        except:
            last_mod = datetime.now().strftime('%Y-%m-%d')
        
        # 添加URL条目
        sitemap_content += f'''    <url>
        <loc>{SITE_URL}{url_path}</loc>
        <lastmod>{last_mod}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.8</priority>
    </url>\n'''
    
    sitemap_content += '</urlset>'
    
    # 写入sitemap.xml
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap_content)

if __name__ == '__main__':
    generate_sitemap()
    print("Sitemap generated successfully!") 