#!/usr/bin/perl
use CGI::Carp qw(fatalsToBrowser);
use Config;
use strict;
use warnings;
use CGI;
use Bio::Phylo::PhyloWS::Service::Tolweb;
use Bio::Phylo::Util::Logger ':levels';

my $script = $ENV{'SCRIPT_NAME'};
$script =~ s/\.cgi$//;
my $url = 'http://' . $ENV{'SERVER_NAME'} . $script . '/phylows/';

my $logger = Bio::Phylo::Util::Logger->new;
open my $fh, '>', 'tolweb.log' or die $!;
$logger->VERBOSE( '-level' => DEBUG );
$logger->set_listeners( sub { print $fh shift } );
$logger->info("Using URL: $url");

eval {
	my $service = Bio::Phylo::PhyloWS::Service::Tolweb->new( '-base_uri' => $url );
	my $cgi = CGI->new;
	$service->handle_request( $cgi );
};
if ( $@ ) {
	$logger->fatal("\n$@");
	die $@;
}
