# STFC Webring!

A little while ago, we thought it would be a pretty cool idea to form a webring with a bunch of Studen-Run Technical Groups from accross the US, or even the world, so we could collaborate, share materials, check each other out, and find each other.  Groups like ours are stronger together, and besides, this is fun and whimsical!  

This is the program that makes that idea work.  It's a very simple flask app I wrote in about an hour during class, because I was bored.  

Realistically, this program can be modified trivially (Changing HTML files to change branding), to work for any form of webring, should someone wish to do so.  

## What is a webring?  

A webring is a collection of sites that all link to each other, in a circular ring, so a user can click "next", or "Previous" to navigate through them.  A directory is encouraged such that a user can click a button to find all members of the webring.  

This is something straight out of the old web, albeit a cool idea from that era.  We're bringing it back because it's fun!  : )

## I'm a student-run technical organization, and I'd like to join!  

Cool!  We'd love to have you!  Please feel free to reach out to us as cif_board@u.rochester.edu

Once you're added to the list, feel free to add this to your site.  Feel free to modify it as you need.  
```
<p>Student Tech Fan Club</p>
<!--Anytime you see {YOU_DOMAIN_HERE}, replace it with your domain (for us, cif.rochester.edu), for you, whatever you submitted to us.   -->
<div id="webring" style="display: flex; gap: 8px; align-items: center;">
    <style type="text/css" scoped>
	#webring {
		text-align: center;
		color: black;
	}
	#webring a {
		color: black;
		text-decoration: none;
	}
    </style>
    <a href="https://stfc.cif.rochester.edu/previous?current={YOUR_DOMAIN_HERE}">⟸</a>
    <a href="https://stfc.cif.rochester.edu">
	    <div><img style="height: 25px;" src="https://stfc.cif.rochester.edu/static/webring-logo.png"><br>
    </a>
    <a href="https://stfc.cif.rochester.edu/random">
        View Random<br></div>
    </a>
    <a href="https://stfc.cif.rochester.edu/next?current={YOUR_DOMAIN_HERE}">⟹</a>
</div>
</div>
```
