

from CSCF.SUBM_D import (
    _00_SIMPLE_REPR as CF_SREPR,
    _00_VALS_IN as CF_V,
  )


locals().update(CF_V.ALL_THE_VALS)


class dict_C():
  def __init__(self):
    self.D = {}

  def __enter__(self):
    return self

  def __exit__(self, *args_):
    pass

  def reset(self):
    self.D = {}

  def length(self):
    return len(self.D)

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
