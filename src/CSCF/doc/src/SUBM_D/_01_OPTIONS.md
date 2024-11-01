
prog=None,
usage=None,
description=None,
epilog=None,
parents=[],
formatter_class=<class 'argparse.HelpFormatter'>,
prefix_chars='-',
fromfile_prefix_chars=None,
argument_default=None,
conflict_handler='error',
add_help=True,
allow_abbrev=True,
exit_on_error=True)


ArgumentParser **kwargs
    - prog -- The name of the program (default:
        ``os.path.basename(sys.argv[0])``)
    - usage -- A usage message (default: auto-generated from arguments)
    - description -- A description of what the program does
    - epilog -- Text following the argument descriptions
    - parents -- Parsers whose arguments should be copied into this one
    - formatter_class -- HelpFormatter class for printing help messages
    - prefix_chars -- Characters that prefix optional arguments
    - fromfile_prefix_chars -- Characters that prefix files containing
        additional arguments
    - argument_default -- The default value for all arguments
    - conflict_handler -- String indicating how to handle conflicts
    - add_help -- Add a -h/-help option
    - allow_abbrev -- Allow long options to be abbreviated unambiguously
    - exit_on_error -- Determines whether or not ArgumentParser exits with
        error info when an error occurs




(%) python parseArgparse.py -n -a 356 676 2435 -bonus 63465 "55z" 34 356 78467 3456 -g                                                                                                                                                 ✘ 2
_args_[0] Namespace(a=['356'], b=['63465', '55z', '34'])
_args_[0].a ['356']
_args_[0].b ['63465', '55z', '34']
_args_[1] ['-n', '676', '2435', '-bonus', '356', '78467', '3456', '-g']



import argparse as AP

_parser_ = AP.ArgumentParser(add_help=True)
_parser_.add_argument("-a", help="This is the first argument", nargs=1)
_parser_.add_argument(option_strings=["-b", "-bonus"], dest="b", type=str, help="swallow 3", nargs=3)


# Parse and print the results
_args_ = _parser_.parse_known_intermixed_args()

print(f"_args_[0] {_args_[0]}")
print(f"_args_[0].a {_args_[0].a}")
print(f"_args_[0].b {_args_[0].b}")

print(f"_args_[1] {_args_[1]}")

    - option_strings -- A list of command-line option strings which
        should be associated with this action.

    - dest -- The name of the attribute to hold the created object(s)

    - nargs -- The number of command-line arguments that should be
        consumed. By default, one argument will be consumed and a single
        value will be produced.  Other values include:
            - N (an integer) consumes N arguments (and produces a list)
            - '?' consumes zero or one arguments
            - '*' consumes zero or more arguments (and produces a list)
            - '+' consumes one or more arguments (and produces a list)
        Note that the difference between the default and nargs=1 is that
        with the default, a single value will be produced, while with
        nargs=1, a list containing a single value will be produced.

    - const -- The value to be produced if the option is specified and the
        option uses an action that takes no values.

    - default -- The value to be produced if the option is not specified.

    - type -- A callable that accepts a single string argument, and
        returns the converted value.  The standard Python types str, int,
        float, and complex are useful examples of such callables.  If None,
        str is used.

    - choices -- A container of values that should be allowed. If not None,
        after a command-line argument has been converted to the appropriate
        type, an exception will be raised if it is not a member of this
        collection.

    - required -- True if the action must always be specified at the
        command line. This is only meaningful for optional command-line
        arguments.

    - help -- The help string describing the argument.

    - metavar -- The name to be used for the option's argument with the
        help string. If None, the 'dest' value will be used as the name.




add_subparsers(self, **kwargs)
    # ==================================
    # Optional/Positional adding methods
    # ==================================

convert_arg_line_to_args(self, arg_line)

error(self, message)
    error(message: string)

    Prints a usage message incorporating the message to stderr and
    exits.

    If you override this in a subclass, it should not return -- it
    should either exit or raise an exception.

exit(self, status=0, message=None)
    # ===============
    # Exiting methods
    # ===============

format_help(self)

format_usage(self)
    # =======================
    # Help-formatting methods
    # =======================

parse_args(self, args=None, namespace=None)
    # =====================================
    # Command line argument parsing methods
    # =====================================

parse_intermixed_args(self, args=None, namespace=None)

parse_known_args(self, args=None, namespace=None)

parse_known_intermixed_args(self, args=None, namespace=None)

print_help(self, file=None)

print_usage(self, file=None)
    # =====================
    # Help-printing methods
    # =====================




#
