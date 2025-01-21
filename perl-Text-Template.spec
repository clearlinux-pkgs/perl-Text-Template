#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Text-Template
Version  : 1.61
Release  : 34
URL      : https://cpan.metacpan.org/authors/id/M/MS/MSCHOUT/Text-Template-1.61.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MS/MSCHOUT/Text-Template-1.61.tar.gz
Summary  : 'Expand template text with embedded Perl'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Text-Template-license = %{version}-%{release}
Requires: perl-Text-Template-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::Warnings)

%description
Text::Template
This is a library for generating form letters, building HTML pages, or
filling in templates generally.  A `template' is a piece of text that
has little Perl programs embedded in it here and there.  When you
`fill in' a template, you evaluate the little programs and replace
them with their values.

%package dev
Summary: dev components for the perl-Text-Template package.
Group: Development
Provides: perl-Text-Template-devel = %{version}-%{release}
Requires: perl-Text-Template = %{version}-%{release}

%description dev
dev components for the perl-Text-Template package.


%package license
Summary: license components for the perl-Text-Template package.
Group: Default

%description license
license components for the perl-Text-Template package.


%package perl
Summary: perl components for the perl-Text-Template package.
Group: Default
Requires: perl-Text-Template = %{version}-%{release}

%description perl
perl components for the perl-Text-Template package.


%prep
%setup -q -n Text-Template-1.61
cd %{_builddir}/Text-Template-1.61

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Text-Template
cp %{_builddir}/Text-Template-1.61/LICENSE %{buildroot}/usr/share/package-licenses/perl-Text-Template/8a2e40b4eb23cc05a0b78330d919a7ffacde7a9a
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Text::Template.3
/usr/share/man/man3/Text::Template::Preprocess.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Text-Template/8a2e40b4eb23cc05a0b78330d919a7ffacde7a9a

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
