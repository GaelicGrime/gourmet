

from setuptools import find_packages
from setuptools import setup
from datetime import datetime as DT


__VERSION__ = DT.now().strftime("%Y.%m.%d.%H%M%S")
with open("CSCF/__VERSION__.py", "tw") as _FD_OUT_:
  _FD_OUT_.write(f"""\n\n__VERSION__ = \"{__VERSION__}\"\n\n#\n""")


setup(
  author="GaelicGrime",
  author_email="will.angus.blaylock@gmail.com",
  license="GPLv3",
  name="CSCF",
  url="https://github.com/ComfortableSoftware/CSCF",
  version=__VERSION__,
  package_dir={"CSCF": "CSCF"},
  packages=find_packages(),
  install_requires=[],
)


#
