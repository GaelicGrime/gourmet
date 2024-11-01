

from CSCF.SUBM_D import (
    _00_VALS_IN as CF_V
)
# from os.path import exists as EXISTS
import subprocess as SP


V = None
locals().update(CF_V.ALL_THE_VALS)


SM_PROGRESSBAR_AUTOCLOSE = "org.kde.kdialog.ProgressDialog.autoClose"
SM_PROGRESSBAR_CLOSE = "org.kde.kdialog.ProgressDialog.close"
SM_PROGRESSBAR_MAXIMUM = "org.kde.kdialog.ProgressDialog.maximum"
SM_PROGRESSBAR_SET_LABEL = "org.kde.kdialog.ProgressDialog.setLabelText"
SM_PROGRESSBAR_SHOW_CANCEL_BUTTON = "org.kde.kdialog.ProgressDialog.showCancelButton"
SM_PROGRESSBAR_VALUE = "org.kde.kdialog.ProgressDialog.value"
SM_PROGRESSBAR_WASCANCELLED = "org.kde.kdialog.ProgressDialog.wasCancelled"


ALL_THE_DLG_KEYS = {
  "K_DLG_ARGS": "args",
  "K_RESULT": "K_RESULT",
  "K_RETURN_CODE": "K_RETURN_CODE",
  "K_SERVICE_ARGS": "K_SERVICE_ARGS",
  "K_SERVICE_METHOD": "K_SERVICE_METHOD",
  "K_SERVICE_NAME": "K_SERVICE_NAME",
  "K_SERVICE_PATH": "K_SERVICE_PATH",
  "K_STATUS": "K_STATUS",
  "K_STDERR": "K_STDERR",
  "K_STDIN": "K_STDIN",
  "K_STDOUT": "K_STDOUT",
  "K_VALUE": "K_VALUE",
}
locals().update(ALL_THE_DLG_KEYS)


def parseProgressbarResult(
    resultToParse_,
    *,
    startingProgressbar=False,
):
  # 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱
  _stdOut_ = resultToParse_.stdout
  # 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱
  if (
      (resultToParse_.returncode == 0) and
      (startingProgressbar is True)
  ):
    _splitStdout_ = _stdOut_.split(" ")
  else:
    _splitStdout_ = ["", ""]
  # ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1
  return {
      K_DLG_ARGS: resultToParse_.args,
      # K_RESULT: resultToParse_,
      K_RETURN_CODE: resultToParse_.returncode,
      K_SERVICE_NAME: _splitStdout_[0],
      K_SERVICE_PATH: _splitStdout_[1][:-1],
      K_STDERR: resultToParse_.stderr,
      # K_STDIN: resultToParse_.stdin,
      K_STDOUT: resultToParse_.stdout,
  }
  # ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1


def runError(errorText_, errorResult_):
  _text_ = f"""An error occurred while {errorText_}"""
  _detail_ = f"""Args: `{errorResult_[K_DLG_ARGS]}`
Return code: {errorResult_[K_RETURN_CODE]}
Stderr: `{errorResult_[K_STDERR]}`
Stdin: `errorResult_[K_STDIN]`
Stdout: `{errorResult_[K_STDOUT]}`
"""
  _commands_ = [
      "kdialog",
      "--title",
      "Kdialog Error",
      "--detailederror",
      _text_,
      _detail_,
  ]
  V.runIt(_commands_)
  exit(errorResult_[K_RETURN_CODE])


def runIt(
  commandsToRun_,
  *,
  KWArgs_={}):
  # 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱
  if (
      ("capture_output" not in KWArgs_)
  ):
    KWArgs_["capture_output"] = True

  if (
      ("text" not in KWArgs_)
  ):
    KWArgs_["text"] = True

  _result_ = SP.run(commandsToRun_, **KWArgs_)
  return _result_
  # ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1





#
