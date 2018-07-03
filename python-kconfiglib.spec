#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-kconfiglib
Version  : 6.0.1
Release  : 6
URL      : https://github.com/ulfalizer/Kconfiglib/archive/v6.0.1.tar.gz
Source0  : https://github.com/ulfalizer/Kconfiglib/archive/v6.0.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : ISC
Requires: python-kconfiglib-bin
Requires: python-kconfiglib-python3
Requires: python-kconfiglib-python
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools
Patch1: 0001-fix-read-utf8-file.patch

%description
.. contents:: Table of contents
:backlinks: none
Overview
--------
Kconfiglib is a `Kconfig
<https://www.kernel.org/doc/Documentation/kbuild/kconfig-language.txt>`_
implementation in Python 2/3. It started out as a helper library, but now has a
enough functionality to work well as a standalone Kconfig implementation
(including ``menuconfig`` implementations).

%package bin
Summary: bin components for the python-kconfiglib package.
Group: Binaries

%description bin
bin components for the python-kconfiglib package.


%package python
Summary: python components for the python-kconfiglib package.
Group: Default
Requires: python-kconfiglib-python3

%description python
python components for the python-kconfiglib package.


%package python3
Summary: python3 components for the python-kconfiglib package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-kconfiglib package.


%prep
%setup -q -n Kconfiglib-6.0.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1528775564
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/alldefconfig
/usr/bin/allmodconfig
/usr/bin/allnoconfig
/usr/bin/allyesconfig
/usr/bin/genconfig
/usr/bin/menuconfig
/usr/bin/oldconfig

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
