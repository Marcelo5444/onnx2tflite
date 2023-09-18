import os
import re
from setuptools import setup, find_packages
from pkg_resources import parse_requirements

PACKAGE_NAME = 'onnx2tflite'
PACKAGE_PATH = PACKAGE_NAME
VERSION_FILE_PATH = os.path.join(PACKAGE_PATH, '__init__.py')
REQUIREMENTS_FILE_PATH = 'requirements.txt'

# Read __version__ from VERSION_FILE_PATH
exec(open(VERSION_FILE_PATH).read())

# Reformat editable requirements with proper VCS links
with open(REQUIREMENTS_FILE_PATH, 'r') as requirements_file:
    text = requirements_file.read()
requirements_text = re.sub(r'^\s*\-e\s+([^=]+)=([^\n]+)', r'\2 @ \1=\2', text, flags=re.MULTILINE)

# Build setup
setup(
    name=PACKAGE_NAME,
    version=__version__,
    package_dir={PACKAGE_NAME: PACKAGE_PATH},
    packages=find_packages(
        include=[PACKAGE_NAME, f'{PACKAGE_NAME}.*'],
        exclude=[],
    ),
    install_requires=[
        req.__str__()
        for req in parse_requirements(requirements_text)
    ],
)
