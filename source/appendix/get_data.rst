获取数据
========

1. 安装 ascp connect
--------------------

aspera connect 的`下载地址 <http://downloads.asperasoft.com/en/downloads/8?list>`_

.. code-block:: bash

   # download ascp connect
   $ wget http://download.asperasoft.com/download/sw/connect/3.6.2/aspera-connect-3.6.2.117442-linux-64.tar.gz
   $ tar zxf aspera-connect-3.6.2.117442-linux-64.tar.gz
   $ ./aspera-connect-3.6.2.117442-linux-64.sh

因为需要 ssh 密钥，软件只能以用户身份安装，不能以 root 安装。软件默认安装位置在 ~/.ascp/connect/
