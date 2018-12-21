from setuptools import setup

setup(
    name='ium',
    packages=['ium/server','ium/database','ium/mqtt-client'],
    include_package_data=True,
    install_requires=[
        'flask',
        'paho-mqtt'
    ],
)

