#define git 20240218
#define gitbranch release/24.02
#define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name:		plasma6-kontrast
Summary:	Contrast checker
Version:	24.12.0
Release:	%{?git:0.%{git}.}1
License:	GPLv3
URL:		https://kde.org/applications/cs/kontrast
%if 0%{?git:1}
Source0:	https://invent.kde.org/accessibility/kontrast/-/archive/%{gitbranch}/kontrast-%{gitbranchd}.tar.bz2#/kontrast-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kontrast-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlCore)
BuildRequires:  cmake(Qt6QmlNetwork)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(QCoro6)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6KirigamiAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(FutureSQL6)

%description
A tool that helps UI designers find colors with sufficient contrast.

%prep
%autosetup -p1 -n kontrast-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang kontrast --with-html

%files -f kontrast.lang
%{_bindir}/kontrast
%{_datadir}/applications/org.kde.kontrast.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.kde.kontrast.svg
%{_datadir}/metainfo/org.kde.kontrast.appdata.xml
