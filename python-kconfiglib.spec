#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-kconfiglib
Version  : 14.1.0
Release  : 123
URL      : https://github.com/ulfalizer/Kconfiglib/archive/v14.1.0/Kconfiglib-14.1.0.tar.gz
Source0  : https://github.com/ulfalizer/Kconfiglib/archive/v14.1.0/Kconfiglib-14.1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : HPND
Requires: python-kconfiglib-bin = %{version}-%{release}
Requires: python-kconfiglib-license = %{version}-%{release}
Requires: python-kconfiglib-python = %{version}-%{release}
Requires: python-kconfiglib-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
.. contents:: Table of contents
:backlinks: none
News
----
Dependency loop with recent linux-next kernels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
%setup -q -n Kconfiglib-14.1.0
cd %{_builddir}/Kconfiglib-14.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583212576
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-kconfiglib
cp %{_builddir}/Kconfiglib-14.1.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/python-kconfiglib/864f15fbb4dcd073bbe20eb3c0b839a45b8902ab
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
/usr/bin/defconfig
/usr/bin/genconfig
/usr/bin/guiconfig
/usr/bin/listnewconfig
/usr/bin/menuconfig
/usr/bin/oldconfig
/usr/bin/olddefconfig
/usr/bin/savedefconfig
/usr/bin/setconfig

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-kconfiglib/864f15fbb4dcd073bbe20eb3c0b839a45b8902ab

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
