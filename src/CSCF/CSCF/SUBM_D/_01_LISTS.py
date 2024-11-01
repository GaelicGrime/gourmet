

from CSCF.SUBM_D import (
    _00_SIMPLE_REPR as CF_SREPR,
    _00_VALS_IN as CF_V,
  )


locals().update(CF_V.ALL_THE_VALS)


class list1_C():
  def __init__(self):
    self.L = []

  def __enter__(self):
    return self

  def __exit__(self, *args_):
    pass

  def __len__(self):
    return len(self.L)

  def reset(self):
    self.L = []

  def str(self, *,
        recursive_=False,
    ):
    _strToRtn_ = ""
    for _thisElement_ in self.L:
      CF_SREPR.strAnObject(
        objectToStr_=_thisElement_,
        recursive_=recursive_,
      )





#
