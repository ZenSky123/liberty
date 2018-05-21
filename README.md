# 校园网绕过深澜拨号连接

学校的联网太傻逼了，每次联网要打开那个丑的不行的深澜客户端，等待一大堆xxxx的加载，然后还不定时出无语BUG——自动断网。

起始我写了个脚本联网，账号密码存在脚本目录的json文件下，然后在win下写一个bat文件，接受命令行参数然后调用Python文件，太丑了，重写。

重新写了读取配置，现在配置可以生成在用户目录下了（我觉得这样很优雅），废弃了bat文件，使用了docopt库，用setup.py安装到scripts中。

具体使用如：
```text
Elegant for Internet
 
Usage:
    connect
    connect init
    connect show
    connect <password>
Options:
    init        Initialize your Internet config.
    show        Show your current Internet config.
    password    If you want to override config's password.
```


第一次运行需要`connect init`，初始化配置。之后可以在命令行下`connect`连接网络

如果密码变更（比如我校电信就经常变换连接密码），`connect <password>`就可以完成连接，同时`<password>`参数会覆盖你用户目录下的配置。

## Todo
- 命令行修改指定配置
- 设置连接计划
    - 例：在周一到周五的7:00之前和23:00之后不进行连接
- 添加系统服务
    - 宽带无法连接自动切换WiFi

## Develop Log
- 2018年5月21日
    - 完成基础功能
    - 添加setup.py