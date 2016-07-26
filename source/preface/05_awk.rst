awk 工具来帮助处理 NGS 数据
===========================

awk_ 工具常用来对文件内容按行进行匹配搜索，一旦某一行中的内容与搜索条件匹配，则对该内容做进一步操作。本质上讲，awk_ 属于数据驱动的程序，因此 awk_ 程序也非常容易编写与阅读。高通量测序技术带来大量的数据，而生物学分析往往直需要其中特定的部分，这时 awk_ 就可以大显身手为测序数据的转换与分析提供帮助。

.. note::
   awk_ 程序内容很简单，主要包括 pattern，action, input_file

   - **pattern**: 表示所要搜索的内容，可以用正则表达式
   - **action**: 则表示搜索匹配后要做的操作
   - **input_file**: 包含所要搜索内容的输入文件

awk_ 可以在 shell 里直接运行：

.. code-block:: bash

   ~$ awk 'pattern { action }' input_file

也可以写成脚本程序来运行。一个 awk_ 程序往往如下所示

.. code-block:: awk

   #!/usr/bin/awk -f
   pattern { action }

awk 可以不需要输入文件；对于pattern和action来说，2者至少要有一个才能运行。如果没有pattern，则默认匹配任何输入，按行输出并执行action。如果没有action，则匹配pattern并按行输出不做额外操作。

.. code-block:: bash

   # 尝试以下语句，在终端打印`hello world`。这里BEGIN是pattern，{ print "hello world" } 是action
   ~$ awk 'BEGIN { print "hello world" }'

   # 模拟cat输出终端输入的字符。这里省略了pattern
   ~$ awk '{ print }'

上面这个例子可以保存成脚本来运行，文件内容如下：

.. code-block:: awk

   #!/usr/bin/env awk -f

   BEGIN { print "hello world" }

运行这个程序：

.. code-block:: bash

    ~$ chmod +x hello_world
    ~$ ./hello_world

--------------------------------------------------------------------------------

1. 了解 awk 的基本用法
----------------------

.. code-block:: bash

   ~$ awk '$1~/gene1/ { print $2 }' input_data

作用与 cat + grep + sed 类似

.. code-block:: bash

   ~$ cat input_data | grep "gene1" | sed {$1}

2. awk 脚本语法
---------------

2.1 Pattern
^^^^^^^^^^^

2.1.1 正则表达式
~~~~~~~~~~~~~~~~

pattern 可以采用正则表达式来匹配内容。用\ ``/ regular expression /``\ 来表示。

.. note::

   几个特殊的Patterns：

   - BEGIN:
   - END:
   - BEGINFILE:
   - ENDFILE:

2.1.2 语句表达
~~~~~~~~~~~~~~

.. code-block:: bash

   ~$ awk '$1 == "gene" { print $2 }' genes.list

2.2 Action
^^^^^^^^^^

2.2.1 if...else
~~~~~~~~~~~~~~~

.. code-block:: bash

    # if block
    ~$ awk '{if(condition) print $1}' input

    # if else block
    ~$ awk '{if(condition)
    >     print $1
    > else
    >     print $2
    > }' input

2.2.2 while
~~~~~~~~~~~

while 控制语句要换行，用4个空格划分控制块。

.. code-block:: bash

    ~$ awk '{ i = 1
    >     while (i <= 3) {
    >         print $i
    >         i++
    >     }
    > }' input

2.3. 内建变量
^^^^^^^^^^^^^

2.3.1 控制 awk 的变量
~~~~~~~~~~~~~~~~~~~~~

-  BINMODE #
-  CONVFMT
-  FIELDWIDTHS #
-  FPAT #
-  FS
-  IGNORECASE #
-  LINT #
-  OFMT
-  OFS
-  ORS
-  PREC #
-  ROUNDMODE #
-  RS
-  SUBSEP
-  TEXTDOMAIN #

2.3.2 传递信息的变量
~~~~~~~~~~~~~~~~~~~~

-  ARGC , ARGV
-  ARGIND #
-  ENVIRON
-  ERRNO #
-  FILENAME
-  FNR
-  NF
-  FUNCTAB #
-  NR
-  PROCINFO #
-  RLENGTH
-  RSTART
-  RT #
-  SYMTAB #

2.4. 内建函数
^^^^^^^^^^^^^

2.4.1 数学函数
~~~~~~~~~~~~~~

-  atan2(y, x)
-  cos(x)
-  exp(x)
-  int(x)
-  log(x)
-  rand()
-  sin(x)
-  sqrt(x)
-  srand([ x ])

2.4.2 字符串函数
~~~~~~~~~~~~~~~~

-  asort(source [ , dest [ , how ] ] ) #
-  asorti(source [ , dest [ , how ] ] ) #
-  gensub(regexp, replacement, how [ , target ] ) #
-  gsub(regexp, replacement [ , target ] )
-  index(in, find)
-  length( [ string ] )
-  match(string, regexp [ , array ] )
-  patsplit(string, array [ , fieldpat [ , seps ] ] ) #
-  split(string, array [ , fieldsep [ , seps ] ] )
-  sprintf(format, expression1, ...)
-  strtonum(str) #
-  sub(regexp, replacement [ , target ] )
-  substr(string, start [ , length ] )
-  tolower(string)
-  toupper(string)

2.4.3 输入输出函数
~~~~~~~~~~~~~~~~~~

-  close(filename [ , how ] )
-  fflush( [ filename ] )
-  system(command)

2.4.4 时间函数
~~~~~~~~~~~~~~

-  mktime(datespec)
-  strftime( [ format [ , timestamp [ , utc-flag ] ] ] )
-  systime()

