from setuptools import setup, find_packages

setup(name='nyaapy',
      version='0.1',
      url='https://github.com/juanjosalvador/nyaapy',
      license='MIT',
      author='Juanjo Salvador',
      author_email='juanjosalvador@netc.eu',
      description='Allows you to make requests on Nyaa.si and nyaa.pantsu.cat',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False)
