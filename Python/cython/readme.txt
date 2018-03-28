error: Unable to find vcvarsall.bat
Execute the following command based on the version of Visual Studio installed:

    Visual Studio 2010 (VS10): SET VS90COMNTOOLS=%VS100COMNTOOLS%
    Visual Studio 2012 (VS11): SET VS90COMNTOOLS=%VS110COMNTOOLS%
    Visual Studio 2013 (VS12): SET VS90COMNTOOLS=%VS120COMNTOOLS%
    Visual Studio 2015 (VS14): SET VS90COMNTOOLS=%VS140COMNTOOLS%
See Building lxml for Python 2.7 on Windows for details.