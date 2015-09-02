
from distutils.core import setup, Extension

setup(name="cEngine",
      version="0.1",
      description="graphics engine",
      author="Sean Riley",
      ext_modules=[Extension("cEngine",
                             ["cEngine.cpp", "engine.cpp"],
                             )]
      )


