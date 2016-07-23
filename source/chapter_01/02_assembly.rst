第2节. 基因组拼接
=================

物种的核酸特性以及测序技术的发展，不断有针对新技术优化的拼接软件出现。这里比较几个微生物拼接评测中比较优秀的工具，看看针对目标物种的拼接结果。个人最常用的拼接软件是spades，目前版本是3.8.2。也可以先对自己的测序物种做一个 assembly evaluation，选择比较适合的拼接软件。


1. SPAdes
---------

1.1 下载并安装 SPAdes
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   ~/tmp$ curl -O http://spades.bioinf.spbau.ru/release3.8.2/SPAdes-3.8.2-Linux.tar.gz
   ~/tmp$ tar zxf SPAdes-3.8.2-Linux.tar.gz -C ~/app
   ~/tmp$ cd ~/app
   ~/app$ sudo ln -s `pwd`/SPAdes-3.8.2-Linux/bin/* /usr/local/sbin

1.2 拼装基因组
^^^^^^^^^^^^^^

.. code-block:: bash

   ~/app$ spades.py -t 2 -1 SRR95386_1.fastq -2 SRR955386_2.fastq -o spades_output

SPAdes会尝试不同的Kmer，因此拼装时间也会根据Kmer选择数量成倍增加。

对于常见的 Miseq v2/v3 试剂盒，采用 PE150/PE250/PE300 的读长测序，常用的拼接命令是：

.. code-block:: bash

   # PE150 读长测序数据
   ~/apps spades.py -k 21,33,55,77 --careful SRR95386_1.fastq -2 SRR955386_2.fastq -o SRR95386_output
   # PE250 读长测序数据
   ~$ apps spades.py -k 21,33,55,77,99,127 --careful SRR95386_1.fastq -2 SRR955386_2.fastq -o SRR95386_output

--------------------------------------------------------------------------------

2. Macursa
----------

2.1 下载并安装 MaSuRCA
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   ~/tmp$ curl -O ftp://ftp.genome.umd.edu/pub/MaSuRCA/MaSuRCA-2.3.0.tar.gz
   ~/tmp$ tar zxvf MaSuRCA-2.3.0.tar.gz -C ~/app
   ~/tmp$ cd ~/app
   ~/app$ ./MaSuRCA-2.3.0/install.sh
   ~/app$ sudo ln -s `pwd`/MaSuRCA-2.3.0/bin/masurca /usr/local/sbin

2.2 建立拼装配置文件
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   ~/data$ touch SRR955386_masurca.config
   ~/data$ nano SRR955386_masurca.config

文件内容修改如下：

.. code-block:: bash

   DATA
   PE= p1 500 50 SRR955386_1.fastq SRR955386_2.fastq
   END

   PARAMETERS
   GRAPH_KMER_SIZE=auto
   USE_LINKING_MATES=1
   LIMIT_JUMP_COVERAGE = 60
   KMER_COUNT_THRESHOLD = 1
   NUM_THREADS= 2
   JF_SIZE=100000000
   DO_HOMOPOLYMER_TRIM=0
   END

设置 **GRAPH_KMER_SIZE=auto**，软件会调用Kmer=31来进行拼装。对于MiSeq PE250以上的插片，可以考虑手动设置使用更大的Kmer。

2.3 开始拼装
^^^^^^^^^^^^

.. code-block:: bash

   ~/app$ masurca SRR955386_masurca.config
   ~/app$ ./assemble.sh

--------------------------------------------------------------------------------

3. Velvet
---------

--------------------------------------------------------------------------------

4. A5-miseq
-----------

`A5-miseq <https://sourceforge.net/projects/ngopt/>`__ 是一个用 perl
开发的针对细菌基因组 de novo assembly 的 pipeline
工具。它本身不参与组装，而是通过组合一套工具来完成工作，工具集包括：

- bwa
- samtools
- SGA
- bowtie
- Trimmomatic
- IDBA-UD
- SSPACE

这些工具都以及集成在 A5-miseq 中，不需要另外安装。为了避免不同版本的
samtools，bowtie 对结果产生的差异，建议采用虚拟环境如 docker
等来隔离运行环境。

4.1 安装 A5-miseq
^^^^^^^^^^^^^^^^^

下载预编译包安装
~~~~~~~~~~~~~~~~

.. code-block:: bash

   ~/tmp$ wget http://downloads.sourceforge.net/project/ngopt/a5_miseq_linux_20150522.tar.gz
   ~/tmp$ tar zxvf a5_miseq_linux_20150522.tar.gz -C ~/app
   ~/tmp$ sudo ln -s ~/app/a5_miseq_linux_20150522/bin/a5_pipeline.pl /usr/local/sbin

建立 Docker 容器安装
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   ~/docker$ mkdir -p a5-miseq && cd a5-miseq
   ~/docker/a5-miseq$ touch Dockerfile

.. code-block:: bash

   FROM ubuntu:latest
   MAINTAINER Mark Renton <indexofire@gmail.com>

   RUN apt-get update -qy
   RUN apt-get install -qy openjdk-7-jre-headless file
   ADD http://downloads.sourceforge.net/project/ngopt/a5_miseq_linux_20150522.tar.gz /tmp/a5_miseq.tar.gz
   RUN mkdir /tmp/a5_miseq
   RUN tar xzf /tmp/a5_miseq.tar.gz --directory /tmp/a5_miseq --strip-components=1
   ADD run /usr/local/bin/
   ADD Procfile /
   ENTRYPOINT ["/usr/local/bin/run"]

4.2 使用 A5-miseq
^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ perl a5_pipeline.pl SRR955386_1.fastq SRR955386_2.fastq ~/data/a5_output

4.3 A5-miseq 文档
^^^^^^^^^^^^^^^^^

查看 A5-miseq 工具的使用文档可以用 a5_pipeline.pl 工具查看。

.. code-block:: bash

    # Usage:
    $ a5_pipeline.pl [--begin=1-5] [--end=1-5] [--preprocessed] <lib_file> <out_base>

Reference:
----------
