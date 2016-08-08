第3节. 基因组进化分析
=====================

Phylogenomics
-------------

病原的溯源，进化以及种群结构是公共卫生研究领域一个非常重要内容。过去基于一代测序的方法，对一个基因（如毒力基因序列）或几个基因（如MLST序列）构建进化树，数据量的不足带来的精度问题，容易造成结果与实际产生偏差。而随着NGS的发展，产生了一门新的学科 **Phylogenomics** 基因组种系学。通过全基因组的数据来构建绘制系统发生树。

phylogenetics analysis
^^^^^^^^^^^^^^^^^^^^^^

在讨论 phylogenomics 之前，我们先对过去 phylogenetics 做一个复习。进化树绘制相信做微生物的工作者平时都在频繁使用，特别是像CDC等做分子流行病学或者一些做微生物系统发育的研究团队。只是目前将进化分析的核酸数据扩展到基因组水平上，绘制树的原理和方法是一致的，只是在之前的多重序列比对方面有一些不同。

phylogenetics 方法
~~~~~~~~~~~~~~~~~~

1. MP
2. NJ
3. ML
4. Bayes

Whole Genome Alignment
~~~~~~~~~~~~~~~~~~~~~~

WGA(Whole Genome Alignment)是对2个以上基因组在核苷酸水平上的进化关系预测方法。对于基因组多重序列比对，几个概念搞清楚后才能更好的理解。

* Homologs:
* Orthologs: 来源与共同祖先的基因簇，由于物种差异产生的分化，基因一般具有相似功能。
* Paralogs: 一般是不同功能。
* Xenologs: 2个物种间水平转移的基因，功能可以相似叶可以不同。一般来说是功能相似的。

WGA的主要方式
~~~~~~~~~~~~~

为了解决 Blast 存在的各种问题，出现了许多针对 WGA 的应用。 目前根据计算策略主要分成2类方式，但这2类方式有各自的优缺点。

1. hierarchical: 速度快，容易遗漏小的重配或分化序列片段。如著名的 progressiveMauve, MUGSY 等
2. local: 精度高。如 MUMmer, MULTIZ/TBA 等。

WGA 应用列表

| Method | Category | Relationships predicted | Pairwise or Multiple | References |
| ------ | -------- | ----------------------- | -------------------- | ---------- |
| BLAST | Local alignment | Homology | Pairwise | (21) |
| LASTZ | Local genomic alignment | Homology | Pairwise | (28) |
| MUMmer | Local genomic alignment | Orthology | Pairwise | (29) |
| CHAOS | Local genomic alignment | Homology | Pairwise | (30) |
| GRIMM-synteny | Orthology mapping | Toporthology | Multiple | (33) |
| DRIMM-synteny | Orthology mapping | Orthology, paralogy | Multiple | (34) |
| Mercator | Orthology mapping | Toporthology | Multiple | (35) |
| Enredo | Orthology mapping | Orthology, paralogy | Multiple | (36) |
| OSfinder | Orthology mapping | Orthology | Multiple | (37) |
| SuperMap | Orthology mapping | Orthology, paralogy | Multiple | (38) |
| progressiveMauve | Hierarchical WGA | Toporthology | Multiple | (39) |
| MUGSY | Hierarchical WGA | Toporthology | Multiple | (40) |
| MAVID | Global genomic alignment | Colinear homology | Multiple | (43) |
| LAGAN/MultiLAGAN | Global genomic alignment | Colinear homology | Pairwise/multiple | (31) |
| DIALIGN | Global genomic alignment | Colinear homology | Multiple | (30) |
| SeqAn::T-Coffee | Global genomic alignment | Colinear homology | Multiple | (44) |
| FSA | Global genomic alignment | Colinear homology | Multiple | (45) |
| Pecan | Global genomic alignment | Colinear homology | Multiple | (36) |
| NUCmer/PROmer | Local WGA | Orthology | Pairwise | (29) |
| MULTIZ/TBA | Local WGA | Orthology, paralogy | Multiple | (8) |
| AXTCHAIN/CHAINNET | Alignment chaining and filtering | Orthology | Pairwise | (50) |

phylogenomics analysis
----------------------

对于微生物而言，特别是细菌因为存在大量的重组，水平转移等。不能直接将基因组数据像同源基因数据一样直接比对。所以一般来说需要先将数据做一些筛选。具体的方法主要有；

