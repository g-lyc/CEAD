#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Usage:
  CEAD package <env_name>
  CEAD deploy <env_file> <env_name>
  CEAD (-h | --help)
  CEAD --version

Options:
  -h --help       Help Doc.
  --deploy        Deploy a packaged conda environment compression package.
  --package       Packaging conda environment.
  --version       Show version.
"""

__author__ = "liyc"
__copyright__ = "Copyright 2020"
__email__ = "liyichen2015@gmail.com"

import os
from docopt import docopt


class CEAD(object):
    def __init__(self, env_file=None, env_name=None, package=False, deploy=False):
        super(CEAD, self).__init__()
        self.env_file = env_file
        self.env_name = env_name
        self.package = package
        self.deploy = deploy

        if self.deploy:
            self.deploy_fun(self.env_file, self.env_name)

        if self.package:
            self.package_fun(self.env_name)


    def __repr__(self):
        return '<Requirements \'{}\'>'.format(self.env_name)


    def deploy_fun(self, env_file, env_name):
        if not os.path.exists(env_file):
            raise ValueError('The given environment gz file does not exist.')

        script = os.path.split(os.path.realpath(__file__))[0]+'/deploy.sh'

        CMD = 'bash {} {} {}'.format(script, self.env_file, self.env_name)

        os.system(CMD)


    def package_fun(self, env_name):

        script = os.path.split(os.path.realpath(__file__))[0]+'/package.sh'

        CMD = 'bash {} {}'.format(script, self.env_name)

        os.system(CMD)



def main():
    args = docopt(__doc__, version='version==v0.1')

    kwargs = {
        'env_file': args['<env_file>'],
        'env_name': args['<env_name>'],
        'deploy': args['deploy'],
        'package': args['package']
    }

    CEAD(**kwargs)


if __name__ == '__main__':
    main()
