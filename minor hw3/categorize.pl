#!/usr/bin/perl
# Andrea Lee
# ID: 111738212
# andrlee
use strict;
use warnings;

# modulatiry : string constants for filenames (.txt files)
my $efiles = "efiles"; # lists files that exists
my $rfiles = "rfiles"; # lists files that are readable
my $wfiles = "wfiles"; # lists files that are writable
my $xfiles = "xfiles"; # lists files that are executable
my $tfiles = "tfiles"; # lists files that are plain text

my $file = $ARGV[0]; # read filename of input as command-line argument
open NAMES, "<", $file or die "Can't open input file: $!";
open EXISTS, ">$efiles.txt" or die "Can't open output file: $!";
open READABLE, ">$rfiles.txt" or die "Can't open output file: $!";
open WRITABLE, ">$wfiles.txt" or die "Can't open output file: $!";
open EXECUTABLE, ">$xfiles.txt" or die "Can't open output file: $!";
open TEXT, ">$tfiles.txt" or die "Can't open output file: $!";
my @sum;
while (my $line = <NAMES>) {
	chomp $line; # remove new line
	if (-e $line) { # if file exists
		print EXISTS "$line\n"; # write to efiles.txt on new line
		$sum[0][0]++; # exists counter
		$sum[0][1] .= "$line "; # list file
	}
	if (-r $line) { # if file is readable
		print READABLE "$line\n"; # write to rfiles.txt on new line
		$sum[1][0]++; # readable counter
		$sum[1][1] .= "$line "; # list file
	}
	if (-w $line) { # if file is writable
		print WRITABLE "$line\n"; # write to wfiles.txt on new line
		$sum[2][0]++; # writable counter
		$sum[2][1] .= "$line "; # list file
	}
	if (-x $line) { # if file is executable
		print EXECUTABLE "$line\n"; # write to xfiles.txt on new line
		$sum[3][0]++; # executable counter
		$sum[3][1] .= "$line "; # list file
	}
	if (-T $line) { # if file is a text file
		print TEXT "$line\n"; # write to tfiles.txt on new line
		$sum[4][0]++; # text counter
		$sum[4][1] .= "$line "; # list file
	}
}
close EXISTS;
close READABLE;
close WRITABLE;
close EXECUTABLE;
close TEXT;
close NAMES;
# print output
print "$sum[0][0] existing files: $sum[0][1]\n";
print "$sum[1][0] readable files: $sum[1][1]\n";
print "$sum[2][0] writable files: $sum[2][1]\n";
print "$sum[3][0] executable files: $sum[3][1]\n";
print "$sum[4][0] plain text files: $sum[4][1]\n";
