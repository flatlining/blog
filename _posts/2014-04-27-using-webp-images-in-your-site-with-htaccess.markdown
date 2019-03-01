---
layout: post
title:  "Using WebP images in your site with .htaccess"
date:   2014-04-27 23:27 -0300
categories: [development]
tags: [web]
---
[WebP](https://developers.google.com/speed/webp/) is a fairly new image
format under development by
[Google](https://developers.google.com/products/) with the intent of
creating smaller files without losing quality. A WebP file is about 34%
smaller than a visual equivalent JPEG, while also supporting
transparency by the use of alpha channels.

Currently only a few [browsers support](https://en.wikipedia.org/wiki/WebP#Support) the format, making a big risk
to simply to simply convert all image in your site. So a more subtle
approach is required, one that is invisible to your site's visitor,
thats where [.htaccess](https://en.wikipedia.org/wiki/Htaccess) comes in
handy.

## Adapting your site

There are two steps to this process, first will create a
[WebP](https://developers.google.com/speed/webp/) equivalente to all
image you want to make available, than will create a .htaccess rule that
will serve to correct file for each browser.

### Converting the images

Keep in mind that we wont replace the image, but rather create WebP
copys of them with the same name and location, e.g.:

```console
$ ls -al
total 436
drwxrwxr-x 2 4096 Abr 27 02:08 .
drwxrwxr-x 3 4096 Abr 27 02:44 ..
-rw-rw-r-- 1 374050 Abr 25 01:53 instalando-o-steam-localmente-no-gnulinux-screenshot.png
-rw-rw-r-- 1 44832 Abr 27 02:08 instalando-o-steam-localmente-no-gnulinux-screenshot.webp
```

For that we will use the libwebp set of tools, more specifically the
`cwebp` program, available for Windows, OSx and Linux and can be
downloaded as
[precompiled](https://developers.google.com/speed/webp/docs/precompiled)
binaries\[2\], but on Ubuntu its easy as using `apt-get`:

```console
$ sudo apt-get install webp
```

Then convert the desired images using:

```console
$ cwebp image_file.jpg -o image_file.webp
```

> Attention
>
> The output file must have the same name of the input file.

There are many other parameters to fine tune the conversions see the
`--longhep` of `cwebp` for more options, one that is really usefull is
the `-preset` a serie of preset (duh) values for the most common
scenarios, e.g.:

```console
$ cwebp -preset [preset] image_file.png -o image_file.webp
```

Where `[preset]` can be:

- default
- photo
- picture
- drawing
- icon
- text

Choose the best for each file.

### Serving the images

Now that our images are converted how can we serve them? If we simply
replace the old files with the WebP versions a good number of browser
wont be able to render them.

Thats where htaccess file comes in, by creating a rewrite rule that that
everytime a image is requested will check if the requesting browser
support the new format, and if so will profile the WebP file instead of
the original requested.

So, create a `.htaccess` in your sites root directory (if there isnt one
already) and add the [following lines](http://mikevoermans.com/apache/serving-right-image-htaccess-webp):

```apacheconf
<IfModule mod_rewrite.c>
  RewriteEngine On
  # check if browser accepts webp
  RewriteCond %{HTTP_ACCEPT} image/webp
  # check if file is jpg or png
  RewriteCond %{REQUEST_FILENAME} (.*)\.(jpe?g|png)$
  # check if corresponding webp file exists image.png -> image.webp
  RewriteCond %1\.webp -f
  # serve up webp instead
  RewriteRule (.+)\.(jpe?g|png)$ $1.webp [T=image/webp,E=accept:1]
</IfModule>

<IfModule mod_headers.c>
  Header append Vary Accept env=REDIRECT_accept
</IfModule>

AddType image/webp .webp
```

To make sure if its working open Chrome
[DevTools](https://developers.google.com/chrome-developer-tools/)
(`SHIFT + CTRL + I`) select the **Network** tab and load an image of
your site and compare the **Type** column with and without the htaccess
rule, i.e:

![Without support to
WebP](/assets/using-webp-images-on-your-site-with-htaccess-without.png)

![With support to
WebP](/assets/using-webp-images-on-your-site-with-htaccess-with.png)

> Tip
>
> Its a go idea to test the site in a browser that lacks support, Internet
  Explorer for example.

## The Future

With many new formats like
[MNG](https://en.wikipedia.org/wiki/Multiple-image_Network_Graphics),
the some what old [JPEG 2000](https://en.wikipedia.org/wiki/JPEG_2000)
and the new [JPEG XR](https://en.wikipedia.org/wiki/JPEG_XR) fighting
along [WebP](https://developers.google.com/speed/webp/) for the place of
image format of choice for the web, the future is uncertain, but having
a giant like [Google](https://developers.google.com/products/) as
supporter cetantly gives
[WebP](https://developers.google.com/speed/webp/) a good start.

Lets wait to see what the future holds for web development!
