SPAdes
======

1. 下载并安装 SPAdes
--------------------

.. code-block:: bash

    $ curl -O http://spades.bioinf.spbau.ru/release3.1.1/SPAdes-3.9.1-Linux.tar.gz
    $ tar zxvf SPAdes-3.9.1-Linux.tar.gz
    $ sudo mv SPAdes-3.9.1-Linux /opt/spades
    $ sudo ln -s /opt/spades/bin/* /usr/local/sbin

2. 拼装基因组
-------------

.. code-block:: bash

    # 对PE250以上的测序数据
    $ spades.py -t 40 -k 21,33,55,77,99,127 --careful \
    > -1 sample1_R1.fastq -2 sample2_R2.fastq -o assembly_spades
