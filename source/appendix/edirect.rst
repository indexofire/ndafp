玩转 edirect
============

`NCBI`_ 的 Entrez 工具集大家很熟悉了，特别是基于 web 的 E-utilis，是日常检索 `NCBI`_ 数据库的最主要应用。而 edirect 是 `NCBI`_ 开发的用于 linux 命令行界面中的快速检索和下载工具。

`NCBI`_ 的 Entrez 工具平时大家都经常使用，既可以从 web 页面访问 `NCBI`_ 来查询，也可以利用 Entrez 提供的 Web Services 来实现诸多功能（如自动查询）。此外 `NCBI`_ 还提供了 Entrez 的命令行工具 edirect。edirect 全称时 EntrezDirect，使用它可以很方便的在服务器上进行 Entrez 的检索和抓取。


1. 下载安装
-----------

.. code-block:: bash

   ~/tmp$ wget ftp://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/edirect.tar.gz
   ~/tmp$ tar zxvf edirect.tar.gz -C ~/app
   ~/tmp$ sh ~/app/edirect/setup.sh

在看到：

> ENTREZ DIRECT HAS BEEN SUCCESSFULLY INSTALLED AND CONFIGURED

字符后，安装完成。可以不运行`setup.sh`直接使用edirect的一些工具，不过如果要使用全部功能，有些perl模块需要安装，所以运行`setup.sh`来完成CPAN的modual安装以及 go 版本的xtract的编译（原来的perl版本速度不够快）。当看到`ENTREZ DIRECT HAS BEEN SUCCESSFULLY INSTALLED AND CONFIGURED`，表明完成安装。

如果是Ubuntu操作系统，由于uname位于/bin，而xtract接口调用脚本使用/usr/bin/uname来判断使用那个版本的xtract，因此要正常使用xtract需要添加一个link。

.. code-block:: bash

  ~$ sudo ln -s /bin/uname /usr/bin/uname

也可以通过 perl 来安装：

.. code-block:: bash

   $ cd ~
   $ perl -MNet::FTP -e \
   > '$ftp = new Net::FTP("ftp.`NCBI`_.nlm.nih.gov", Passive => 1); $ftp->login; \
   > $ftp->binary; $ftp->get("/entrez/entrezdirect/edirect.zip");'
   $ unzip -u -q edirect.zip
   $ rm edirect.zip
   $ export PATH=$PATH:$HOME/edirect
   $ ./edirect/setup.sh

.. note::

    NCBI 从2016年11月起，网站从http迁移到https协议，因此老的版本edirect会无法使用。


2. 工具使用

2.2 数据库列表
^^^^^^^^^^^^^^

**主要工具列表**

| 工具名称 | 用途 |
| -------- | -------- |
| **efetch** | 下载 `NCBI`_ 数据库中的记录和报告并以相应格式打印输出 |
| **einfo** | 获取目标结果在数据库中的信息 |
| **elink** | 对目标结果在其他数据库中比配结果 |
| **epost** | 上传 UIDs 或者 序列登记号 |
| **esearch** | 在 Entrez 中执行搜索命令 |
| **efilter** | 对之前的检索结果进行过滤或限制 |
| **xtract** | converts XML into a table of data values. |
| **nquire** | sends a URL request to a web page or CGI service. |

5. 具体例子

查看2012年至今发表的霍乱弧菌CTX相关文献摘要

.. code-block:: bash

   ~$ esearch -db pubmed -mindate 2012 -maxdate 2016 -datetype PDAT -query "vibrio cholerae[CTX]" | efetch -format abstract > abstract.txt

查看2016年CDC发布的所有用 miseq 测序的沙门菌文库制备方法

.. code-block:: bash

   ~$ esearch -db sra -query "salmonella miseq CDC" -mindate 2016 -maxdate 2016 -datetype PDAT | efetch -format runinfo | cut -d ',' -f 12 > library.txt

绘制单增李斯特菌 hlyA 蛋白质进化树图

.. code-block:: bash

   ~$ esearch -db protein -query "(listeria monocytogenes hlyA) NOT partial" | efetch -db protein -format fasta > hlyA.fasta
   ~$ raxml -p 12345 -x

对10年内发表的 hlyA 相关文献的作者排序

.. code-block:: bash

   ~$ esearch -db pubmed -mindate 2006 -maxdate 2016 -datetype PDAT -query "hlyA"

查看 taxonomy

.. code-block:: bash

   ~$ esearch -db taxonomy -query "lis* OR sal*"

下载所有甲型副伤寒沙门菌基因组序列

.. code-block:: bash

   ~$ esearch -db nuccore -query "Salmonella[porgn:__txid54388] complete genome" | efetch -db nuccore -format fasta > SPA.fasta

Reference:

1. http://www.ncbi.nlm.nih.gov/books/NBK179288
2. https://dataguide.nlm.nih.gov/


.. _NCBI: http://www.ncbi_.nlm.nih.gov
