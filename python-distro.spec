%define module	distro
%define _python_bytecompile_build 0
  
Summary:	Python library for getting information about Linux distros
Name:		python-distro
Version:	1.9.0
Release:	1
Group:		Development/Python
License:	Python
Url:		https://github.com/nir0s/distro
Source0:	https://files.pythonhosted.org/packages/source/d/%{module}/%{module}-%{version}.tar.gz
BuildArch:	noarch 
BuildRequires:	python%{pyver}dist(setuptools)
BuildSystem:	python
 
%description 
A much more elaborate, renewed alternative implementation for Python's
platform.linux_distribution()

%files
%doc *.md
%{_bindir}/distro
%license LICENSE
%{python_sitelib}/%{module}-*.egg-info/
%{python_sitelib}/%{module}
