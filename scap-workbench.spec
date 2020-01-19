# Somehow, _pkgdocdir is already defined and points to unversioned docs dir
# RHEL 7.X uses versioned docs dir, hence the definition below
%global _pkgdocdir %{_docdir}/%{name}-%{version}

Name:       scap-workbench
Version:    1.1.6
Release:    1%{?dist}
Summary:    Scanning, tailoring, editing and validation tool for SCAP content

License:    GPLv3+
URL:        http://www.open-scap.org/tools/scap-workbench
Source0:    https://github.com/OpenSCAP/scap-workbench/releases/download/%{version}/scap-workbench-%{version}.tar.bz2
Group:      System Environment/Base

BuildRequires:  cmake >= 2.6
BuildRequires:  qt-devel >= 4.0.0

BuildRequires:  openscap-devel >= 1.2.0
BuildRequires:  openscap-utils >= 1.2.0
Requires:       openscap-utils >= 1.2.0
# to show number of selected rules in (default) profile and avoid segfaults
# see https://github.com/OpenSCAP/scap-workbench/pull/98 for more info
Requires:       openscap       >= 1.2.13
# ssh to scan remote machines
BuildRequires:  openssh-clients
Requires:       openssh-clients
Requires:       openssh-askpass
# because of 'setsid' which we use to force ssh to use GUI askpass
BuildRequires:  util-linux
Requires:       util-linux
# for privileged local scanning
Requires:       polkit
# default content
Requires:       scap-security-guide
# fonts, see https://bugzilla.redhat.com/show_bug.cgi?id=1134418
Requires:       font(:lang=en)

%description
scap-workbench is GUI tool that provides scanning functionality for SCAP
content. The tool is based on OpenSCAP library.

%prep
%setup -q

