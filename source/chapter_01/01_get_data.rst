第1节. 公共数据库获取数据
=========================

完成测序后一般需要将测序原始数据如 reads 数据上传到公共数据库，以便在发表的文章中引用原始的测序结果。很多时候，我们也需要获取他人发表的公开测序数据，来帮助自己的研究领域。本节我们就来了解一下如何上传自己的测序数据和下载别人的测序数据。首先让我们来了解一下网络上的测序公共数据库：

**最常用的测序公共数据库：**

1. `SRA <http://www.ncbi.nlm.nih.gov/sra>`_ 短序列数据库：由 `NCBI <http://www.ncbi.nlm.nih.gov>`_ 负责维护
2. `ENA <http://www.ebi.ac.uk/ena>`_ 欧洲核酸数据库：由 `EBI <http://www.ebi.ac.uk>`_ 负责维护

`SRA <http://www.ncbi.nlm.nih.gov/sra>`_ 是 `NCBI <http://www.ncbi.nlm.nih.gov>`_ 为了应对越来越多的高通量测序数据而在 2007 年底推出的测序数据库，用于存储、显示、提取和分析高通量测序数据。而 `ENA <www.ebi.ac.uk/ena>`__ 则是由 `EBI <www.ebi.ac.uk>`__ 负责维护的功能类似的数据库，同时作为 `Ensembl <www.ensembl.org>`__\ 、\ `UniProt <www.uniprot.org>`__ 和 `ArrayExpress <www.ebi.ac.uk/arrayexpress>`__ 等服务的底层基础。2者在主要功能方面非常类似，同时数据互通。

--------------------------------------------------------------------------------

SRA 数据库简介
--------------

.. note::

    `SRA <www.ncbi.nlm.nih.gov/sra>`__ 是 **S**\ equence **R**\ ead
    **A**\ rchive 的首字母缩写。SRA 与 Trace 最大的区别是将实验数据与
    metadata（元数据）分离。metadata
    是指与测序实验及其实验样品相关的数据，如实验目的、实验设计、测序平台、样本数据(物种，菌株，个体表型等)。metadata可以分为以下几类：

-  Study：accession number 以 DRP，SRP，ERP
   开头，表示的是一个特定目的的研究课题，可以包含多个研究机构和研究类型等。study
   包含了项目的所有 metadata，并有一个 NCBI 和 EBI
   共同承认的项目编号（universal project id），一个 study
   可以包含多个实验（experiment）。
-  Sample：accession number以 DRS，SRS，ERS
   开头，表示的是样品信息。样本信息可以包括物种信息、菌株(品系)
   信息、家系信息、表型数据、临床数据,组织类型等。可以通过
   `Trace <http://www.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=search_obj>`__
   来查询。
-  Experiment：accession number 以 DRX，SRX，ERX
   开头。表示一个实验记载的实验设计（Design），实验平台（Platform）和结果处理
   （processing）三部分信息。实验是 `SRA <www.ncbi.nlm.nih.gov/sra>`__
   数据库的最基本单元，一个实验信息可以同时包含多个结果集（run）。
-  Run：accession number 以DRR，SRR，ERR 开头。一个 Run
   包括测序序列及质量数据。
-  Submission：一个 study 的数据，可以分多次递交至 SRA
   数据库。比如在一个项目启动前期，就可以把 study，experiment
   的数据递交上去，随着项目的进展，逐批递交 run 数据。study
   等同于项目，submission 等同于批次的概念。

下面以 SRA 数据库为例介绍数据下载和上传的操作方法。

--------------

下载数据
--------

从 `SRA <www.ncbi.nlm.nih.gov/sra>`__
数据库下载数据有多种方法。可以用\ ``ascp``\ 快速的来下载 sra
文件，也可以用\ ``wget``\ 或\ ``curl``\ 等传统命令从 FTP 服务器上下载
sra 文件。另外 sratoolkit 工具集也支持直接下载。

1. Aspera
~~~~~~~~~



1.2 获取 SRA 数据
^^^^^^^^^^^^^^^^^

    注意新版的\ ``ascp``\ 用\ ``.openssh``\ 作为密钥文件而不是原来的\ ``.putty``

