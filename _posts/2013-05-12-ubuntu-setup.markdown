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
OSX-side `Dropbox` with the VM.

{% highlight bash %}
sudo ln -s /mnt/hgfs/Dropbox Dropbox
{% endhighlight %}

