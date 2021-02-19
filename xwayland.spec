Summary:	X server that runs under Wayland
Name:		xwayland
Version:	21.0.99.901
Release:	1
License:	MIT
Group:		System/X11
Url:		http://www.x.org
Source0:	https://www.x.org/releases/individual/xserver/%{name}-%{version}.tar.xz
BuildRequires:	meson
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	pkgconfig(wayland-eglstream-protocols)
Requires:	x11-server-common
Obsoletes:	x11-server-xwayland < 21.0.99.901
Provides:	x11-server-xwayland = 21.0.99.901

%description
This package provides an X server running on top of wayland,
using wayland input devices for input and forwarding either
the root window or individual top-level windows as wayland
surfaces.

%package -n devel
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{name} = %{EVRD}

%description -n devel
Development files and headers for %{name}.

%prep
%autosetup -p1

%build
%meson
%meson_build


%install
%meson_install

%files
%{_bindir}/Xwayland
%{_mandir}/man1/Xwayland.1*

%files -n devel
%{_libdir}/pkgconfig/xwayland.pc
