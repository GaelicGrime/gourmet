import optparse
import version

parser = optparse.OptionParser(
    version=version.version,
    option_list=[
    #optparse.make_option("-h","--help",action="help"),
    optparse.make_option("--gourmet-directory",
                         action="store",
                         dest="gourmetdir",
                         help="Gourmet configuration directory",
                         default=""),
    optparse.make_option("--debug-threading-interval",
                         action="store",
                         type="float",
                         dest='thread_debug_interval',
                         help="Interval for threading debug calls",
                         default=5.0),
    optparse.make_option("--debug-threading",action="store_true",dest='thread_debug',
                         help="Print debugging information about threading."),
    optparse.make_option("-q",action='store_const',const=-1,
                         dest='debug',
                         help="Don't print gourmet error messages"),
    optparse.make_option("--showtimes",action="store_true",dest="time",
                         help="Print timestamps on debug statements."),
    optparse.make_option("-v",action='count',
                         help="Be verbose (extra v's will increase the verbosity level",
                         dest='debug'),
    optparse.make_option("--data-directory",
                         dest="datad",
                         help="Directory for Gourmet data files.",
                         action="store",
                         default=""),
    optparse.make_option("--image-directory",
                         dest="imaged",
                         help="Directory for Gourmet image files.",
                         action="store",
                         default=""),
    optparse.make_option("--glade-directory",
                         dest="gladed",
                         help="Directory for Gourmet glade files.",
                         action="store",
                         default=""),    
    ]
    )

(options, args) = parser.parse_args()
