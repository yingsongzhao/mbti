# MBTI 性格测试系统

一个基于 **FastAPI** 的 MBTI 性格在线测试系统，支持 24 题梯度选择、星座匹配搭子推荐、管理后台数据统计。

在线体验：<https://clawopen.ink/test>

## 功能特性

- **24 题梯度测试** — 4 维度 × 6 题，每题 3-4 梯度选项，权重计分更精确
- **16 型人格解析** — 含详细描述、擅长领域、适合职业、推荐兴趣、相似名人
- **星座 + MBTI 双维度搭子匹配** — 综合星座契合度和 MBTI 互补性，推荐 TOP 5 最佳搭子
- **管理后台** — 类型分布、四维度统计、测试结果明细、CSV 导出
- **扫码访问** — 自动生成二维码，手机扫码即可开始测试

## 技术栈

| 组件 | 技术 |
|------|------|
| 后端 | Python 3.11 + FastAPI |
| 数据库 | SQLite |
| 前端 | 原生 HTML/CSS/JS，无框架依赖 |
| 部署 | Nginx 反向代理 + Let's Encrypt HTTPS |

## 项目结构

```
├── main.py           # FastAPI 主服务
├── models.py         # SQLite 数据模型
├── questions.py      # 24 题题库 + 16 型人格描述（职业/兴趣/名人）
├── scoring.py        # 梯度计分算法
├── zodiac.py         # 12 星座数据 + 星座+MBTI 双维度匹配
── requirements.txt  # Python 依赖
├── static/
│   ├── test.html     # 测试页面
│   ├── admin.html    # 管理后台
│   └── style.css     # 样式
└── data/
    └── mbti.db       # SQLite 数据库
```

## 本地运行

```bash
pip install -r requirements.txt
python main.py
```



## 部署到阿里云

1. 上传项目文件到服务器 `/opt/mbti`
2. 安装 Python 3.11+ 和 Nginx
3. 创建虚拟环境并安装依赖
4. 配置 systemd 服务 + Nginx 反向代理
5. 使用 certbot 配置 HTTPS

详见项目中的 `deploy.sh` 脚本。

## License

MIT
