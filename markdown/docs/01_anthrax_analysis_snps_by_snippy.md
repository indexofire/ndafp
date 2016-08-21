## 炭疽芽胞杆菌基因组 SNPs 分析

G20备战期间，单位要加强生物恐怖事件的防控。最著名的细菌性生物恐怖战剂就是含有炭疽芽胞杆菌的白色粉末。由于日常工作中我们无法接触到这些病原，因此在经验和技能方面都只能处于理论状态（真有实战也是由军方出面）。但是对于能力建设，为了应对万一发生的可疑事件，在基因组数据分析的技术方面我们还是要首先做好储备。构建相应的数据库，在获得菌株后可以第一时间就掌握到基因组溯源方面的资料。

因此在工作的基础上形成了该文档。主要目的也是为了举一反三，在应用生物信息学对其他细菌性病原微生物溯源分析提供参考。

软件中使用的一些参数是根据我们自己的服务器设置的，你需要根据自己的计算机进行相应的调整。我们服务器的配置如下：

* CPU: E3 2650 x2
* Memory: ECC 16G x8
* Harddisk: 7200转 1T x4 组 Raid 5 + 1 Hotspare
* System: Ubuntu 16.04 LTS 64bit

### 1. 获取公共数据库数据

手中没有炭疽芽胞杆菌的资源，自己没有办法做测序的前提下，我们只能通过下载 NCBI SRA 数据库中他人提交的基因组测序数据来作分析。

首先检索 NCBI SRA 数据库中所有使用 illumina 平台对炭疽芽胞杆菌基因组进行 PE 测序的 大于 100M 的 NGS 数据，并在下载这些 sra 数据后转换成 fastq.gz 格式。使用的工具主要为 `edirect` 和 `sra-tools`。

```bash
$ esearch -db sra -query '"Bacillus anthracis"[Organism] AND \
> (Hiseq[ALL] OR Miseq[ALL]) AND "strategy wgs"[Properties]' | \
> efetch -db sra -format runinfo | grep 'PAIRED' | grep '^[DSE]RR*' | \
> awk -F',' '{if($5>100000000) print $1}' | sort -n | \
> xargs fastq-dump --split-files --gzip --outdir bacillus_anthracis
```

### 2. 数据的前期处理

由于是公共数据库下载的数据，并不能保证测序实验质量或者数据提交者是否提交的是质控后的数据。因此建议要对数据做一些前期的质控处理。

#### 2.1 数据 QC

首先对基因组 GC 含量和 Q 值进行初步筛选，对于偏差较大的数据考虑直接剔除（或者用其他软件验证看是否是错误物种）。这里使用的工具为 `bioawk` 或 `parallel`。

```bash
# 因为 reads 覆盖度可能并不均一，高覆盖度的区域 GC 含量比重会略高。但是大部分情况下，正常测序的基因组这种区域相对来说不多，平均到基因组后会整体 GC 含量影响不大。
$ for i in *.fastq.gz; do bioawk -c fastx 'BEGIN{n=0;q=0}{n+=gc($seq);q+=meanqual($seq)}END{print $name,n/NR,q/NR}' $i >> result.txt; done
# awk 类工具是单进程的，为了加速可以使用 parallel 来并行计算
$ parallel "bioawk -c fastx 'BEGIN{n=0;q=0}{n+=gc(\$seq);q+=meanqual(\$seq)}END{print \$name,n/NR,q/NR}' >> result.txt" ::: *.fastq.gz
# 绘制 gc 分布图，如果 gc 含量偏差超过 n% 时就剔除该基因组数据。
$
```

#### 2.2 去除接头

其次要看一下接头污染的情况。因为分析流程中不仅包括 mapping 的方式，还包含 de novo assembly，为了避免接头序列对基因组拼接的影响，这里最好进行。这里使用的工具是 `FastQC` 和 `fadapa`

```bash
# 使用脚本 scan_adaptors.py 来扫描下载的高通量基因组测序数据是否有接头污染的情况。
$ fastqc -t 40 -d qc -q --extract *.fastq.gz
```

### 3. 用 Snippy 获得 snps

```bash
$ for i in *.fastq.gz | sort | uniq; \
> do snippy --cpus 20 --outdir $i -ref reference.fa \
> --R1 $i*_1*.fastq.gz --R2 $i*_2*.fastq.gz; done
$ snippy-core --prefix core-snps SRR* DRR* ERR*
```

### 4. 用 RAxML 绘制进化树

```bash
$ raxmlHPC -f a -x 12345 -p 12345 -# 100 -m GTRGAMMA -s alignment.phy -n .ex -T 40
```

### 相关软件安装

**edirect**

```bash
$ wget ftp://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/edirect.tar.gz
$ sudo tar zxf edirect.tar.gz -C /opt
$ sudo chown -R root:root /opt/edirect
$ cd /opt/edirect && sudo ./setup.sh
$ sudo ln -s /opt/edirect/* /usr/local/sbin/
```

**sra-tools**

```bash
$ wget http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.7.0/sratoolkit.2.7.0-ubuntu64.tar.gz
$ sudo tar zxf sratoolkit.2.7.0-ubuntu64.tar.gz -C /opt/sratoolkit
$ sudo chown -R root:root /opt/sratoolkit && cd /opt/sratoolkit
$ sudo ln -s `pwd`/bin/* /usr/local/sbin/
```

**bio-awk**

```bash
$ sudo apt-get install bison
$ git clone https://github.com/lh3/bioawk
$ cd bioawk && make
$ sudo cp bioawk /usr/local/sbin
```

**parallel**

```bash
$ sudo apt install parallel
```

**gplot**

```bash
$ sudo apt install gnuplot
$ git clone https://github.com/RhysU/gplot
$ sudo cp gplot/gplot /usr/local/sbin
```

**FastQC**

```bash
$ wget http://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.5.zip
$ sudo unzip fastqc_v0.11.5.zip
$ sudo mv fastqc_v0.11.5 /opt/fastqc && sudo chown -R root:root /opt/fastqc
$ sudo cp /opt/fastqc/fastqc /usr/local/sbin
```

**Fadapa**

```bash
$ sudo pip install fadapa
```

**snippy**

```bash
$ git clone https://github.com/tseemann/snippy
$ sudo cp snippy/bin/* /usr/local/sbin
$ sudo cp snippy/binaries/linux/* /usr/local/sbin
```

**RAxML**

```bash
$ wget https://github.com/stamatak/standard-RAxML/archive/v8.1.17.tar.gz
$ sudo tar zxf v8.1.17.tar.gz -C /opt/raxml
$ sudo chown -R root:root /opt/raxml && cd /opt/raxml
$ sudo make -f Makefile.gcc
$ sudo cp raxmlHPC /usr/local/sbin
```

### Reference

1. edirect help book: http://www.ncbi.nlm.nih.gov/books/NBK179288/
2. sra-tools wiki: https://github.com/ncbi/sra-tools/wiki
3. parallel tutorial: https://www.biostars.org/p/63816/
4. gnuplot tutorial: http://lzz5235.github.io/2016/01/12/gnuplot.html
5. gplot usage: https://github.com/RhysU/gplot/blob/master/README.md
