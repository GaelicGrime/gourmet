

# import magic as MAGIC
#import stat as STAT
from os import path as OSPATH
from tqdm import tqdm as TQ_DM  ## remove to _00_TQDM_C
import pathlib as PL  ## remove to _00_PL_C
import glob as GLOB_  ## remove to _00_GLOB
import inspect as INS  ## remove to _00_INSPECT_C
import os as OS
import re as RE
import subprocess as SP  ## remove to _00_SUBPROCESS_C
import sys as SYS


from CSCF.CONST_D import _00_PATHLIB_KEYS as PL_K
from CSCF.SUBM_D import (
    _00_VALS_IN as CF_V,
    _00_WHO_WHERE as WW,
    _01_LISTS as L,
  )


V = None
locals().update(CF_V.ALL_THE_VALS)
LOG_DIR = "/storage/logs/scripts"
ABS_PATH = OSPATH.abspath
HOME = f"""{OSPATH.expanduser('~')}"""


# MIME = MAGIC.Magic(mime=True)
ACCESS                     = OS.access
BASE_NAME                  = OSPATH.basename
CHDIR                      = OS.chdir
CHMOD                      = OS.chmod
CHOWN                      = OS.chown
COMMON_PATH                = OSPATH.commonpath
COMMON_PREFIX              = OSPATH.commonprefix
DIR_NAME                   = OSPATH.dirname
ENVIRON                    = OS.environ
ESCAPE                     = GLOB_.escape
EXISTS                     = OSPATH.exists
EXIT                       = SYS.exit
EXPAND_USER                = OSPATH.expanduser
EXPAND_VARS                = OSPATH.expandvars
GET_A_TIME                 = OSPATH.getatime
GET_C_TIME                 = OSPATH.getctime
GET_M_TIME                 = OSPATH.getmtime
GET_SIZE                   = OSPATH.getsize
GETCWD                     = OS.getcwd
GETEGID                    = OS.getegid
GETEUID                    = OS.geteuid
GETGID                     = OS.getgid
GETLOGIN                   = OS.getlogin
GETUID                     = OS.getuid
GLOB                       = GLOB_.glob
IGLOB                      = GLOB_.iglob
IS_ABS                     = OSPATH.isabs
IS_DIR                     = OSPATH.isdir
IS_FILE                    = OSPATH.isfile
IS_LINK                    = OSPATH.islink
IS_MOUNT                   = OSPATH.ismount
JOIN                       = OSPATH.join
L_EXISTS                   = OSPATH.lexists
LC                         = L.list1_C
LN                         = OS.link
LNS                        = OS.symlink
LOGW                       = None
MKDIR                      = OS.mkdir
MV                         = OS.rename
NORM_CASE                  = OSPATH.normcase
NORM_PATH                  = OSPATH.normpath
PLP                        = PL.Path
PLP                        = PL.Path
REAL_PATH                  = OSPATH.realpath
REL_PATH                   = OSPATH.relpath
RENAME                     = OS.rename
RM                         = OS.remove
RMDIR                      = OS.rmdir
RMDIRS                     = OS.removedirs
SAME_FILE                  = OSPATH.samefile
SAME_OPEN_FILE             = OSPATH.sameopenfile
SAME_STAT                  = OSPATH.samestat
SPLIT                      = OSPATH.split
SPLIT_DRIVE                = OSPATH.splitdrive
SPLIT_EXT                  = OSPATH.splitext
STAT                       = OS.stat
SUB                        = RE.sub
SUPPORTS_UNICODE_FILENAMES = OSPATH.supports_unicode_filenames
WAIS                       = WW.whereStr


ABS_DOT = ABS_PATH(EXPAND_USER("."))


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * Keys
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

