from setuptools import setup, find_packages



setup(
    name='my-python-app',
    version=__version__,
    packages=find_packages(),
    install_requires=[],  # Add dependencies here if needed
    entry_points={
        'console_scripts': [
            'myapp = my_app.main:main'
        ]
    }
)
