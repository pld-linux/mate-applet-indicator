#
# Conditional build:
%bcond_with	gtk3		# use GTK+ 3.x instead of 2.x
#
Summary:	Small applet to display information from various applications consistently in the panel
Summary(pl.UTF-8):	Mały aplet do spójnego wyświetlania w panelu informacji od różnych aplikacji
Name:		mate-applet-indicator
Version:	1.14.1
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://pub.mate-desktop.org/releases/1.14/mate-indicator-applet-%{version}.tar.xz
# Source0-md5:	92ee2f8e1cb5495d8206c3223ec3e764
URL:		http://mate-desktop.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-tools >= 0.10.40
BuildRequires:	glib2-devel >= 2.0
%{!?with_gtk3:BuildRequires:	gtk+2-devel >= 2:2.24}
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.0}
BuildRequires:	intltool >= 0.35.0
%{!?with_gtk3:BuildRequires:	libindicator-devel >= 0.4}
%{?with_gtk3:BuildRequires:	libindicator-gtk3-devel >= 0.4}
BuildRequires:	libtool >= 1:1.4.3
BuildRequires:	mate-panel-devel
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
%{!?with_gtk3:Requires:	gtk+2 >= 2:2.24}
%{?with_gtk3:Requires:	gtk+3 >= 3.0}
Requires:	hicolor-icon-theme
Requires:	mate-panel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/mate-panel

%description
The indicator applet exposes Ayatana Indicators in the MATE Panel.
Ayatana Indicators are an initiative by Canonical to provide crisp and
clean system and application status indication. They take the form of
an icon and associated menu, displayed (usually) in the desktop panel.
Existing indicators include the Message Menu, Battery Menu and Sound
menu.

MATE Indicator Applet is a fork of Indicator Applet for GNOME
(<https://launchpad.net/indicator-applet>).

%description -l pl.UTF-8
Aplet indicator uwidacznia wskaźniki Ayatana w panelu MATE. Wskaźniki
Ayatana (Ayatana Indicators) to inicjatywa Canonical mająca na celu
zapewnienie świeżych i przejrzystych wskazań dotyczących stanu systemu
i aplikacji. Mają postać ikony i związanego z nią menu, wyświetlanych
(zwykle) w panelu pulpitu. Istniejące wskaźniki obejmują menu
komunikatów, menu baterii oraz menu dźwięku.

MATE Indicator Applet to odgałęzienie pakietu Indicator Applet dla
GNOME (<https://launchpad.net/indicator-applet>).

%prep
%setup -q -n mate-indicator-applet-%{version}

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{?with_gtk3:--with-gtk=3.0}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{frp,jv}

%find_lang mate-indicator-applet

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f mate-indicator-applet.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libexecdir}/mate-indicator-applet
%attr(755,root,root) %{_libexecdir}/mate-indicator-applet-appmenu
%attr(755,root,root) %{_libexecdir}/mate-indicator-applet-complete
%{_datadir}/dbus-1/services/org.mate.panel.applet.IndicatorApplet*.service
%{_datadir}/mate-panel/applets/org.ayatana.panel.IndicatorApplet*.mate-panel-applet
%{_iconsdir}/hicolor/scalable/apps/mate-indicator-applet.svg