ALL_THE_KEYS = {
  "K_F_OK": OS.F_OK,
  "K_R_OK": OS.R_OK,
  "K_W_OK": OS.W_OK,
  "K_X_OK": OS.X_OK,
}
ALL_THE_KEYS.update(PL_K.ALL_THE_KEYS)
locals().update(ALL_THE_KEYS)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * File Entry Vars
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
SHORT_ENTRY_TUP = (
    (K_DIR, ""),  # Just the directory portion of the path.
    (K_EXTENSION, ""),  # Just the extension
    (K_FILENAME, ""),  # The filename and extension.
    (K_JUST_FILENAME, ""),  # Just the filename without the extension.
    (K_NUMS, 0),  # Numerical prefixes if asked for.
    (K_PATH, ""),  # The whole path to the file.
)
def E_SHORT_ENTRY():
  return dict((x, y) for x, y in SHORT_ENTRY_TUP)


PL_ENTRY_TUP = (
    (K_ALLOCATED_SIZE, 0),
    (K_BLOCKS_ALLOCATED, 0),
    (K_DIR, ""),  # Just the directory portion of the path.
    (K_ERROR_CONDITION, False),
    (K_ERROR_TEXT, ""),
    (K_EXTENSION, ""),  # Just the extension
    (K_FILENAME, ""),  # The filename and extension.
    (K_FILETYPE, KFT_UNKNOWN),
    (K_GID, ""),
    (K_I_CAN_EXECUTE, False),
    (K_I_CAN_READ, False),
    (K_I_CAN_WRITE, False),
    (K_IS_A_DIR, False),
    (K_IS_A_FILE, False),
    (K_IS_A_KNOWN_FILE_TYPE, False),
    (K_IS_A_SYMLINK, False),
    (K_JUST_FILENAME, ""),  # Just the filename without the extension.
    (K_MODE, ""),
    (K_NEW_DIR, ""),
    (K_NEW_EXTENSION, ""),
    (K_NEW_JUST_FILENAME, ""),
    (K_NEW_JUST_FILENAME_SUFFIX, ""),
    (K_NEW_PATH, ""),
    (K_NUMS, 0),  # Numerical prefixes if asked for.
    (K_PATH, ""),  # The whole path to the file.
    (K_SIZE, 0),
    (K_TIME_ACCESSED, 0),
    (K_TIME_CHANGED, 0),
    (K_TIME_CREATED, 0),
    (K_TIME_META_MODIFIED, 0),
    (K_UID, ""),
    (KD_BLACK_NAME, ""),
    (KD_WHITE_NAME, ""),
    (KF_BLACK_NAME, ""),
    (KF_WHITE_NAME, ""),
    (KPL_PARTS, ""),
    (KPL_PATH_ENTRY, ""),
)
def E_PL_ENTRY():
  return dict((x, y) for x, y in PL_ENTRY_TUP)


ENTRY_TUP = (
    (K_ALLOCATED_SIZE, 0),
    (K_BLOCKS_ALLOCATED, 0),
    (K_DIR, ""),  # Just the directory portion of the path.
    (K_ERROR_CONDITION, False),
    (K_ERROR_TEXT, ""),
    (K_EXTENSION, ""),  # Just the extension
    (K_FILENAME, ""),  # The filename and extension.
    (K_FILETYPE, KFT_UNKNOWN),
    (K_GID, 0),
    (K_I_CAN_EXECUTE, False),
    (K_I_CAN_READ, False),
    (K_I_CAN_WRITE, False),
    (K_IS_A_DIR, False),
    (K_IS_A_FILE, False),
    (K_IS_A_KNOWN_FILE_TYPE, False),
    (K_IS_A_SYMLINK, False),
    (K_JUST_FILENAME, ""),  # Just the filename without the extension.
    (K_NEW_JUST_FILENAME_SUFFIX, ""),
    (K_MODE, -1),
    (K_NEW_DIR, ""),
    (K_NEW_EXTENSION, ""),
    (K_NEW_JUST_FILENAME, ""),
    (K_NEW_PATH, ""),
    (K_NUMS, 0),  # Numerical prefixes if asked for.
    (K_PATH, ""),  # The whole path to the file.
    (K_SIZE, 0),
    (K_TIME_ACCESSED, 0),
    (K_TIME_CHANGED, 0),
    (K_TIME_CREATED, 0),
    (K_TIME_META_MODIFIED, 0),
    (K_UID, 0),
)
def E_ENTRY():
  return dict((x, y) for x, y in ENTRY_TUP)


