from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="yolov8_inference",
    version="1.0.0",
    packages=find_packages(),
    install_requires=requirements,
    description="Vehicle YoloV8 Inference",
    url="",
    author=["Haikal Ardikatama"],
    author_email=["ardikatamah@gmail.com"]
)
