#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-kconfiglib
Version  : 10.19.0
Release  : 37
URL      : https://github.com/ulfalizer/Kconfiglib/archive/v10.19.0.tar.gz
Source0  : https://github.com/ulfalizer/Kconfiglib/archive/v10.19.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : ISC
Requires: python-kconfiglib-bin = %{version}-%{release}
Requires: python-kconfiglib-license = %{version}-%{release}
Requires: python-kconfiglib-python = %{version}-%{release}
Requires: python-kconfiglib-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
.. contents:: Table of contents
:backlinks: none
Overview
--------
Kconfiglib is a `Kconfig
<https://www.kernel.org/doc/Documentation/kbuild/kconfig-language.txt>`__
implementation in Python 2/3. It started out as a helper library, but now has a
enough functionality to also work well as a standalone Kconfig implementation
(including `menuconfig interfaces <Menuconfig interfaces_>`_ and `Kconfig extensions`_).

%package bin
Summary: bin components for the python-kconfiglib package.
Group: Binaries
Requires: python-kconfiglib-license = %{version}-%{release}

%description bin
bin components for the python-kconfiglib package.


%package license
Summary: license components for the python-kconfiglib package.
Group: Default

%description license
license components for the python-kconfiglib package.


%package python
Summary: python components for the python-kconfiglib package.
Group: Default
Requires: python-kconfiglib-python3 = %{version}-%{release}

%description python
python components for the python-kconfiglib package.


%package python3
Summary: python3 components for the python-kconfiglib package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-kconfiglib package.


%prep
%setup -q -n Kconfiglib-10.19.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541071772
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-kconfiglib
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/python-kconfiglib/LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
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
/usr/bin/olddefconfig

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-kconfiglib/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
