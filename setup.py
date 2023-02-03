
from setuptools import setup


setup(name='temp-sensor',


      version='0.1dev1',
      description='A test snap to write configuration into a TOML file',

      author='Muhammad Yahya & Felix Forster @ OLI Systems 2020',
      url='https://github.com/olisystems/intersnap-com-demo.git',
      packages=['temp_sensor'],
      install_requires=['paho-mqtt'],

      classifiers=[
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "Topic :: Utilities",
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: Operating System :: POSIX :: Linux", ],

      entry_points={
          'console_scripts': [
              'temp-sensor = temp_sensor.temp_sensor:main'
          ]
      },

      )
