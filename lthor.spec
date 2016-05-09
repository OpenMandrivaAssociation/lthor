Name:		lthor
Summary:	Flashing tool for Tizen lunchbox
Version:	1.4
Release:	4
Group:		Development/Other
License:	Apache
URL:		https://download.tizendev.org/tools/lthor/
Source0:	%{name}_%{version}.tar.gz

BuildRequires:	pkgconfig(libarchive)
BuildRequires:	cmake

Requires:	udev

%description
Tool for downloading binaries from a Linux host PC to a target phone.
It uses a USB cable as a physical communication medium.
It is prerequisite that the boot-loader should support download protocol
which is compatible with 'lthor'.

%prep 
%setup -q

%build
%cmake
%make

%install
%makeinstall_std -C build

%files
#% dir %{_sysconfdir}/udev
#% dir %{_sysconfdir}/udev/rules.d
%{_bindir}/%{name}
%{_sysconfdir}/udev/rules.d/*.rules
