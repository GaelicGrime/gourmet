

from . import _01_ZENITY_VARS as V


V.V = V


def radioList(*,
    columnList_  : list = [("TRUE", "Quit", "Quit.")],
    columnNames_ : list = ["Select", "Value", "Description"],
    height_      : int = 400,
    hideColumn_  : int = 2,
    text_        : str = "Which one would you like to do?",
    title_       : str = "Pick one.",
    width_       : int = 500,
    ) -> str:
  # 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱
  _commands_ = [
      "zenity",
      f"""--width={width_}""",
      f"""--height={height_}""",
      "--list",
      f"""--title='{title_}'""",
      f"""--text='{text_}'""",
      "--radiolist",
    ]

  for _thisColumn_ in columnNames_:
    _commands_ += [f"""--column='{_thisColumn_}'"""]

  _commands_ += [f"""--hide-column={hideColumn_}"""]

  for _thisDefault_, _thisValue_, _thisDescription_ in columnList_:
    _commands_ += [f"""{_thisDefault_}""", f"""'{_thisValue_}'""", f"""'{_thisDescription_}'"""]

  print(f"""Executing""", _commands_)
  _result_ = V.SP.run(_commands_, capture_output=True, text=True)
  return _result_
  # ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1





#
