from distutils.core import setup

setup(
    name='communities',
    version='1.6',
    py_modules=['communities'],
    entry_points={
        "console_scripts": ["communities=communities:run_script"]
    },
    license='',
    author='Gladys',
    author_email='',
    description='Show the meaning of community',
)