.. code:: bash

    ~/data$ ascp -i ~/.aspera/connect/etc/asperaweb_id_dsa.openssh \
    > --user=anonftp --host=ftp.ncbi.nlm.nih.gov --mode=recv -l 100m -pQTk1 \
    > /sra/sra-instant/reads/ByRun/sra/SRR/SRR955/SRR955386/SRR955386.sra .

2. sratoolkit
~~~~~~~~~~~~~

`NCBI <www.ncbi.nlm.nih.gov>`__ 开发了 sratoolkit 工具来帮助处理 SRA
数据，正确配置后可以很方便的下载 SRA 数据。

2.1 安装sratoolkit
^^^^^^^^^^^^^^^^^^

可以直接从 `NCBI <www.ncbi.nlm.nih.gov>`__ 上下载。最新的源码可以在
`Github <https://github.com/ncbi/sra-tools>`__ 获得。

.. code:: bash

    # download from NCBI
    ~$ cd /tmp
    /tmp$ wget http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.5.6/sratoolkit.2.5.6-ubuntu64.tar.gz
    /tmp$ tar zxf sratoolkit.2.5.6-ubuntu64.tar.gz -C ~/app

2.2 下载 SRA 格式文件
^^^^^^^^^^^^^^^^^^^^^

如果你安装并设置了 `Aspera
Connect <download.asperasoft.com/download/docs/connect/3.6.1/user_linux/webhelp/index.html#dita/introduction.html>`__\ ，那么\ ``prefetch``\ 会优先使用\ ``ascp``\ 方式来下载，如果没有安装或则\ ``ascp``\ 下载失败，则切换成
HTTP 方式下载 sra
数据。另外\ ``fastq-dump``\ 命令也能从远端直接下载数据，加上\ ``-X 1``\ 参数，会预先下载最前的5个
reads，加上\ ``-Z``\ 参数，则会将这些 reads 打印到终端输出。

.. code:: bash

    # 下载 SRR955386.sra 到 你安装 sratoolkit 时配置的 public 目录中，默认是 ~/ncbi/public/sra
    ~$ prefetch -v SRR955386
    # 下载 SRR955386.sra 到 你安装 sratoolkit 时配置的 public 目录中，默认是 ~/ncbi/public/sra，并且在终端输出5行 reads 数据。
    ~$ fastq-dump -X 5 -Z SRR955386

.. code-block:: bash

    $ cat sra.list | xargs prefetch -v

2.3 并转换成 .fastq 格式
^^^^^^^^^^^^^^^^^^^^^^^^

获得了 .sra 文件后，需要将其转换成 .fastq
格式的文件，用\ ``fastq-dump``\ 可以很方便的实现。转换之前要注意的是该
run 的 metadata 里，测序类型是 SE 还是 PE 的。

.. code:: bash

    # 将 sra 文件移动到 ~/data 目录中
    ~$ mv ~/.ncbi/public/sra/SRR955386.sra ~/data
    # 如果是 SE 测序数据，直接运行以下命令
    ~$ fastq-dump SRR955386.sra
    # 如果是 PE 测序数据，则要添加参数：--split-files
    ~$ fastq-dump --split-files SRR955386.sra

2.4 SE/PE 文件判断
^^^^^^^^^^^^^^^^^^

正常的 sra 文件的 metadata 应该包含测序采用的是 SE 还是 PE
的方式。但如果你不知道所下载的到底是 SE 还是 PE
格式的文件可以用\ ``fastq-dump -X 1 --split-spot``\ 的方法来判断。

.. code:: bash

    # it's SE if nreads=1, and PE when nreads=2，统计整个文件，因此速度比较慢
    ~$ sra-stat -xs SRR955386.sra | grep "nreads"

    # 如果输出是4，那么就是SE，如果是8,则是PE
    ~$ fastq-dump -X 1 --split-spot -Z SRR955386.sra | wc -l

    # 或者加上参数让 fastq-dump 自己判断
    # 当 sra 文件是 SE 测序时，fastq-dump只能dump出1个 *_1.fastq 文件
    ~$ fastq-dump --split-files ERR493452.sra
    ~$ mv ERR493452_1.fastq ERR493452.fastq

