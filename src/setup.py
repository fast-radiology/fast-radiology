import setuptools

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lines = (line.strip() for line in open(filename))
    return [line for line in lines if line and not line.startswith("#")]

requirements = parse_requirements('requirements.txt')

setuptools.setup(
    name="fast-radiology",
    setup_cfg=True,
    install_requires=requirements,
    packages=["fast_radiology"],
    package_dir={"fast_radiology": "fast_radiology"},
)
