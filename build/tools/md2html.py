#!/usr/bin/env python

import sys
import os
import re
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import mistune
from common import getMyLogger
from argparse import ArgumentParser

if __name__ == "__main__":

    parg = ArgumentParser(description='markdown to HTML snippet converter', version="0.1")

    ## positional arguments
    parg.add_argument('md_file',
                      metavar = 'markdown file',
                      nargs   = 1,
                      help    = 'the path to the markdown file')

    parg.add_argument('-o', '--output',
                      action='store',
                      dest='html_file',
                      default='',
                      help='specify the output HTML file path. Determined from the input markdown file if not specified')

    parg.add_argument('-l', '--loglevel',
                      action='store',
                      dest='verbose',
                      type=int,
                      choices=[0, 1, 2, 3],
                      default=0,
                      help='set one of the following verbosity levels. 0|default:WARNING, 1:ERROR, 2:INFO, 3:DEBUG')

    args = parg.parse_args()

    logger = getMyLogger(name=os.path.basename(__file__), lvl=args.verbose)

    renderer = mistune.Renderer(escape=False, hard_wrap=True)
    markdown = mistune.Markdown(renderer=renderer)

    for f in args.md_file:
        fpath_i = os.path.abspath(f)
        if not os.path.exists(fpath_i):
            logger.warn('skip non-existing input file: %s' % f)
            continue

        if not args.html_file:
            odir = os.path.dirname(fpath_i)
            oname = re.sub(r'\.(md|txt)$', '', os.path.basename(fpath_i)) + '.html'
            fpath_o = os.path.join(odir, oname)

        md_file = open(fpath_i)
        md_doc = md_file.read()
        md_file.close()

        html_doc = markdown(md_doc)

        html_file = open(fpath_o,'w')
        html_file.write(html_doc)
        html_file.close()

        logger.info('converted %s to %s' % (fpath_i, fpath_o))
