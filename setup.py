from setuptools import setup, find_packages

version = "0.18"
setup(name="staffjoy",
      packages=find_packages(),
      version=version,
      description="Staffjoy API Wrapper in Python",
      author="Philip Thomas",
      author_email="help@staffjoy.com",
      license="MIT",
      url="https://github.com/staffjoy/client_python",
      download_url="https://github.com/StaffJoy/client_python/archive/%s.tar.gz" % version,
      keywords=["staffjoy-api", "staffjoy", "staff joy"],
      install_requires=["requests[security]"], )
