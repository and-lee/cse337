#!/usr/bin/perl
# Andrea Lee
# ID: 111738212
# andrlee
use strict;
use warnings;

my $path = `echo \$PATH`; # save shell command to scalar
my @dirs = $path =~ /[^\/:][\w-.]*/g; # regex to seperate directory names
print join("\n", @dirs); # print name of each directory on a new line
