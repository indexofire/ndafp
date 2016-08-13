基因组可视化工具
================

1. NCBI gbench
--------------

1.1 安装 gbench
^^^^^^^^^^^^^^^

.. code-block:: bash

   $ wget ftp://ftp.ncbi.nlm.nih.gov/toolbox/gbench/ver-2.10.7/gbench-src-2.10.7.tgz
   $ tar zxf gbench-src-2.10.7.tgz
   $ mv gbench-src-2.10.7 /opt/gbench
   $ cd /opt/gbench
   $ ./configure
   $ sudo make && make install
