#!/usr/bin/env python
import sys
import os
import json
from jsonschema.validators import validate
from jsonschema.exceptions import ValidationError
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from common import getMyLogger
import argparse

if __name__ == "__main__":

    # command-line argument validators
    def valid_path(s):
        if os.path.isfile(s):
            return s
        else:
            msg = "Invalid filesystem path: %s" % s
            raise argparse.ArgumentTypeError(msg)

    #parg = argparse.ArgumentParser(description='validate JSON document agains schema', version="0.1")
    parg = argparse.ArgumentParser(description='validate JSON document agains schema')

    parg.add_argument('json_doc', type=valid_path, help='path to the JSON document')
    parg.add_argument('json_schema', type=valid_path, help='path to the JSON schema')
    parg.add_argument('-l', '--loglevel',
                      action='store',
                      dest='verbose',
                      type=int,
                      choices=[0, 1, 2, 3],
                      default=0,
                      help='set one of the following verbosity levels. 0|default:WARNING, 1:ERROR, 2:INFO, 3:DEBUG')

    args = parg.parse_args()
    logger = getMyLogger(name=os.path.basename(__file__), lvl=args.verbose)

    # load schema
    f_schema = open(args.json_schema, 'r')
    j_schema = json.load(f_schema)
    f_schema.close()

    # load json document
    f_doc = open(args.json_doc, 'r')
    j_doc = json.load(f_doc)
    f_doc.close()

    # valid json document
    try:
        validate(j_doc, j_schema)
        exit(0)
    except ValidationError as e:
        logger.error(e)
        exit(1)