%build
%cmake -D CMAKE_INSTALL_DOCDIR=%{_pkgdocdir} .
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/scap-workbench
%{_datadir}/applications/scap-workbench.desktop
%{_datadir}/scap-workbench/*.png
%{_datadir}/scap-workbench/translations/*
%{_libexecdir}/scap-workbench-oscap.sh
%{_libexecdir}/scap-workbench-pkexec-oscap.sh
%{_libexecdir}/scap-workbench-rpm-extract.sh
%{_datadir}/polkit-1/actions/scap-workbench-oscap.policy
%{_datadir}/pixmaps/scap-workbench.png
%{_datadir}/pixmaps/scap-workbench.svg
%{_datadir}/appdata/scap-workbench.appdata.xml
%doc %{_mandir}/man8/scap-workbench.8.gz
%doc %{_pkgdocdir}/user_manual.html
%doc %{_pkgdocdir}/COPYING
%doc %{_pkgdocdir}/README.md

%changelog
* Fri Nov 10 2017 Martin Preisler <mpreisle@redhat.com> 1.1.6-1
- Updated to new upstream release 1.1.6
- Tri-state checkboxes for tailoring
- Fixed remote host and port being cleared when scan starts
- Fiixed formating of Profile html description in Tailoring Window
- Fixed oscap message "Downloading ... ok" appearing as an error
- Fixed tab order of widgets in main window
- Load Content as the default button of the SSG integration dialog
- New validation of the customization file name
- Generate bash and Ansible remediation roles from profiles
- Generate bash and Ansible remediation roles from results after scanning
- Fixed a short integer overflow when using ssh port numbers higher than 32k
- Fixed long loading times on OSX
- Open tailoring file directly via command line

* Thu Jun 01 2017 Wesley Ceraso Prudencio <wcerasop@redhat.com> - 1.1.4-5
- Fixes resources downloading message bug

* Fri Feb 10 2017 Watson Sato <wsato@redhat.com> 1.1.4-4
- Fix dependency on OpenSCAP library

* Thu Feb 09 2017 Watson Sato <wsato@redhat.com> 1.1.4-3
- Set dependency on OpenSCAP to version 1.2.13 or later

* Mon Feb 06 2017 Watson Sato <wsato@redhat.com> 1.1.4-2
- Place docs in versioned docs dir

* Fri Feb 03 2017 Watson Sato <wsato@redhat.com> 1.1.4-1
- Updated to new upstream release 1.1.4 (rhbz#1404394)
- UX improvements
- Fixed fetch remote resources warning (rhbz#1367923)
- Improved error message when scanning a remote machine in which openscap-scanner
  is not installed (rhbz#1368463)
- Fixed search on disabled item (rhbz#1368493)
- Fixed multi benchmark tailoring use case
- Fixed a bug that caused tailored profiles to have titles duplicated (rhbz#1320197)
- Fixed path of tailoring file in dry run output (rhbz#1368516)
- Now Workbench doesn't allow edit of values with prohibitedChanges attribute
- Added --version and --help command line options (rhbz#1368527)
- Improved workflow of dry run execution (rhbz#1385549)
- Check capabilities of oscap with propper arguments (rhbz#1368463)
- Show number of selected rules in profile listing

* Mon Jun 20 2016 Martin Preisler <mpreisle@redhat.com> 1.1.2-1
- Updated to new upstream release 1.1.2

* Thu Mar 17 2016 Martin Preisler <mpreisle@redhat.com> 1.1.1-1
- Require English fonts (bz#1134418)
- Updated with latest upstream URLs
- Reorganized the spec a little
- Removed SCL related parts from the spec
- Updated to new upstream release 1.1.1

* Tue Oct 21 2014 Martin Preisler <mpreisle@redhat.com> 1.0.2-2
- Fix RPM open functionality, see rhbz#1154039

* Wed Sep 24 2014 Martin Preisler <mpreisle@redhat.com> 1.0.2-1
- Updated to new upstream release 1.0.2

* Fri Sep 05 2014 Martin Preisler <mpreisle@redhat.com> 1.0.1-1
- Updated to new upstream release 1.0.1

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 27 2014 Martin Preisler <mpreisle@redhat.com> 1.0.0-1
- Updated to new version

* Tue Jun 10 2014 Martin Preisler <mpreisle@redhat.com> 0.8.9-1
- Updated to new version
- appdata is now available

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 26 2014 Martin Preisler <mpreisle@redhat.com> 0.8.8-1
- Updated to new version

* Wed Feb 19 2014 Martin Preisler <mpreisle@redhat.com> 0.8.7-1
- Updated to new version

* Fri Jan 31 2014 Jan iankko Lieskovsky <jlieskov@redhat.com> 0.8.6-2
- Disable the optional qtwebkit BR

* Thu Jan 30 2014 Martin Preisler <mpreisle@redhat.com> 0.8.6-1
- Upgrade to upstream 0.8.6 version:
  https://fedorahosted.org/scap-workbench/query?milestone=0.8.6&status=closed
- Require polkit

* Mon Jan 20 2014 Martin Preisler <mpreisle@redhat.com> 0.8.5-2
- Require openssh-askpass for GUI openssh challenge responses

* Fri Jan 10 2014 Martin Preisler <mpreisle@redhat.com> 0.8.5-1
- Updated to new version

* Mon Dec 09 2013 Martin Preisler <mpreisle@redhat.com> 0.8.4-1
- Updated to new version

* Fri Nov 29 2013 Martin Preisler <mpreisle@redhat.com> 0.8.3-1
- Updated to new version
- Added measures to deal with unversioned pkgdocdir in Fedora 20+

* Mon Nov 18 2013 Martin Preisler <mpreisle@redhat.com> 0.8.2-2
- Removed the openscap detection workaround, it is no longer needed with openscap 0.9.13

* Wed Oct 30 2013 Martin Preisler <mpreisle@redhat.com> 0.8.2-1
- Updated to new version
- Added a workaround to the cmake invocation because of faulty openscap .pc file

* Fri Sep 20 2013 Martin Preisler <mpreisle@redhat.com> 0.8.1-1
- Updated to new version

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 04 2013 Martin Preisler <mpreisle@redhat.com> 0.8.0-1
- Initial release of the rewritten workbench
