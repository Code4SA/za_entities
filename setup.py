from setuptools import setup

setup(
    name='aleph_za_entities',
    entry_points={
        'aleph.analyzers': [
            'za_companies = aleph_za_entities.companies:CompanyAnalyzer',
            'za_persons = aleph_za_entities.sa_ids:PersonAnalyzer',
        ]
    },
    version='0.1',
    description='Aleph Analyzer to identify South African entities',
    url='http://github.com/code4sa/za_entities',
    author='Code For South Africa',
    author_email='info@code4sa.org',
    license='MIT',
    packages=["aleph_za_entities"],
    zip_safe=False,
    install_requires=[
        'luhn'
    ],
)
