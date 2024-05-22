import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
            name='FRScraper',
            version='0.1.0',
            description='Python module for Football Reference scraping and easy access to football data from various leagues',
            long_description=long_description,
            long_description_content_type="text/markdown",
            url='https://github.com/GabrielPastorello/FRScraper',
            author='Gabriel Speranza Pastorello',
            author_email='gabriel.pastorello01@gmail.com',
            license='MIT',
            packages=setuptools.find_packages(),
            keywords=['football reference','scraper','premier league','la liga',
                      'ligue 1','serie a','bundesliga','eredivisie','football data'],
            python_requires=">=3.6",
            install_requires=['pandas>=2.2.2',
                              'numpy>=1.26.4',
                              'python-dateutil>=2.8.2',
                              'pytz>=2024.1'
                              ],
            classifiers=[
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
            ],
)
