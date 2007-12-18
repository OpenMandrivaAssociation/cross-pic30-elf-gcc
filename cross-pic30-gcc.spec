%define name		cross-pic30-elf-gcc
%define version		3.3.mplab.2.01
%define release		%mkrel 2

Summary:	GNU Compiler Collection
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Other
URL:		http://ww1.microchip.com/downloads/en/DeviceDoc/mplabc30v2_01.tgz
Source0:	mplabc30v2_01.tar.bz2
BuildRequires:	byacc gcc gettext texinfo dos2unix
Patch0:		pic30-gcc-makefile-in.diff.bz2
Patch1:		pic30-gcc-t-pic30.diff.bz2
Patch2:		pic30-gcc-pic30-standard-prefix.diff.bz2
Patch3:		pic30-gcc-gcc4-fix.diff.bz2
 
%description
Microchip gcc cross compiler for dsPICs.

%prep
%setup -q -n gcc-3.3
find . -type f -exec dos2unix '{}' ';'
%patch0 -p0 -b .makefile-in
%patch1 -p1 -b .t-pic30
%patch2 -p1 -b .pic30-standard-prefix
%patch3 -b .gcc4
%build
cd gcc-3.3
CC="gcc-`gcc4.1-version` -DMCHP_VERSION=2.01 -O2" ./configure --target=pic30-elf --prefix=%{_prefix} --enable-languages=c
%make tooldir=%{_prefix} all

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_prefix}
cd gcc-3.3
%makeinstall_std
rm -rf $RPM_BUILD_ROOT%{_prefix}/lib/gcc-lib/pic30-elf/install-tools
mv $RPM_BUILD_ROOT%{_prefix}/lib/gcc-lib $RPM_BUILD_ROOT%{_prefix}/lib/gcc
ln -s %{_bindir}/pic30-elf-gcc $RPM_BUILD_ROOT%{_bindir}/pic30-elf-cc
mkdir -p $RPM_BUILD_ROOT%{_prefix}/share
mv $RPM_BUILD_ROOT%{_prefix}/man $RPM_BUILD_ROOT%{_prefix}/share

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man?/*
%{_prefix}/lib/gcc/*

