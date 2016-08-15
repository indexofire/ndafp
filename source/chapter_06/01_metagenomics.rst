第1节. Metagenomics 概述
========================

.. note::
    Metagenomics 实验操作和数据分析主要包括2个方面：

    1. **shotgun metagenomics**
    2. **16s rRNA metagenomics**

1. shotgun Metagenomics
-----------------------

我们在第1-3节介绍如何用软件处理 shotgun metagenomics 测序数据。

Metegenomics de novo assembly 中的几个难题：

* 重复序列
* 低覆盖度
* 测序错误

重复序列
^^^^^^^^

重复序列是

低覆盖度
^^^^^^^^

测序错误
^^^^^^^^

2. 16s rRNA Metagenomics
------------------------

16s rRNA 数据有偏向性：

- Degenerate primers Degenerate primers
- PCR Amplification
- Databases
- Does not capture viruses and eukaryotes

主要用于菌群分析。

用途：需要深度测序的数据，样本一般分为：宿主来源，如人或动物等；环境来源，如土壤或水体等。数据分析时，前者一定要考去除宿主缘DNA，后者要高度深度测序对后期拼接有较大帮助。

**Methods Protocol**:

- DNA isolation
- Library preparation
- Sequencing
- Data QC: FastQC, FastX_toolkit
- Reads assembly: IDBA-UD, Mira, Velvet/MetaVelvet, Spades
- Partipation: FCP，Phymm/PhymmBL, AMPHORA2, NBC, MEGAN, MG-RAST, CAMERA, IMG/M
- Analysis: MetaPhAln, PhyloSift/pplacer

3. Reference
------------

1. http://www.slideshare.net/c.titus.brown/2015-beaconmetagenometutorial