当需要判断批量下载的 sra 文件时，区分那些是 PE 的那些是 SE
的文件，可以用以下脚本：

.. code:: python

    import os
    import subprocess


    def check_SRA_type(fn):
        fn = os.path.abspath(fn);
        try:
            contents = subprocess.check_output(["fastq-dump", "-X", "1", "-Z", "--split-spot", fn]);
        except subprocess.CalledProcessError, e:
            raise Exception("Error running fastq-dump on", fn);
        # -X 1 will output 4 lines if SE, and 8 lines if PE
        if(contents.count("\n") == 4):
            return False;
        elif(contents.count("\n") == 8):
            return True:
        else:
            raise Exception("Unexpected output from fastq-dump on ", filename);

2.5 利用entrez批量下载
^^^^^^^^^^^^^^^^^^^^^^

如果想下载一个完整的 project 数据，可以利用 entrezdirect 工具。

.. code:: bash

    ~/tmp$ wget ftp://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/edirect.tar.gz
    ~/tmp$ tar zxvf edirect.tar.gz -C ~/app
    ~/tmp$ sudo ln -s ~/app/edirect/* /usr/local/sbin/
    ~/data$ esearch -db sra -query PRJNA40075  | efetch --format runinfo | cut -d ',' -f 1 | grep SRR | xargs fastq-dump --split-files

如果想下载不同 research 的数据，可以自己建立一个 accession number list
的文件，比如利用 `NCBI <www.ncbi.nlm.nih.gov>`__ 的 entrez
网页界面，导出所需要的数据 accession number，然后利用 ``ascp``
下载。不过建议\ ``ascp``\ 下载不要太狠心，否则容易被
`NCBI <www.ncbi.nlm.nih.gov>`__ 给封掉。

--------------

上传数据
--------

SRA 上传测序结果可以参照
`NCBI文档 <http://www.ncbi.nlm.nih.gov/books/NBK47529/>`__
来实现。一般上传数据到NCBI SRA的过程需要6步：

1. Create a BioProject for this research
2. Create a BioSample submission for your biological sample(s)
3. Gather Sequence Data Files
4. Enter Metadata on SRA website 4.1 Create SRA submission 4.2 Create
   Experiment(s) and link to BioProject and BioSample 4.3 Create Run(s)
5. Transfer Data files to SRA
6. Update Submission with PubMed links, Release Date, or Metadata
   Changes

需要注意的一点是，上传的过程中很多地方一旦保存或提交就不可以修改，尤其是各处的Alias。但是，可以联系NCBI的工作人员修改内容。NCBI的工作效率是很高的，一般不超过48小时，就可以得到确认，并拿到登录号。

Reference
---------

1. `NCBI上传数据文档 <http://www.ncbi.nlm.nih.gov/books/NBK47529/>`__
2. 熊筱晶, NCBI高通量测序数据库SRA介绍, 生命的化学[J], 2010:6, 959-963.
3. http://blog.sciencenet.cn/blog-656335-908140.html
4. https://www.biostars.org/p/139422/
5. https://www.youtube.com/watch?v=NSIkUHKRPpo

--------------

old stuff will be remove soon
=============================

SRA 数据处理
------------

本节基本内容介绍：

1. SRA 数据库简介
2. SRA 数据下载
3. SRA 数据转换
4. 从基因组数据模拟短序列数据

1. SRA 数据库简介
^^^^^^^^^^^^^^^^^

**SRA** 是 **S**\ equence **R**\ ead **A**\ rchive 的首字母缩写。

SRA 与 Trace
最大的区别是将实验数据与元数据分离。元数据现在可以划分为以下几类。

-  Study：study 包含了项目的所有 metadata，并有一个 NCBI 和 EBI
   共同承认的项目编号（universal project id），一个 study
   可以包含多个实验（experiment）。
-  Experiment：一个实验记载实验设计（Design），实验平台（Platform）和结果处理
   （processing）三部分信息，并同时包含多个结果集（run）。
-  Run：一个结果集包括一批测序数据。
-  Submission：一个 study 的数据，可以分多次递交至 SRA
   数据库。比如在一个项目启动前期，就可以把 study，experiment
   的数据递交上去，随着项目的进展，逐批递交 run 数据。study
   等同于项目，submission 等同于批 次的概念。

2. SRA 数据下载
^^^^^^^^^^^^^^^

对于单个SRA数据，带图形界面的电脑可以通过浏览器下载。对于只有命令行的服务器端的操作，终端环境下无法使用GUI软件，所以要通过命令工具来下载SRA数据。

**1. 用 edirect 下载数据**

edirect 是 NCBI 最近发布的 entrez 数据操作命令行工具。过去往往要通过
biopython 之类的第三方脚本工具来实现查找，索引以及抓取 entrez
的数据。现在可以用 edirect 来很方便的实现。

::

    ~/tmp$ wget ftp://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/edirect.tar.gz
    ~/tmp$ tar zxvf edirect.tar.gz -C ~/app
    ~/tmp$ sudo ln -s ~/app/edirect/*

**2. 用 sra toolkit 下载数据**

选择美国 FDA 提交的 SRR955386 数据。该数据是在Illumina
Miseq平台上PE250的数据。生物样本是一株分离自奶酪的单增李斯特菌
CFSAN006122。如果你已经安装好 NCBI 的 sra\_toolkit
工具，可以直接用里面的 prefetch 下载。

::

    ~/data$ prefetch -v SRR955386
    ~/data$ mv ~/.ncbi/public/sra/SRR955386.sra .

**Notes:** *2.3.x版本的 sra\_toolkit
会有些配置问题，建议使用最新版。不过2.4.x版本的程序调用ascp时，比如
prefetch 调用 ascp 时选择的 ssh 密钥是老版 ``asperaweb_id_dsa.putty``,
而目前新版的ascp在linux里是使用 ``asperaweb_id_dsa.openssh``\ 。*

**3. 用aspera connect下载**

用 aspera connect 工具下载 NCBI 的数据速度非常快，而且不光可以下载 SRA
数据库里的数据，还可以下载 NCBI FTP 里的其他资源。

::

    ~/data$ ascp -i ~/.aspera/connect/etc/asperaweb_id_dsa.openssh \
    > --user=anonftp --host=ftp.ncbi.nlm.nih.gov --mode=recv -l100m -T -k 1 \
    > /sra/sra-instant/reads/ByRun/sra/ERR/ERR175/ERR175655/ERR175655.sra .

**4. 用 ascp 批量下载 sra 数据**

从 NCBI SRA
数据库检索到需要的序列，比如搜索关键词\ ``Listeria monocytogenes miseq``\ ，左侧filters定义为DNA和Genome。

用 python 脚本批量转换路径。

.. code:: python

    # filename: format_path.y
    with open('acc_list.txt', 'r') as f:
        data = f.read().split('\n')

    list=[]

    for i in data:
        path = '/sra/sra-instant/reads/ByRun/sra/%s/%s/%s/%s.sra\n' % (i[0:3], i[0:6], i, i)
        list.append(path)

    with open('acc_list_full.txt', 'w') as f:
       d = f.writelines(list)

下载数据

::

    ~/data$ touch acc_list_full.txt
    ~/data$ python format_path.py
    ~/data$ mkdir -p sra
    ~/data$ ascp -i ~/.aspera/connect/etc/asperaweb_id_dsa.openssh --user=anonftp --host=ftp-private.ncbi.nlm.nih.gov --mode=recv --file-list acc_list_full.txt sra/

3. SRA 数据转换
^^^^^^^^^^^^^^^

1. 安装 sra toolkit (for ubuntu x64 version)

   ::

       ~/tmp$ curl -O http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.4.3/sratoolkit.2.4.3-ubuntu64.tar.gz
       ~/tmp$ tar zxvf sratoolkit.2.4.3-ubuntu64.tar.gz -C ~/app
       ~/tmp$ cd ~/app/sratoolkit.2.4.3-ubuntu64
       ~/tmp$ sudo ln -s `pwd`/bin/* /usr/local/sbin/

2. sra数据转成fastq格式

SRR955386 这个数据的样本还用 Pacbio SMRT 平台进行了测序，Pacbio
单分子测序技术获得基因组完成图。用该完成图作为模板，考量一下不同拼接软件的拼接结果。

将 CSFAN006122 的基因组完成图数据下载。

::

    ~/data$ prefetch -v SRR955386
    ~/data$ mv ~/.ncbi/public/sra/SRR955386.sra .
    ~/data$ fastq-dump --split-files SRR955386.sra

完成后可以看到 ``data`` 目录下新增了2个文件 ``SRR955386_1.fastq`` 和
``SRR955386_2.fastq``

4. 从基因组数据模拟短序列数据
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

前面介绍如何从 NCBI SRA 数据库下载 NGS 数据并转换成 fastq
格式的文件。可能有些人做的数据分析或验证需要从基因组逆向模拟成短序列格式数据，这种需求也有人开发了相的软件。

`wgsim <https://github.com/lh3/wgsim>`__
就是这样一个软件，它是由开发了BWA等软件大牛 Li heng
写的基因组转成短序列的软件。

**安装wgsim**

::

    ~/app$ git clone https://github.com/lh3/wgsim.git && cd wgsim
    ~/app$ gcc -g -O2 -Wall -o wgsim wgsim.c -lz -lm
    ~/app$ sudo ln -s `pwd`/wgsim /usr/local/sbin
    ~/app$ wsgim -h

    Program: wgsim (short read simulator)
    Version: 0.3.1-r13
    Contact: Heng Li <lh3@sanger.ac.uk>

    Usage:   wgsim [options] <in.ref.fa> <out.read1.fq> <out.read2.fq>

    Options: -e FLOAT      base error rate [0.020]
             -d INT        outer distance between the two ends [500]
             -s INT        standard deviation [50]
             -N INT        number of read pairs [1000000]
             -1 INT        length of the first read [70]
             -2 INT        length of the second read [70]
             -r FLOAT      rate of mutations [0.0010]
             -R FLOAT      fraction of indels [0.15]
             -X FLOAT      probability an indel is extended [0.30]
             -S INT        seed for random generator [-1]
             -A FLOAT      disgard if the fraction of ambiguous bases higher than FLOAT [0.05]
             -h            haplotype mode

**模拟基因组短序列数据**

使用所有参数为默认值，将大肠杆菌基因组数据转换为PE250 fastq 格式数据。

::

    ~/data$ wget https://raw.github.com/ecerami/samtools_primer/master/tutorial/genomes/NC_008253.fna
    ~/data$ wgsim -S11 -1250 -2250 NC_008253.fna reads_1.fastq reads_2.fastq
    ~/data$ head -8 reads_1.fastq

    @gi|110640213|ref|NC_008253.1|_3151106_3151623_4:0:0_5:1:0_0/1
    AACATAAGTGGTATTAATTCCCCAAGATTCAAGATTACGAATAGTATTATCCGCAAAAATATCATCACCTACTTTCGTCAGCATCAGGACTTTTGAATTCAATTTAGCCGCCGCCACCGCTTGATTAGCACCTTTGCCACCACATCCGATTTTGAAGGCAGGTGCTTCCAGAGTTTCTCCTTCTTTAGGCATCTGATAAGTGTAAGTAATGAGATCCACCATATTGGAACCAATAAGTGCAATGTCCATT
    +
    2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
    @gi|110640213|ref|NC_008253.1|_2429297_2429873_8:0:0_7:0:0_1/1
    ACGGTATCACCATGATTGCCCGTTCCGTCAACAGCATGGGGCTGGTCATTATAGGCGGTGGATCGCTTGAAGAAGCGTTAACTGAACTGGAAACCGGACGCGGCGACGCGGTGGTGGTGCTGGAAAACGAACTGCATCGTCACGCTTGCGCTACCCGCGTGAATGCTGCGCTGGCTAAAGCGCCGCTGGTGATTGTGGTTGACCATCAACGCACAGCGATTATGGAAAACGCTCATCTGGTACTATCCGC
    +
    2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222

Reference
^^^^^^^^^

1. `SRA数据库帮助 <http://download.bioon.com.cn/view/upload/201401/20235821_1284.pdf>`__
2. `SRA Handbook <http://www.ncbi.nlm.nih.gov/books/NBK47528/>`__
3. 熊筱晶, NCBI高通量测序数据库SRA介绍, 生命的化学[J]: 2010, 06,
   959-962.
