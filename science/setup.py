from setuptools import setup

setup(name='YourAppName', version='1.0',
      description='OpenShift Python-2.7 Community Cartridge based application',
      author='Your Name', author_email='ramr@example.org',
      url='http://www.python.org/sigs/distutils-sig/',

      #  Uncomment one or more lines below in the install_requires section
      #  for the specific client drivers/modules your application needs.
      install_requires=['greenlet', 'gevent', 'Django==1.5.2',
                            'Pillow==2.0.0',
                            'South==0.8.2',
                            'django-json-field==0.5.4',
                            'django-mptt==0.6.0',
                            'django-registration==1.0',
                            
                            'python-dateutil==2.1',
                            'six==1.3.0',

                        
                        #  'MySQL-python',
                        #  'pymongo',
                        #  'psycopg2',
      ],
     )
