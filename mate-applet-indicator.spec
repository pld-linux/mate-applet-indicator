Summary:	Small applet to display information from various applications consistently in the panel
Summary(pl.UTF-8):	Mały aplet do spójnego wyświetlania w panelu informacji od różnych aplikacji
Name:		mate-applet-indicator
Version:	1.26.0
Release:	2
License:	GPL v3
Group:		X11/Applications
Source0:	https://pub.mate-desktop.org/releases/1.26/mate-indicator-applet-%{version}.tar.xz
# Source0-md5:	6db4d42a268fb17ed7587fbb54f60c0d
URL:		http://mate-desktop.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	ayatana-ido-devel >= 0.4.0
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	libayatana-indicator-gtk3-devel >= 0.6.0
BuildRequires:	libtool >= 1:1.4.3
BuildRequires:	mate-panel-devel >= 1.17.0
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires:	ayatana-ido >= 0.4.0
Requires:	gtk+3 >= 3.22
Requires:	hicolor-icon-theme
Requires:	libayatana-indicator-gtk3 >= 0.6.0
Requires:	mate-panel >= 1.17.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# use the same libexecdir as mate-panel
# (better solution: store mate-panel libexecdir in libmatepanelapplet-*.pc and read it here)
%define		matepanel_libexecdir	%{_libexecdir}/mate-panel

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
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--libexecdir=%{matepanel_libexecdir} \
	--disable-silent-rules \
	--with-ayatana-indicators

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# es_ES,ku_IQ,ur_PK are outdated versions of es,ku,ur; the rest not supported by glibc
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{es_ES,frp,ie,jv,ku_IQ,nqo,pms,ur_PK,zh-Hans}

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
%attr(755,root,root) %{matepanel_libexecdir}/mate-indicator-applet
%attr(755,root,root) %{matepanel_libexecdir}/mate-indicator-applet-appmenu
%attr(755,root,root) %{matepanel_libexecdir}/mate-indicator-applet-complete
%{_datadir}/dbus-1/services/org.mate.panel.applet.IndicatorApplet*.service
%{_datadir}/mate-panel/applets/org.mate.applets.Indicator*.mate-panel-applet
%{_iconsdir}/hicolor/scalable/apps/mate-indicator-applet.svg
