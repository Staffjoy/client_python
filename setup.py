from distutils.core import setup

setup(
    name = "staffjoy",
    packages = ["staffjoy"],
    version = "0.1",
    description = "Staffjoy API Wrapper in Python",
    author = "Philip Thomas",
    author_email = "help@staffjoy.com",
    url = "https://github.com/staffjoy/client_python",
    download_url = "https://github.com/staffjoy/client_python/Tarball/0.1",  # TODO - how does tarball get generated?
    keywords = ["staffjoy-api", "staffjoy", "staff joy"],
    install_requires = [
        "requests[security]"
    ]
)
