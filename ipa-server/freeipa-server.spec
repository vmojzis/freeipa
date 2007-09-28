Name:           freeipa-server
Version:        0.4.0
Release:        1%{?dist}
Summary:        FreeIPA authentication server

Group:          System Environment/Base
License:        GPL
URL:            http://www.freeipa.org
Source0:        %{name}-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: fedora-ds-base-devel openldap-devel krb5-devel nss-devel mozldap-devel openssl-devel

Requires: python fedora-ds-base krb5-server krb5-server-ldap nss-tools openldap-clients httpd mod_python mod_auth_kerb python-ldap freeipa-python ntp cyrus-sasl-gssapi nss TurboGears

%define httpd_conf /etc/httpd/conf.d
%define plugin_dir /usr/lib/dirsrv/plugins

%description
FreeIPA is a server for identity, policy, and audit.

%prep
%setup -q

%build

make DESTDIR=%{buildroot}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{plugin_dir}

make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_sbindir}/ipa-server-install
%{_sbindir}/ipa_kpasswd
%attr(755,root,root) %{_initrddir}/ipa-kpasswd

%dir %{_usr}/share/ipa
%{_usr}/share/ipa/*

%attr(755,root,root) %{plugin_dir}/libipa_pwd_extop.so
%attr(755,root,root) %{plugin_dir}/libipa-memberof-plugin.so
%attr(755,root,root) %{plugin_dir}/libipa-dna-plugin.so


%changelog
* Fri Sep 7 2007 Karl MacMillan <kmacmill@redhat.com> - 0.3.0-1
- Added support for libipa-dna-plugin

* Fri Aug 10 2007 Karl MacMillan <kmacmill@redhat.com> - 0.2.0-1
- Added support for ipa_kpasswd and ipa_pwd_extop

* Mon Aug  5 2007 Rob Crittenden <rcritten@redhat.com> - 0.1.0-3
- Abstracted client class to work directly or over RPC

* Wed Aug  1 2007 Rob Crittenden <rcritten@redhat.com> - 0.1.0-2
- Add mod_auth_kerb and cyrus-sasl-gssapi to Requires
- Remove references to admin server in ipa-server-setupssl
- Generate a client certificate for the XML-RPC server to connect to LDAP with
- Create a keytab for Apache
- Create an ldif with a test user
- Provide a certmap.conf for doing SSL client authentication

* Fri Jul 27 2007 Karl MacMillan <kmacmill@redhat.com> - 0.1.0-1
- Initial rpm version


