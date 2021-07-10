import setuptools
from setuptools import setup

install_deps = ['numpy', 'scipy', 'natsort',
                'tifffile', 'tqdm', 'numba', 
                'torch>=1.6',
                'opencv-python-headless']


setup(
    name="cellpose",
    license="BSD",
    author="Marius Pachitariu and Carsen Stringer",
    author_email="stringerc@janelia.hhmi.org",
    description="anatomical segmentation algorithm",
    long_description_content_type="text/markdown",
    url="https://github.com/MouseLand/cellpose",
    packages=setuptools.find_packages(),
    install_requires = install_deps,
    entry_points = {
        'console_scripts': [
          'cellpose = cellpose.__main__:main']
     }
)
