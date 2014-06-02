.. title: Shockingly Big IE6 Warning
.. slug: shockingly-big-ie6-warning
.. date: 31-12-2013 17:11:34 UTC-03:00
.. tags: wordpress, plug-in
.. link: http://wordpress.org/plugins/shockingly-big-ie6-warning/
.. description: A shockingly BIG or SMALL warning popup with customizable message about the dangers of using IE6. And now an option to crash IE6
.. type: text


The `Internet Explorer 6`_ was released in 2001 and nowadays it is still largely used (almost 25% market share). Despite any anti-microsoft fanatism IE6 is by far the most buggy, unsecure, off the standards, and not to mention obsolete (8 years people!) web browser ever made.

Because of this I have made this plugin. When activated in your WordPress blog it shows a warning message to every user using IE6 (or less) showing some links to alternate and much more up-to-date web browsers.

Attention
    I’m no professional programmer, this plugin is mantained in the little spare time that I have between work and university and neither is english my native language so ANY suggestion for the plugin coding or text will be appreciated.

Features
========

* Two types of warnings: a small and discreete top bar or a huge-fullscreen-site-cover popup
* Option to crash IE6 browsers instead of giving any warning (oh! that’s a secure browser)
* Customizable message, be kind or be mean with your visitors
* Suggest up to six different browsers: Firefox, Opera, Chrome, Safari, Internet Explorer
* Test mode, preview the warning in any browser

Registry Viewer
---------------

On the Shockingly Big IE6 Warning options page, if you click on the Red IE6 Logo a tab named Registry will showed up, click it to see the value of all the fields. nice for debugging.

Installation
============

1. Upload **shockingly-big-ie6-warning.X.X.X.zip** through WordPress interface or install it directly from the plugin area
2. Activate it through the ‘Plugins’ menu
3. Visit the settings page in the admin area at **Settings > S. Big IE6 Warning** and configure it

Download
--------

* `Download from wordpress.org`_

Screenshots
===========

.. slides::

   /galleries/shockingly-big-ie6-warning/001.png
   /galleries/shockingly-big-ie6-warning/002.png
   /galleries/shockingly-big-ie6-warning/003.png

Donation
========

If this plugin helped you in some way, or you just like it and want to contribute to my late night coffee (I code at night!), just use the button below:

Changelog
=========

* 1.6.3

  - You can know use links and html code at the warning massages
  - readme.txt updated
  - pt-BR localization added
  - Some code optimization

* 1.6.2

  - Minor code fixes

* 1.6.1

  - Options Page redesigned
  - JavaScript IE6 detection improved
  - Debug Mode added

* 1.5.9

  - Blank Options Page fixed(?)
  - IE6 PHP detection function inserted, for those with layout errors

* 1.5.6

  - Some options page styles fixed

* 1.5.5

  - Ready for localization (pt_BR already done)

* 1.5.4

  - Fixed the JS error, was just a comma misplaced =/

* 1.5.2

  - Estetical changes in the option page and readme.txt

* 1.5.1

  - Now you can use HTML and special characters in the messages
  - TEST Mode code changed
  - Fixed the bug that reset the options of the plugin

* 1.5.0

  - Conditional comments fixed
  - Fixed the CRASH mode (after some tuning i think we are finally REALLY stable)

* 1.4.9

  - Some links erros

* 1.4.7

  - Almost everything recoded
  - Now uses wordpress jQuery not an external .js
  - Browsers download urls now editable
  - Test mode, to preview the warning in any browser

* 1.4.4

  - Settings accessible via plugin page
  - Minor code change

* 1.4.2

  - Menu text changed to 1 line

* 1.4.0

  - Test mode added

----

.. _Internet Explorer 6: http://en.wikipedia.org/wiki/Internet_Explorer_6
.. _Download from wordpress.org: http://wordpress.org/extend/plugins/shockingly-big-ie6-warning/
