脚本编程 Perl
=============

普通 Linux 发行版都会默认安装 Perl，可以用 `perl -v` 查看所安装的 perl 版本。

.. code-block:: bash

   $ perl -v


检查是否安装了 perl 模块可以用下面方法查看，如果安装了模块则没有打印输出，否则会提示找不到模块。

.. code-block:: bash

   $ perl -e 'use Bio::Seq'

用 CPAN 安装模块

.. code-block:: bash

   $ perl -MCPAN -e shell

   >install HTML::TokeParser::Simple

用 cpan 脚本安装模块

.. code-block:: bash

   $ cpan HTML::TokeParser::Simple
