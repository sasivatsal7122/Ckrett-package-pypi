from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='ckret',
  version='1.0.0',
  description='a basic ciphering/deciphering tool',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/sasivatsal7122/ckret-library-pypi',
  author='Sasi Vatsal',
  author_email='sasivatsal7122@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='ckret',
  packages=find_packages(),
  install_requires=[''] 
)
