#!/usr/bin/perl
# Andrea Lee
# ID: 111738212
# andrlee
use strict;
use warnings;

my $file = $ARGV[0]; # read filename as command-line argument
open HTML, "<", $file or die "Can't open input file: $!";
while (my $line = <HTML>) {
	$line =~ s/<span>//g; # remove <span>
	$line =~ s/<\/span>//g; # remove </span>
	if ($line =~ m/[<][p][>]/) { # match <p>
		$line =~ s/<p>//g; # remove <p>
		$line =~ s/<\/p>//g; # remove </p>
		chomp $line; # remove ending new line
		$line .= "<br><br>\n"; # add pair of line-break tags at the end
	}
	print "$line";
}
close HTML;
