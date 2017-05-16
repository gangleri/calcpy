from setuptools import setup
setup(
    name="calcpy",
    version="0.0.1",
    description="A basic calculator",
    entry_points={
        "console_scripts": [
            "calcpy = calcpy.cli:run_cli"
        ]
    },
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
    ],
    author="Dan Nixon",
    packages=["calcpy", "calcpy.calculator"],
    install_requires=[
        "numpy"
    ])

