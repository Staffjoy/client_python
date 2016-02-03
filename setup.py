from setuptools import setup

setup(name="staffjoy",
      packages=["staffjoy"],
      version="0.3",
      description="Staffjoy API Wrapper in Python",
      author="Philip Thomas",
      author_email="help@staffjoy.com",
      license="MIT",
      url="https://github.com/staffjoy/client_python",
      download_url="https://github.com/StaffJoy/client_python/archive/0.3.tar.gz",
      keywords=["staffjoy-api", "staffjoy", "staff joy"],
      install_requires=["requests[security]"], )
