import os
from setuptools import setup, find_packages
from test.commands.version import Version


def file_read(fname):
    return open(os.path.join(os.path.dirname(__file__), 'docs', fname)).read()

setup(
    name='test',
    version=Version().get_version(),
    description='A cool app',
    long_description=(file_read('README.rst')),
    url='http://test.com',
    license='MIT',
    author='Christopher Simpkins',
    author_email='chris@zerolabs.net',
    platforms=['any'],
    #py_modules=['naked'],
    #scripts=['naked'],
    entry_points = {
        'console_scripts': [
            'test = test.app:main'
        ],
    },
    packages=find_packages("lib"),
    package_dir={'': 'lib'},
    install_requires=['Naked', 'requests'],
    keywords='python,command line,system,application,framework,CLI,bootstrap',
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
