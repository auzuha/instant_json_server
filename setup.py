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
    long_description='''Package to create backend API server with all basic CRUD operations for any JSON File.
    Meant for developers who need to quickly wind up a server for a json file. It creates all basic CRUD endpoints for each resource of a JSON file of your choice.

    To Install
    pip install instant-json-server
    To use
    instant-json-server path_to_your_json
    Example JSON File that works:
      {
        "blogs": [
            {
                "id": 1,
                "content": "first blog"
            },
            {
                "id": 2,
                "content": "second blog"
            }
        ],
        "users": [
            {
                "id": "usr1",
                "username": "username1"
            },
            {
                "id": "usr2",
                "username": "username2"
            },
            {
                "id": 1233,
                "username": "asdasdad"
            },
            {
                "id": 12234234242433,
                "username": "asdasdad"
            }
        ]
    }''',
    long_description_content_type='text/markdown',
    url='https://github.com/auzuha/instant_json_server',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
