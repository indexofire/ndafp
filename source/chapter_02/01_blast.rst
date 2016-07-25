第1节. 构建 Local Blast 应用
============================

blast_ 工具用来进行序列相似性比对。常见的使用是通过访问 http://blast.ncbi.nlm.nih.gov/Blast.cgi，使用基于 Web 及面的 blast_ 工具，调用 NCBI 相应的序列数据库来进行比对。此外在 NCBI 很多工具集里

Local Blast 使用说明
--------------------

.. note::
    blast_ 工具可以进行序列相似性比对。在 NGS 数据分析中经常会被使用到，特别是一些工具中需要使用 blast 来作序列比对。拿到测序完成的草图后，因为基因组数据较大，连接NCBI网站往往又非常缓慢，所以要做 Blast 比对的话都需要做 Local Blast。这里介绍2个方式来实现：

1. 用命令行进行 Blast
2. 快速构建 Blast Web 服务

1. 基于命令行的 Local Blast
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**blast** 和 **ncbi_blast+** 这2个程序集容易搞混。NCBI 最早在1989年创建 Basic Local Alignment Search Tool 工具，沿用至2009年无论是命令行工具或是在线程序，都称呼其为blast。2009年 NCBI 鉴于 ``blast`` 的一些不足，重新开发了新的 ncbi_blast+ 命令行工具，新的 ncbi_blast+ 工具在速度上有了提升，在输入输出上也更为灵活。

目前 Blast 工具最新版是2012年发布的\ **2.2.26**\ （已经暂停版本更新并不做进一步支持），而 ncbi_blast+ 目前一直在更新。要区分2者也很简单，blast 是通过 blastall -p 的方式调用子程序来比对搜索的，而 blast+ 则是直接使用 blastn 或 blastp 等子程序来比对搜索。另外前者用 formatdb 程序来格式化数据库，后者用 makeblastdb 程序来格式化数据。

1.1 Blast
^^^^^^^^^

**Blast的下载与安装**

.. code-block:: bash

   # 安装 Ubuntu 编译包。
   ~$ sudo apt-get install blast2

   # 或者直接下载NCBI Linux预编译包，并解压缩安装
   ~$ wget ftp://ftp.ncbi.nih.gov/blast/executables/legacy/2.2.26/blast-2.2.26-x64-linux.tar.gz
   ~$ tar zxvf blast-2.2.26-x64 -C ~/app
   ~$ sudo ln -s ~/app/blast-2.2.26-x64/blastall /usr/local/sbin

**运行 Blast**

Blast 通过调用 blastall 这个程序来调用不同算法和程序实现序列比对。在命令行中输入 blastall ，会打印出一份参数列表。你也可以使用 ``man blast`` 来查看 Blast 工具的用户手册。

.. code-block:: bash

   ~$ blastall

**参数说明：**

.. code-block:: bash

    -p: 指定要运行的 blast 程序。可以调用的有:
        blastp             将氨基酸序列与蛋白质数据库比对
        blastn             将核酸序列与核酸数据库比对
        blastx             将核酸序列翻译成蛋白序列后与非冗余(nr)蛋白质数据库比对
        psitblastn
        tblastn
        tblastx
    -d: 指定要调用数据库，默认值是非冗余(nr)数据库。本地 Blast 比对一般来说都是调用 formatdb 格式化的数据库。
    -i: 输入，默认值是终端输入，也可以使用文件的方式，比如 -i seq.fasta
    -o: 输出，默认值是终端打印输出，也可以使用文件的方式，比如 -o result.txt
    -e: 期望值。
    -T: 输出文件格式，默认值为F(False)，想输出HTML格式的可以用 -T T
    -M: 矩阵算法选择，默认值是 BLOSUM62
    -n: 如果想使用MegaBlast，就设置 -n T
    -b: 数据库中的比对结果显示条目数，默认是250条记录。
    -m: 比对结果的输出显示方式，值为0~11，默认是0。各个数字含义见下表。

+-----------+-----------------------------------------------------+
| 数值      | 代表含义                                            |
+===========+=====================================================+
| 0         | pairwise                                            |
+-----------+-----------------------------------------------------+
| 1         | query-anchored showing identities                   |
+-----------+-----------------------------------------------------+
| 2         | query-anchored no identities                        |
+-----------+-----------------------------------------------------+
| 3         | flat query-anchored, show identities                |
+-----------+-----------------------------------------------------+
| 4         | flat query-anchored, no identities                  |
+-----------+-----------------------------------------------------+
| 5         | query-anchored no identities and blunt ends         |
+-----------+-----------------------------------------------------+
| 6         | flat query-anchored, no identities and blunt ends   |
+-----------+-----------------------------------------------------+
| 7         | XML Blast output                                    |
+-----------+-----------------------------------------------------+
| 8         | tabular                                             |
+-----------+-----------------------------------------------------+
| 9         | tabular with comment lines                          |
+-----------+-----------------------------------------------------+
| 10        | ASN, text                                           |
+-----------+-----------------------------------------------------+
| 11        | ASN, binary [Integer]                               |
+-----------+-----------------------------------------------------+

其他参数参见\ ``man blast``\ 。

