# Copyright © 2002-2011, Intel Corporation.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms and conditions of the GNU General Public License,
# version 2, as published by the Free Software Foundation.
#
# This program is distributed in the hope it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin St - Fifth Floor, Boston, MA 02110-1301 USA.
#----------------------------------------------------------------------------

#Just for now until the libs are ran using gcc rather than ld.
#This causes the omission of --build-id which causes debuginfo
#generation to puke.

%define debug_package %{nil}
%define libversion 1.5.15.3226

Name: emgd-bin
Summary: Intel EMGD graphics driver
Version: 2667
Release: 1.8%{?dist}
License: Intel Proprietary
Group: System/Libraries
ExclusiveArch: %{ix86}
URL: http://edc.intel.com/Software/Downloads/EMGD/
BuildRoot: %{_tmppath}/%{name}-%{version}-build

Source0: %{name}-%{version}.tar.bz2
Source1: emgd-bin.init
Source2: emgd-bin.service

%description
EMGD runtime graphics libraries

%package common
Summary: Common Intel EMGD graphics driver
Provides: libPVRScopeServices.so
Conflicts: mesa-libEGL mesa-libGLESv1 mesa-libGLESv2 mesa-libOpenVG pvr-bin-mrst pvr-bin-oaktrail pvr-bin-cdv
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description common
Common EMGD runtime graphics libraries

%package x
Summary: Special X libraries
Group: System/Libraries
Requires: pciutils
Requires: %{name}-common

%description x
Special X libraries

%package devel
Summary: EMGD development headers
Group: Development/Libraries
Conflicts: mesa-libEGL-devel mesa-libGLESv1-devel mesa-libGLESv2-devel mesa-libOpenVG-devel mesa-libgbm-devel

%description devel
Development headers needed to build applications against EMGD libraries.
Khronos API headers and Wayland headers are provided.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_libdir}/xorg/modules/drivers/
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man4/
mkdir -p $RPM_BUILD_ROOT/lib/systemd/system/
mkdir -p $RPM_BUILD_ROOT/usr/lib/pkgconfig/
mkdir -p $RPM_BUILD_ROOT/usr/libexec/
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}/

install -m 644 -D usr/share/doc/emgd/license.txt $RPM_BUILD_ROOT%{_docdir}/%{name}/
install -m 644 -D usr/share/doc/emgd/readme.txt $RPM_BUILD_ROOT%{_docdir}/%{name}/
install -m 644 -D usr/share/doc/emgd/emgd-cb.conf $RPM_BUILD_ROOT%{_docdir}/%{name}/
install -m 644 -D usr/share/doc/emgd/emgd-rv.conf $RPM_BUILD_ROOT%{_docdir}/%{name}/
install -m 755 -D %{SOURCE1} $RPM_BUILD_ROOT/usr/libexec/emgd-bin.init
install -m 755 -D %{SOURCE2} $RPM_BUILD_ROOT/usr/lib/systemd/system/emgd-bin.service

install -m 644 -D etc/powervr.ini $RPM_BUILD_ROOT/etc/powervr.ini
install -m 644 -D usr/share/man/man4/emgd.4.gz $RPM_BUILD_ROOT%{_mandir}/man4/

mkdir -p $RPM_BUILD_ROOT%{_libdir}/dri/
pushd usr/lib
install -m 755 xorg/modules/drivers/emgd_drv.so $RPM_BUILD_ROOT%{_libdir}/xorg/modules/drivers/
install -m 755 dri/emgd_dri.so $RPM_BUILD_ROOT%{_libdir}/dri/
install -m 755 dri/emgd_drv_video.so $RPM_BUILD_ROOT%{_libdir}/dri/
install -m 755 libEMGD2d.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/
install -m 755 libGLES_CM.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/
install -m 755 libGLESv2.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/
install -m 755 libOpenVG.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/
install -m 755 libOpenVGU.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/
install -m 755 libEMGDegl.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/
install -m 755 libEGL.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/
install -m 755 libEMGDOGL.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/
install -m 755 libEMGDScopeServices.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/
install -m 755 libemgdsrv_init.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/
install -m 755 libemgdsrv_um.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/
install -m 755 libemgdglslcompiler.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/
install -m 755 libemgdPVR2D_DRIWSEGL.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/
install -m 755 libgbm.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/
install -m 755 libwayland-egl.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/
install -m 755 libwayland-emgd.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/
install -m 755 libemgdPVR2D_WAYLANDWSEGL.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/
install -m 755 libemgdPVR2D_GBMWSEGL.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/
install -m 755 libva.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/
#
# Development pkgconfig - GLES2, EGL, gbm
#
install -m 644 -D pkgconfig/egl.pc $RPM_BUILD_ROOT/usr/lib/pkgconfig/egl.pc
install -m 644 -D pkgconfig/glesv2.pc $RPM_BUILD_ROOT/usr/lib/pkgconfig/glesv2.pc
install -m 644 -D pkgconfig/gbm.pc $RPM_BUILD_ROOT/usr/lib/pkgconfig/gbm.pc
install -m 644 -D pkgconfig/glesv1_cm.pc $RPM_BUILD_ROOT/usr/lib/pkgconfig/glesv1_cm.pc
install -m 644 -D pkgconfig/vg.pc $RPM_BUILD_ROOT/usr/lib/pkgconfig/vg.pc
install -m 644 -D pkgconfig/wayland-egl.pc $RPM_BUILD_ROOT/usr/lib/pkgconfig/wayland-egl.pc
popd

