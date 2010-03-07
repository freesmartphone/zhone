from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from distutils.command.build import build as _build
from distutils.command.clean import clean as _clean
import os
import subprocess
import shlex

class my_build(_build):
    def run(self):
        _build.run(self)

        # compile theme files
        import subprocess
        result = subprocess.call( "cd ./data/themes/toby; edje_cc -v -fd ../fonts zhone.edc; mv zhone.edj ../", shell=True )
        if result != 0:
            raise Exception( "Can't build theme files. Built edje_cc?" )

class my_clean(_clean):
    def run(self):
        _clean.run(self)

        if os.path.exists('./data/themes/zhone.edj'):
            os.remove('./data/themes/zhone.edj')

def getstatusoutput(cmdline):
    cmd = shlex.split(cmdline)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    out, err = p.communicate()
    return p.returncode, out

def pkgconfig(*packages, **kw):
    flag_map = {'-I': 'include_dirs', '-L': 'library_dirs', '-l': 'libraries',
                '-D': 'prepro_vars'}
    pkgs = ' '.join(packages)
    cmdline = 'pkg-config --libs --cflags %s' % pkgs

    status, output = getstatusoutput(cmdline)
    if status != 0:
        raise ValueError("could not find pkg-config module: %s" % pkgs)

    for token in output.split():
        flag  = flag_map.get(token[:2], None)
        if flag is not None:
            kw.setdefault(flag, []).append(token[2:])
        elif token.startswith("-Wl,"):
            kw.setdefault("extra_link_args", []).append(token)
        else:
            kw.setdefault("extra_compile_args", []).append(token)

    if "extra_link_args" in kw:
        print "Using extra_link_args: %s" % " ".join(kw["extra_link_args"])
    if "extra_compile_args" in kw:
        print "Using extra_compile_args: %s" % " ".join(kw["extra_compile_args"])

    return kw

setup(
    name = "zhone",
    version = "milestone4.1+git",
    author = "See AUTHORS",
    author_email = "mlauer@vanille-media.de",
    url = "http://www.freesmartphone.org",
    ext_modules = [
        Extension( "illume", sources=['src/illume.pyx'], **pkgconfig('"ecore >= 0.9.9.050" ''"eina-0 >= 0.0.1"') )
        ],
    cmdclass = { 'build_ext': build_ext ,
                 'build'    : my_build  ,
                 'clean'    : my_clean  },
    scripts = [ "src/zhone", "src/zhone-fsogsmd" ],
    data_files = [
        ( "zhone", ["data/themes/zhone.edj"] ),
        ( "zhone/locale/ru/LC_MESSAGES", ["data/locale/ru/LC_MESSAGES/zhone.mo"] ),
        ( "zhone/locale/pl/LC_MESSAGES", ["data/locale/pl/LC_MESSAGES/zhone.mo"] ),
        ( "pixmaps", ["data/launcher/zhone.png"] ),
        ( "applications", ["data/launcher/zhone.desktop"] ),
        ]
)
