import setuptools
import distutils.core

setuptools.setup(
    name="macdotool",
    version=0.1,
    author="Tal",
    author_email="Wrii",
    description="Partial reimplementation of xdotool that works with mac based on pyautogui",
    license="GPLv3",
    packages=["macdotool"],
    entry_points={"console_scripts": ["macdotool=macdotool.macdotool:main"]},
    install_requires=["PyAutoGui"],
    classifiers=[],
)
