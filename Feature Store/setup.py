from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: MacOS :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='Rasterdata',
  version='0.0.1',
  description='A very basic featurestore',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Simrandeep Singh',
  author_email='simrandeep.singh@student.uts.edu.au',
  license='MIT', 
  classifiers=classifiers,
  keywords='raster', 
  packages=find_packages(),
  install_requires=['rasterio','numpy','matplotlib'] 
)

