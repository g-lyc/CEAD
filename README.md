CEAD
====

Quickly package existing conda environments and quickly deploy already packaged environments.

[![View Source][SOURCE-BADGE]](https://github.com/g-lyc/CEAD/tree/master/CEAD)
[![View PIP][PIP-BADGE]](https://pypi.org/project/CEAD/)

[SOURCE-BADGE]: https://img.shields.io/badge/view-source-brightgreen.svg
[PIP-BADGE]: https://img.shields.io/badge/download-pip-brightgreen.svg

Contents
--------

* [Introduction](#introduction)
* [Dependece](#dependece)
* [Install](#install)
* [Example](#example)

Introduction
------------

This repository contains the source code of a tools package existing conda environments or quickly deploy already packaged environments. The existing method is to export a conda environment to a yaml table, and reinstall it according to the yaml table when migrating. This tool will no longer make migrating the environment so cumbersome and needs to be declared is developed based on conda-pack.

Dependece
---------

Anaconda3 or miniconda3 need to be installed before installation.

Install
-------

1、install from pip

`pip install CEAD`

2、download sources code and setup

`git clone https://github.com/g-lyc/CEAD.git`

`cd CEAD`

`python setup.py install`

Example
-------

1、Package the exist conda environment:

`CEAD package exist_env_name`

2、Deploy the package:

`CEAD deploy exist_env_name.gz new_env_name`