MEDIA_TUP = (
  (K_COLOR_DEPTH, ""),        # %[bit-depth]
  (K_COLORS, 0),              # expensive %[colors]
  (K_COLORSPACE, ""),         # %[colorspace]
  (K_FORMAT, ""),             # %m
  (K_FRAME, 0),               # repurposed for number of frames identified
  (K_GEOMETRY_ORIGIN, ""),    # unused
  (K_GEOMETRY_PAGE, (0, 0)),  # %g
)
def E_MEDIA():
  return dict((x, y) for x, y in MEDIA_TUP)


PL_CLASS_DICT_TUPLE = (
    (KTP_COLOUR, "#af33EE"),
    (KTP_DESC, "progress"),
    (KTP_EXTENDED, False),
    (KTP_LEAVE, True),
    (KTP_PAD_CHR, "…"),
    (KTP_PAD_DESC, True),
    (KTP_PAD_NUM, 17),
    (KTP_POSITION, 0),
    (KTP_SHOW_PROGRESS, True),
  )
def E_PL_CLASS_DICT() -> dict:
  return dict((x, y) for x, y in PL_CLASS_DICT_TUPLE)



# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * Sanity Checks
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
DIR_BLACK_LIST = "[a-zA-Z0-9\-_\./]"
DIR_WHITE_LIST = "[^a-zA-Z0-9\-_\./]"
FILE_BLACK_LIST = "[a-zA-Z0-9\-_\.]"
FILE_WHITE_LIST = "[^a-zA-Z0-9\-_\.]"

"""
DIR_BLACK_LIST = "[a-zA-Z0-9./]"
DIR_WHITE_LIST = "[^a-zA-Z0-9\-_\./]"
FILE_BLACK_LIST = "[a-zA-Z0-9.]"
FILE_WHITE_LIST = "[^a-zA-Z0-9\-_\.]"
"""

ILLEGAL_PATHS = ILLEGALPATHS = [  # list of absolute paths to be completely ignored if used
  "/",  # do not operate on / ever
]

ILLEGAL_WILDCARDS = ILLEGALWILDCARDS = [  # list all of the portions of a filename which will result in an error [0:] based
  "/bin/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/boot/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/dev/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/efi/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/etc/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/home/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/lib/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/lib64/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/media/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/opt/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/proc/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/root/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/run/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/sbin/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/srv/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/sys/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/tmp/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/usr/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/var/",  # illegal wildcards, these are most often /path/ and will be [0:] based
]


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * Start of sortDedupeList
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def sortDedupeList(listIn_):
  # fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
  _listToRtn_ = list(sorted(set(listIn_)))
  return _listToRtn_
  # fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * End of sortDedupeList
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * File Type Lists
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


FTL_ARCHIVES = [
  ".lzma",
  ".rar",
  ".tgz",
  ".zip",
]

FTL_CODE = [
  ".c",
  ".coffee",
  ".htm",
  ".html",
  ".js",
  ".php",
  ".pl",
  ".py",
  ".sh",
  ".ts",
  ".zsh",
]

FTL_DATA = [
  ".cson",
  ".csv",
  ".db",
  ".json",
  ".kml",
  ".kmz",
  ".sqlite",
]

FTL_TEXT_DATA = [
  ".cson",
  ".csv",
  ".json",
  ".kml",
]

FTL_DOCS = [
  ".md",
  ".pdf",
  ".txt",
  ".pkl",
  ".odt",
]

FTL_TEXT_DOCS = [
  ".md",
  ".txt",
]

FTL_PICS = [
  ".apng",
  ".bmp",
  ".gif",
  ".jp2",
  ".jpe",
  ".jpeg",
  ".jpg",
  ".png",
  ".psd",
  ".riff",
  ".webp",
]

