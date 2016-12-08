Snippy
======

`snippy`_ 是澳大利亚墨尔本大学的 `Torsten Seemann`_ 开发的用于细菌基因组 snps 分析的软件。`Torsten Seemann`_ 是著名的细菌基因组注释软件 `prokka`_ 的作者，而 `snippy`_ 也是被广泛使用的软件之一。`snippy`_ 的前身叫做 `wombac`_，

.. note::
    `wombac`_ 是由 `Victorian Bioinformatics Consortium`_ 开发的用于获取细菌基因组 SNP 分析的工具集。`wombac`_ 使用 perl 开发，本质上是一个 perl pipeline，使用的工具是 bwa, samtools, freebayes, vcfutils.pl, bgzip, tabix 等依赖包。`wombac`_ 会寻找碱基替换，但不会搜索 indels，精确度上来说可能会有一些 snps 的丢失，但其精度已足够用来进行大部分基因组的快速分析。

.. code-block:: bash

   # 数据
   $ tree data/
   S01_R1_L001.fastq.gz
   S01_R2_L001.fastq.gz
   S02_R1_L001.fastq.gz
   S02_R2_L001.fastq.gz
   ...


1. 下载安装
-----------

`snippy`_ 的软件仓库托管在 `Github`_ 上，在 Linux 系统里安装了 git 工具可以将代码仓库克隆到本地运行。

.. code-block:: bash

   # 克隆代码仓库
   $ git clone https://github.com/tseemann/snippy
   # 添加 snippy 以及依赖库的路径到环境变量中，使终端下直接运行 snippy 即可调用程序
   $ echo 'export PATH="$HOME/repos/snippy/bin:$HOME/repos/snippy/binary/linux:$PATH"' >> ~/.bashrc
   $ source ~/.bashrc

2. 使用sinppy
-------------

`snippy`_ 最基本的用法，可以将测序数据比对到参考基因组，获得相对应的 snps：

.. code-block:: bash

   # --cpus 20 表示采用20个进程执行命令
   $ snippy --cpus 20 --outdir S01 -ref reference.fa --R1 S01_R1_L001.fastq.gz --R2 S01_R2_L001.fastq.gz

对于多个样本的分析，寻找共同 snps，可以用 snippy-core 将各个样本的 snps 合并来实现。

.. code-block:: bash

   # 依次将 mapping 到 reference.fa 的比对结果中的 snps 数据
   $ snippy --cpus 20 --outdir S01 -ref reference.fa --R1 S01_R1_L001.fastq.gz --R2 S01_R2_L001.fastq.gz
   $ snippy --cpus 20 --outdir S02 -ref reference.fa --R1 S02_R1_L001.fastq.gz --R2 S02_R2_L001.fastq.gz
   $ snippy --cpus 20 --outdir S03 -ref reference.fa --R1 S03_R1_L001.fastq.gz --R2 S02_R2_L001.fastq.gz
   # 将所有 snps 结果汇总，获得 core snps
   $ snippy-core --prefix core-snps S01 S02 S03

也可以用 shell 的循环命令来调用 `snippy`_ 工具。

.. code-block:: bash

   # 用 shell 脚本循环完成样本 snps 比对工作
   $ for i in $(awk -F'_' '{print $1}' <(ls -D *.fastq.gz) | sort | uniq); \
   > do snippy --cpus 20 --outdir $i -ref reference.fa --R1 $i*R1*.fastq.gz --R2 $i*R2*.fastq.gz; \
   > done
   $ snippy-core --prefix core-snps S*

snippy-core 生成的 core-snps.aln 文件，可以用进化树绘制工具生成进化树。

.. code-block:: bash

   # 生成 clustal 格式的 core.aln 比对文件，这里用 splittree 构建进化树
   $ splittree -i core-snps/core.aln

   # 或者将生成的 .aln 格式比对文件转换成 .phy 格式，然后再用 raxml 构建 ML 树
   $ raxml -f a -x 12345 -# 100  -p 12345 -m GTRGAMMA -s core.phy -n ex -T 40

.. note::
    有很多中方法 可以将 aln 格式的文件转换成 phy 格式的比对文件。比如用 biopython

    >>> from Bio import AlignIO
    >>> AlignIO.convert(core-snps/core.aln, "clustal", core-snps/core.phy, "phylip-relaxed")

3. Reference
------------


.. _snippy: https://github.com/tseemann/snippy
.. _prokka: https://github.com/tseemann/prokka
.. _Torsten Seemann: https://twitter.com/torstenseemann
.. _wombac: https://github.com/tseemann/wombac
.. _Victorian Bioinformatics Consortium: http://www.vicbioinformatics.com/
.. _Github: https://github.com
