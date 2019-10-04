from setuptools import setup
import mistletoe_notey

setup(name='mistletoe_notey',
      version=mistletoe_notey.__version__,
      description='A fast, extensible Notey Markdown parser in pure Python based on mistletoe_notey.',
      url='https://github.com/denizgenc/mistletoe_notey',
      author='Deniz Genc',
      author_email='25902330+denizgenc@users.noreply.github.com',
      license='MIT',
      packages=['mistletoe_notey'],
      entry_points={'console_scripts': ['mistletoe_notey = mistletoe_notey.__main__:main']},
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Text Processing :: Markup',
          ],
      python_requires='~=3.3',
      zip_safe=False)
