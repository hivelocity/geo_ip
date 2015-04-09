from setuptools import setup

setup(
    name='geo_ip',
    version='1.0.0',
    author='Hivelocity',
    author_email='dev@hivelocity.net',
    description='Small PyGeoIP wrapper, including GeoIP data',
    long_description=open('README.md').read(),
    packages=['geo_ip'],
    package_data=dict(geo_ip=['GeoLiteCity.dat']),
    include_package_data=True,
    install_requires=['pygeoip>=0.3.1'],
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
)
