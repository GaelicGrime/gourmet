#!/usr/bin/python


# Base64 Encoder - encodes a folder of PNG files and creates a .py file with definitions
import base64
import os
import PySimpleGUI as SG
from CF.SUBM_D import _00_VALS_IN as CF_V


locals().update(CF_V.ALL_THE_VALS)


def __main__():
  OUTPUT_FILENAME = 'output.py'

  _folder_ = SG.popup_get_folder(
      f"""Source folder for images{NEWLINE}Images will be encoded and results saved to {OUTPUT_FILENAME}""",
      title='Base64 Encoder',
  )

  if (
      (not _folder_)
  ):
    SG.popup_cancel('Cancelled - No valid folder entered')
    return
  try:
    _namesonly_ = [_thisFile_ for _thisFile_ in os.listdir(_folder_) if _thisFile_.endswith('.png') or _thisFile_.endswith('.ico') or _thisFile_.endswith('.gif')]
  except:
    SG.popup_cancel('Cancelled - No valid folder entered')
    return

  _FDOut_ = open(os.path.join(_folder_, OUTPUT_FILENAME), 'w')
  _listToRtn_ = []
  for _TI1_, _file_ in enumerate(_namesonly_):
        _contents_ = open(os.path.join(_folder_, _file_), 'rb').read()
        _encoded_ = base64.b64encode(_contents_)
        _name_ = _file_[:_file_.index(".")]
        _FDOut_.write(f"""{NEWLINE}{NEWLINE}{NEWLINE}{_name_} = {_encoded_}""")
        _listToRtn_.append(_name_)
        SG.OneLineProgressMeter('Base64 Encoding', _TI1_+1, len(_namesonly_), key='-METER-')

  _strToRtn_ = f"""{NEWLINE}{NEWLINE}{NEWLINE}ALL_THE_IMGS = {OBRCE}{NEWLINE}"""
  for _thisName_ in _listToRtn_:
    _strToRtn_ += f"""{NTAB(2)}{DBLQT}{_thisName_}{DBLQT}: {_thisName_},{NEWLINE}"""
  _strToRtn_ += f"""{CBRCE}{NEWLINE}"""
  _FDOut_.write(_strToRtn_)
  _FDOut_.close()
  SG.popup(f"""Completed!""", f"""Encoded {_TI1_ + 1} files)""")


__main__()
