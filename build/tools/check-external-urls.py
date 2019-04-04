#!/usr/bin/env python
import sys
import os
import re
import cookielib
import urllib2
import json
import zipfile
import tarfile
import operator
import socket
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from common import getMyLogger

import argparse

class MyHTTPRedirectHandler(urllib2.HTTPRedirectHandler):
    '''
    Stop following the redirect.
    '''
    def http_error_302(self, req, fp, code, msg, headers):
        raise urllib2.HTTPError(fp=fp,code=302,msg=msg,hdrs=headers,url='')
    http_error_301 = http_error_303 = http_error_307 = http_error_302

if __name__ == "__main__":

    # command-line argument validators
    def valid_zipfile(s):
        if zipfile.is_zipfile(s):
            return s
        else:
            msg = "Invalid release file: %s" % s
            raise argparse.ArgumentTypeError(msg)

    def valid_tarfile(s):
        if tarfile.is_tarfile(s):
            return s
        else:
            msg = "Invalid release file: %s" % s
            raise argparse.ArgumentTypeError(msg)

    parg = argparse.ArgumentParser(description='check availability of external URLs defined by an index file (e.g. external_urls.json) within the release zipfile', version="0.1")

    parg.add_argument('pkg_zipfile', type=valid_tarfile, help='path to the zipped package for release')

    parg.add_argument('-p', '--prefix',
                      action='store',
                      dest='url_prefix',
                      default='http://data.donders.ru.nl/doc',
                      help='set the prefix of the external URLs of which the contents are provided by the release zipfile. The URLs matching this prefix will be checked whether the corresponding files are presented in the zipfile; otherwise, actual HTTP requests will be made to check their availability.')

    parg.add_argument('-i', '--index',
                      action='store',
                      dest='idx_file',
                      default='external_urls.json',
                      help='set the name of the index file in which the external URLs are defined.')

    parg.add_argument('-l', '--loglevel',
                      action='store',
                      dest='verbose',
                      type=int,
                      choices=[0, 1, 2, 3],
                      default=0,
                      help='set the verbosity level. 0|default:WARNING, 1:ERROR, 2:INFO, 3:DEBUG')

    args = parg.parse_args()
    logger = getMyLogger(name=os.path.basename(__file__), lvl=args.verbose)

    zf = None
    try:
        #zf = tarfile.TarFile(args.pkg_zipfile, 'r')
        #files_in_zip = zf.namelist()
        zf = tarfile.open(args.pkg_zipfile, mode='r:gz')
        files_in_zip = zf.getnames()
        dirs_in_zip = list(set(map(lambda x:os.path.dirname(x), files_in_zip)))

        # check existence of external_urls.json
        if args.idx_file not in files_in_zip:
            raise IOError('index file not found: {}'.format(args.idx_file))

        f_urls = zf.extractfile(args.idx_file)
        #f_urls = zf.open(args.idx_file, 'r')
        d_urls = json.load(f_urls)
        f_urls.close()

        bad_urls={}
        
        cookies = cookielib.LWPCookieJar()
        handlers = [ urllib2.HTTPHandler(), urllib2.HTTPSHandler(), urllib2.HTTPCookieProcessor(cookies), MyHTTPRedirectHandler() ]
        opener = urllib2.build_opener(*handlers)
        for k, v in sorted(d_urls.items(), key=operator.itemgetter(1)):

            if re.match('.*{.*.}.*', v ):
                logger.warn("file or dir for {}: SKIPPED".format(v))
                continue

            if re.match('^%s' % args.url_prefix, v):

                # remove the possible anchor part
                v = v.split('#')[0]

                # the URL matches url_prefix, should just check whether the file is provided by the package
                rel_fname = os.path.relpath(v, args.url_prefix)

                # determine whether the check should be on directories of files in the zip file
                list2check = files_in_zip
                if v[-1] == '/':
                    list2check = dirs_in_zip

                if rel_fname not in list2check:
                    # check whether the file/directory exists in the zip file
                    logger.error("file or dir not found: {}".format(rel_fname))
                    bad_urls[k] = v
                else:
                    logger.info("file or dir for {}: OK".format(k))
            else:
                try:
                    #connection = urllib2.urlopen(v)
                    connection = opener.open(v,timeout=3)
                    code = connection.getcode()
                    connection.close()
                    logger.info("URL of {0}: [{1}] OK".format(k, code))
                except socket.timeout, e:
                    logger.error("URL of {0}: {1} - {2}".format(k, "socket timeout",v))
                    bad_urls[k] = v
                except urllib2.HTTPError, e:
                    if 300 <= e.code < 400:
                        # take redirect as "success"
                        logger.info("URL of {0}: [{1}] {2}".format(k, e.code, e.reason))
                    else:
                        logger.error("URL of {0}: [{1}] {2}".format(k, e.code, e.reason))
                        bad_urls[k] = v
                except urllib2.URLError, e:
                    logger.error("URL of {0}: {1}".format(k, e.reason))
                    bad_urls[k] = v
    except Exception:
        raise
    finally:
        if zf:
            zf.close()

    # exit with proper code
    if bad_urls:
        sys.exit(1)
    else:
        sys.exit(0)
