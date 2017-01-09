from setuptools import setup

requires = [
    'pyramid',
    'pyramid_chameleon',
    'pytest'
]

setup(name='hello',
    install_requires=requires,
    entry_points="""\
    [paste.app_factory]
    main = hello:main
    """,
)
