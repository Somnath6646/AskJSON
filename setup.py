from setuptools import setup, find_packages

# It's important to open the README.md file using UTF-8 encoding to prevent encoding issues on different platforms
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='AskJSON',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'openai',
        'termcolor',
        'python-dotenv',
        'langchain',
        'stdlib-list',
        'python-Levenshtein',  # If this is a required dependency, it should be listed here.
    ],
    author='Somnath Mishra',  # Replace with your name
    author_email='somnathmishra6646@gmail.com',  # Replace with your email address
    description='A library to ask questions in natural language to JSON data',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Somnath6646/AskJSON',  # Replace with the actual URL to your project repository
    classifiers=[
        # Classifiers help users find your project by categorizing it.
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities"
    ],
    python_requires='>=3.6',
    keywords='json query ai openai python code generation',  # Add some relevant keywords
    project_urls={  # Optional
        'Bug Tracker': 'https://github.com/Somnath6646/AskJSON/issues',
        'Documentation': 'https://github.com/Somnath6646/AskJSON#readme',
        'Source Code': 'https://github.com/Somnath6646/AskJSON',
        # Add any other relevant links
    },
    include_package_data=True,  # Includes files specified by MANIFEST.in
    # Optional settings:
    # package_data={
    #   'package_name': ['data/*.dat'],
    # },
    # entry_points={
    #   'console_scripts': [
    #     'askjson=askjson.cli:main',
    #   ],
    # },
)
