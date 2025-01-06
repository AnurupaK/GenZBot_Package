from setuptools import setup, find_packages

with open("README.md", "r",encoding='utf-8') as fh:
    long_description = fh.read()
    
setup(
    name='GenZBot',
    version='0.8',
    author='Anurupa Karmakar and Vishnu Kumar',
    author_email='anurupakarmakar.dgp18@gmail.com',
    maintainer='Anurupa Karmakar',
    maintainer_email='anurupakarmakar.dgp18@gmail.com',
    packages=find_packages(), 
    package_data={'': ['Images_list/*']},
    include_package_data=True,
    description='GenZBot is a beginner-friendly Python package designed to provide hands-on experience in building AI chatbots from scratch. With support for multiple LLMs and customizable options for behavior and design, it simplifies chatbot development while introducing essential concepts for GenAI projects.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent"
    ],
)