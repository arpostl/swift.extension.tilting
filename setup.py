# -*- coding: utf-8 -*-

"""
To upload to PyPI, PyPI test, or a local server:
python setup.py bdist_wheel upload -r <server_identifier>
"""

import setuptools

setuptools.setup(
    name="tilting",
    version="0.1.0",
    author="Andreas Postl",
    author_email="dedicated.codes@gmail.com",
    description= "Calculate an approximation for the tilting angle of a"\
                +" specimen based on the aspect ratio of an ellipse graphic"\
                +" (IMPORTANT: The corresponding ellipse graphic has to be"\
                +" selected when the button is clicked!)",
    packages=["nionswift_plugin.tilting"],
    install_requires=[],
    license='GPLv3',
    classifiers=[
        "Development Status :: 1 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
    ],
    include_package_data=True,
    python_requires='~=3.6',
    zip_safe=False
)
