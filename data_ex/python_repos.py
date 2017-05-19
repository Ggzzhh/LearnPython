#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并储存响应
url="https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("Status code:", r.status_code)

# 将Api响应储存在一个变量中
response_dict = r.json()
print("总的仓库数量：", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print('返回仓库数', len(repo_dicts))

# 研究第一个仓库
#repo_dict = repo_dicts[0]
names, plot_dicts = [], []

print('\n仓库信息：')
for repo_dict in repo_dicts:
    # print('名字:', repo_dict['name'])
    # print('主人:', repo_dict['owner']['login'])
    # print('星数:', repo_dict['stargazers_count'])
    # print('仓库地址:', repo_dict['html_url'])
    # print('创造于:', repo_dict['created_at'])
    # print('更新于:', repo_dict['updated_at'])
    # print('描述:', repo_dict['description'])
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)
    

# 可视化
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Github 星数排名靠前的仓库'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')

# 处理结果
#print(response_dict.keys())