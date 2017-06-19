from setuptools import find_packages
from setuptools import setup


install_requires = [
    'selenium==3.4.3'
]


dependency_links = [

]


setup(
    name='selpages',
    version='0.1',
    description='Selenium page objects-like implementation',
    author='King Chung Huang',
    author_email='kchuang@ucalgary.ca',
    url='https://github.com/ucalgary/python-selpages',
    packages=find_packages(),
    package_data={

    },
    install_requires=install_requires,
    dependency_links=dependency_links,
    entry_points="""
    """,
    zip_safe=True
)
