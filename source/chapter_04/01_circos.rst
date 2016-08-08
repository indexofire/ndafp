用 circos 来画基因组
====================

circos_ 是一个绘制可视化关系图的软件，就是我们常说的用来做 Data Visulization。它的特点是采用圈图来表示关系，因此也常被用来绘制环状的原核生物染色体或质粒的基因组图谱，或者用来展示比较基因组关系图等。circos_ 生成的圈图非常优美，可以用来表示多种类型的数据。但是由于功能强大，因此牵涉绘图的内容过于复杂，参数设置繁多，采用的术语名称的含义不够直观，导致学习曲线比较陡峭。而且缺乏易用的所见即所得的工具，因此对于新手来说难度非常大。

circos_ 的作为绘制图形的工具，不是一步速成的获得某种图形的方法，而是需要通过自己设计的图形样式来定义各种参数，让程序绘制出图。

1. 安装 circos
--------------

1.1 使用 ubuntu 官方软件源安装
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

可以使用 ubuntu 官方软件源来安装。这样安装最简单，缺点是不是最新版，可能会有一些程序BUG。

.. code-block:: bash

   ~$ sudo apt install circos

1.2 使用官方安装包
^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   # 安装依赖包 gd2-xpm 库
   ~$ sudo apt-get install libgd2-xpm-dev
   # 修改 ubuntu 发行版的 perl 路径
   ~$ sudo ln -s /usr/bin/env /bin/env
   # 安装 perl 模块
   ~$ sudo cpan install Clone \
   > Config::General \
   > Font::TTF \
   > List::MoreUtils \
   > Math::Bezier \
   > Math::VecStat \
   > Math::Round \
   > Params::Validate \
   > Readonly \
   > Regexp::Common \
   > Set::IntSpan \
   > Text::Format \
   > GD \
   > Statistics::Basic

   # 下载安装包，并解压缩
   ~$ wet http://circos.ca/distribution/circos-0.69-3.tgz
   ~$ tar xfz circos-0.69-3.tgz -C ~/apps/circos
   # 将 circos 添加到系统路径中
   ~$ sudo ln -s ~/apps/circos/bin/circos /usr/local/sbin/circos
   # 或者将 circos 添加到用户路径中
   ~$ export PATH=$HOME/apps/circos/bin/

   # 查看是否安装成功
   ~$ circos -v
   # 如果命令行打印出类似以下内容，表示安装成功
   circos | v 0.69-3 | 16 Jun 2016 | Perl 5.018002

--------------------------------------------------------------------------------

2. circos 基本概念
------------------

circos 主要需要2类文件：

* 可视化结果的数据文件
* 用于告诉circos如何展示的配置文件。

2.1 数据文件
^^^^^^^^^^^^

由于circos只是画图工具，因此你图中要展示的数据需要自己预先准备好。比如基因组的GC含量，需要用其他程序先生成以下这种类型的文本格式文件。

.. code-block::

   染色体 开始位置 结束位置 颜色值 其他选项[可选]
   2.chr1  1000    2000  red

2.2 配置文件
^^^^^^^^^^^^

一般绘图需要以下配置文件：

- circos.conf
- ideogram.conf
- ticks.conf
- image.conf
- highlight.conf
- colors_fonts_patterns.conf

你可以将配置文件内容全部放在circos.conf里，也可以分离成单独的文件通过include方式导入。

2.2.1 circos.conf
~~~~~~~~~~~~~~~~~

这是circos主配置文件，其他的配置文件可以通过include的方式来导入。

.. code-block::

   <<include your_other_configure.conf>>

2.2.2 ideogram.conf
~~~~~~~~~~~~~~~~~~~

2.2.3 image.conf
~~~~~~~~~~~~~~~~

2.2.4 highlight.conf
~~~~~~~~~~~~~~~~~~~~

2.2.5 ticks.conf
~~~~~~~~~~~~~~~~

3. 可视化的组成要素
-------------------

\<plots\>\<\/plots>，\<links\>\<\/links> 区块内的参数是属于 Global 的。
\<plot\>\<\/plot> 区块内的参数是属于 Local 的。

如果是某个参数在多个block中都重复使用，那么可以设置成 global 的参数，当某个block要使用新的值时，再用 local 的参数覆盖即可。

.. code-block::

   # plot可以理解为图层，多个圈图图层构成一个plots
   <plot></plot>
   # plots 由
   # type 描述图层内容类型，如text
   type = text
   # r0, r1 表示圈图半径，<1在内圈，>1在外圈, r0-r1为宽度
   r0 = 0.95r
   r1 = 0.85r
   #

1. ideogram
2. highlight
3. tick
4. label
5. link

circos.conf 参数

.. code-block::

   # 染色体的数据集
   karyotype = data.txt
   # 定义圈图标尺
   chromosomes_units = 1000
   # 如果设置成yes，所有ideogram上都会现实ticks
   chromosomes_display_default = yes

3.4 circos 常量的单位
^^^^^^^^^^^^^^^^^^^^^

--------------------------------------------------------------------------------

4. 用 circos 来绘图
-------------------

4.1 绘制环状 Salmonella LT2 基因组
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

之前的教程里介绍了用DNAPlotter绘制一个基因组完成图的圈图，圆圈内容strand，GC content和GC skew。从某个角度上看，DNAplotter的配置文件与circos有一定的类似，2个软件的区别在于前者专注于绘制单个细菌基因组，后者可以完成更多的功能。第一个例子我们通过用circos来绘制类似DNAplotter生成的基因组圈图，从而学习circos的基本用法，

4.1.1 数据文件的准备
~~~~~~~~~~~~~~~~~~~~

从NCBI上下载Salonella LT基因组数据文件。

.. code-block:: bash

   ~$ esearch -db nuccore -query "NC_003197.1[accn]" | efetch -db nuccore -format fasta > LT2.fasta
   ~$ esearch -db nuccore -query "NC_003197.1[accn]" | efetch -db nuccore -format gb > LT2.gb

绘制 circos 所需要的 ideogram 所需要的几类数据，我们通过一个 python 脚本 get\_circos\_data.py 来获得。

.. code-block:: python

运行脚本：

~$ python get_circos_data.py

4.1.2 配置文件的准备

建立circos.conf配置文件

~$ cd circos_data
~/circos_data$ touch circos.conf





.. _circos: http://circos.ca
