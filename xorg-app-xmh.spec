Summary:	xmh application - send and read mail with an X interface to MH
Summary(pl.UTF-8):	Aplikacja xmh - czytanie i wysyłanie poczty poprzez interfejs X do MH
Name:		xorg-app-xmh
Version:	1.0.5
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/xmh-%{version}.tar.xz
# Source0-md5:	9708ee1127647cde2ee82313c2a26d12
Patch0:		%{name}-man.patch
Patch1:		%{name}-format.patch
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-data-xbitmaps >= 1.1.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.3.0
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
Requires:	xorg-lib-libXt >= 1.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xmh application provides a graphical user interface to the MH
Message Handling System. To actually do things with your mail, it
makes calls to the MH package.

%description -l pl.UTF-8
Aplikacja xmh udostępnia graficzny interfejs do systemu poczty
MH (Message Handling System). Właściwe operacje na poczcie są
wykonywane poprzez odwołania do pakietu MH.

%prep
%setup -q -n xmh-%{version}
%patch0 -p1
%patch1 -p1

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
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/xmh
%{_datadir}/X11/app-defaults/Xmh
%{_mandir}/man1/xmh.1*
