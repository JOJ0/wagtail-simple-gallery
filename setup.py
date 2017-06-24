import os
from setuptools import find_packages, setup
from wagtail_simple_gallery import __version__

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='wagtail-simple-gallery',
    version=__version__,
    author='Teemu Nieminen',
    author_email='temeez.dev@gmail.com',
    description='A simple gallery app for Wagtail.',
    long_description=README,
    license='MIT License',
    url='https://github.com/temeez/wagtail-simple-gallery',
    keywords='wagtail cms model page tempaltetags',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'wagtail>=1.10,<1.11',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
