setup(
    name='my-python-app',
    version='0.1.10',
    packages=find_packages(),
    install_requires=[
        'flask'
    ],
    entry_points={
        'console_scripts': [
            'myapp = my_app.main:main'
        ]
    }
)
