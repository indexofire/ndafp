第2节. 使用 Centrifuge 分析
===========================

Centrifuge 是一个快速检索 reads 的软件，可以用于对微生物样本测序后的宏基因组数据分析。

1. 安装 Centrifuge
------------------

.. code-block:: bash

   # 安装软件
   $ git clone https://github.com/infphilo/centrifuge
   $ cd centrifuge
   $ make
   $ sudo make install
   # 下载数据库
   $ cd indices
   $ make b+h+v

2. 使用 Centrifuge
------------------
