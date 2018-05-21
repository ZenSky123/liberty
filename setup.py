from setuptools import find_packages, setup

setup(
    name="liberty",
    version="1.0",
    keywords=("liberty"),
    description="Elegant for Internet",
    license="MIT License",

    author="realsky",
    author_emial="carotwang@126.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[],

    scripts=[],
    entry_points={
        'console_scripts': [
            'connect = liberty.command_line:main'
        ]
    },
    zip_safe=False
)