pushd usr/include
#
# Development headers - EGL
#
install -m 644 -D EGL/egl.h $RPM_BUILD_ROOT/usr/include/EGL/egl.h
install -m 644 -D EGL/eglext.h $RPM_BUILD_ROOT/usr/include/EGL/eglext.h
install -m 644 -D EGL/eglplatform.h $RPM_BUILD_ROOT/usr/include/EGL/eglplatform.h

#
# Development headers - GLES1
#
install -m 644 -D GLES/glext.h $RPM_BUILD_ROOT/usr/include/GLES/glext.h
install -m 644 -D GLES/gl.h $RPM_BUILD_ROOT/usr/include/GLES/gl.h
install -m 644 -D GLES/glplatform.h $RPM_BUILD_ROOT/usr/include/GLES/glplatform.h

#
# Development headers - GLES2
#
install -m 644 -D GLES2/gl2ext.h $RPM_BUILD_ROOT/usr/include/GLES2/gl2ext.h
install -m 644 -D GLES2/gl2.h $RPM_BUILD_ROOT/usr/include/GLES2/gl2.h
install -m 644 -D GLES2/gl2platform.h $RPM_BUILD_ROOT/usr/include/GLES2/gl2platform.h

#
# Development headers - Khronos platform
#
install -m 644 -D KHR/khrplatform.h $RPM_BUILD_ROOT/usr/include/KHR/khrplatform.h

#
# Development headers - Wayland
#
install -m 644 -D gbm.h $RPM_BUILD_ROOT/usr/include/gbm.h

