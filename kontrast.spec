Name:		kontrast
Summary:	Contrast checker
Version:	1.0.0
Release:	1
License:	GPLv3
Source0:	https://download.kde.org/stable/kontrast/%{name}-%{version}.tar.xz

%description
A tool that helps UI designers find colors with sufficient contrast

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
