from setuptools import setup, find_packages

setup(name='nyaapy',
      version='0.6.0',
      url='https://github.com/juanjosalvador/nyaapy',
      download_url = 'https://github.com/juanjosalvador/nyaapy/archive/0.1.tar.gz',
      license='MIT',
      author='Juanjo Salvador',
      author_email='juanjosalvador@netc.eu',
      description='Allows you to make requests on Nyaa.si and nyaa.pantsu.cat',
      packages=find_packages(exclude=['tests']),
      zip_safe=False)
