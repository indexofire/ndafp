第1节. 数据质控
===============

查看测序数据的质量情况。

1. FastQC
---------

FastQC 可能是最常用，也是最直观的测序数据质量控制软件。

1.1 安装 FastQC
^^^^^^^^^^^^^^^

FastQC
可以在图形界面下运行，如果在不带有图形界面的系统环境里也可以通过生成
html 报告再通过浏览器打开来查看结果。

.. code-block:: bash

    ~/tmp$ wget http://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.5.zip
    ~/tmp$ unzip fastqc_v0.11.5.zip -d ~/app
    ~/tmp$ sudo ln -s ~/app/FastQC/fastqc /usr/local/sbin

.. code-block:: bash

    # run fastqc in GUI mode
    ~$ fastqc
    # run fastqc in command line mode
    ~$ fastqc -f fastq ~/data/*.fastq

1.2 生成报告
^^^^^^^^^^^^

生成 html 报告文件和对应的 zip 压缩文件，并通过 scp
命令传输到本地后用浏览器打开查看。

.. code-block:: bash

    # scp  your linux/mac desktop system
    ~$ scp -i username@server-ip:~/data/* ~/
    # open it by google-chrome
    ~$ google-chrome *.html

1.3 结果说明
^^^^^^^^^^^^

FastQC 结果由11个模块组成，对于结果报告各个模块的说明可以参见
`FastQC <http://www.bioinformatics.babraham.ac.uk/projects/fastqc/>`__
文档。

+-----------------------------------+------------------------------------------+
| Module                            | Explanation                              |
+===================================+==========================================+
| **Basic Statistics**              | fastq文件的基本信息，可以看到序列数量和  |
|                                   | 读长，fastq文件版本，GC含量等。          |
+-----------------------------------+------------------------------------------+
| **Per base sequence quality**     | 最重要的结果模块之一，你可以从这个模块   |
|                                   | 的图示中了解序列中各个碱基的质量。       |
+-----------------------------------+------------------------------------------+
| **Per sequence quality score**    | ...                                      |
+-----------------------------------+------------------------------------------+
| **Per base sequence content**     | ...                                      |
+-----------------------------------+------------------------------------------+

数据处理：通过FastQC各个模块查看，发现低质量的序列需要切除或者序列污染的，比如smallRNA测序，文库被污染了接头等情况时，需要对数据进行去除污染序列的处理。

--------------------------------------------------------------------------------

2. Picard
---------

`Picard <http://broadinstitute.github.io/picard/>`__ 是
`BroadInstitute <https://www.broadinstitute.org/>`__ 使用 Java
语言开发的针对 BAM 等高通量测序数据的处理工具，特别是针对 Illumina
平台的数据。它可以提供一个测序质量和数据基本特性的报告。

2.1 安装 Picard
^^^^^^^^^^^^^^^

.. code-block:: bash

   ~/tmp$ wget https://github.com/broadinstitute/picard/releases/download/1.123/picard-tools-1.123.zip
   ~/tmp$ unzip -n picard-tools-1.123.zip -d ~/app

2.2 使用 Picard
^^^^^^^^^^^^^^^

Reference
---------

1. `Fastx\_toolkit <http://hannonlab.cshl.edu/fastx_toolkit/>`__
2. `The Picard
   Pipeline <https://www.broadinstitute.org/files/shared/mpg/plathumgen/plathumgen_fennell.pdf>`__
