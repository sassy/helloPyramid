from setuptools import setup

requires = [
    'pyramid',
]

setup(name='hello',
    install_requires=requires,
    entry_points="""\
    [paste.app_factory]
    main = hello:main
    """,
)