#
# Development headers - OpenVG
#
install -m 644 -D VG/openvg.h $RPM_BUILD_ROOT/usr/include/VG/openvg.h
install -m 644 -D VG/vgext.h $RPM_BUILD_ROOT/usr/include/VG/vgext.h
install -m 644 -D VG/vgplatform.h $RPM_BUILD_ROOT/usr/include/VG/vgplatform.h
install -m 644 -D VG/vgu.h $RPM_BUILD_ROOT/usr/include/VG/vgu.h
popd
pushd $RPM_BUILD_ROOT%{_libdir}
ln -s -f libEMGDOGL.so.%{libversion} libEMGDOGL.so.1
ln -s -f libEMGDOGL.so.%{libversion} libEMGDOGL.so
ln -s -f libemgdsrv_init.so.%{libversion} libemgdsrv_init.so.1
ln -s -f libemgdsrv_init.so.%{libversion} libemgdsrv_init.so
ln -s -f libemgdsrv_um.so.%{libversion} libemgdsrv_um.so.1
ln -s -f libemgdsrv_um.so.%{libversion} libemgdsrv_um.so
ln -s -f libemgdglslcompiler.so.%{libversion} libemgdglslcompiler.so.1
ln -s -f libemgdglslcompiler.so.%{libversion} libemgdglslcompiler.so
ln -s -f libemgdPVR2D_DRIWSEGL.so.%{libversion} libemgdPVR2D_DRIWSEGL.so.1
ln -s -f libemgdPVR2D_DRIWSEGL.so.%{libversion} libemgdPVR2D_DRIWSEGL.so
ln -s -f libemgdPVR2D_WAYLANDWSEGL.so.%{libversion} libemgdPVR2D_WAYLANDWSEGL.so.1
ln -s -f libemgdPVR2D_WAYLANDWSEGL.so.%{libversion} libemgdPVR2D_WAYLANDWSEGL.so
ln -s -f libEMGD2d.so.%{libversion} libEMGD2d.so.1
ln -s -f libEMGD2d.so.%{libversion} libEMGD2d.so
ln -s -f libOpenVG.so.%{libversion} libOpenVG.so.1
ln -s -f libOpenVG.so.%{libversion} libOpenVG.so
ln -s -f libOpenVGU.so.%{libversion} libOpenVGU.so.1
ln -s -f libOpenVGU.so.%{libversion} libOpenVGU.so
ln -s -f libGLESv2.so.%{libversion} libGLESv2.so.2
ln -s -f libGLESv2.so.%{libversion} libGLESv2.so
ln -s -f libGLES_CM.so.%{libversion} libGLES_CM.so.1
ln -s -f libGLES_CM.so.%{libversion} libGLES_CM.so
ln -s -f libEGL.so.%{libversion} libEGL.so.1
ln -s -f libEGL.so.%{libversion} libEGL.so
ln -s -f libEMGDegl.so.%{libversion} libEMGDegl.so.1
ln -s -f libEMGDegl.so.%{libversion} libEMGDegl.so
ln -s -f libgbm.so.%{libversion} libgbm.so.1
ln -s -f libgbm.so.%{libversion} libgbm.so
ln -s -f libwayland-egl.so.%{libversion} libwayland-egl.so.1
ln -s -f libwayland-egl.so.%{libversion} libwayland-egl.so
ln -s -f libwayland-emgd.so.%{libversion} libwayland-emgd.so.1
ln -s -f libwayland-emgd.so.%{libversion} libwayland-emgd.so
ln -s -f libEMGDScopeServices.so.%{libversion} libPVRScopeServices.so
ln -s -f libemgdPVR2D_GBMWSEGL.so.%{libversion} libemgdPVR2D_GBMWSEGL.so
ln -s -f libva.so.%{libversion} libva.so.1.0.12
ln -s -f libva.so.%{libversion} libva.so.1
ln -s -f libva.so.%{libversion} libva.so
popd


%clean
rm -rf $RPM_BUILD_ROOT

%post
# Kind of a hack, but RPM doesn't seem to remove the old libraries until after
# we've installed the new ones, so ldconfig will see the old libraries
# (which had an incorrect SONAME) and use them to overwrite our development
# symlinks, then remove the old libraries they were pointing at.
rm -f /usr/lib/libGLES_CM.so.1.1.*
rm -f /usr/lib/libGLESv2.so.1.1.*
rm -f /usr/lib/libEGL.so.1.1.*

/sbin/ldconfig

mkdir -p /usr/lib/systemd/system/sysinit.target.wants/
pushd /usr/lib/systemd/system/sysinit.target.wants/
ln -sf ../emgd-bin.service emgd-bin.service
popd

if [ -x /bin/systemctl ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
    /bin/systemctl start emgd-bin.service > /dev/null 2>&1 || :
fi

%postun
/sbin/ldconfig
rm -f /usr/lib/systemd/system/sysinit.target.wants/emgd-bin.service
if [ -x /bin/systemctl ]; then
    systemctl daemon-reload >/dev/null 2>&1 || :
fi


%preun
if [ -x /bin/systemctl ]; then
    sytemctl stop emgd-bin.service >/dev/null 2>&1 || :
fi


%files common
%defattr(-,root,root,-)
%{_docdir}/%{name}/license.txt
%{_docdir}/%{name}/readme.txt
%doc %{_mandir}/man4/emgd*
%config(noreplace) /etc/powervr.ini
%{_libdir}/dri/*
%{_libdir}/lib*

%files x
%defattr(-,root,root,-)
%{_libdir}/xorg/*
%{_docdir}/%{name}/emgd-*.conf
/usr/libexec/emgd-bin.init
%{_libdir}/systemd/system/emgd-bin.service

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/libEGL.so
%{_libdir}/libGLES_CM.so
%{_libdir}/libGLESv2.so
%{_libdir}/libOpenVG.so
%{_libdir}/libOpenVGU.so
%{_libdir}/libgbm.so
%{_libdir}/libwayland-egl.so
%{_libdir}/pkgconfig/*
