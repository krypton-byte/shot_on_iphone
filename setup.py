from setuptools import setup
from os import path
base_dir = path.abspath(path.dirname(__file__))
setup(
  name = 'shot_on_iphone',        
  packages = ['shot_on_iphone'],
  long_description=open(base_dir+'/README.md','r').read(),
  long_description_content_type='text/markdown',
  include_package_data=True,
  version = '0.2',    
  license='MIT',     
  description = 'Iphone Meme Maker', 
  author = 'Krypton Byte',                  
  author_email = 'galaxyvplus6434@gmail.com',     
  url = 'https://github.com/krypton-byte/shot_on_iphone',   
  download_url = 'https://github.com/krypton-byte/shot_on_iphone/archive/0.2.tar.gz',    
  keywords = ['Iphone', 'Meme', 'generator','Maker'], 
  install_requires=[           
          'moviepy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)