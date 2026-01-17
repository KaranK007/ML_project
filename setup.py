from setuptools import find_packages, setup



HYPHEN_E_DOT = '-e .'
def get_requirements(str) :
    ''' returns the list of requirements '''

    with open(str) as file:
        return file.readlines().remove(HYPHEN_E_DOT)

setup(
    name = "mlproject",
    version = "0.0.1",
    author = "Karan",
    author_email = "Kukreti.karan@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt'),
)