第1节. 测序数据构建 Pangenomics 分析
====================================

数据准备：



1. 使用 Roary 来分析 Pangenomes
-------------------------------

1.1 安装 roary
^^^^^^^^^^^^^^

**使用 Ubuntu apt 安装预编译包**

.. code-block:: bash

    ~$ sudo apt install roary

**下载官方预编译包**

.. code-block:: bash

    ~$ wget

.. code-block:: bash

    ~$ roary -e -n -v data/*.gff -f roary_output
