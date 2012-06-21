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
Version: 2535
Release: 1.8%{?dist}
License: Intel Proprietary
Group: System/Libraries
ExclusiveArch: %{ix86}
URL: http://edc.intel.com/Software/Downloads/EMGD/
BuildRoot: %{_tmppath}/%{name}-%{version}-build

Source0: %{name}-%{version}.tar.bz2
Source1: license.txt
Source2: readme.txt
Source3: emgd-cb.conf
Source4: emgd-rv.conf
Source5: emgd-bin.init
Source6: emgd-bin.service

Provides: libPVRScopeServices.so
Conflicts: mesa-libEGL mesa-libGLESv1 mesa-libGLESv2 mesa-libOpenVG pvr-bin-mrst pvr-bin-oaktrail pvr-bin-cdv
#Requires: xorg-x11-server-Xorg
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
EMGD runtime graphics libraries


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
mkdir -p $RPM_BUILD_ROOT/usr/libexec/

install -m 644 -D %{SOURCE1} $RPM_BUILD_ROOT%{_docdir}/%{name}/license.txt
install -m 644 -D %{SOURCE2} $RPM_BUILD_ROOT%{_docdir}/%{name}/readme.txt
install -m 644 -D %{SOURCE3} $RPM_BUILD_ROOT%{_docdir}/%{name}/emgd-cb.conf
install -m 644 -D %{SOURCE4} $RPM_BUILD_ROOT%{_docdir}/%{name}/emgd-rv.conf
install -m 755 -D %{SOURCE5} $RPM_BUILD_ROOT/usr/libexec/emgd-bin.init
install -m 755 -D %{SOURCE6} $RPM_BUILD_ROOT/lib/systemd/system/emgd-bin.service

install -m 644 -D powervr.ini $RPM_BUILD_ROOT/etc/powervr.ini
install -m 644 -D emgd.4.gz $RPM_BUILD_ROOT%{_mandir}/man4/

install -m 755 emgd_drv.so $RPM_BUILD_ROOT%{_libdir}/xorg/modules/drivers/emgd_drv.so

mkdir -p $RPM_BUILD_ROOT/%{_libdir}/dri/

install -m 755 emgd_dri.so $RPM_BUILD_ROOT%{_libdir}/dri/emgd_dri.so
install -m 755 emgd_drv_video.so $RPM_BUILD_ROOT%{_libdir}/dri/emgd_drv_video.so

install -m 755 libEMGD2d.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/libEMGD2d.so.%{libversion}
install -m 755 libGLES_CM.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/libGLES_CM.so.%{libversion}
install -m 755 libGLESv2.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/libGLESv2.so.%{libversion}
install -m 755 libOpenVG.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/libOpenVG.so.%{libversion}
install -m 755 libOpenVGU.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/libOpenVGU.so.%{libversion}
install -m 755 libEMGDegl.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/libEMGDegl.so.%{libversion}
install -m 755 libEGL.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/libEGL.so.%{libversion}
install -m 755 libEMGDOGL.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/libEMGDOGL.so.%{libversion}
install -m 755 libEMGDScopeServices.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/libEMGDScopeServices.so.%{libversion}
install -m 755 libemgdsrv_init.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/libemgdsrv_init.so.%{libversion}
install -m 755 libemgdsrv_um.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/libemgdsrv_um.so.%{libversion}
install -m 755 libemgdglslcompiler.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/libemgdglslcompiler.so.%{libversion}
install -m 755 libemgdPVR2D_DRIWSEGL.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/libemgdPVR2D_DRIWSEGL.so.%{libversion}

install -m 755 libgbm.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/libgbm.so.%{libversion}
install -m 755 libwayland-egl.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/libwayland-egl.so.%{libversion}
install -m 755 libemgdPVR2D_WAYLANDWSEGL.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/libemgdPVR2D_WAYLANDWSEGL.so.%{libversion}
install -m 755 libemgdPVR2D_GBMWSEGL.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/libemgdPVR2D_GBMWSEGL.so.%{libversion}
install -m 755 libva.so.%{libversion} $RPM_BUILD_ROOT%{_libdir}/libva.so.%{libversion}


