from setuptools import setup
from crimpy import __version__

setup(
    version=__version__,
    name="crimpy",
    author="André Jaenisch",
    author_email="andre.jaenisch@posteo.de",
    description="Python-based CRM system",
    packages=["crimpy", ],
    install_requires=["pony", "PySide2", "shiboken2"],
    url="https://github.com/Ryuno-Ki/crimpy",
    license="GPL-3+",
    data_files=[("", ["LICENSE.txt", ])],
    platforms=["Linux", ],
    keywords=["crm"],
    include_package_data=True,
    project_urls={
      "Code": "https://github.com/Ryuno-Ki/crimpy",
      "Issue tracker": "https://github.com/Ryuno-Ki/crimpy/issues"
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ]
)