FTL_ANIMATED_PICS = [
  ".apng",
  ".gif",
]

FTL_SNDS = [
  ".au",
  ".mp3",
  ".wav",
]

FTL_TEXT = [
  ".lst",
  ".txt",
]
FTL_TEXT.extend(FTL_CODE)
FTL_TEXT.extend(FTL_TEXT_DOCS)
FTL_TEXT.extend(FTL_TEXT_DATA)
FTL_TEXT = sortDedupeList(FTL_TEXT)

FTL_VIDS = [
  ".asx",
  ".avi",
  ".divx",
  ".flv",
  ".gifv",
  ".hdv1",
  ".hdv2",
  ".hdv3",
  ".m2ts",
  ".m4a",
  ".m4v",
  ".mkv",
  ".mov",
  ".mp1v",
  ".mp4",
  ".mpeg",
  ".mpg",
  ".mpg1",
  ".ogv",
  ".qt",
  ".vcr2",
  ".video",
  ".webm",
  ".wmv",
]

# LEAVE AT BOTTOM OF FILE TYPES
FTL_MEDIA = []
FTL_MEDIA.extend(FTL_PICS)
FTL_MEDIA.extend(FTL_SNDS)
FTL_MEDIA.extend(FTL_VIDS)
FTL_MEDIA = sortDedupeList(FTL_MEDIA)

FTL_ALL_KNOWN = []
FTL_ALL_KNOWN.extend(FTL_CODE)
FTL_ALL_KNOWN.extend(FTL_DATA)
FTL_ALL_KNOWN.extend(FTL_DOCS)
FTL_ALL_KNOWN.extend(FTL_PICS)
FTL_ALL_KNOWN.extend(FTL_SNDS)
FTL_ALL_KNOWN.extend(FTL_TEXT)
FTL_ALL_KNOWN.extend(FTL_VIDS)
FTL_ALL_KNOWN = sortDedupeList(FTL_ALL_KNOWN)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * Ignore File Lists
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
IL_PYTHON = [
    "__enter__.py",
    "__exit__.py",
    "__init__.py",
    "__main__.py",
]

IL_MEDIA = [
    "thumbs.db",
    "__unrename__.zsh"
]


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * File Modes
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
A_R = lambda __MODE__: __MODE__ and 0o004
A_RW = lambda __MODE__: __MODE__ and 0o006
A_RWX = lambda __MODE__: __MODE__ and 0o007
A_W = lambda __MODE__: __MODE__ and 0o002
A_X = lambda __MODE__: __MODE__ and 0o001
G_R = lambda __MODE__: __MODE__ and 0o040
G_RW = lambda __MODE__: __MODE__ and 0o060
G_RWX = lambda __MODE__: __MODE__ and 0o070
G_W = lambda __MODE__: __MODE__ and 0o020
G_X = lambda __MODE__: __MODE__ and 0o010
U_R = lambda __MODE__: __MODE__ and 0o400
U_RW = lambda __MODE__: __MODE__ and 0o600
U_RWX = lambda __MODE__: __MODE__ and 0o700
U_W = lambda __MODE__: __MODE__ and 0o200
U_X = lambda __MODE__: __MODE__ and 0o100


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * DEPRECATED USE _01_DIALOG instead
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * Start of KD_ERROR_DIALOG
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def KD_ERROR_DIALOG(*,
    details_=None,
    message_,
):
  # fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
  # 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱
  if (
      (details_ in V.CF_V.EMPTY_STR_LST)
  ):
    _listToRtn_ = [
        "kdialog",
        "--error",
        f"""{V.CF_V.DBLQT}{message_}{V.CF_V.DBLQT}""",
    ]
  # ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱
  else:
    _listToRtn_ = [
        "kdialog",
        "--detailederror",
        f"""{V.CF_V.DBLQT}{message_}{V.CF_V.DBLQT}""",
        f"""{V.CF_V.DBLQT}{details_}{V.CF_V.DBLQT}""",
    ]
  # ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1
  return _listToRtn_
  # fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * End of KD_ERROR_DIALOG
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


