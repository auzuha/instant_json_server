from setuptools import setup, find_packages

setup(
    name='instant_json_server',
    version='0.1.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "fastapi"
    ],
    author='Augustine Stephens',
    entry_points={
        'console_scripts': [
            'instant-json-server = server.main:main',
        ],
    },
    author_email='auzuha@gmail.com',
    description='Package to create backend API server with all basic CRUD operations for any JSON File.',
    long_description='Package to create backend API server with all basic CRUD operations.',
    long_description_content_type='text/markdown',
    url='https://github.com/auzuha/instant_json_server',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
