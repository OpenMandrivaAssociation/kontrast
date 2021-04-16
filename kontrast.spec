%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name:		kontrast
Summary:	Contrast checker
Version:	21.04.0
Release:	1
License:	GPLv3
URL:		https://kde.org/applications/cs/kontrast
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Declarative)

%description
A tool that helps UI designers find colors with sufficient contrast.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang kontrast

%files -f kontrast.lang
%{_bindir}/kontrast
%{_datadir}/applications/org.kde.kontrast.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.kde.kontrast.svg
%{_datadir}/metainfo/org.kde.kontrast.appdata.xml
