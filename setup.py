from setuptools import setup, find_packages

setup(
    name='nethytech',
    version='1.2',
    packages=find_packages(),
    install_requires=[
        'selenium>=4.0.0',
        'webdriver-manager>=3.8.0',
    ],
    entry_points={
        'console_scripts': [
            'listen=nethytech.STT:listen',  # Adjust based on the exact location and function in nethytech
        ],
    },
    author='Anubhav Chaturvedi',
    author_email='chaturvedianubhav520@gmail.com',
    description='NethyTech: One of the finest automation toolkits crafted by Anubhav Chaturvedi, bringing you powerful real-time text monitoring, dynamic weather insights, file utilities, and seamless automation – all in one Python package.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/AnubhavChaturvedi-GitHub/NetHyTech-Package',  # Update to your GitHub repo if available
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    project_urls={
        'Documentation': 'https://anubhav-chaturvedi.netlify.app/',
        'Source': 'https://github.com/anubhav-chaturvedi/nethytech',
        'Tracker': 'https://github.com/anubhav-chaturvedi/nethytech/issues',
    },
    python_requires='>=3.8',
    license='MIT',
)


#python setup.py sdist bdist_wheel
#twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
