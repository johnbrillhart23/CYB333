from setuptools import setup, find_packages

setup(
    name='failed-login-attempt-monitor',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A monitor and notifier for failed login attempts on Windows systems.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pywin32',
        # Add other dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: Microsoft :: Windows',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)