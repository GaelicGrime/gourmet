

import subprocess as SUBP
ALL_THE_KEYS = {
    "K_ARGS": "args",
    "K_BUFSIZE": "bufsize",
    "K_CAPTURE_OUTPUT": "capture_output",
    "K_CHECK": "check",
    "K_CLOSE_FDS": "close_fds",
    "K_CREATIONFLAGS": "creationflags",
    "K_CWD": "cwd",
    "K_ENCODING": "encoding",
    "K_ENV": "env",
    "K_ERRORS": "errors",
    "K_EXECUTABLE": "executable",
    "K_EXTRA_GROUPS": "extra_groups",
    "K_GROUP": "group",
    "K_INPUT": "input",
    "K_KWARGS": "kwargs",
    "K_PASS_FDS": "pass_fds",
    "K_PIPESIZE": "pipesize",
    "K_PREEXEC_FN": "preexec_fn",
    "K_RESTORE_SIGNALS": "restore_signals",
    "K_RETURNCODE": "returncode",
    "K_SHELL": "shell",
    "K_START_NEW_SESSION": "start_new_session",
    "K_STARTUPINFO": "startupinfo",
    "K_STDERR": "stderr",
    "K_STDIN": "stdin",
    "K_STDOUT": "stdout",
    "K_TEXT": "text",
    "K_TIMEOUT": "timeout",
    "K_UMASK": "umask",
    "K_UNIVERSAL_NEWLINES": "universal_newlines",
    "K_USER": "user",
    "KSP_ARGS": "args_",
    "KSP_KWARGS": "KWArgs_",
    "KSPR_RESULT": "KSPR_RESULT",
    "KSPR_STDOUT": "KSPR_STDOUT",
}
locals().update(ALL_THE_KEYS)


KWARGS_TUP = (
    (K_BUFSIZE, -1),
    (K_CAPTURE_OUTPUT, True),
    (K_CHECK, False),
    (K_CLOSE_FDS, True),
    (K_CREATIONFLAGS, 0),
    (K_CWD, None),
    (K_ENCODING, "UTF-8"),
    (K_ENV, None),
    (K_ERRORS, None),
    (K_EXECUTABLE, None),
    (K_EXTRA_GROUPS, None),
    (K_GROUP, None),
    (K_INPUT, None),
    (K_PASS_FDS, ()),
    (K_PIPESIZE, -1),
    (K_PREEXEC_FN, None),
    (K_RESTORE_SIGNALS, True),
    (K_SHELL, False),
    (K_START_NEW_SESSION, False),
    (K_STARTUPINFO, None),
    (K_STDERR, None),
    (K_STDIN, None),
    (K_STDOUT, None),
    (K_TEXT, None),
    (K_TIMEOUT, None),
    (K_UMASK, -1),
    (K_UNIVERSAL_NEWLINES, None),
    (K_USER, None),
)
def E_KWARGS():
  return dict((x, y) for x, y in KWARGS_TUP)


RETURN_TUP = (
    (K_ARGS, []),
    (K_RETURNCODE, 0),
    (K_STDERR, ""),
    (K_STDOUT, ""),
)
def E_RETURN():
  return dict((x, y) for x, y in RETURN_TUP)

























#
