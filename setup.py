from setuptools import setup

requires = [
    'pyramid',
    'pytest'
]

setup(name='hello',
    install_requires=requires,
    entry_points="""\
    [paste.app_factory]
    main = hello:main
    """,
)