DEBUG_ERROR_CODES = {
    1: "IO error.",
    2: "File or directory not found.",
    3: "Incorrect parameters given."
}


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * Start of KD_WARNING_DIALOG_LIST
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def KD_WARNING_DIALOG_LIST(*,
    message_,
):
  # fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
  _strToRtn_ = f"""{V.CF_V.DBLQT}{message_}{V.CF_V.DBLQT}"""
  _listToRtn_ = [
      "kdialog",
      "--warningyesno",
      _strToRtn_,
  ]
  return _listToRtn_
  # fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * End of KD_WARNING_DIALOG_LIST
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * Start of KD_TWO_BTN_DIALOG
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def KD_TWO_BTN_DIALOG(*,
    noLabel_="no",
    message_=None,
    yesLabel_="yes",
):
  # fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
  # 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱
  if (
      (message_ is None)
  ):
    message_ = ""
  # ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1
  _listToRtn_ = [
      "kdialog",
      "--yesno"
      f"""{V.CF_V.DBLQT}{message_}{V.CF_V.DBLQT}""",
      "--no-label",
      f"""{V.CF_V.DBLQT}{noLabel_}{V.CF_V.DBLQT}""",
      "--yes-label",
      f"""{V.CF_V.DBLQT}{yesLabel_}{V.CF_V.DBLQT}""",
  ]
  return _listToRtn_
  # fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * End of KD_TWO_BTN_DIALOG
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * DEPRECATED USE _01_DIALOG instead
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


def SP_FIND_DIRS(*,
    filename_,
    rootDir_,
):
  # 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱
  _listToRtn_ = [
      "find",
      f"""{rootDir_}""",
      "-type",
      "d",
      "-name",
      f"""{filename_}"""
  ]
  _dictToRtn_ = {
      "capture_output": True,
      "text": True,
  }
  return (_listToRtn_, _dictToRtn_)
  # ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1


def SP_FIND_FILES(*,
    filename_,
    rootDir_,
):
  # 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱
  _listToRtn_ = [
      "find",
      f"""{rootDir_}""",
      "-type",
      "f",
      "-name",
      f"""{filename_}"""
  ]
  _dictToRtn_ = {
      "capture_output": True,
      "text": True,
  }
  return (_listToRtn_, _dictToRtn_)
  # ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1


#ALL_THE_KEYS = {
#    "K_TIME_ACCESSED": K_TIME_ACCESSED,
#    "K_ALLOCATED_SIZE": K_ALLOCATED_SIZE
#    "K_BLOCKS_ALLOCATED": K_BLOCKS_ALLOCATED,
#    "K_TIME_META_MODIFIED": K_TIME_META_MODIFIED,
#    "K_DEFAULT": K_DEFAULT,
#    "K_DIR": K_DIR,
#    "K_EXTENSION": K_EXTENSION,
#    "K_F_OK": K_F_OK,
#    "K_FILENAME": K_FILENAME,
#    "K_FILETYPE": K_FILETYPE,
#    "KFT_CODE": KFT_CODE,
#    "KFT_DATA": KFT_DATA,
#    "KFT_DOCS": KFT_DOCS,
#    "KFT_PICS": KFT_PICS,
#    "KFT_SNDS": KFT_SNDS,
#    "KFT_TEXT": KFT_TEXT,
#    "KFT_UNKNOWN": KFT_UNKNOWN,
#    "KFT_VIDS": KFT_VIDS,
#    "K_GID": K_GID,
#    "K_I_CAN_EXECUTE": K_I_CAN_EXECUTE,
#    "K_I_CAN_READ": K_I_CAN_READ,
#    "K_I_CAN_WRITE": K_I_CAN_WRITE,
#    "K_IS_A_DIR": K_IS_A_DIR,
#    "K_IS_A_FILE": K_IS_A_FILE,
#    "K_IS_A_KNOWN_FILE_TYPE": K_IS_A_KNOWN_FILE_TYPE,
#    "K_IS_A_SYMLINK": K_IS_A_SYMLINK,
#    "K_JUST_FILENAME": K_JUST_FILENAME,
#    "K_LAST": K_LAST,
#    "K_LIST": K_LIST,
#    "K_MODE": K_MODE,
#    "K_TIME_META_MODIFIED": K_TIME_META_MODIFIED,
#    "K_NEW_JUST_FILENAME": K_NEW_JUST_FILENAME,
#    "K_NUMS": K_NUMS,
#    "K_PATH": K_PATH,
#    "K_QUIT": K_QUIT,
#    "K_R_OK": K_R_OK,
#    "K_SIZE": K_SIZE,
#    "K_UID": K_UID,
#    "K_VERSION": K_VERSION,
#    "K_W_OK": K_W_OK,
#    "K_X_OK": K_X_OK,
#}


