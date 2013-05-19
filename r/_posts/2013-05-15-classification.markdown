---
layout: post
title: "Classification for data quality"
---

I wrote a section on spatial analysis for the [econometrics
course](https://github.com/danhammer/ARE212) at Berkeley. I used the
features of farmer's markets as an example.  The [data set from
data.gov](https://explore.data.gov/Agriculture/Farmers-Markets-Geographic-Data/wfna-38ey?)
has information on the products sold at 7,683 markets in the United
States.  The question was whether it is possible to determine the
state of the farmer's markets, based purely on the features of the
farmer's market.  That is, does state policy impact the
characteristics of farmer's markets?  I had intended to make this a
section on discontinuity analysis through space; but instead, I found
an anomaly in the data rather than a discontinuity in economic
decision making.  

Consider the farmer's markets in four states with an easy border: New
Mexico, Utah, Arizona, and Colorado.  The features are binary
indicators of whether the market sells yogurt or honey or any of the
34 representative characteristics. Based purely on hierarchical
clustering of the binary features of the markets in the four states,
we can categorize the markets.  Given that the features are _all_
indicator variables, I used the binary metric in R:

{% highlight r %}
hclust.res <- hclust(dist(X, method = "binary"))
cl <- cutree(hclust.res, k = 4)
{% endhighlight %}

The result is an indicator variable, one of four, for each market.  If
we plot the markets, colored by cluster, then we can see that there is
something that distinguishes the markets in New Mexico:

![](/images/zoom.png)

To shoehorn this analysis into a regression discontinuity framework, I
calculated the distance to the border for each market; and distances
for markets within New Mexico are scaled by -1.

![](/images/disc.png)

It is clear that there is a difference in the features of markets
within and outside of New Mexico.  At this point I said, _sweet_. This
is an interesting result for section.  However, this indicates the
existence of a difference, but does not reveal what the difference
actually is.  I plotted the markets in CartoDB and started to browse
the data.  It turns out that, according the the data.gov data, most
farmer's markets in New Mexico don't sell anything but accept WIC
(supplemental nutrition credit for women, infants, and children).
This probably does not reflect truth, but instead a gap in the data.
Exploration of the data on CartoDB has yielded insight, even if it's
not publishable.

<script id='cartodb-1368508512960' src='http://danhammer.cartodb.com/tables/farmers_mkts/embed_map.js?title=false&description=false&search=false&shareable=false&cartodb_logo=true&scrollwheel=true&sql=&zoom=3&center_lat=37.73806173328396&center_lon=-95.33573716878891&height=400&id=cartodb-1368508512960'></script>



