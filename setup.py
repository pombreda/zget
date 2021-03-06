import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name='zget',

        version="0.5",

        description='Zeroconf based peer to peer file transfer',
        long_description="""Simply transfer a file using

.. code:: bash

    $ zput file.zip

on the sender and

.. code:: bash

    $ zget file.zip

on the receiver.

Done.""",

        author='Nils Werner',
        author_email='nils.werner@gmail.com',
        url='https://github.com/nils-werner/zget',

        license='MIT',

        packages=setuptools.find_packages(),

        install_requires=[
            'zeroconf',
        ],

        extras_require={
            'docs': [
                'sphinx',
                'sphinxcontrib-napoleon',
                'sphinx_rtd_theme',
                'numpydoc',
            ],
            'tests': [
                'pytest',
                'pytest-cov',
                'pytest-pep8',
            ],
        },

        tests_require=[
            'pytest',
            'pytest-cov',
            'pytest-pep8',
        ],

        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'License :: OSI Approved :: MIT License',
            'Topic :: Communications :: File Sharing',
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Utilities',
        ],

        entry_points={'console_scripts': [
            'zget=zget.get:get',
            'zput=zget.put:put'
        ]},
    )
