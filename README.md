<!DOCTYPE html>
<html lang="en" prefix="og: http://ogp.me/ns# fb: https://www.facebook.com/2008/fbml">
<head>
    <title>Introduction to Data Science - Dmitry Shatalov</title>
    <!-- Using the latest rendering mode for IE -->
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">


    <link href="http://dshatalov.com/extra/favicon.ico" rel="icon">

<link rel="canonical" href="http://dshatalov.com/2016/05/introduction-to-data-science/">

        <meta name="author" content="" />
        <meta name="description" content="As most of us know Python is widely used for scientific purposes. Recently I have done a few steps in this direction learning how to visualize data using very powerful APIs that are available today. Primarily this post is about my first personal experience of handling raw data and making ..." />

        <meta property="og:site_name" content="Dmitry Shatalov" />
        <meta property="og:type" content="article"/>
        <meta property="og:title" content="Introduction to Data Science"/>
        <meta property="og:url" content="http://dshatalov.com/2016/05/introduction-to-data-science/"/>
        <meta property="og:description" content="As most of us know Python is widely used for scientific purposes. Recently I have done a few steps in this direction learning how to visualize data using very powerful APIs that are available today. Primarily this post is about my first personal experience of handling raw data and making ..."/>
        <meta property="article:published_time" content="2016-05-14" />
            <meta property="article:section" content="Posts" />


    <!-- Bootstrap -->
        <link rel="stylesheet" href="http://dshatalov.com/theme/css/bootstrap.flatly.min.css" type="text/css"/>
    <link href="http://dshatalov.com/theme/css/font-awesome.min.css" rel="stylesheet">

    <link href="http://dshatalov.com/theme/css/pygments/native.css" rel="stylesheet">
    <link href="http://dshatalov.com/theme/tipuesearch/tipuesearch.css" rel="stylesheet">
    <link rel="stylesheet" href="http://dshatalov.com/theme/css/style.css" type="text/css"/>




        <link href="http://dshatalov.com/feeds/posts.atom.xml" type="application/atom+xml" rel="alternate"
              title="Dmitry Shatalov Posts ATOM Feed"/>

</head>
<body>

<div class="navbar navbar-default navbar-fixed-top" role="navigation">
	<div class="container">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a href="http://dshatalov.com/" class="navbar-brand">
Dmitry Shatalov            </a>
        </div>
        <div class="collapse navbar-collapse navbar-ex1-collapse">
            <ul class="nav navbar-nav">
                    <li><a href="/">Home</a></li>
                    <li><a href="/archives.html">Posts</a></li>
                         <li><a href="http://dshatalov.com/projects/">
                             Projects
                          </a></li>
                         <li><a href="http://dshatalov.com/resume/">
                             Resume
                          </a></li>
                         <li><a href="http://dshatalov.com/about/">
                             About
                          </a></li>
            </ul>
            <ul class="nav navbar-nav navbar-right">
              <li><span>
                <form class="navbar-search" action="/search.html">
                  <input type="text" class="search-query" placeholder="Search" name="q" id="tipue_search_input" required>
                </form></span>
              </li>
            </ul>
        </div>
        <!-- /.navbar-collapse -->
    </div>
</div> <!-- /.navbar -->
<!-- Banner -->
<!-- End Banner -->
<div class="container">
    <div class="row">
        <div class="col-sm-9">
    <section id="content">
        <article>
            <header class="page-header">
                <h1>
                    <a href="http://dshatalov.com/2016/05/introduction-to-data-science/"
                       rel="bookmark"
                       title="Permalink to Introduction to Data Science">
                        Introduction to Data Science
                    </a>
                </h1>
            </header>
            <div class="entry-content">
                <div class="panel">
                    <div class="panel-body">
<footer class="post-info">
    <span class="label label-default">Date</span>
    <span class="published">
        <i class="fa fa-calendar"></i><time datetime="2016-05-14T20:00:00-05:00"> Sat 14 May 2016</time>
    </span>





    
