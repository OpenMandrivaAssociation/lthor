Name:		lthor
Summary:	Flashing tool for Tizen lunchbox
Version:	1.4
Release:	9
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
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build

%files
#% dir %{_sysconfdir}/udev
#% dir %{_sysconfdir}/udev/rules.d
%{_bindir}/%{name}
%{_sysconfdir}/udev/rules.d/*.rules
