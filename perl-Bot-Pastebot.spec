# TODO
# - make noarch
#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Bot
%define		pnam	Pastebot
Summary:	The original clipboard-to-chat gateway
Name:		perl-Bot-Pastebot
Version:	0.50
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/pastebot/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c95628bdc58bbc472728ba43e23e9792
URL:		http://sourceforge.net/projects/pastebot/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-File-ShareDir
BuildRequires:	perl-POE
BuildRequires:	perl-POE-Component-IRC
BuildRequires:	perl-Text-Template
BuildRequires:	perl-libwww
BuildRequires:	perltidy
%endif
# no arch files installed, but pkg installs to arch dir so therefore noarch
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pastebot is an IRC bot that saves channels from large amounts of
pasted material. Text is pasted into a web form, and the bot announces
an URL where it can be read. Interested people can partake in the joy
without the whole channel scrolling to hell.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
# Don't use pipes here: they generally don't work. Apply a patch.
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES

%attr(755,root,root) %{_bindir}/pastebot
%{_mandir}/man1/pastebot.1p*
%{perl_vendorarch}/Bot/Pastebot
%{perl_vendorarch}/auto/Bot/Pastebot
