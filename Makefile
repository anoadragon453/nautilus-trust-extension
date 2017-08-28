INSTALL_OPTS = -D
INSTALL = install $(INSTALL_OPTS)
INSTALL_PROGRAM = $(INSTALL)
INSTALL_DATA = $(INSTALL) -m 0644

install:
	$(INSTALL_DATA) qvm_trust.py $(DESTDIR)/usr/share/nautilus-python/extensions/qvm_trust.py
