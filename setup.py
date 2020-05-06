import setuptools

with open("README.md", 'r') as fh:
    long_description = fh.read()

with open("requirements.txt", 'r') as fh:
    requirements = fh.read().split('\n')

setuptools.setup(
    name="bee-racers",
    version="0.0.1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rewolf93/bee-racers",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
    include_package_data=True,
)
