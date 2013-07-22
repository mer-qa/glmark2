Name:           glmark2
Summary:        Wayland GL ES2 performance test tool
Version:        2012.12.20130722
Release:        1
Group:          Development/Tools
License:        GPLv3 and MIT
Source0:        %{name}-%{version}.tar.gz
URL:            http://code.launchpad.net/glmark2
BuildRequires:  mesa-llvmpipe-libGL-devel
BuildRequires:  mesa-llvmpipe-libEGL-devel
BuildRequires:  mesa-llvmpipe-libGLESv2-devel
BuildRequires:  pkgconfig(libpng)
BuildRequires:  python
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  mesa-llvmpipe-libwayland-egl-devel
BuildRequires:  libxkbcommon-devel

%description
 A benchmark for OpenGL (ES) 2.0. It uses only the subset of the
 OpenGL 2.0 API that is compatible with OpenGL ES 2.0.

%prep
%setup -q

%build
cd glmark2
./waf configure --with-flavors=wayland-glesv2 --prefix=/usr
./waf

%install
cd glmark2
rm -rf %{buildroot}
./waf install --destdir=%{buildroot}

%files
%defattr(-,root,root,-)
%doc glmark2/COPYING glmark2/COPYING.SGI glmark2/NEWS
%doc /usr/share/man/man1/glmark2-es2-wayland.1.gz
/usr/bin/glmark2-es2-wayland
/usr/share/glmark2/models/*
/usr/share/glmark2/shaders/*
/usr/share/glmark2/textures/*
