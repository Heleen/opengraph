from os.path import join, dirname
from distutils.core import setup

try:
    f = open(join(dirname(__file__), 'README.rst'))
    long_description = f.read().strip()
    f.close()
except IOError:
    long_description = ""


version = '0.9.1.1'

setup(
    name='ogp',
    version=version,
    description="A module to parse the Open Graph Protocol",
    long_description=long_description + "\n",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Markup :: HTML',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='opengraph protocol facebook',
    author='Erik Rivera',
    author_email='erik.river@gmail.com',
    url='https://github.com/graingert/opengraph',
    license='MIT',
    packages=["ogp",],
    install_requires=['BeautifulSoup'],
)
    
