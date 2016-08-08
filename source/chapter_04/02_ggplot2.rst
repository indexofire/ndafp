R语言与ggplot2
==============


.. code-block:: bash

   ~$ sudo apt install r-base

.. code-block:: bash

   ~$ R
   R version 3.2.5 (2016-04-14) -- "Very, Very Secure Dishes"
   Copyright (C) 2016 The R Foundation for Statistical Computing
   Platform: x86_64-pc-linux-gnu (64-bit)
   ...
   # 安装ggplot2
   > install.packages("ggplot2")



.. code-block:: bash

   ~$ sudo echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" | sudo tee -a /etc/apt/sources.list
   ~$ gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9
   ~$ gpg -a --export E084DAB9 | sudo apt-key add -
   ~$ sudo apt update
   ~$ sudo apt install r-base r-base-dev

   # 安装 R Studio
   ~$ sudo apt-get install gdebi-core
   ~$ wget https://download1.rstudio.org/rstudio-0.99.896-amd64.deb
   ~$ sudo gdebi -n rstudio-0.99.896-amd64.deb
   
