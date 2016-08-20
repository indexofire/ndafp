# 炭疽芽胞杆菌基因组 SNPs 分析

## 1. 获取公共数据库数据

```bash
# 检索使用 illumina 平台对炭疽芽胞杆菌进行测序的 sra 数据。
$ esearch -db sra -query '"Bacillus anthracis"[Organism] AND illumina[All Fields] AND "biomol dna"[Properties] AND "strategy wgs"[Properties]'


```

## 2. 数据的前期处理

## 3. 用 Snippy 获得 snps
