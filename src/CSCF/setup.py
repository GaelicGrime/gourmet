

from setuptools import find_packages
from setuptools import setup
#from rsaaf import __VERSION__ as VS
from datetime import datetime as DT


__VERSION__ = DT.now().strftime("%Y.%m.%d.%H%M%S")
with open("__PACKAGE_NAME__/__VERSION__.py", "tw") as _FD_OUT_:
  _FD_OUT_.write(f"""\n\n__VERSION__ = \"{__VERSION__}\"\n\n#\n""")


setup(
  author="GaelicGrime",
  author_email="will.angus.blaylock@gmail.com",
  license="GPLv3",
  name="__PACKAGE_NAME__",
  url="https://github.com/ComfortableSoftware/__PACKAGE_NAME__",
  version=__VERSION__,
  package_dir={"__PACKAGE_NAME__": "__PACKAGE_NAME__"},
  package_data={
      "__PACKAGE_NAME__": [
          "../doc/*",
      ],
  },
  packages=find_packages(),
  install_requires=[
      "CSCF",
  ],
  scripts=[
      "scripts/__PACKAGE_NAME__",
  ],
)


#
