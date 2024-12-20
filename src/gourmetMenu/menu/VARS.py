from CSCF.SUBM_D import _00_OS as CF_OS


BACKGROUND_COLOR = "#103010"
DATABASES = []
FONT = "Source Code Pro"
FONT_SIZE = 10
MENU = ""
SOURCE_DIR = f"""{CF_OS.HOME}/stuff/recipes"""
TEXT_COLOR = "#800095"
TASKS = []

QUIT128 = b'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'


BTNQUIT = {
  "button_color": (TEXT_COLOR, BACKGROUND_COLOR),
  "button_text": "",
  "focus": True,
  "font": (FONT, FONT_SIZE),
  "image_data": QUIT128,
}

mainLayout = [
  [
    SG.Col(CLMTIMER),
  ],
  [
    SG.Text(
      key="_upTime_",
      **TEXTUPTIME,
    ),
    SG.Text(
      key="_downTime_",
      **TEXTDOWNTIME,
    ),
    SG.Col(
      [
        [
          SG.Btn(
            key="Quit",
            **BTNQUIT,
          ),
        ],
        [
          SG.Btn(
            key="zeroAll",
            **BTNZEROALL,
          ),
        ],
      ],
    ),
  ],
  [
    SG.Col(CLMTASK1),
    SG.Col(CLMTASK2),
    SG.Col(CLMTASK3),
    SG.Col(CLMTASK4),
  ],
]

mainWindowParms = {
  "title": MAINWINDOWTITLE,
  "layout": mainLayout,
  "location": (0, 0),
  "element_padding": (0, 0),
  "no_titlebar": False,
}

mainFrame = SG.Window(
  **mainWindowParms
).finalize()


def TASK_ENTRY(*,
    key_,
    bbuttonInfo_,
  ):
  # 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱
  return [
      SG.Button(
        key="task1+",
        **BTNTASKUP,
      ),
      SG.Btn(
        key="task1+nt",
        **BTNUPNOTIME,
      ),
    ],
  ]
  # ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1

def BUTTON(*,
    text_):
  # 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱
  return {
    "button_text": text_,
    "font": (FONT, FONT_SIZE),
    "focus": True,
    "button_color": (TEXT_COLOR, BACKGROUND_COLOR),
  }
  # ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1
