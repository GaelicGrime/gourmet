

from tqdm import tqdm as TQ_DM
import os as OS
from . import _00_VALS_IN as CF_V


locals().update(CF_V.ALL_THE_VALS)


class CPMV_C():
  # 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱
  def __init__(self, *,
        destURL_,
        sourceURL_,
      ):
    # 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱
    self.DEST_URL = destURL_
    self.ERROR_STATUS = False
    self.ERROR_STR = ""
    self.INFO_STR = ""
    self.SOURCE_URL = sourceURL_
    # ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2

  def __enter__(self, *, parms):
    # 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱
    pass
    # ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2

  def __exit__(self, *, parms):
    # 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱
    pass
    # ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2

  def cpmv(self, *, parms):
    pass

  def cleanup(self, *, parms):
    pass

  # ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1
