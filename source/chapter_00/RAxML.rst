RAxML
=====

1. 安装 RAxML
-------------

从 github 仓库克隆代码安装。

.. code-block:: bash

   $ git clone https://github.com/stamatak/standard-RAxML
   $ cd standard-RAxML
   $ make -f Makefile.SSE3.PTHREADS.gcc && rm *.o
   $ sudo ln -s `pwd`/raxmlHPC-PTHREADS-SSE3 /usr/local/bin/raxml

2. 使用 RAxML
-------------

.. code-block:: bash

   # 绘制无根树
   $ raxml -s alignment.phy -m GTRGAMMA -p 12345 -T 40 -w raxml_output -n raxml
   # 绘制有跟树，如根名叫 xyz
   $ raxml -s alignment.phy -m GTRGAMMA -p 12345 -o xyz

3. Reference
------------

* http://sco.h-its.org/exelixis/resource/doc/Phylo100225.pdf
