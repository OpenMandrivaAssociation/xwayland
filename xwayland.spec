Summary:	X server that runs under Wayland
Name:		xwayland
Version:	21.1.1
Release:	2
License:	MIT
Group:		System/X11
Url:		http://www.x.org
Source0:	https://www.x.org/releases/individual/xserver/%{name}-%{version}.tar.xz

# (tpg) patches from upstream
Patch1:		0001-xwayland-Move-dmabuf-interface-to-common-glamor-code.patch
Patch2:		0002-xwayland-move-formats-and-modifiers-functions-to-com.patch
Patch3:		0003-xwayland-Add-check_flip-glamor-backend-function.patch
Patch4:		0004-xwayland-implement-pixmap_from_buffers-for-the-eglst.patch
Patch5:		0005-xwayland-eglstream-fix-X11-rendering-to-flipping-GL-.patch
Patch6:		0006-xwayland-eglstream-Check-buffer-creation.patch
Patch7:		0007-xwayland-Check-buffer-prior-to-attaching-it.patch
Patch8:		0008-glamor-Dump-backtrace-on-GL-error.patch
Patch9:		0009-xwayland-glamor-Add-return-status-to-post_damage.patch
Patch10:	0010-xwayland-eglstream-Check-framebuffer-status.patch
Patch11:	0011-xwayland-eglstream-Small-refactoring.patch
Patch12:	0012-xwayland-eglstream-Add-more-error-checking.patch
Patch13:	0013-xwayland-eglstream-Dissociate-pending-stream-from-wi.patch
Patch14:	0014-xwayland-eglstream-Keep-a-reference-to-the-pixmap.patch
Patch15:	0015-xwayland-eglstream-Drop-the-list-of-pending-streams.patch
Patch16:	0016-xwayland-eglstream-Do-not-commit-without-surface.patch
Patch17:	0017-xwayland-eglstream-Fix-calloc-malloc.patch
Patch18:	0018-xwayland-eglstream-Check-eglSwapBuffers.patch
Patch19:	0019-xwayland-eglstream-Do-not-always-increment-pixmap-re.patch
Patch20:	0020-xwayland-eglstream-Set-ALU-to-GXCopy-for-blitting.patch
Patch21:	0021-xwayland-eglstream-allow-commits-to-dma-buf-backed-p.patch
Patch22:	0022-xwayland-eglstream-flush-stream-after-eglSwapBuffers.patch
Patch23:	0023-xwayland-Add-preferred-GLVND-vendor-to-xwl_screen.patch
Patch24:	0024-xwayland-eglstream-Use-nvidia-for-GLVND.patch
Patch25:	0025-xwayland-eglstream-Log-when-GL_OES_EGL_image-is-miss.patch
Patch26:	0026-glx-don-t-create-implicit-GLXWindow-if-one-already-e.patch
Patch27:	0027-glx-Set-ContextTag-for-all-contexts.patch

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
	-Dxwayland_eglstream=true \
	-Dbuilder_addr="%{disturl}" \
	-Dbuilder_string="Build ID: %{name} %{version}-%{release}" \
	-Dvendor_name="%{vendor}" \
	-Dvendor_name_short="%{distsuffix}" \
	-Dvendor_web="%{bugurl}" \
	-Dxkb_dir="%{_datadir}/X11/xkb" \
	-Dxkb_output_dir="%{_localstatedir}/lib/xkb" \
	-Ddefault_font_path="catalogue:%{_sysconfdir}/X11/fontpath.d,built-ins"

%meson_build

%install
%meson_install

# (tpg) remove useless files
rm -rf %{buildroot}%{_mandir}/man1/Xserver.1*
rm -rf %{buildroot}%{_libdir}/xorg

%files
%{_bindir}/Xwayland
%{_mandir}/man1/Xwayland.1*

%files devel
%{_libdir}/pkgconfig/xwayland.pc
