from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from distutils.command.build import build as _build
from distutils.command.clean import clean as _clean
import os

class my_build(_build):
    def run(self):
        _build.run(self)

        # compile theme files
        import subprocess
        result = subprocess.call( "cd ./data/themes; edje_cc -v -id ../images -fd ../fonts zhone.edc", shell=True )
        if result != 0:
            raise Exception( "Can't build theme files. Built edje_cc?" )

class my_clean(_clean):
    def run(self):
        _clean.run(self)

        if os.path.exists('./data/themes/zhone.edj'):
            os.remove('./data/themes/zhone.edj')

setup(
    name = "zhone",
    version = "milestone2+git",
    author = "See AUTHORS",
    author_email = "mlauer@vanille-media.de",
    url = "http://www.freesmartphone.org",
    ext_modules = [
        Extension( "illume", ["src/illume.pyx"], libraries = ["ecore", "ecore_x"] )
        ],
    cmdclass = { 'build_ext': build_ext ,
                 'build'    : my_build  ,
                 'clean'    : my_clean  },
    scripts = [ "src/zhone" ],
    data_files = [
        ( "zhone/", ["data/themes/zhone.edj"] ),
        ( "pixmaps", ["data/launcher/zhone.png"] ),
        ( "applications", ["data/launcher/zhone.desktop"] ),
        ]
)