2.4.5 Bit操作函数
~~~~~~~~~~~~~~~~~

-  and(v1, v2 [, ...])
-  compl(val)
-  lshift(val, count)
-  or(v1, v2 [, ...])
-  rshift(val, count)
-  xor(v1, v2 [, ...])

2.4.6 其他
~~~~~~~~~~

-  isarray(x)
-  bindtextdomain(directory [ , domain ] )
-  dcgettext(string [ , domain [ , category ] ] )
-  dcngettext(string1, string2, number [ , domain [ , category ] ] )

--------------------------------------------------------------------------------

3. 示例
-------

示例部分介绍 awk 在日常中，特别是处理 ngs 数据时的一些例子。

3.1 对列的操作
^^^^^^^^^^^^^^

**调整列顺序**\ ：在有GUI的操作系统里，一般采用类似 excel, calc
之类的软件导入数据文件，然后剪切各列调整顺序。如果用 awk
来解决也很方便，你只需要考虑好调整的各列顺序即可，action 里的{ print
...}顺序就是重新调整后的各列顺序：

.. code-block:: bash

    ~$ awk '{ print $3, $5, $7, $2, $1, $4, $6 }' infile.txt > outfile.txt

**插入列**\ ：有时候要插入一列数据，用awk可以很方便的实现：

.. code-block:: bash

    ~$ awk '{ print $1, $2 "gene expression", $3}' infile.txt > outfile.txt

3.2 对行的操作
^^^^^^^^^^^^^^

**去除重复的行**：有时候数据里含有重复的行，而当你只需要唯一性数据时，就可以用这行程序，只保留具有唯一性的数据行。

.. code-block:: bash

    ~$ awk '!x[$0]++' infile.txt > outfile.txt

3.3 格式化输出
^^^^^^^^^^^^^^

.. code-block:: bash

    ~$ awk -F":" 'BEGIN { printf "%-8s %-3s", "User", "UID" } \
    > NR==1,NR==20 { printf "%-8s %-3d", $1, $3 }' /etc/passwd

3.4 合并文件
^^^^^^^^^^^^

--------------------------------------------------------------------------------

4. Bioawk
---------

bioawk_ 是 Heng Li 开发的 awk_ 扩展工具，增加了对压缩的 BED, GFF, SAM, VCF, FASTA/Q 等文件格式的支持，并内建一些函数，适用于NGS数据的快速输入输出。

内建以下常用的测序数据函数：

.. code::

   -  gc($seq): 返回序列 $seq 的 GC 含量
   -  meanqual($seq) 返回 fastq 格式的序列 $seq 的平均Q值
   -  reverse($seq) 返回序列 $seq 的反意链
   -  revcomp($seq) 返回序列 $seq 的反意互补链
   -  qualcount($qual, threshold) Returns the number of quality values above the threshold parameter.
   -  trimq(qual, beg, end, param) Trims the quality string qual in the Sanger scale using Richard Motts algorithm (used in Phred). The 0-based beginning and ending positions are written back to beg and end, respectively. The last argument param is the single parameter used in the algorithm, which is optional and defaults 0.05.
   -  and(x, y) bit AND operation (& in C)
   -  or(x, y) bit OR operation (\| in C)
   -  xor(x, y) bit XOR operation (^ in C)

4.1 安装 bioawk
^^^^^^^^^^^^^^^

bioawk_ 的源代码托管在 github_ 上，如先用 git clone 命令先将代码下载到本地，然后编译生成 bioawk_ 将其添加到系统路径。

.. code-block:: bash

    ~$ sudo apt-get install bison
    ~$ git clone https://github.com/lh3/bioawk
    ~$ cd bioawk && make
    ~$ sudo cp bioawk /usr/local/sbin

4.2 使用 bioawk
^^^^^^^^^^^^^^^

文件格式：

* bed:
  * chrom
  * start
  - end
  - name
  - score
  - strand
  - thickstart
  - thickend
  - rgb
  - blockcount
  - blocksizes
  - blockstarts
- sam:
  - qname
  - flag
  - rname
  - pos
  - mapq
  - cigar
  - rnext
  - pnext
  - tlen
  - seq
  - qual
- vcf:




4.3 bioawk 应用示例
^^^^^^^^^^^^^^^^^^

构建测序数据分析 pipeline 时，当 fastq_ 数据在做完 trimming 后，我们往往要关注剩下多少 reads，可以用 bioawk_ 进行快速统计。

.. code-block:: bash

    # 快速统计fastq里的reads数量
    ~$ bioawk -c fastx 'END { print NR }' my_fastq.tar.gz

在一些特殊场合里，需要分析 reads 系列，用 bioawk_ 可以很方便快速来完成。比如统计特殊碱基开头的 reads 数。

.. code-block:: bash

    # 统计以GATTAC开头的reads的数量
    ~$ bioawk -c fastx '$seq~/^GATTAC/ {++n} END { print n }' my_fastq.tar.gz

如果想看GC含量大于60%的reads的质量情况，可以用下面方法：

.. code-block:: bash

    ~$ bioawk -c fastx '{if (gc($seq)>0.6) printf "%s\n%s\n\n", $seq, $qual}' my_fastq.tar.gz

生成reads的平均Q值

.. code-block:: bash

    ~$  bioawk -c fastx '{print $name, meanqual($seq)}' my_fastq.tar.gz > meanqual.txt

Reference
---------


.. _awk: https://www.gnu.org/software/gawk/manual/gawk.html
.. _bioawk: https://github.com/lh3/bioawk
.. _github: https://github.com
.. _fastq: https://en.wikipedia.org/wiki/FASTQ_format
