#
# The Qubes OS Project, http://www.qubes-os.org
#
# Copyright (C) 2017  Andrew Morgan <andrew@amorgan.xyz>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
#

%define version %(cat version)

Name:		qubes-nautilus-trust-extension
Version:	%{version}
Release:	1%{?dist}
Summary:	Nautilus extension to interact with file trust levels

Group:		Qubes
License:	GPL
URL:		http://qubes-os.org

Requires:	qubes-nautilus-trust
Requires:	qubes-nautilus-python-trust
Requires:	qubes-file-trust

%define _builddir %(pwd)

%description
This package adds a new right-click menu item in Nautilus that allows users to
toggle the trust level of files or folders.

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
/usr/share/nautilus-python/extensions/qvm_trust.py*

%changelog
* Mon Aug 28 2017 Andrew Morgan <andrew@amorgan.xyz> 0.1.1
- Initial release
