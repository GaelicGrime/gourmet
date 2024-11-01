

import argparse as AP

_parser_ = AP.ArgumentParser(add_help=True)
_parser_.add_argument("-a", help="This is the first argument", nargs=1)
_parser_.add_argument("-b", help="should swallow what's left", nargs=3)


# Parse and print the results
_args_ = _parser_.parse_known_intermixed_args()
for _thisArg_ in _args_:
  print(f"""_thisArg_ {_thisArg_}""")