#
# Development pkgconfig - GLES2, EGL, gbm
#
install -m 644 -D pkgconfig/egl.pc $RPM_BUILD_ROOT/usr/lib/pkgconfig/egl.pc
install -m 644 -D pkgconfig/glesv2.pc $RPM_BUILD_ROOT/usr/lib/pkgconfig/glesv2.pc
install -m 644 -D pkgconfig/gbm.pc $RPM_BUILD_ROOT/usr/lib/pkgconfig/gbm.pc
install -m 644 -D pkgconfig/glesv1_cm.pc $RPM_BUILD_ROOT/usr/lib/pkgconfig/glesv1_cm.pc
install -m 644 -D pkgconfig/vg.pc $RPM_BUILD_ROOT/usr/lib/pkgconfig/vg.pc
install -m 644 -D pkgconfig/wayland-egl.pc $RPM_BUILD_ROOT/usr/lib/pkgconfig/wayland-egl.pc

#
# Development headers - EGL
#
install -m 644 -D EGL/egl.h $RPM_BUILD_ROOT/usr/include/EGL/egl.h
install -m 644 -D EGL/eglext.h $RPM_BUILD_ROOT/usr/include/EGL/eglext.h
install -m 644 -D EGL/eglplatform.h $RPM_BUILD_ROOT/usr/include/EGL/eglplatform.h
ln -s -f /usr/lib/libEGL.so.1 $RPM_BUILD_ROOT/usr/lib/libEGL.so

#
# Development headers - GLES1
#
install -m 644 -D GLES/glext.h $RPM_BUILD_ROOT/usr/include/GLES/glext.h
install -m 644 -D GLES/gl.h $RPM_BUILD_ROOT/usr/include/GLES/gl.h
install -m 644 -D GLES/glplatform.h $RPM_BUILD_ROOT/usr/include/GLES/glplatform.h
ln -s -f /usr/lib/libGLES_CM.so.1 $RPM_BUILD_ROOT/usr/lib/libGLES_CM.so

#
# Development headers - GLES2
#
install -m 644 -D GLES2/gl2ext.h $RPM_BUILD_ROOT/usr/include/GLES2/gl2ext.h
install -m 644 -D GLES2/gl2.h $RPM_BUILD_ROOT/usr/include/GLES2/gl2.h
install -m 644 -D GLES2/gl2platform.h $RPM_BUILD_ROOT/usr/include/GLES2/gl2platform.h
ln -s -f /usr/lib/libGLESv2.so.2 $RPM_BUILD_ROOT/usr/lib/libGLESv2.so

#
# Development headers - Khronos platform
#
install -m 644 -D KHR/khrplatform.h $RPM_BUILD_ROOT/usr/include/KHR/khrplatform.h

#
# Development headers - OpenVG
#
install -m 644 -D VG/openvg.h $RPM_BUILD_ROOT/usr/include/VG/openvg.h
install -m 644 -D VG/vgext.h $RPM_BUILD_ROOT/usr/include/VG/vgext.h
install -m 644 -D VG/vgplatform.h $RPM_BUILD_ROOT/usr/include/VG/vgplatform.h
install -m 644 -D VG/vgu.h $RPM_BUILD_ROOT/usr/include/VG/vgu.h
ln -s -f /usr/lib/libOpenVG.so.1 $RPM_BUILD_ROOT/usr/lib/libOpenVG.so
ln -s -f /usr/lib/libOpenVGU.so.1 $RPM_BUILD_ROOT/usr/lib/libOpenVGU.so

#
# Development headers - Wayland
#
install -m 644 -D wayland/gbm.h $RPM_BUILD_ROOT/usr/include/gbm.h
ln -s -f /usr/lib/libgbm.so.1 $RPM_BUILD_ROOT/usr/lib/libgbm.so
ln -s -f /usr/lib/libwayland-egl.so.1 $RPM_BUILD_ROOT/usr/lib/libwayland-egl.so


pushd $RPM_BUILD_ROOT%{_libdir}
ln -s libEMGDScopeServices.so.%{libversion} libPVRScopeServices.so
ln -s libemgdPVR2D_GBMWSEGL.so.%{libversion} libemgdPVR2D_GBMWSEGL.so
ln -s libva.so.%{libversion} libva.so.1.0.12

# These three should technically be in a separate -devel package rather
# than here.  Let ldconfig create all of our other symlinks; no need
# to do so here.
ln -s -f libEGL.so.1 libEGL.so
ln -s -f libGLESv2.so.2 libGLESv2.so
ln -s -f libGLES_CM.so.1 libGLES_CM.so
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
#/sbin/chkconfig --add emgd-bin
#/sbin/chkconfig --levels 345 emgd-bin on
#/sbin/chkconfig --levels 0126 emgd-bin off

