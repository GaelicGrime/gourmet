

import pathlib as PL


ABSOLUTE = PL.absolute
CHMOD = PL.chmod
EXISTS = PL.exists
expanduser(self)
    Return a new path with expanded ~ and ~user constructs
    (as returned by os.path.expanduser)

glob(self, pattern)
    Iterate over this subtree and yield all existing files (of any
    kind, including directories) matching the given relative pattern.

group(self)
    Return the group name of the file gid.

hardlink_to(self, target)
    Make this path a hard link pointing to the same file as *target*.

    Note the order of arguments (self, target) is the reverse of os.link's.

is_block_device(self)
    Whether this path is a block device.

is_char_device(self)
    Whether this path is a character device.

is_dir(self)
    Whether this path is a directory.

is_fifo(self)
    Whether this path is a FIFO.

is_file(self)
    Whether this path is a regular file (also True for symlinks pointing
    to regular files).

is_mount(self)
    Check if this path is a POSIX mount point

is_socket(self)
    Whether this path is a socket.

is_symlink(self)
    Whether this path is a symbolic link.

iterdir(self)
    Iterate over the files in this directory.  Does not yield any
    result for the special paths '.' and '..'.

lchmod(self, mode)
    Like chmod(), except if the path points to a symlink, the symlink's
    permissions are changed, rather than its target's.

link_to(self, target)
    Make the target path a hard link pointing to this path.

    Note this function does not make this path a hard link to *target*,
    despite the implication of the function and argument names. The order
    of arguments (target, link) is the reverse of Path.symlink_to, but
    matches that of os.link.

    Deprecated since Python 3.10 and scheduled for removal in Python 3.12.
    Use `hardlink_to()` instead.

lstat(self)
    Like stat(), except if the path points to a symlink, the symlink's
    status information is returned, rather than its target's.

mkdir(self, mode=511, parents=False, exist_ok=False)
    Create a new directory at this given path.

open(self, mode='r', buffering=-1, encoding=None, errors=None, newline=None)
    Open the file pointed by this path and return a file object, as
    the built-in open() function does.

owner(self)
    Return the login name of the file owner.

read_bytes(self)
    Open the file in bytes mode, read it, and close the file.

read_text(self, encoding=None, errors=None)
    Open the file in text mode, read it, and close the file.

readlink(self)
    Return the path to which the symbolic link points.

rename(self, target)
    Rename this path to the target path.

    The target path may be absolute or relative. Relative paths are
    interpreted relative to the current working directory, *not* the
    directory of the Path object.

    Returns the new Path instance pointing to the target path.

replace(self, target)
    Rename this path to the target path, overwriting if that path exists.

    The target path may be absolute or relative. Relative paths are
    interpreted relative to the current working directory, *not* the
    directory of the Path object.

    Returns the new Path instance pointing to the target path.

resolve(self, strict=False)
    Make the path absolute, resolving all symlinks on the way and also
    normalizing it (for example turning slashes into backslashes under
    Windows).

rglob(self, pattern)
    Recursively yield all existing files (of any kind, including
    directories) matching the given relative pattern, anywhere in
    this subtree.

rmdir(self)
    Remove this directory.  The directory must be empty.

samefile(self, other_path)
    Return whether other_path is the same or not as this file
    (as returned by os.path.samefile()).

stat(self, *, follow_symlinks=True)
    Return the result of the stat() system call on this path, like
    os.stat() does.

symlink_to(self, target, target_is_directory=False)
    Make this path a symlink pointing to the target path.
    Note the order of arguments (link, target) is the reverse of os.symlink.

touch(self, mode=438, exist_ok=True)
    Create this file with the given access mode, if it doesn't exist.

unlink(self, missing_ok=False)
    Remove this file or link.
    If the path is a directory, use rmdir() instead.

write_bytes(self, data)
    Open the file in bytes mode, write to it, and close the file.

write_text(self, data, encoding=None, errors=None, newline=None)
    Open the file in text mode, write to it, and close the file.
