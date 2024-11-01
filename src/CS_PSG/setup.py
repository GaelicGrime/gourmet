

from setuptools import find_packages
from setuptools import setup
from datetime import datetime as DT


__VERSION__ = DT.now().strftime("%Y.%m.%d.%H%M%S")
with open("CS_PSG/__VERSION__.py", "tw") as _FD_OUT_:
  _FD_OUT_.write(f"""\n\n__VERSION__ = \"{__VERSION__}\"\n\n#\n""")


setup(
  author="GaelicGrime",
  author_email="will.angus.blaylock@gmail.com",
  license="GPLv3",
  name="CS_PSG",
  url="https://github.com/ComfortableSoftware/CS_PSG",
  version=__VERSION__,
  package_dir={"CS_PSG": "CS_PSG"},
  package_data={
      "CS_PSG": [
          "../doc/*",
      ],
  },
  scripts=[
    ],
  packages=find_packages(),
  install_requires=[
      "PySimpleGUI",
  ],
)


#
