Aspera connect
==============

`Aspera <asperasoft.com>`__ 是 IBM 研发的加速在线数据传输的一系列服务器端与客户端的应用。\ `Aspera <asperasoft.com>`__ 的相关工具可以在 `这里 <http://downloads.asperasoft.com/downloads>`__ 下载获得。对于服务器用户，可以使用 `Aspera Connent <http://download.asperasoft.com/download/sw/connect/3.6.1/aspera-connect-3.6.1.110647-linux-64.tar.gz>`__\ ，目前的最新版本是 3.6.1（基于的 ascp 版本是3.5.6）。\ `Aspera
Connect <download.asperasoft.com/download/docs/connect/3.6.1/user_linux/webhelp/index.html#dita/introduction.html>`__
是 `Aspera <asperasoft.com>`__
其中的一款用于浏览器下载的高效插件，因为其内嵌了\ ``ascp``
命令可以用于服务器，而选择安装这个工具不是使用其 asperaconnect
工具。不过安装了 `Aspera
Connect <download.asperasoft.com/download/docs/connect/3.6.1/user_linux/webhelp/index.html#dita/introduction.html>`__
的带图形界面的客户端，浏览器会在有 Connect, Faspex 或者 Shares
页面的链接处添加 ascp 下载快捷按钮。

1. 下载安装
-----------

`Aspera
Connect <download.asperasoft.com/download/docs/connect/3.6.1/user_linux/webhelp/index.html#dita/introduction.html>`__
就会安装到当前用户 ``~/.aspera/connect`` 目录或安装在
``/opt/aspera/connect`` 目录下。

.. code:: bash

    ~$ cd /tmp
    /tmp$ curl -O http://download.asperasoft.com/download/sw/connect/3.6.1/aspera-connect-3.6.1.110647-linux-64.tar.gz
    /tmp$ tar zxf asper-commect-3.6.1.110647-linux.tar.gz
    /tmp$ ./aspera-connect-3.6.1.110647-linux-64.sh*

对于喜欢使用客户端的桌面用户，也可以使用 `Aspera Desktop Client <http://downloads.asperasoft.com/en/downloads/2>`__ 客户端程序来下载数据。

2. 设置
-------

服务器端没有 GUI 图形化界面。如果在 Desktop 版本的 Linux 操作系统上，可以运行 `asperaconnect`, 可以看到相应的配置界面。
