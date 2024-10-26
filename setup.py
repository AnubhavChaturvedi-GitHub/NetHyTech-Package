from setuptools import setup, find_packages

setup(
    name='nethytech',  # Updated to match the package name
    version='0.8',
    packages=find_packages(),
    install_requires=[
        'selenium',
        'webdriver-manager',
    ],
    entry_points={
        'console_scripts': [
            'listen=nethytech.STT:listen',  # Updated path according to your package structure
        ],
    },
    author='Anubhav Chaturvedi',
    author_email='chaturvedianubhav520@gmail.com',
    description='A Selenium-based script to listen for text changes on a webpage and save them to a file.',
    long_description=open('README.md', encoding='utf-8').read(),  # Ensure you have README.md in the same directory
    long_description_content_type='text/markdown',
    url='https://anubhav-chaturvedi.netlify.app/',  # Your repository URL
)


#python setup.py sdist bdist_wheel
#twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
#