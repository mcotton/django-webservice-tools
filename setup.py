from setuptools import setup, find_packages

setup(
    name='django-webservice-tools',
    version=__import__('webservice_tools').__version__,
    description='A generic toolbox for building webservices',
    author='Joel Semar',
    license='MIT',
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=False, # because we're including media that Django needs
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)