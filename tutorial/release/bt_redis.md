# Redis - 宝塔

- 安装 [宝塔](https://www.bt.cn/new/download.html)

- 软件商店搜索redis并安装

- 在性能配置里设置密码

- 如果需要外网访问

  - 点击redis设置，选择配置文件并修改以下内容

      ```
      bind 0.0.0.0
      protected-mode no
      ```
  
  - 重启redis服务

- 开放端口

  - 选择安全菜单

  - 添加端口规则

    ```
    协议：TCP/UDP
    端口：redis的端口
    ```

  - 保存