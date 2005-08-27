Summary:	xmh application
Summary(pl):	Aplikacja xmh
Name:		xorg-app-xmh
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/xmh-%{version}.tar.bz2
# Source0-md5:	161faf9cfb9cca5fa044fd835ab96c11
Patch0:		xmh-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkgconfig >= 0.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xmh application.

%description -l pl
Aplikacja xmh.

%prep
%setup -q -n xmh-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/X11/app-defaults/*
%attr(755,root,root) %{_bindir}/*
%{_includedir}/X11/bitmaps/*
%{_mandir}/man1/*.1*
