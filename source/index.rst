病原微生物高通量测序数据分析笔记
================================

.. note::
    本电子书为基于BSD授权，版权归作者所有；欢迎下载及编辑(个人用途)，但未经作者同意必须保留此段声明，且不可用于商业用途，否则保留追究法律责任的权利。

    - 作者：indexofire <indexofire@gmail.com>
    - Github地址：https://github.com/indexofire/ndafp

关于本笔记
----------

随着高通量测序技术快速发展，小型台式测序仪的出现降低了高通量测序的门槛。对于开展微生物特别是病原微生物的测序工作的需求，在各种临床，科研以及政府的小型实验室中迅速扩展。目前已经上市的比较适合小型实验室的测序仪如 Illumina Miseq，Illumina NextSeq500，Ion S5，Ion PGM 等，即将上市的测序仪如 Illumina MiniSeq，Qiagen GeneReader。除了传统的二代测序仪，不需要扩增的基于单分子测序技术的三代测序技术的 PacBio Sequel 和最近开展埃博拉实时测序项目的基于纳米孔技术的 Oxford MinION 产品都是非常适合开展病原微生物测序的平台。

测序数据的不断产出，需要生物信息学人才来参与到测序数据的分析以便获得有价值的生物学信息对于许多小型实验室来说，很难招募到优秀的生物信息学人才。对于非专业背景的人来说，命令行以及软件的安装可能是学习中遇到的首要难题。本笔记主要是通过介绍微生物，特别是病原细菌的高通量测序数据分析，帮助原来从事湿实验领域的同事能较好的了解和掌握高通量测序数据分析，将学习曲线变得平缓。同时也希望能对从事该领域的其他工作者提供便利，让大家在需要分析微生物基因组数据时，能有一个资料与实例汇集的手册可以快速参考和学习。

本笔记主要针对 Miseq 机器的产出数据开展分析，由于原理类似分析软件也大都可以应用在 Illumina 其他型号的仪器数据上。例子都是运行在安装了 Ubuntu 发行版的 Linux PC 服务器或者 Ubuntu 的个人电脑上。

|image0| |image1|

本笔记使用开源工具 `Sphinx-doc <http://sphinx-doc.org/>`__ 创作，并在 `Read the Docs <https://readthedocs.org/>`__ 网站发布。笔记中的许多内容都是来源于网络上的资料，部分来源可能有误或记忆不全，如果原作者发现没有内容链接，或者链接错误，请发送 `电子邮件 <mailto:indexofire@gmail.com>`__ 通知修改。同时希望 `Open Source <http://opensource.org/>`__ 思想能对科研工作和科研工作者有所帮助。

本笔记代码托管在 `Github <https://www.github.com/>`__, 所有内容可以在 http://github.com/indexofire/ndafp.git 获得。笔者接触 NGS 时间不长，内容中肯定会有许多错误之处，希望能有NGS领域的专家帮助指正。对于
笔记中的错误会内容更新，可以提交 `issues <https://github.com/indexofire/ndafp/issues>`__\ ，帮助完善笔记内容。

Fork笔记方法
------------

1. 在GitHub上访问本书源码，并fork成为自己的仓库。如下图所示，点击fork按钮，然后用 git clone 到本地，设置好代码仓库用户信息。就可以修改并提交代码了。
   |image2|

  .. code-block:: bash

     ~$ git clone git@github.com:your_github_username/ndafp.git
     ~$ cd ndafp
     ~/ndafp$ git config user.name "your github username"
     ~/ndafp$ git config user.email your_email@something.com

2. 对需要的内容做修改后提交，并 git push 到之前 fork 的仓库。

   .. code-block:: bash

      ~/ndafp$ git add -A
      ~/ndafp$ git commit -am "Fix issue #1: change typo: helo to hello"
      ~/ndafp$ git push

3. 这样你自己的代码分支 master 与源代码分支就会出现差异，要合并这些差异，就要在 GitHub 网站上提交 pull request。如下图所示如果有代码。
   |image3|

4. 由于源代码仓库也会经常更新或者合并其他 pull request 代码，需要定期使用源项目仓库内容来更新自己仓库内容。

   .. code-block:: bash

      ~/ndafp$ git remote add upstream https://github.com/indexofire/ndafp.git
      ~/ndafp$ git fetch upstream
      ~/ndafp$ git checkout master
      ~/ndafp$ git merge upstream/master
      ~/ndafp$ git push origin master

内容目录
--------

.. toctree::
   :maxdepth: 2
   :glob:

   preface/index
   chapter_01/index
   chapter_02/index
   chapter_03/index

版本更新
--------

v0.0.1: 2016.07.20

- 将gitbook内容转换成rst格式，并对原有内容做了适当调整，逐步补充完整
  原计划的章节内容。

.. |image0| image:: _static/img/miseq.jpg
.. |image1| image:: _static/img/ubuntu.jpg
.. |image2| image:: _static/img/fork.png
.. |image3| image:: _static/img/pull_request.png

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
