Summary:	Set the value reported for a network card MAC address
Name:		fakeuname
Version:	0.1
Release:	0.1
License:	?
Group:		Libraries
Source0:	ftp://ftp.slackware.pl/pub/armedslack/armedslack-devtools/slackkit/%{name}.c
# Source0-md5:	6d814c9f2c4710b7aa4a6fd3cf322b23
URL:		http://www.chiark.greenend.org.uk/~peterb/linux/fakeif/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is so that we can build software that does not know the names of more
recent ARM architectures such as armv5, and also fake host names and MAC
addresses for some particularly weird stuff ;-)

%prep
%setup -qcT
cp -p %{SOURCE0} .

%build
%{__cc} %{rpmcflags} %{rpmcppflags} -c -fPIC -Wall %{name}.c
%{__cc}  -W1,export-dynamic -shared -fPIC -o lib%{name}.so %{rpmldflags} -ldl %{name}.o

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}
install -p lib%{name}.so $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfakeuname.so
