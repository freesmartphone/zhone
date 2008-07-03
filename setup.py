from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

# compile theme files
import subprocess
result = subprocess.call( "cd ./data/themes; edje_cc -v -id ../images -fd ../fonts zhone.edc", shell=True )

setup(
    name = "Zen Phone",
    version = "milestone1+git",
    author = "See AUTHORS",
    author_email = "mlauer@vanille-media.de",
    url = "http://www.freesmartphone.org",
    ext_modules = [
        Extension( "illume", ["src/illume.pyx"], libraries = [] )
        ],
    cmdclass = { 'build_ext': build_ext },
    scripts = [ "src/zhone" ],
    data_files = [
        ( "share/zhone/", ["data/themes/zhone.edj"] ),
        ]
)
