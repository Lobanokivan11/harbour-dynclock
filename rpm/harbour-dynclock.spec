Name:          harbour-dynclock
Version:       0.5.6
Release:       1
Summary:       Dynamic clock icon that changes with the hour
Group:         System/Tools
Vendor:        fravaccaro
Distribution:  SailfishOS
Requires:      sailfish-version >= 5.0.0
Packager:      fravaccaro <fravaccaro@jollacommunity.it>
URL:           https://www.jollacommunity.it
License:       GPLv3+

%description
DynClock changes the clock icon on your Sailfish OS device according to the current hour.

%prep
# No prep needed for this package

%build
# No build needed for this package

%install
mkdir -p %{buildroot}/usr/share/harbour-dynclock
mkdir -p %{buildroot}/usr/share/applications
mkdir -p %{buildroot}/etc/systemd/system
cp -r * %{buildroot}/usr/share/harbour-dynclock/

%files
%defattr(-,root,root,-)
/usr/share/harbour-dynclock/
/etc/systemd/system/harbour-dynclock.service
/etc/systemd/system/harbour-dynclock.timer

%post
chmod +x %{_datadir}/harbour-dynclock/*.sh
install -Dm644 %{_datadir}/harbour-dynclock/harbour-dynclock.service %{_sysconfdir}/systemd/system/
install -Dm644 %{_datadir}/harbour-dynclock/harbour-dynclock.timer %{_sysconfdir}/systemd/system/
mkdir -p %{_datadir}/harbour-dynclock/images
%{_datadir}/harbour-dynclock/harbour-dynclock.sh
systemctl daemon-reload
systemctl enable --now harbour-dynclock.timer
systemctl enable --now harbour-dynclock.service

%preun
%{_datadir}/harbour-dynclock/harbour-dynclock-uninstall.sh

%postun
if [ $1 -eq 0 ]; then
    # Uninstall
    systemctl disable --now harbour-dynclock.timer
    systemctl disable --now harbour-dynclock.service
    rm -f %{_sysconfdir}/systemd/system/harbour-dynclock.timer
    rm -f %{_sysconfdir}/systemd/system/harbour-dynclock.service
    rm -rf %{_datadir}/harbour-dynclock
else
    # Upgrade
    %{_datadir}/harbour-dynclock/harbour-dynclock.sh
    systemctl daemon-reload
    systemctl restart harbour-dynclock.timer
    systemctl restart harbour-dynclock.service
fi

%changelog
* Fri Feb 27 2026 0.5.6
- Updated for Sailfish OS 5.x compatibility
- Modernized spec file and systemd handling

* Fri Jul 7 2017 0.5.5
- Bug fix.

* Tue Jul 4 2017 0.5.4
- Bug fix.

* Thu Jan 5 2017 0.5.3
- Bug fix.

* Thu Sep 29 2016 0.5.2
- Black icon fixed.

* Sat Sep 24 2016 0.5.1
- Icon jumping to the bottom of the app tray may be fixed.

* Tue Jan 19 2016 0.5.0
- Sailfish OS 2.0.7 support.

* Tue Jan 19 2016 0.4.0
- High resolution support added.

* Thu Oct 8 2015 0.3.0
- Clock style updated.

* Wed Oct 7 2015 0.2.1
- Icon jumping to the bottom of the app tray may be fixed.

* Tue Sep 29 2015 0.2
- Bugfix.

* Mon Sep 28 2015 0.1
- First build.
