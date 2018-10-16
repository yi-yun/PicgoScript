# iOS图片上传
## 介绍

- Pythonista
这个被称为神器不是没有原因的，能利用 Python 获取 iOS 的原生接口，这一条就能打败 80% 的应用。68RMB 真的物超所值！

- 腾讯云的对象存储
[这篇文章](https://yi-yun.github.io/%E5%9B%BE%E5%BA%8A%E7%9A%84%E9%80%89%E6%8B%A9/)介绍了详细内容

## 配置环境

1. 打开 `Pythonista` 输入
    ```Python
    import requests as r
    exec(r.get('https://bit.ly/get-stash').text)
    ```
    运行即可在目录下得到 `launch_stash.py`，打开这个文件再次点击运行即可进入控制台

2. 输入 `pip install -U cos-python-sdk-v5` 安装环境，若报错可将 -U 去掉，之后再安装缺少的模块即可

3. 下载[这个文件](https://yiyun-1253940215.cos.ap-shanghai.myqcloud.com/ImageBed.py)，配置相应参数
PS：需要五处

## 使用
在相册中分享图片，选中 `Run Pythonista Script`，选中相应的脚本 `run` 剪贴板就会有 `MarkDown` 形式的链接

PS：可以在 `Pythonista` 首页设置