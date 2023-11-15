from distutils.core import setup

setup(
    name='community',
    version='2.8',
    py_modules=['communities'],
    entry_points={
        "console_scripts": ["community=communities:run_script"]
    },
    license='',
    author='Gladys',
    author_email='',
    description='Show the meaning of community',
)
