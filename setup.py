from distutils.core import setup

setup(name='pokesgen',
      version='1.0',
      description='pokemon image generation',
      long_description=open('README.md').read(),
      author='Chris Messier',
      license='BSD 3-Clause',
      author_email='messier.development@gmail.com',
      url='https://github.com/messiest/pokegen',
      packages=['pokegen'],
      classifiers=['Development Status :: 1 - Planning',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3',
                   'Topic :: Scientific/Engineering :: Artificial Intelligence'],
      )
