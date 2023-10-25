from distutils.core import setup

setup(
    name='communities',
    version='1.2',
    py_modules=['communities'],
    entry_points={
        "console_scripts": ["communities=communities:command_line_tool"]
    },
    license='',
    author='Gladys',
    author_email='',
    description='Run my script to know the meaning of the community'
)
