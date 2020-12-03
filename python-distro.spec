%define module	distro
%define _python_bytecompile_build 0
  
Summary:	Python library for getting information about Linux distros
Name:		python-distro
Version:	1.5.0
Release:	3
Group:		Development/Python
License:	Python
Url:		https://pypi.python.org/pypi/distro
Source0:	https://github.com/nir0s/distro/archive/v%{version}.tar.gz
BuildArch:	noarch 
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python3)
 
%description 
A much more elaborate, renewed alternative implementation for Python's
platform.linux_distribution()

%prep
%setup -qn %{module}-%{version}
  
# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%py_build

%install
%py_install

%files
%doc *.md
%license LICENSE
%{python_sitelib}/%{module}-*.egg-info/
%{python_sitelib}/%{module}.py
#{python_sitelib}/__pycache__/%{module}.*
