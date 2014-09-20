nexml.github.io
===============

Static website elements for the NeXML project website.

### Build documentation from NeXML schema

    $ git clone https://github.com/nexml/nexml.github.io.git
    $ cd nexml.github.io
    $ git submodule update --init --recursive

    # install deps
    # 1. graphviz for 'dot' command
    $ <brew/apt-get/yum> install graphviz
    # 2. perl modules for everything else
    $ [sudo] cpan XML::Twig
    $ [sudo] cpan Template
    $ [sudo] cpan Bio::Phylo::Util::Logger

    # fetch latest NeXML schema
    # you would do this when schema has changed upstream
    $ git submodule foreach 'git checkout master; git pull'

    # build docs
    $ echo "Last updated: $(date)" > templates/refreshDate.txt
    $ NEXML_HOME="$PWD" sitebuilder/src/bin/index.cgi nexml/xsd/nexml.xsd
