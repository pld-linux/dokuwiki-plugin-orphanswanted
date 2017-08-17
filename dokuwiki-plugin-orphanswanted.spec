%define		subver	2017-06-25
%define		ver		%(echo %{subver} | tr -d -)
%define		plugin		orphanswanted
%define		php_min_version 5.3.0
%include	/usr/lib/rpm/macros.php
Summary:	DokuWiki plugin to find orphan pages, Wanted pages with reference counts
Name:		dokuwiki-plugin-%{plugin}
Version:	%{ver}
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/lupo49/dokuwiki-plugin-orphanswanted/archive/163625f/%{plugin}-%{subver}.tar.gz
# Source0-md5:	b14fbb365e9b9e0dfcde770e7b50a0d3
URL:		https://www.dokuwiki.org/plugin:orphanswanted
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.553
Requires:	dokuwiki >= 20131208
Requires:	php(core) >= %{php_min_version}
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
mv *-%{plugin}-*/* .

%build
version=$(awk '/^date/{print $2}' plugin.info.txt)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
rm $RPM_BUILD_ROOT%{plugindir}/{COPYING,README}

%find_lang %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%dir %{plugindir}
%{plugindir}/*.php
%{plugindir}/*.txt
%{plugindir}/conf
