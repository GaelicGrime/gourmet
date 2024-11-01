

import subprocess as SUBP


ARGS = [
    "ls",
    "-lash",
    "/home/will/",
]


KWARGS = {
    "capture_output": True,
    "shell": False,
    "encoding": "UTF-8",
}

# run(*popenargs, input=None, capture_output=False, timeout=None, check=False,
#     **kwargs)


#  bufsize=-1, executable=None, stdin=None, stdout=None, stderr=None,
#     preexec_fn=None, close_fds=True, shell=False, cwd=None, env=None,
#     universal_newlines=None, startupinfo=None, creationflags=0,
#     restore_signals=True, start_new_session=False, pass_fds=(), *, user=None,
#     group=None, extra_groups=None, encoding=None, errors=None, text=None, umask=-1,
#     pipesize=-1)

_result_ = SUBP.run(ARGS, **KWARGS)
print(f"""_result_ {_result_}""")
print(f"""_result_.stdout {_result_.stdout}""")