OPERATIONS_DATA = {
    "ABS_DOT"                    : ABS_DOT,
    "ABS_PATH"                   : ABS_PATH,
    "ACCESS"                     : ACCESS,
    "BASE_NAME"                  : BASE_NAME,
    "CHDIR"                      : CHDIR,
    "CHMOD"                      : CHMOD,
    "CHOWN"                      : CHOWN,
    "COMMON_PATH"                : COMMON_PATH,
    "COMMON_PREFIX"              : COMMON_PREFIX,
    "DIR_NAME"                   : DIR_NAME,
    "ENVIRON"                    : ENVIRON,
    "ESCAPE"                     : ESCAPE,
    "EXISTS"                     : EXISTS,
    "EXIT"                       : EXIT,
    "EXPAND_USER"                : EXPAND_USER,
    "EXPAND_VARS"                : EXPAND_VARS,
    "GET_A_TIME"                 : GET_A_TIME,
    "GET_C_TIME"                 : GET_C_TIME,
    "GET_M_TIME"                 : GET_M_TIME,
    "GET_SIZE"                   : GET_SIZE,
    "GETCWD"                     : GETCWD,
    "GETEGID"                    : GETEGID,
    "GETEUID"                    : GETEUID,
    "GETGID"                     : GETGID,
    "GETLOGIN"                   : GETLOGIN,
    "GETUID"                     : GETUID,
    "GLOB"                       : GLOB,
    "HOME"                       : HOME,
    "IGLOB"                      : IGLOB,
    "IS_ABS"                     : IS_ABS,
    "IS_DIR"                     : IS_DIR,
    "IS_FILE"                    : IS_FILE,
    "IS_LINK"                    : IS_LINK,
    "IS_MOUNT"                   : IS_MOUNT,
    "JOIN"                       : JOIN,
    "L_EXISTS"                   : L_EXISTS,
    "LC"                         : LC,
    "LN"                         : LN,
    "LNS"                        : LNS,
    "LOG_DIR"                    : LOG_DIR,
    "LOGW"                       : LOGW,
    "MKDIR"                      : MKDIR,
    "MV"                         : MV,
    "NORM_CASE"                  : NORM_CASE,
    "NORM_PATH"                  : NORM_PATH,
    "PLP"                        : PLP,
    "PLP"                        : PLP,
    "REAL_PATH"                  : REAL_PATH,
    "REL_PATH"                   : REL_PATH,
    "RENAME"                     : RENAME,
    "RM"                         : RM,
    "RMDIR"                      : RMDIR,
    "RMDIRS"                     : RMDIRS,
    "SAME_FILE"                  : SAME_FILE,
    "SAME_OPEN_FILE"             : SAME_OPEN_FILE,
    "SAME_STAT"                  : SAME_STAT,
    "SPLIT_DRIVE"                : SPLIT_DRIVE,
    "SPLIT_EXT"                  : SPLIT_EXT,
    "SPLIT"                      : SPLIT,
    "STAT"                       : STAT,
    "SUB"                        : SUB,
    "SUPPORTS_UNICODE_FILENAMES" : SUPPORTS_UNICODE_FILENAMES,
    "WAIS"                       : WAIS,
  }


