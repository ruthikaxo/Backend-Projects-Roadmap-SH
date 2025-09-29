from setuptools import setup

setup(
    name="task-cli",
    version="0.1.0",
    py_modules=["task_tracker"],
    install_requires=["tabulate"],
    entry_points={
        "console_scripts": [
            "task-cli=task_tracker:main",
        ],
    },
)
