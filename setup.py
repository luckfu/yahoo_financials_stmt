try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='yahoo_financials_stmt',
    packages=['yahoo_financials_stmt'],
    install_requires=[
        'requests'
    ],
    version='0.0.1',
    description='Scrapes data from Yahoo! Finance earnings calendar',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='luckfu',
    author_email='luckfu@gmail.com',
    url='https://github.com/luckfu/yahoo_financials_stmt',
    keywords=['stock', 'earnings', 'yahoo', 'scrape', 'finance'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
