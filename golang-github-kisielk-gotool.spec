Name     : golang-github-kisielk-gotool
Version  : 94d5dba705240ba73ce5d65d83ce44adc749b440
Release  : 1
URL      : https://github.com/kisielk/gotool/archive/94d5dba705240ba73ce5d65d83ce44adc749b440.tar.gz
Source0  : https://github.com/kisielk/gotool/archive/94d5dba705240ba73ce5d65d83ce44adc749b440.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : go

%description
gotool
======
[![GoDoc](https://godoc.org/github.com/kisielk/gotool?status.svg)](https://godoc.org/github.com/kisielk/gotool)
[![Build Status](https://travis-ci.org/kisielk/gotool.svg?branch=master)](https://travis-ci.org/kisielk/gotool)

%prep
%setup -q -n gotool-94d5dba705240ba73ce5d65d83ce44adc749b440

%build
export LANG=C

%install
rm -rf %{buildroot}
%global gopath /usr/lib/golang
%global library_path github.com/kisielk/gotool

# Copy all *.go and *.s files
install -d -p %{buildroot}%{gopath}/src/%{library_path}/
for ext in go s src golden template; do
    for file in $(find . -iname "*.$ext") ; do
         install -d -p %{buildroot}%{gopath}/src/%{library_path}/$(dirname $file)
         cp -pav $file %{buildroot}%{gopath}/src/%{library_path}/$file
    done
done

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export GOPATH=%{buildroot}%{gopath}
go test %{library_path}/... || :

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/kisielk/gotool/go13.go
/usr/lib/golang/src/github.com/kisielk/gotool/go14-15.go
/usr/lib/golang/src/github.com/kisielk/gotool/go16.go
/usr/lib/golang/src/github.com/kisielk/gotool/match.go
/usr/lib/golang/src/github.com/kisielk/gotool/match_test.go
/usr/lib/golang/src/github.com/kisielk/gotool/tool.go
