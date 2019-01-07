from setuptools import setup
def readme():
    with open('README.rst') as f:
        return f.read()
    
setup(name='dsconnect',
      version='0.0.1',
      description='Power your data connections with python',
      long_description=readme(),
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='MySQL, MS SQL Server, MS Azure SQL Database, Oracle, IBM-DB, PostgreSQL, Redshift, GSheets, download-url, SFTP, Pandas, CSV, JSON',        
      url='http://github.com/nit567esh/dsconnect',
      author='Nitesh Kumar',
      author_email='nit567esh@gmail.com',
      license='MIT',
      packages=['dsconnect'],
      install_requires=['pandas', 'psycopg2', 'pyodbc', 'pygsheets', 'pysftp','boto3', 'mysql-connector-python', 'cx_Oracle', 'ibm_db'],
      include_package_data=True,      
      zip_safe=False)