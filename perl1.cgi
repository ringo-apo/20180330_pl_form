#! /usr/bin/perl

$buffer = $ENV{'QUERY_STRING'};

print "Content-type: text/html\n\n";
print "<text>$buffer</text>"
