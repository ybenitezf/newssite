"""App para crear un sitio de noticias"""
from setuptools import find_packages, setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='newssite',
    version='0.0.0',
    url='https://github.com/ybenitezf/newssite',
    license='GPL',
    author='Yoel Benítez Fonseca',
    author_email='ybenitezf@gmail.com',
    description='News site for adelante.cu',
    long_description=read('README.md'),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    setup_requires=['pytest-runner'],
    tests_require=[
        'pytest',
        'pytest-cov'
    ],
    install_requires=[
        'wheel',
        'Flask',
        'python-dotenv',
        'roman-discovery>=0.2.0',
        'Flask-Static-Digest>=0.2.1',
        'Flask-SQLAlchemy',
        'Flask-Migrate',
        'adelacommon @ https://github.com/ybenitezf/adela-common/releases/download/v0.0.3/adelacommon-0.0.3-py3-none-any.whl'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary',
    ]
)
