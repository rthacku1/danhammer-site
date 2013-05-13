---
layout: post
title: "Ubuntu set up"
---

I use OSX to consume content and Linux to create content.  Or, rather,
my wife screws up my Netflix preferences on OSX and I spend too much
time fucking with syntax highlighting on Ubuntu.  I recently bought a
new Macbook Pro, and I've documented the steps to set up Ubuntu on a
virtual machine.  I'll save the machine image so that I don't actually
have to go through these steps again; but it may be useful as a
script, of sorts:

### VM Fusion and Ubuntu

Download Ubuntu 12.04 from the [Ubuntu
website](http://www.ubuntu.com/) and follow [these
instructions](http://www.macinstruct.com/node/394) to install the
platform on OSX using [VMware Fusion](http://goo.gl/rC43X).  You can
use it immediately with the _Electronic Software Download_.  If you
have retina display, then you'll have to turn off the option for
Accelerate 3D Graphics found in **Virtual Machine > Settings >
Display**.  Don't enable the option to use the full resolution for
retina display in that menu.  Instead, set the screen resolution on
the OSX side: **System Preferences > Display**.

### Folder sharing

I keep everything on Dropbox, including code and configurations.  I
don't want to duplicate storage on my computer, so I share the
OSX-side `Dropbox` folder with the VM.  Go to **Virtual Machine >
Settings > Sharing** and add the `Dropbox` folder.  The shared folder
will show up on the virtual machine in the `/mnt/hgfs/` directory.  I
like to have it up-front, in my home folder, so I symlinked it from
within the home directory:

{% highlight bash %}
sudo ln -s /mnt/hgfs/Dropbox Dropbox
{% endhighlight %}

Depending on what version of Ubuntu and VMware you download, it may
not be so easy to share folders across platforms.  It's worth
struggling through, however, so that you don't waste valuable disk
space with duplicated files (and risk strange overwrites).  

I also removed a bunch of the default folders:

{% highlight bash %}
rm -rf Documents/ Music/ Pictures/ Public/ Templates/ Videos/ examples.desktop 
{% endhighlight %}

### Configuration files

I keep all of my configuration and credential files within
`Dropbox/settings`.  For example, I keep a global bash profile,
unhidden, in the `settings` directory, which I symlink into my home
directory on the VM:

{% highlight bash %}
sudo ln -s Dropbox/settings/ssh/ .ssh
sudo ln -s Dropbox/settings/starcluster/ .starcluster
sudo ln -s Dropbox/settings/emacs.d/ .emacs.d
sudo ln -s Dropbox/settings/s3cfg .s3cfg
sudo ln -s Dropbox/settings/bashrc .bashrc
{% endhighlight %}

You may have to make minor adjustments to this step.  You may, for
example, have to remove the default `.bashrc` file before symlinking
your custom bash script.  I forked my Emacs configuration from
[here](https://github.com/eschulte/emacs24-starter-kit).  Within
`.ssh/`, I keep my AWS keypairs and Google Earth Engine credentials,
like `.ssh/ee-privatekey.p12`.  This way, if I lose my computer, I'll
have all the customizations backed up on Dropbox.

### Install Yakuake and Emacs 24

I like Yakuake to work at the command line.  It looks great and it's
easy to use.  Install it and then configure the layout, removing _all_
animation (for the love):

{% highlight bash %}
sudo apt-get install yakuake
yakuake
{% endhighlight %}

Then install Emacs, along with some modes and programs that you'll
need for statistics work:

{% highlight bash %}
sudo add-apt-repository ppa:cassou/emacs
sudo apt-get update
sudo apt-get install emacs24 emacs24-el emacs24-common-non-dfsg
sudo apt-get install r-base-core ess clojure git s3cmd
{% endhighlight %}

The result will look like this:

![](/images/desktop.png)

### Install Java and Leiningen

Install the JVM for Clojure, maybe multiple versions depending on the
projects you require:

{% highlight bash %}
sudo apt-get install openjdk-7-jre openjdk-6-jre
{% endhighlight %}

Then [Leiningen](https://github.com/technomancy/leiningen) for easy
use of Clojure.

{% highlight bash %}
cd /tmp
sudo wget https://raw.github.com/technomancy/leiningen/preview/bin/lein
sudo mv lein /usr/bin/lein
sudo chmod 755 /usr/bin/lein
lein -v
{% endhighlight %}

Also, I like working with the `nrepl` package for Emacs, so hit `M-x
package-list-packages` in Emacs and make sure it's installed.  You can
enter a REPL, then, by just hitting `M-x nrepl-jack-in` from within a
Clojure buffer.

### Install elastic-mapreduce

I use [elastic-mapreduce](http://aws.amazon.com/developertools/2264)
for creating, describing and terminating Job Flows using Amazon
Elastic MapReduce.  Follow [these
instructions](http://docs.aws.amazon.com/ElasticMapReduce/latest/DeveloperGuide/emr-cli-install.html).
If you already have your credentials.json file, then it's pretty
simple.  First grab Ruby and wget:

{% highlight bash %}
sudo apt-get install ruby-full wget
{% endhighlight %}

Then get the command line interface:

{% highlight bash %}
mkdir elastic-mapreduce-cli
wget http://elasticmapreduce.s3.amazonaws.com/elastic-mapreduce-ruby.zip
unzip elastic-mapreduce-ruby.zip -d elastic-mapreduce-cli
{% endhighlight %}

Put your `credentials.json` file in the `elastic-mapreduce-cli`
directory.  And ensure that the following is in your `.bashrc` file.

{% highlight bash %}
export PATH=$PATH:~/elastic-mapreduce-cli/elastic-mapreduce-ruby
{% endhighlight %}

### Install StarCluster

[StarCluster](http://star.mit.edu/cluster/) is an open source project
to build, configure, and manage clusters of virtual machines on
Amazon’s EC2 cloud.  We use it to launch simple, accessible jobs in
Python, R, or Stata if Hadoop seems excessive.  

{% highlight bash %}
sudo apt-get install python-setuptools
sudo easy_install StarCluster
{% endhighlight %}

The configuration files are located in `~/.starcluster`, but really
reside on Dropbox, as described above.  

### Configure git

For coloring and other handy stuff:

{% highlight bash %}
git config --global color.branch auto
git config --global color.diff auto
git config --global color.interactive auto
git config --global color.status auto
{% endhighlight %}

### Install Jekyll

In a sort of meta, final step, you should install Jekyll -- which is
what I used to generate this site.  

{% highlight bash %}
git clone git://github.com/rubygems/rubygems.git
cd rubygems
ruby setup.rb
sudo gem1.8 install jekyll
sudo gem1.8 install rdiscount
sudo easy_install Pygments
sudo apt-get install markdown
{% endhighlight %}

Oh and maybe MongoDB:

{% highlight bash %}
sudo apt-get install mongodb
{% endhighlight %}
