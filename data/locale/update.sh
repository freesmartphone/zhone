#!/bin/sh
xgettext\
 --foreign-user\
 --package-name="zhone"\
 -L python -o zhone.pot -D ../../src zhone
for i in */LC_MESSAGES; do\
 msgmerge -U $i/zhone.po zhone.pot;
 msgfmt -o $i/zhone.mo $i/zhone.po;
 done

