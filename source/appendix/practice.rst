数据分析实践
============

.. code-block:: bash

   $ for i in (ls .); do mkdir -p ; done


**观察覆盖度与污染序列的关系**


**用 Blast 的方法来筛选污染序列**

.. code-block:: bash

   # 下载污染物种的基因组数据，进行序列比对，看组装的nodes里那些是来源于污染物种。如果有多个污染物种，则可以将基因组数据合并 `cat 1.fa 2.fa 3.fa > containment.fasta`
   $ makeblastdb -db containment.fasta -parse_seqids -db_type nucl
   $ blastn -db containment.fasta -query scaffolds.fasta -max_hsps 1 -outfmt 6 -out result

   # blast 结果的相似性筛选，小于90认为与污染物种不同。将过滤的片段长度求和，判断过滤的片段是否与物种基因组大小一致。如果接近，那么即使有部分片段遗漏，但是大部分基因组数据已经保留。
   $ awk '{ if ($3 < 90) print $1 }' result > filter_nodes
   $ awk -F'_' 'BEGIN {len=0} {len+=$4} END {print len}' filter_nodes

   # 进一步用目的物种的参考基因组进行blast，以确保没有其他物种污染。
   $ makeblastdb -db reference.fasta -parse_seqids -db_type nucl
   $ blastn -db reference.fasta -query assembly.fasta -max_hsps 1 -outfmt 6

**用 Mapping 目的基因组来筛选 reads 再进行拼接**

**抓取目标nodes**

.. code-block:: python

   # 保存代码到 get_nodes.py 文件中，运行　python get_nodes.py
   from Bio import SeqIO

   input_file = 'scaffolds.fasta'
   filter_file = 'filter_nodes'
   output_file = 'assembly.fasta'

   wanted = set(line.rstrip("\n").split(None,1)[0] for line in open(filter_file))
   print "Found %i unique identifiers in %s" % (len(wanted), filter_file)
   records = (r for r in SeqIO.parse(input_file, "fasta") if r.id in wanted)
   count = SeqIO.write(records, output_file, "fasta")
   print "Saved %i records from %s to %s" % (count, input_file, output_file)
   if count < len(wanted):
       print "Warning %i IDs not found in %s" % (len(wanted)-count, input_file)
