from distutils.core import setup

setup(
    name='git_edit_commit',
    version='0.0.2',
    py_modules=['git_edit_commit'],
    entry_points={
        "console_scripts": ["git_edit_commit=git_edit_commit:command_line_tool"]
    },
    license='',
    author='Gladys',
    author_email='',
    description='Edit commit configs metadata'
)
