%{?scl:%scl_package perl-ExtUtils-ParseXS}

%global base_version 3.30
Name:           %{?scl_prefix}perl-ExtUtils-ParseXS
# Epoch to compete with perl.spec
Epoch:          1
Version:        3.31
Release:        366%{?dist}
Summary:        Module and a script for converting Perl XS code into C code
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/ExtUtils-ParseXS/
Source0:        http://www.cpan.org/authors/id/S/SM/SMUELLER/ExtUtils-ParseXS-%{base_version}.tar.gz
# Unbundled from perl 5.24.0
Patch0:         ExtUtils-ParseXS-3.30-Upgrade-to-3.31.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.46
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Cwd)
BuildRequires:  %{?scl_prefix}perl(Exporter) >= 5.57
# ExtUtils::XSSymSet not needed
BuildRequires:  %{?scl_prefix}perl(File::Basename)
# Getopt::Long not tested
BuildRequires:  %{?scl_prefix}perl(re)
BuildRequires:  %{?scl_prefix}perl(Symbol)
# Tests:
BuildRequires:  %{?scl_prefix}perl-devel
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(attributes)
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(DynaLoader)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::CBuilder)
BuildRequires:  %{?scl_prefix}perl(File::Temp)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(overload)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.47
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(Exporter) >= 5.57
# perl-ExtUtils-Typemaps has been merged into perl-ExtUtils-ParseXS, bug #891952
Obsoletes:      %{?scl_prefix}perl-ExtUtils-Typemaps

# Remove under-specified dependencies
%if 0%{?rhel} < 7
# RPM 4.8 style
%{?filter_setup:
%filter_from_requires /^%{?scl_prefix}perl(Exporter)$/d
%?perl_default_filter
}
%else
# RPM 4.9 style
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\(Exporter\\)$
%endif

%description
ExtUtils::ParseXS will compile XS code into C code by embedding the
constructs necessary to let C functions manipulate Perl values and creates
the glue necessary to let Perl access those functions.

%prep
%setup -q -n ExtUtils-ParseXS-%{base_version}
%patch0 -p1

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*
# Do not install xsubpp twice, RT#117289
rm $RPM_BUILD_ROOT%{perl_vendorlib}/ExtUtils/xsubpp
ln -s ../../../../bin/xsubpp $RPM_BUILD_ROOT%{perl_vendorlib}/ExtUtils/

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc Changes README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Mon Jul 11 2016 Petr Pisar <ppisar@redhat.com> - 1:3.31-366
- SCL

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.31-365
- Increase release to favour standalone package

* Wed May 11 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.31-1
- 3.31 bump in order to dual-live with perl 5.24

* Mon Apr 18 2016 Petr Pisar <ppisar@redhat.com> - 1:3.30-3
- Remove dependency on perl-devel (bug #1129443)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 31 2015 Petr Pisar <ppisar@redhat.com> - 1:3.30-1
- 3.30 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.28-346
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.28-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.28-2
- Perl 5.22 rebuild

* Wed May 06 2015 Petr Pisar <ppisar@redhat.com> - 1:3.28-1
- 3.28 bump in order to dual-live with perl 5.22

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.24-310
- Perl 5.20 rebuild
- Increase release to favour standalone package

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 10 2014 Petr Pisar <ppisar@redhat.com> - 1:3.24-1
- 3.24 bump

* Mon Sep 02 2013 Petr Pisar <ppisar@redhat.com> - 1:3.22-1
- 3.22 bump

* Mon Aug 26 2013 Petr Pisar <ppisar@redhat.com> - 1:3.21-1
- 3.21 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.18-291
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Petr Pisar <ppisar@redhat.com> - 1:3.18-290
- Increase release to favour standalone package

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1:3.18-2
- Perl 5.18 rebuild

* Fri Mar 22 2013 Petr Pisar <ppisar@redhat.com> 1:3.18-1
- Specfile autogenerated by cpanspec 1.78.
