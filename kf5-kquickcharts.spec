%define		kdeframever	5.88
%define		qtver		5.15.0
%define		kfname		kquickcharts

Summary:	Plugin for beautiful and interactive charts
Name:		kf5-%{kfname}
Version:	5.88.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	47514d2c5e84f715fa3f14f4d5104e55
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt Quick plugin for beautiful and interactive charts.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/qt5/qml/org/kde/quickcharts
%dir %{_libdir}/qt5/qml/org/kde/quickcharts/controls
%dir %{_libdir}/qt5/qml/org/kde/quickcharts/controls/styles
%dir %{_libdir}/qt5/qml/org/kde/quickcharts/controls/styles/org.kde.desktop
%{_libdir}/qt5/qml/org/kde/quickcharts/controls/libchartscontrolsplugin.so
%{_libdir}/qt5/qml/org/kde/quickcharts/controls/styles/org.kde.desktop/Theme.qml
%{_libdir}/qt5/qml/org/kde/quickcharts/controls/qmldir
%{_libdir}/qt5/qml/org/kde/quickcharts/controls/Theme.qml
%{_libdir}/qt5/qml/org/kde/quickcharts/controls/PieChartControl.qml
%{_libdir}/qt5/qml/org/kde/quickcharts/controls/LegendDelegate.qml
%{_libdir}/qt5/qml/org/kde/quickcharts/controls/LineChartControl.qml
%{_libdir}/qt5/qml/org/kde/quickcharts/controls/Legend.qml
%{_libdir}/qt5/qml/org/kde/quickcharts/controls/Logging.qml
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/quickcharts/libQuickCharts.so
%{_libdir}/qt5/qml/org/kde/quickcharts/qmldir
%{_datadir}/qlogging-categories5/kquickcharts.categories

%files devel
%defattr(644,root,root,755)
# %{_includedir}/KF5/kqtquickcharts_version.h
%{_libdir}/cmake/KF5QuickCharts