</footer><!-- /.post-info -->                    </div>
                </div>
                <p>As most of us know Python is widely used for scientific purposes. Recently I have done a few steps in this direction learning how to visualize data using very powerful APIs that are available today. Primarily this post is about my first personal experience of handling raw data and making good visualizations using different visualizing techniques. </p>
<p>For this project my team used <strong>Airbnb data</strong> that we found on <a href="https://www.kaggle.com/c/airbnb-recruiting-new-user-bookings">Kaggle</a>. Our aim was to understand Airbnb users' booking behavior so that the company was able to target the right customers by customized marketing skills and expand the user community.</p>
<p>As a member of a team I worked on exploring and visualizing user demographics, one of the directions our team decided to take. First, I explored correlations between categories of our highly categorical data using <a href="http://www.tableau.com/">Tableau</a>. I believe that it is a good tool for starting exploring your data since it does not require much effort to format and handle data sets, and you can create nice simple graphs pretty easily. Tableau helped me to find first patterns and contribute many graphs (heatmaps, stacked bar and line graphs). Most of these graphs were later used by the team as a first step towards deep exploratory analysis. </p>
<p>To continue working on visualizations demanding more complex techniques I wanted to choose a tool that would be useful for analyzing categorical data. Having experience with Python I came across some very powerful APIs for graphical analysis such as Seaborn, Pandas, and Matplotlib. </p>
<p>Eventually, I came up with two visualizations using Seaborn API. I found their <a href="https://stanford.edu/~mwaskom/software/seaborn/api.html">documentation and examples</a> very handy. </p>
<p>I created the <strong>counter plot</strong> that showed which weekdays were more and less popular for creating account and highlighted the age distribution. Combining this plot with histograms on the axises (JointGrid function of “Seaborn” library gave me a hand) allowed me to explore and explain some patterns.</p>
<p><img alt="graph1" src="http://dshatalov.com/uploads/graph1.jpg" /></p>
<p>For the second visualization I used the <strong>violin plot</strong>. It allowed me to combine multiple aspects of data in a single graph and find interesting patterns. With the help of Python APIs I compared four years of observations and plotted it as a single graph. </p>
<p><img alt="graph2" src="http://dshatalov.com/uploads/graph2.jpg" /></p>
<h3>Lessons learned</h3>
<ul>
<li>80% of work in Data Science is spent on handling data and only 20% - on visualizing it. </li>
<li>It is very important and at the same time very difficult to choose a proper visualization technique that will clearly show some patterns in your data. Experimenting worked for me.</li>
<li>It is always a bad idea to fit your data to some technique. It should be the other way round. </li>
<li>Python itself and a great collection of visualization tools created for it make this language one of the best options for Data Science.</li>
</ul>
<h3>The code for these two graphs can be found in my repository on <a href="https://github.com/shatalovdm/data_visualization">GitHub</a>.</h3>
            </div>
            <!-- /.entry-content -->
    <hr />
    <!-- AddThis Button BEGIN -->
    <div class="addthis_toolbox addthis_default_style">
            <a class="addthis_button_facebook_like" fb:like:layout="button_count"></a>
            <a class="addthis_button_tweet"></a>
            <a class="addthis_button_google_plusone" g:plusone:size="medium"></a>
    </div>
    <!-- AddThis Button END -->
    <hr/>
    <section class="comments" id="comments">
        <h2>Comments</h2>

        <div id="disqus_thread"></div>
        <script type="text/javascript">
            /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
            var disqus_shortname = 'dshatalov'; // required: replace example with your forum shortname
                    var disqus_identifier = 'introduction-to-data-science';
                var disqus_url = 'http://dshatalov.com/2016/05/introduction-to-data-science/';
            var disqus_config = function () {
                this.language = "en";
            };
            /* * * DON'T EDIT BELOW THIS LINE * * */
            (function () {
                var dsq = document.createElement('script');
                dsq.type = 'text/javascript';
                dsq.async = true;
                dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
                (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
            })();
        </script>
        <noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript">comments powered by
            Disqus.</a></noscript>
        <a href="http://disqus.com" class="dsq-brlink">comments powered by <span class="logo-disqus">Disqus</span></a>

    </section>
        </article>
    </section>

        </div>
        <div class="col-sm-3" id="sidebar">
            <aside>

<section class="well well-sm">
    <ul class="list-group list-group-flush">
            <li class="list-group-item"><h4><i class="fa fa-home fa-lg"></i><span class="icon-label">Social</span></h4>
              <ul class="list-group" id="social">
                <li class="list-group-item"><a href="https://www.facebook.com/shatalov.da"><i class="fa fa-facebook-square fa-lg"></i> Facebook</a></li>
                <li class="list-group-item"><a href="https://twitter.com/DmitryShatalov"><i class="fa fa-twitter-square fa-lg"></i> Twitter</a></li>
                <li class="list-group-item"><a href="https://github.com/shatalovdm"><i class="fa fa-github-square fa-lg"></i> GitHub</a></li>
              </ul>
            </li>

            <li class="list-group-item"><h4><i class="fa fa-home fa-lg"></i><span class="icon-label">Recent Posts</span></h4>
                <ul class="list-group" id="recentposts">
                    <li class="list-group-item">
                        <a href="http://dshatalov.com/2016/06/hands-on-experience-with-web2py/">
                            Hands-on experience with Web2py
                        </a>
                    </li>
                    <li class="list-group-item">
                        <a href="http://dshatalov.com/2016/05/introduction-to-data-science/">
                            Introduction to Data Science
                        </a>
                    </li>
                    <li class="list-group-item">
                        <a href="http://dshatalov.com/2016/04/testing-pelican/">
                            Testing pelican
                        </a>
                    </li>
                </ul>
            </li>




    </ul>
</section>
            </aside>
        </div>
    </div>
</div>
<footer>
   <div class="container">
      <hr>
      <div class="row">
         <div class="col-xs-10">&copy; 2016 
            &middot; Powered by <a href="https://github.com/DandyDev/pelican-bootstrap3" target="_blank">pelican-bootstrap3</a>,
            <a href="http://docs.getpelican.com/" target="_blank">Pelican</a>,
            <a href="http://getbootstrap.com" target="_blank">Bootstrap</a>              <p><small>  <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="//i.creativecommons.org/l/by-nc/4.0/80x15.png" /></a>
    Content
  licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>, except where indicated otherwise.
</small></p>
         </div>
         <div class="col-xs-2"><p class="pull-right"><i class="fa fa-arrow-up"></i> <a href="#">Back to top</a></p></div>
      </div>
   </div>
</footer>
<script src="http://dshatalov.com/theme/js/jquery.min.js"></script>

<!-- Include all compiled plugins (below), or include individual files as needed -->
<script src="http://dshatalov.com/theme/js/bootstrap.min.js"></script>

<!-- Enable responsive features in IE8 with Respond.js (https://github.com/scottjehl/Respond) -->
<script src="http://dshatalov.com/theme/js/respond.min.js"></script>

    <!-- Disqus -->
    <script type="text/javascript">
        /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
        var disqus_shortname = 'dshatalov'; // required: replace example with your forum shortname
        /* * * DON'T EDIT BELOW THIS LINE * * */
        (function () {
            var s = document.createElement('script');
            s.async = true;
            s.type = 'text/javascript';
            s.src = '//' + disqus_shortname + '.disqus.com/embed.js';
            (document.getElementsByTagName('HEAD')[0] || document.getElementsByTagName('BODY')[0]).appendChild(s);
        }());
    </script>
    <!-- End Disqus Code -->
    <!-- Google Analytics -->
    <script type="text/javascript">
        var _gaq = _gaq || [];
        _gaq.push(['_setAccount', 'UA-76746335-1']);
        _gaq.push(['_trackPageview']);
        (function () {
            var ga = document.createElement('script');
            ga.type = 'text/javascript';
            ga.async = true;
            ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
            var s = document.getElementsByTagName('script')[0];
            s.parentNode.insertBefore(ga, s);
        })();
    </script>
    <!-- End Google Analytics Code -->

    <script type="text/javascript" src="//s7.addthis.com/js/300/addthis_widget.js#pubid=ra-572d3e8d9f519dfd"></script>
</body>
</html>
