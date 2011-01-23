%define		plugin		orphanswanted
Summary:	DokuWiki plugin to find orphan pages, Wanted pages with reference counts
Name:		dokuwiki-plugin-%{plugin}
Version:	20100411
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://github.com/downloads/andywebber/dokuwiki-plugin-orphanswanted/orphanswanted.zip
# Source0-md5:	50e45168d9ac8d3bf7e663f4f274f57a
URL:		http://www.dokuwiki.org/plugin:orphanswanted
BuildRequires:	rpmbuild(macros) >= 1.520
BuildRequires:	unzip
Requires:	dokuwiki >= 20091225
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}
%define		find_lang 	%{_usrlibrpm}/dokuwiki-find-lang.sh %{buildroot}

%description
Use this plugin to find orphan pages and wanted pages.

OrphansWanted show which pages are:
- Orphans (the page exists, but it has no links to it)
- Wanted (the page does not exist, but there are link(s) to it
  elsewhere on the site)
- Valid (the page exists, and it can be reached through a link)

Each table shows the reference count and a link to backlinks.

%prep
%setup -qc
mv %{plugin}/* .

version=$(cat VERSION)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
rm $RPM_BUILD_ROOT%{plugindir}/{COPYING,README,VERSION}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{plugindir}
%{plugindir}/*.php
