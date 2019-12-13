(function($) {
    "use strict";

    $(document).ready(function() {


        /*=========================================================================
         ===  MENU SCROLL FIXED
         ========================================================================== */
        var s = $(".lgx-header-position");
        var pos = s.position();

        $(window).on('scroll', function() {
            var windowpos = $(window).scrollTop();
            if (windowpos >= pos.top) {
                s.addClass("menu-onscroll");
            } else {
                s.removeClass("menu-onscroll");
            }
        });

        /*=========================================================================
         ===  // SITE PATH
         ========================================================================== */
        // var lgx_path = window.location.protocol + '//' + window.location.host;
        // var pathArray = window.location.pathname.split('/');
        // for (var i = 1; i < (pathArray.length - 1); i++) {
        //     lgx_path += '/';
        //     lgx_path += pathArray[i];
        // }

        /*=========================================================================
         ===  COUNTER START
         ========================================================================== */
        var lgxCounter = $('.lgx-counter');
        if (lgxCounter.length) {
            lgxCounter.counterUp({
                delay: 10,
                time: 5000
            });
        }

        /*=========================================================================
         ===  countdown
         ========================================================================== */
        if ($('#lgx-countdown').length) {

            var dataTime = $('#lgx-countdown').data('date'); // Date Format : Y/m/d

            $('#lgx-countdown').countdown(dataTime, function(event) {
                var $this = $(this).html(event.strftime(''
                    /*+ '<span class="lgx-weecks">%w <i> weeks </i></span> '*/
                    +
                    '<span class="lgx-days">%D <i> Days </i></span> ' +
                    '<span class="lgx-hr">%H <i> Hour </i></span> ' +
                    '<span class="lgx-min">%M <i> Min </i></span> ' +
                    '<span class="lgx-sec">%S <i> Sec </i></span>'
                ));
            });
        }

        /*=========================================================================
         ===  countdown END
         ========================================================================== */


        /*=========================================================================
         ===  SMOOTH SCROLL - REQUIRES JQUERY EASING PLUGIN
         ========================================================================== */

        $('a.lgx-scroll').on('click', function(event) {
            var $anchor = $(this);
            var topTo = $($anchor.attr('href')).offset().top;

            if (window.innerWidth < 768) {
                topTo = (topTo - 90);
            }

            $('html, body').stop().animate({
                scrollTop: topTo
            }, 1500, 'easeInOutExpo');
            event.preventDefault();
            return false;
        });

        /*=========================================================================
         ===  SMOOTH SCROLL END
         ========================================================================== */


        // HEADER DISPLAY FLEX ISSUE
        if ($(window).width() < 787) {
            $('#navbar').removeClass('lgx-collapse');
        }


        /*=========================================================================
         ===  Start Contact Form Validation And Ajax Submission END
         ========================================================================== */

    }); //DOM READY


})(jQuery);