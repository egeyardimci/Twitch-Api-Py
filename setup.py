from distutils.core import setup
setup(
  name = 'TwitchApiPy',
  packages = ['TwitchApiPy'],
  version = '0.1',
  license='MIT',
  description = 'This Lib allows you to use the twitch api with basic functions , you can find example codes in my github page : xegepa/Twitch-Api-Py',
  author = 'Ege Yardimci',
  author_email = 'egeyardimci2003@gmail.com',
  url = 'https://github.com/xegepa/Twitch-Api-Py',
  download_url = 'hhttps://github.com/xegepa/Twitch-Api-Py/archive/1.0.tar.gz',
  keywords = ['Twitch', 'Api', 'Easy'],
  install_requires=[
          'requests',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)