mkdir -p /lib/systemd/system/sysinit.target.wants/
pushd /lib/systemd/system/sysinit.target.wants/
ln -sf ../emgd-bin.service emgd-bin.service
popd

if [ -x /bin/systemctl ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
    /bin/systemctl start emgd-bin.service > /dev/null 2>&1 || :
fi

%postun
/sbin/ldconfig
rm -f /lib/systemd/system/sysinit.target.wants/emgd-bin.service
if [ -x /bin/systemctl ]; then
    systemctl daemon-reload >/dev/null 2>&1 || :
fi


%preun
if [ -x /bin/systemctl ]; then
    sytemctl stop emgd-bin.service >/dev/null 2>&1 || :
fi


%files
%defattr(-,root,root,-)
%{_docdir}/%{name}/license.txt
%{_docdir}/%{name}/readme.txt
%{_docdir}/%{name}/emgd-*.conf
%config(noreplace) /etc/powervr.ini
%doc %{_mandir}/man4/emgd*

%{_libdir}/xorg/modules/drivers/emgd_drv.so
%{_libdir}/libEMGD2d.so.%{libversion}
%{_libdir}/libEMGDOGL.so.%{libversion}
%{_libdir}/libPVRScopeServices.so
%{_libdir}/libEMGDScopeServices.so.%{libversion}
%{_libdir}/libemgdsrv_um.so.%{libversion}
%{_libdir}/libemgdsrv_init.so.%{libversion}
%{_libdir}/libemgdglslcompiler.so.%{libversion}
%{_libdir}/libGLES_CM.so
%{_libdir}/libGLES_CM.so.%{libversion}
%{_libdir}/libGLESv2.so
%{_libdir}/libGLESv2.so.%{libversion}
%{_libdir}/libOpenVG.so.%{libversion}
%{_libdir}/libOpenVGU.so.%{libversion}
%{_libdir}/libEMGDegl.so.%{libversion}
%{_libdir}/libEGL.so
%{_libdir}/libEGL.so.%{libversion}
%{_libdir}/libemgdPVR2D_DRIWSEGL.so.%{libversion}
%{_libdir}/dri/emgd_dri.so
%{_libdir}/dri/emgd_drv_video.so
%{_libdir}/libemgdPVR2D_WAYLANDWSEGL.so.%{libversion}
%{_libdir}/libwayland-egl.so.%{libversion}
%{_libdir}/libgbm.so.%{libversion}
%{_libdir}/libemgdPVR2D_GBMWSEGL.so.%{libversion}
%{_libdir}/libemgdPVR2D_GBMWSEGL.so
%{_libdir}/libva.so.%{libversion}
%{_libdir}/libva.so.1.0.12

#%{_initddir}/emgd-bin
/usr/libexec/emgd-bin.init
/lib/systemd/system/emgd-bin.service

%files devel
%defattr(-,root,root,-)
%{_includedir}/GLES2/gl2.h
%{_includedir}/GLES2/gl2platform.h
%{_includedir}/GLES2/gl2ext.h
%{_includedir}/EGL/eglplatform.h
%{_includedir}/EGL/egl.h
%{_includedir}/EGL/eglext.h
%{_includedir}/KHR/khrplatform.h
%{_includedir}/VG/openvg.h
%{_includedir}/VG/vgext.h
%{_includedir}/VG/vgplatform.h
%{_includedir}/VG/vgu.h
%{_includedir}/GLES/gl.h
%{_includedir}/GLES/glplatform.h
%{_includedir}/GLES/glext.h
%{_includedir}/gbm.h
%{_libdir}/libEGL.so
%{_libdir}/libGLES_CM.so
%{_libdir}/libGLESv2.so
%{_libdir}/libOpenVG.so
%{_libdir}/libOpenVGU.so
%{_libdir}/libgbm.so
%{_libdir}/libwayland-egl.so
%{_libdir}/pkgconfig/egl.pc
%{_libdir}/pkgconfig/gbm.pc
%{_libdir}/pkgconfig/glesv1_cm.pc
%{_libdir}/pkgconfig/glesv2.pc
%{_libdir}/pkgconfig/vg.pc
%{_libdir}/pkgconfig/wayland-egl.pc
