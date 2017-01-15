from setuptools import setup

setup(
    name='Warframe Mastery checklist',
    packages=['wfmastery'],
    include_package_data=True,
    install_requires=[
        'flask',
        'sqlalchemy'
    ],
)
