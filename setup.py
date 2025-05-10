from setuptools import setup, find_packages

setup(
    name="metatemplating",
    version="1.0.0",
    description="A Python templating engine for dynamic text generation.",
    author="guanxiaohan",
    author_email="guanxiaohan84@gmail.com",
    url="https://github.com/你的GitHub账户/MetaTemplating",
    license="MIT",
    packages=find_packages(),
    install_requires=["uuid", "pprint", "json", "re"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.11",
)