from distutils.core import setup
setup(
  name = 'Topsis_Ira_102017029',         # How you named your package folder (MyLib)
  packages = ['Topsis_Ira_102017029'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'TOPSIS Package',   # Give a short description about your library
  author = 'Ira Vashisht',                   # Type in your name
  author_email = 'iravashisht2002@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/ira20022/Topsis_Ira_102017029',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/ira20022/Topsis_Ira_102017029/archive/refs/tags/0.1.tar.gz',    # I explain this later on
  keywords = ['TOPSIS', 'MCDM', '102017029'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
          'pandas',
          'sys',
          'os',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
