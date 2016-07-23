第3节. 注释拼接基因组
=====================

基因组草图获得后，对其进行注释。

1. Prokka
---------

1.1 安装 Prokka
^^^^^^^^^^^^^^^

安装 Bioperl
~~~~~~~~~~~~

.. code-block:: bash

   ~$ sudo apt-get install cpanminus
   ~$ cpanm Bio::Perl XML::Simple

安装 rRNA predictor
~~~~~~~~~~~~~~~~~~~

这里选择Barrnap

.. code-block:: bash

   ~/tmp$ wget http://www.vicbioinformatics.com/barrnap-0.5.tar.gz
   ~/tmp$ tar zxvf barrnap-0.5.tar.gz -C ~/app/
   ~/tmp$ echo "export PATH=$PATH:$HOME/app/barrnap-0.5/bin" >> ~/.bashrc
   ~/tmp$ source ~/.bashrc

安装 prokka
~~~~~~~~~~~

.. code-block:: bash

   ~/tmp$ wget http://www.vicbioinformatics.com/prokka-1.11.tar.gz
   ~/tmp$ tar zxvf prokka-1.11.tar.gz -C ~/app
   ~/tmp$ echo "export PATH=$PATH:$HOME/app/prokka-1.11/bin" >> ~/.bashrc
   ~/tmp$ source ~/.bashrc
   ~/tmp$ prokka --setupdb

1.2 注释基因组
^^^^^^^^^^^^^^

.. code-block:: bash

    ~/data$ prokka genome_contig.fasta

--------------------------------------------------------------------------------

2. PGAAP
--------

http://www.ncbi.nlm.nih.gov/genome/annotation_prok/
http://www.ncbi.nlm.nih.gov/books/NBK174280/

--------------------------------------------------------------------------------

3. RAST
-------

Reference:
----------

1.
2.
