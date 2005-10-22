Summary:	xmh application
Summary(pl):	Aplikacja xmh
Name:		xorg-app-xmh
Version:	0.99.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/app/xmh-%{version}.tar.bz2
# Source0-md5:	113b6584263ef09f16e2a320cbd4c93f
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
# for dir (only?)
Requires:	xorg-data-xbitmaps
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xmh application.

%description -l pl
Aplikacja xmh.

%prep
%setup -q -n xmh-%{version}

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
	DESTDIR=$RPM_BUILD_ROOT \
	appmandir=%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_libdir}/X11/app-defaults/*
%{_includedir}/X11/bitmaps/*
%{_mandir}/man1/*.1x*
