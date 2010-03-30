# setup.py file for MapScript
#
# BUILD
#   python setup.py build
#
# INSTALL (usually as root)
#   python setup.py install
#   or easy_install mapscript
#
# DEVELOP (build and run in place)
#   python setup.py develop
import os

from setuptools import setup, Extension, find_packages

ms_install_dir, ms_macros, ms_includes, ms_libraries_pre, ms_extra_libraries = (
    "", "", "", "", ""
)
def mapserver_config_path():
    return os.popen('which mapserver-config').read().replace('\n', '')

def mapserver_config(arg):
    res = os.popen('mapserver-config --%s' % arg).read()
    if res:
        if res[-1] == '\n':
            res = res[:-1]
    return res
ms_version = '5.6.3'
ms_version += '.0'
try:
    if ms_version[0] in mapserver_config('version'):
        ms_install_dir = os.path.dirname(
            os.path.dirname(mapserver_config_path())
        )
        lib = os.path.join(ms_install_dir, 'lib')
        ms_macros = mapserver_config('defines')
        ms_includes = "%s %s %s %s" % (mapserver_config('includes'),
                                       mapserver_config('cflags'),
                                       ms_macros,
                                       os.environ.get('CFLAGS', '') )
        ms_libraries_pre = "%s" % (mapserver_config('libs'))
        ms_extra_libraries = mapserver_config('dep-libs')
except Exception, e:
    import pdb;pdb.set_trace()  ## Breakpoint ##
    pass
if not os.path.exists('mapscript_wrap.c') :
    os.system('swig -python -shadow -modern %s '
              '-o mapscript_wrap.c '
              '../mapscript.i' % " ".join(ms_macros))
os.environ['CFLAGS']  = '%s %s' % (ms_includes, ms_macros)
os.environ['LDFLAGS']  = '%s %s' % (ms_libraries_pre, ms_extra_libraries)
setup(
    name = "mapscript",
    version = ms_version,
    description = "Python interface to MapServer",
    author = "MapServer Project",
    url = "http://mapserver.org/",
    zip_safe = False,
    packages = find_packages(),
    include_package_data = True,
    install_requires = [ 'setuptools>=0.6c9',],
    ext_modules = [Extension("_mapscript",
                             ["mapscript_wrap.c", "pygdioctx/pygdioctx.c"],
                             libraries = ['mapserver']),
                  ],
    py_modules = ["mapscript"]
)

