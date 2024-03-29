from setuptools import setup

setup(
    name='Sandbox-Pelican',
    version='0.1',
    include_package_data=True,
    install_requires=[
        'Click',
        'docker-py',
        'dockerpty'
    ],
    entry_points={
        'console_scripts': [
            'sandbox=rout:sandbox'
        ]
    },
)
