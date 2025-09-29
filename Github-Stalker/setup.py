from setuptools import setup

setup(
    name="github-stalker-cli",
    version="0.1.0",
    py_modules=["github_stalker"],
    entry_points={
        "console_scripts": [
            "github-stalker=github_stalker:main",
        ],
    },
)
