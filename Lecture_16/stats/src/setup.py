# License MIT

import os
from setuptools import setup, find_packages

DISTRO_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

def extract_requirements(file):
    """
    Extract requirements from requirements file

    :param file: path to requirements file
    :type file: str
    :return: list[str] -- list of requirements
    """

    with open(file,'r') as file:
        return file.read().splitlines()


setup(
    name='supertool-distro',
    version='0.1',
    description='Super-super tool',
    author='Ilya Chulkov',
    author_email='4ylkov@mail.ru',
    license='MIT',
    classifiers=[
        'Topic :: Education',
        'Programming Language :: Python :: 3.6'
    ],
    packages=find_packages(exclude=['tests', 'requirements']),
    install_requires=extract_requirements(os.path.join(DISTRO_ROOT_PATH, 'requirements', 'base.txt')),
    test_requires=extract_requirements(os.path.join(DISTRO_ROOT_PATH, 'requirements', 'test.txt')),
    test_suite='nose.collector',
    zip_safe=False
)
