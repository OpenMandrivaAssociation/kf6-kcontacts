%define major %(echo %{version} |cut -d. -f1-2)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname KF6Contacts
%define devname %mklibname KF6Contacts -d
#define git 20240217

Name: kf6-kcontacts
Version: 6.11.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/kcontacts/-/archive/master/kcontacts-master.tar.bz2#/kcontacts-%{git}.tar.bz2
%else
Source0: https://download.kde.org/%{stable}/frameworks/%{major}/kcontacts-%{version}.tar.xz
%endif
Summary: Library for working with contact information
URL: https://invent.kde.org/frameworks/kcontacts
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: gettext
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6Codecs)
Requires: %{libname} = %{EVRD}
BuildSystem: cmake
BuildOption: -DBUILD_QCH:BOOL=ON
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Library for working with contact information

%package -n %{libname}
Summary: Library for working with contact information
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Library for working with contact information

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Library for working with contact information

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kcontacts.*

%files -n %{devname}
%{_includedir}/KF6/KContacts
%{_libdir}/cmake/KF6Contacts
%{_qtdir}/doc/KF6Contacts.*

%files -n %{libname}
%{_libdir}/libKF6Contacts.so*
%{_qtdir}/qml/org/kde/contacts
