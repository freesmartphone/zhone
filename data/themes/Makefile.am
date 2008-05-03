THEME = zhone
EDC = $(THEME).edc
EET = $(EDC:%.edc=%.edj)
SUFFIXES = .edc .edj

MAINTAINERCLEANFILES = $(EET) Makefile.in
EXTRA_DIST = $(EDC)

themedir = $(pkgdatadir)
theme_DATA = $(EET)

all: $(EDC)

zhone.edj: zhone.edc zhone_dial.edc zhone_contacts.edc zhone_message.edc zhone_location.edc

.edc.edj:
	edje_cc -v -id ../images -fd ../fonts $< $@
