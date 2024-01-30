from setuptools import setup, find_packages



with open("README.md", "r", encoding="utf-8") as readme_file:
    readme = readme_file.read()


setup(
  name='vimeworld',
  version='0.0.1',
  author='xtraswed',
  author_email='xtraswed@gmail.com',
  description='SDK для работы с API VimeWorld',
  long_description=readme,
  long_description_content_type='text/markdown',
  url='https://github.com/xtraswed/vimeworld',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='vimeworld VimeWorld Vimeworld vimeWorld xtraswed Xtraswed minecraft api sdk SDK',
  project_urls={
    'GitHub': 'https://github.com/xtraswed'
  },
  python_requires='>=3.8'
)