**应用举例:**

Local blast例子：获得一条大肠杆菌序列 myseq.fasta，要和 EDL933 进行比对。首先下载 EDL933 的基因组数据，并格式化作为本地数据库，然后使用 blastn 对序列进行比对。

.. code-block:: bash

   # 使用 edirect 工具的 efetch 下载 EDL933 基因组数据
   ~$ efetch db=nuccore -format=fasta -id=AE005174 > AE005174.fasta
   # 使用 blast 的 formatdb 工具将 EDL933 基因组数据格式化成用于比对的数据库格式
   ~$ formatdb -i AE005174.2.fasta -o T -p F
   # 调用 blastn 的方式比对 myseq.fasta 和 EDL933 序列
   ~$ blastall -i myseq.fasta -d AE005174.2.fasta -p blastn

1.2 NCBI_blast+
^^^^^^^^^^^^^^^

目前 NCBI_blast+ 最新版为 v2.4.0。

**下载安装 NCBI Blast+**

.. code-block:: bash

   # 安装 Ubuntu 编译包
   ~$ sudo apt-get install ncbi-blast+

   # 直接在 NCBI 官方 FTP 站点下载预编译包解压缩安装
   ~/tmp$ wget ftp://ftp.ncbi.nih.gov/blast/executables/blast+/2.4.0/ncbi-blast-2.4.0+-x64-linux.tar.gz
   ~/tmp$ tar zxf ncbi-blast-2.4.0+-x64-linux.tar.gz

**构建数据库**

.. code-block:: bash

   ~$ makeblastdb -in data/database.fasta -dbtype nucl -parse_seqids

**应用举例:**

NGS 测序时为了保证 DNA 质量，往往会对物种进行鉴定，采用 16s rDNA 测序的方法。公司给了一堆拼接的txt文件，里面内容是不同物种样本的 16s rDNA 序列。当样本量很大，比如1000条时，如果一条条去 NCBI 上比对也是浪费精力和时间。可以用 local blast 来批量处理。首先下载各个目的物种的16s rDNA序列，并将其格式化成数据库。

.. code-block:: bash

   # 生成结果报告
   ~$ for i in *.txt; do blastn -db database.fasta -query $i -outfmt 6 >> result; done


http://www.personal.psu.edu/iua1/courses/files/2014/lecture-12.pdf

2. 构建自己的blast web服务
~~~~~~~~~~~~~~~~~~~~~~~~~~

2.1 blastkit
^^^^^^^^^^^^

blastkit 是一个包含webserver等工具的blast工具集。

**安装依赖包**

.. code-block:: bash

   ~$ sudo pip install pygr
   ~$ sudo pip install whoosh
   ~$ sudo pip install git+https://github.com/ctb/pygr-draw.git
   ~$ sudo pip install git+https://github.com/ged-lab/screed.git
   ~$ sudo apt-get -y install lighttpd

**对lighttpd webserver进行配置**

.. code-block:: bash

   ~$ cd /etc/lighttpd/conf-enabled
   ~$ sudo ln -fs ../conf-available/10-cgi.conf ./
   ~$ sudo echo 'cgi.assign = ( ".cgi" => "" )' >> 10-cgi.conf
   ~$ sudo echo 'index-file.names += ( "index.cgi" ) ' >> 10-cgi.conf
   ~$ sudo /etc/init.d/lighttpd restart

**本地安装 Blast**

.. code-block:: bash

   ~$ cd tmp
   ~/tmp$ wget ftp://ftp.ncbi.nih.gov/blast/executables/legacy/2.2.26/blast-2.2.26-x64-linux.tar.gz
   ~/tmp$ tar xzf blast-2.2.26-x64-linux.tar.gz -C ~/app
   ~/tmp$ sudo cp ~/app/blast-2.2.26/bin/* /usr/local/sbin
   ~/tmp$ sudo cp -r ~/app/blast-2.2.26/data /usr/local/blast-data

**安装 blastkit**

.. code-block:: bash

   ~/tmp$ cd ~/app
   ~/app$ git clone https://github.com/ctb/blastkit.git -b ec2
   ~/app$ cd blastkit/www
   ~/app/blastkit/www$ sudo ln -fs $PWD /var/www/blastkit
   ~/app/blastkit/www$ mkdir files
   ~/app/blastkit/www$ chmod a+rxwt files
   ~/app/blastkit/www$ chmod +x /root
   ~/app/blastkit/www$ cd ..
   ~/app/blastkit$ python ./check.py

如果安装顺利，就会提示一切已经准备完毕。接下来要准备数据。

.. code-block:: bash

   ~$ cp /mnt/assembly/ecoli.21/contigs.fa ~/app/blastkit/db/db.fa
   ~$ cd ~/app/blastkit
   ~$ formatdb -i db/db.fa -o T -p F
   ~$ python index-db.py db/db.fa

Reference
---------

-  `Blastkit <https://github.com/ctb/blastkit.git>`__
-  `Caltech workshop <https://github.com/dib-lab/2013-caltech-workshop/blob/master/blastkit.txt>`__



.. _blast: http://blast.ncbi.nlm.nih.gov/Blast.cgi
