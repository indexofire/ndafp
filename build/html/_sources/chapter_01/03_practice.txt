Miseq 下机数据分析应用实例
==========================

在 Miseq 上通过对24个混合样本的PE测序，获得的下机 PF Data，从 Quality Control
到 de novo assembly 过程的基本操作流程。[#f1]_

1. 前期处理
-----------

1.1 分样
~~~~~~~~

为了避免文件混乱，首先将获得的001~024样本的 fastq 文件分别移动到以样本名命名的
24个文件夹中，分别进行操作。

.. code-block:: bash

    # 产生的数据文件名为格式为 0*_S*_L001_R1_001.fastq.gz/0*_S*_L001_R2.fastq.gz
    ~/data$ ls
    001_S1_L001_R1_001.fastq.gz   003_S3_L001_R1_001.fastq.gz   005_S5_L001_R1_001.fastq.gz
    001_S1_L001_R2_001.fastq.gz   003_S3_L001_R2_001.fastq.gz   005_S5_L001_R2_001.fastq.gz
    002_S2_L001_R1_001.fastq.gz   004_S4_L001_R1_001.fastq.gz   006_S6_L001_R1_001.fastq.gz
    002_S2_L001_R2_001.fastq.gz   004_S4_L001_R2_001.fastq.gz   006_S6_L001_R2_001.fastq.gz
    ...
    022_S22_L001_R1_001.fastq.gz   023_S23_L001_R1_001.fastq.gz   024_S24_L001_R1_001.fastq.gz
    022_S22_L001_R2_001.fastq.gz   023_S23_L001_R2_001.fastq.gz   024_S24_L001_R2_001.fastq.gz

    # 新建以样本名为文件夹名，并移动数据到文件夹的raw目录下
    ~/data$ for i in $(awk -F"L001" '{gsub("_$","",$1);print $1}' \
    > <(ls *.fastq.gz) | sort | uniq); \
    > do mkdir $(basename $i) && mkdir $(basename $i)/raw; \
    > mv $i*.fastq.gz $(basename $i)/raw/. ; done

    # 查看生成的各个样本的文件夹
    ~/data$ ls -d */
    001_S1    002_S2    003_S32   004_S4    005_S5    006_S6
    ...

1.2 查看测序质量
~~~~~~~~~~~~~~~~

1.2.1 FastQC
^^^^^^^^^^^^

用 FastQC 生成 html 格式的质量结果报告，用 Python 自带模块
SimpleHTTPServer 建立一个简便的 HTTP Server，以便查看 html 文档。

.. code-block:: bash

    ~/data$ mkdir -p qc
    ~/data$ for i in $(ls -d 0*/raw/*.fastq.gz); \
    > do fastqc $i --extract -t 40 -q -o qc ; done
    ~/data$ python -m SimpleHTTPServer

然后用客户端浏览器访问服务器IP:8080来查看，比如我们的服务器IP地址是
10.44.35.122，就在浏览器地址栏里输入http://10.44.35.122:8000，可以看到所在文件
夹的文件链接页面了。

1.2.2 Quast
^^^^^^^^^^^

用Quast生成

1.3 去除接头
~~~~~~~~~~~~

从前面的数据显示，部分插入片段比较短，因此部分reads测出接头序列。

1.4 去除低质量reads
~~~~~~~~~~~~~~~~~~~

Miseq v3
的PE300试剂最大的问题在于3'端急速下降的质量，特别是PE测序中R2端的质量。


.. rubric:: Reference

.. [#f1] fdakljfdla
