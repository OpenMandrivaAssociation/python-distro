%define module	distro
%define _python_bytecompile_build 0
  
Summary:	Python library for getting information about Linux distros
Name:		python-distro
Version:	1.3.0
Release:	1
Group:		Development/Python
License:	Python
Url:		https://pypi.python.org/pypi/distro
Source0:	https://files.pythonhosted.org/packages/source/d/distro/distro-%{version}.tar.gz
BuildArch:	noarch 
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python3)
 
%description 
A much more elaborate, renewed alternative implementation for Python's
platform.linux_distribution()

%prep
%setup -qn %{module}-%{version}
  
%install 
PYTHONDONTWRITEBYTECODE= %__%py_install --record=FILE_LIST

%files -f FILE_LIST