FILESYSTEM_DATA = {
    "A_R"               : A_R,
    "A_RW"              : A_RW,
    "A_RWX"             : A_RWX,
    "A_W"               : A_W,
    "A_X"               : A_X,
    "DEBUG_ERROR_CODES" : DEBUG_ERROR_CODES,
    "DIR_BLACK_LIST"    : DIR_BLACK_LIST,
    "DIR_WHITE_LIST"    : DIR_WHITE_LIST,
    "E_ENTRY"           : E_ENTRY,
    "E_SHORT_ENTRY"     : E_SHORT_ENTRY,
    "FILE_BLACK_LIST"   : FILE_BLACK_LIST,
    "FILE_WHITE_LIST"   : FILE_WHITE_LIST,
    "FTL_ALL_KNOWN"     : FTL_ALL_KNOWN,
    "FTL_ANIMATED_PICS" : FTL_ANIMATED_PICS,
    "FTL_CODE"          : FTL_CODE,
    "FTL_DATA"          : FTL_DATA,
    "FTL_DOCS"          : FTL_DOCS,
    "FTL_MEDIA"         : FTL_MEDIA,
    "FTL_PICS"          : FTL_PICS,
    "FTL_SNDS"          : FTL_SNDS,
    "FTL_TEXT_DATA"     : FTL_TEXT_DATA,
    "FTL_TEXT_DOCS"     : FTL_TEXT_DOCS,
    "FTL_TEXT"          : FTL_TEXT,
    "FTL_VIDS"          : FTL_VIDS,
    "G_R"               : G_R,
    "G_RW"              : G_RW,
    "G_RWX"             : G_RWX,
    "G_W"               : G_W,
    "G_X"               : G_X,
    "IL_MEDIA"          : IL_MEDIA,
    "IL_PYTHON"         : IL_PYTHON,
    "ILLEGALPATHS"      : ILLEGALPATHS,
    "ILLEGALWILDCARDS"  : ILLEGALWILDCARDS,
    "ILLEGAL_WILDCARDS" : ILLEGAL_WILDCARDS,
    "U_R"               : U_R,
    "U_RW"              : U_RW,
    "U_RWX"             : U_RWX,
    "U_W"               : U_W,
    "U_X"               : U_X,
}


KDIALOG_DATA = {
    "KD_WARNING_DIALOG_LIST" : KD_WARNING_DIALOG_LIST,
    "KD_TWO_BTN_DIALOG"      : KD_TWO_BTN_DIALOG,
    "KD_ERROR_DIALOG"        : KD_ERROR_DIALOG,
}


SUBPROCESS_DATA = {
    "SP_FIND_FILES": SP_FIND_FILES,
}


DEBUG_DATA = {
    "DEBUG_ERROR_CODES": DEBUG_ERROR_CODES,
}


ALL_THE_OS_DATA = {
    "ALL_THE_VALS" : CF_V.ALL_THE_VALS,
    "CF_V"         : CF_V,
    "EXIT"         : EXIT,
    "GLOB_"        : GLOB_,
    "INS"          : INS,
    "OS"           : OS,
    "OSPATH"       : OSPATH,
    "PL"           : PL,
    "RE"           : RE,
    "SP"           : SP,
    "SYS"          : SYS,
#    "MIME"        : MIME,
#    "STAT"        : STAT,
}


ALL_THE_OS_DATA.update(ALL_THE_KEYS)
ALL_THE_OS_DATA.update(FILESYSTEM_DATA)
ALL_THE_OS_DATA.update(KDIALOG_DATA)
ALL_THE_OS_DATA.update(SUBPROCESS_DATA)
ALL_THE_OS_DATA.update(DEBUG_DATA)
ALL_THE_OS_DATA.update(CF_V.ALL_THE_VALS)
ALL_THE_OS_DATA.update(OPERATIONS_DATA)


#
