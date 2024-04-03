%global optflags %{optflags} -O3

Summary:	X server that runs under Wayland
Name:		xwayland
Version:	23.2.5
Release:	1
License:	MIT
Group:		System/X11
Url:		http://www.x.org
Source0:	https://www.x.org/releases/individual/xserver/%{name}-%{version}.tar.xz
BuildRequires:	meson
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-protocols)
%ifnarch %{armx} riscv64
BuildRequires:	pkgconfig(wayland-eglstream-protocols)
%endif
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
BuildRequires:	pkgconfig(libxcvt)
BuildRequires:	pkgconfig(epoxy)
BuildRequires:	pkgconfig(dri)
BuildRequires:	pkgconfig(gbm)
BuildRequires:	pkgconfig(libtirpc)
Requires:	x11-server-common
Requires:	dri-drivers
Requires:	%{_lib}EGL1
Obsoletes:	x11-server-xwayland < 21.0.99.901
Provides:	x11-server-xwayland = 21.0.99.901

%description
This package provides an X server running on top of wayland,
using wayland input devices for input and forwarding either
the root window or individual top-level windows as wayland
surfaces.

%package devel
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{name} = %{EVRD}

%description devel
Development files and headers for %{name}.

%prep
%autosetup -p1

%build
%meson \
	-Dglamor=true \
	-Ddri3=true \
	-Dsha1=libgcrypt \
%ifnarch %{armx} riscv64
	-Dxwayland_eglstream=true \
%else
	-Dxwayland_eglstream=false \
%endif
	-Dbuilder_addr="%{disturl}" \
	-Dbuilder_string="Build ID: %{name} %{version}-%{release}" \
	-Dvendor_name="%{vendor}" \
	-Dvendor_name_short="%{distsuffix}" \
	-Dvendor_web="%{bugurl}" \
	-Dxkb_dir="%{_datadir}/X11/xkb" \
	-Dxkb_output_dir="%{_localstatedir}/lib/xkb" \
	-Ddefault_font_path="catalogue:%{_sysconfdir}/X11/fontpath.d,built-ins" \
	-Dxselinux=false \
	-Dxcsecurity=true

%meson_build

%install
%meson_install

# (tpg) remove useless files
rm -rf %{buildroot}%{_mandir}/man1/Xserver.1*
rm -rf %{buildroot}%{_libdir}/xorg
rm -Rf %{buildroot}%{_includedir}/xorg
rm -Rf %{buildroot}%{_datadir}/aclocal
rm -Rf %{buildroot}%{_localstatedir}/lib/xkb

%files
%{_bindir}/Xwayland
%{_datadir}/applications/*.desktop
%doc %{_mandir}/man1/Xwayland.1*

%files devel
%optional %doc %{_docdir}/xorg-server/Xserver-DTrace.*
%{_libdir}/pkgconfig/xwayland.pc
