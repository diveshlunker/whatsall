from distutils.core import setup
setup(
  name = 'whatsall',         
  packages = ['whatsall'],   
  version = '0.0.4',      
  license='MIT',        
  description = 'Automate sending messages on whatsapp to n number of users without even saving the number',   
  author = 'Divesh Lunker',             
  author_email = 'diveshdj92@gmail.com',      
  url = 'https://github.com/diveshlunker/whatsall',
  download_url = 'https://github.com/diveshlunker/whatsall/archive/0.0.4.tar.gz',   
  keywords = ['whatsapp', 'automated messaging', 'whatsapp web','whatspip'], 
  install_requires=[ 
          "selenium"
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
