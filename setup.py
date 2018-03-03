from distutils.core import setup

setup(name='PyCave',
      version='0.11',
      description='Find the treasure',
      author='mutetext',
      author_email='mutetext@outlook.com',
      packages=['grid'],
      install_requires=[
          'numpy',
          'math',
          'system',
          'random',
          'nose',
      ],
     )