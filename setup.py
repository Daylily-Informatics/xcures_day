from setuptools import setup, find_packages

setup(
    name="xcures_day",
    version="0.0.2",
    author="John Major",
    author_email="john@daylilyinformatics.com",
    description="python wrapper for the xcures REST api, found here https://partner.xcures.com/api-docs .",
    long_description="see description",
    long_description_content_type="text/markdown",
    url="https://github.com/Daylily-Informatics/xcures_day",
    packages=find_packages(),
    scripts=[
    ],
    include_package_data=True,
    package_data={
        'xcures': [
            'bin/*',
        ],
    },
    python_requires=">=3.10",
    install_requires=["pytest", "requests", "yaml_config_day", "pytz", "ipython"], 
    )
 
 
