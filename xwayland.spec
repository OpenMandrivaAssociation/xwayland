Summary:	X server that runs under Wayland
Name:		xwayland
Version:	21.0.99.901
Release:	1
License:	MIT
Group:		System/X11
Url:		http://www.x.org
Source0:	https://www.x.org/releases/individual/xserver/%{name}-%{version}.tar.xz
BuildRequires:	meson
BuildRequires:	cmake
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	pkgconfig(wayland-eglstream-protocols)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xtrans)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(pixman-1)
BuildRequires:	pkgconfig(xshmfence)
BuildRequires:	pkgconfig(xkbfile)
BuildRequires:	pkgconfig(xkbcomp)
BuildRequires:	pkgconfig(xfont2)
BuildRequires:	pkgconfig(libbsd)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(epoxy)
BuildRequires:	pkgconfig(dri)
BuildRequires:	pkgconfig(gbm)
BuildRequires:	pkgconfig(libtirpc)
Requires:	x11-server-common
Requires:	dri-drivers
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
%meson \
	-Dglamor=true \
	-Ddri3=true \
	-Dsha1=libgcrypt \
	-Dxwayland_eglstream=true \
	-Dbuilder_addr="%{disturl}" \
	-Dbuilder_string="Build ID: %{name} %{version}-%{release}" \
	-Dvendor_name="%{vendor}" \
	-Dvendor_name_short="%{distsuffix}" \
	-Dvendor_web="%{bugurl}" \
	-Dxkb_output_dir=%{_localstatedir}/lib/xkb \
	-Ddefault_font_path="catalogue:%{_sysconfdir}/X11/fontpath.d,built-ins"

%meson_build

%install
%meson_install

%files
%{_bindir}/Xwayland
%{_mandir}/man1/Xwayland.1*

%files -n devel
%{_libdir}/pkgconfig/xwayland.pc
