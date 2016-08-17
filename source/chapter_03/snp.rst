
1. 需要参考基因组比对的软件
---------------------------

1.1 REALPHY
^^^^^^^^^^^

REALPHY 取了一个比较容易起争议的名字，这个软件可以选择不同的参考基因组进行分析。

**下载安装**


1.2 Snippy
^^^^^^^^^^

**下载安装**

.. code-block:: bash

   $ cd repos && git clone https://github.com/tseemann/snippy
   $ echo 'export PATH="$HOME/repos/snippy/bin:$HOME/repos/snippy/binary/linux:$PATH"' >> ~/.bashrc
   $ source ~/.bashrc

**Docker容器使用**

.. literalinclude:: realphy.docker
   :language: bash

2. 不需要参考基因组的软件
-------------------------

2.1 kSNP
^^^^^^^^

kSNP 采用的是基于 kmer 的算法，不需要进行序列的多重比对，也不需要参考基因组进行 Mapping。kSNP 可以分析细菌完成基因组和未完成基因组，也可以直接分析测序 reads 数据。

**下载安装**

.. code-block:: bash

    # 下载软件包
    $ wget http://nchc.dl.sourceforge.net/project/ksnp/kSNP3.021_Linux_package.zip
    $ sudo unzip kSNP3.021_Linux_package.zip
    $ sudo mv kSNP3.021_Linux_package /opt/ksnp
    $ cd /opt/ksnp
    # 添加版本信息文件
    $ touch v3.021