方法1 基于距离
^^^^^^^^^^^^^^^^

计算全基因矩阵距离，通过距离来构建系统发生树。

方法2 基于核心基因(core genes)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

通过将同种细菌基因组同源基因（core genes）的异同构建进化树。这种方法的流程一般是将测序数据拼接成contigs/，对拼接结果进行注释，鉴定所有菌株基因组数据的orthologous基因，对这些基因经行多重序列比对，再根据比对结果构建进化树。

方法3 基于参考基因组
^^^^^^^^^^^^^^^^^^^^^^

通过将测序获得的短片段mapping到参考基因组上，找到核心基因组上的variants位点，连锁这些位点进行多重比对，再构建系统发生树。这也是目前最常用的构建微生物基因组SNP进化树的方法流程。

方法2. 应用工具
^^^^^^^^^^^^^^^

**1. orthMCL**

方法3. 应用工具
^^^^^^^^^^^^^^^

**1. Wombac**

[wombac][] 是由 [Victorian Bioinformatics Consortium](http://www.vicbioinformatics.com/) 开发的用于获取细菌基因组 SNP 的工具集。[wombac][] 使用 perl 开发，本质上是一个 perl pipeline，使用的工具是 bwa, samtools 和 freebayes，这3个工具 Linux 版 [wombac][] 已经自动提供了，要正常运行的话系统中还必须安装vcfutils.pl, bgzip, tabix 这几个依赖包。

[wombac][] 会寻找碱基替换，但不会搜索 indels，精确度上来说可能会有一些 SNP 的丢失，但其精度已足够用来进行大部分基因组的快速分析。

**1.1 安装并运行**

.. code-block:: bash

   $ wget http://www.vicbioinformatics.com/wombac-1.3.tar.gz
   $ tar zxvf wombac-1.3.tar.gz -C ~/app
   $ cd ~/app/wombac-1.3/bin
   $ perl wombac --outdir ~/data/wombac --ref ~/data/egd.fasta --run /data/draft

**1.2 绘制SNP进化树树**

[wombac][] 对每个基因组产生BAM，VCF文件，同时产生一个整体多重比对的ALN文件用于绘制进化树。

.. code-block:: bash

   $ SplitsTree -i Tree/snps.aln


**2. kSNP**

**3. REALPHY**

**3.1 下载并安装**

RealPhy 需要 java 支持，所以系统要至少安装有 jre 环境。可以输入`java -version`查看，如果提示没有安装java，可以先安装 openjdk：`sudo apt-get install open-jre-1.7-headless`

.. code-block:: bash

   $ wget http://realphy.unibas.ch/downloads/REALPHY_v110_exec.zip
   $ unzip REALPHY_v110_exec.zip -d ~/apps/realphy

**3.2 脚本所依赖工具**

Realphy需要以下工具，这些工具的安装已经在前文中实现过了。

1. samtools
2. bowtie2
3. TREE-PUZZLE
4. RAxML
5. PhyML
6. Phylip

**3.3 运行程序并分析**

.. code-block:: bash

   $ java -XmM800

**4. core-phylogenomics**

.. code-block:: bash

   $ snp_phylogenomics_control --mode mapping --input-dir my_fastq_folder/ --output pipeline_out --reference my_reference.fasta

SeqSphere

One Disrupting Technology Fits it All -Towards Standardized Bacterial Whole Genome Sequencing for Global Surveillance. Dag Harmsen, University of Münster, German.


## Reference

1. https://github.com/apetkau/microbial-informatics-2014/
2. Single Nucleotide Polymorphisms Methods and Protocols 2nd. Anton A. Komar, Springer protocols.
3. Methods in Molecular Biology, Chapter8 Whole Genome Alignment, Colin N. Dewey, Springer.


[wombac]: http://www.vicbioinformatics.com/software.wombac.shtml "wombac"
[CSI Phylogeny]: http://cge.cbs.dtu.dk/services/CSIPhylogeny/ "CSI Phylogeny"
[GenoBox]: https://github.com/srcbs/GenoBox "GenoBox"
[REALPHY]: http://realphy.unibas.ch/fcgi/realphy "REALPHY"
[kSNP]: http://sourceforge.net/projects/ksnp/ "kSNP v2"
