
jQuery(document).ready(function () {
    (function($) {
        "use strict"; // Start of use strict

        // jQuery for page scrolling feature - requires jQuery Easing plugin
        $('a.page-scroll').bind('click', function(event) {
            var $anchor = $(this);
            $('html, body').stop().animate({
                scrollTop: ($($anchor.attr('href')).offset().top - 50)
            }, 1250, 'easeInOutExpo');
            event.preventDefault();
        });

        // Highlight the top nav as scrolling occurs
        $('body').scrollspy({
            target: '.navbar-fixed-top',
            offset: 51
        });

        // Closes the Responsive Menu on Menu Item Click
        $('.navbar-collapse ul li a').click(function() {
            $('.navbar-toggle:visible').click();
        });

        // Offset for Main Navigation
        $('#mainNav').affix({
            offset: {
                top: 100
            }
        })

        // Initialize and Configure Scroll Reveal Animation
        window.sr = ScrollReveal();
        sr.reveal('.sr-icons', {
            duration: 600,
            scale: 0.3,
            distance: '0px'
        }, 200);
        sr.reveal('.sr-button', {
            duration: 1000,
            delay: 200
        });
        sr.reveal('.sr-contact', {
            duration: 600,
            scale: 0.3,
            distance: '0px'
        }, 300);

        // Initialize and Configure Magnific Popup Lightbox Plugin
        $('.popup-gallery').magnificPopup({
            delegate: 'a',
            type: 'image',
            tLoading: 'Loading image #%curr%...',
            mainClass: 'mfp-img-mobile',
            gallery: {
                enabled: true,
                navigateByImgClick: true,
                preload: [0, 1] // Will preload 0 - before current, and 1 after the current image
            },
            image: {
                tError: '<a href="%url%">The image #%curr%</a> could not be loaded.'
            }
        });

        scrollToTop();

    })(jQuery); // End of use strict
});

// Scroll to top
function scrollToTop() {
    if ($('.scroll-top').length) {

        //Check to see if the window is top if not then display button
        $(window).scroll(function() {
            if ($(this).scrollTop() > 200) {
                $('.scroll-top').fadeIn();
            } else {
                $('.scroll-top').fadeOut();
            }
        });

        //Click event to scroll to top
        $('.scroll-top').click(function() {
            $('html, body').animate({ scrollTop: 0 }, 1500);
            return false;
        });
    }
}

// Language switcher
function languageSwitcher() {
    if ($("#polyglot-language-options").length) {
        $('#polyglotLanguageSwitcher').polyglotLanguageSwitcher({
            effect: 'slide',
            animSpeed: 150,
            testMode: false,
            pagePrefix: '',
            paramName: 'language',
            paramNextUrl: 'next',
            onChange: function(evt) {
            }
        });
    }
}

// carousel
function reviewsCarousel() {
    /**
     * Создает слайдер для отзывов
     * https://owlcarousel2.github.io/OwlCarousel2/
     */
    $(".reviews-carousel").each(function() {
        $(this).on('initialized.owl.carousel resized.owl.carousel', function(event) {
            /**
             * Скрывает стрелки навигации по слайдам. Если ширина области просмотра:
             * <ul>
             * <li>больше 1000px, при количестве элементов меньше либо равно 4
             * <li>от 992px до 1000px, при количестве элементов меньше либо равно 3
             * <li>от 667px до 992px, при количестве элементов меньше либо равно 2
             * <li>до 667px, при количестве элементов равно 1
             * </ul>
             */
            let items = event.item.count;
            let $owlControls = $(this).children('.owl-controls');

            if (window.matchMedia("(min-width: 1000px)").matches) {
                items <= 4 ? $owlControls.hide() : $owlControls.show();
            } else if (window.matchMedia("(min-width: 999px)").matches) {
                items <= 3 ? $owlControls.hide() : $owlControls.show();
            } else if (window.matchMedia("(min-width: 599px)").matches) {
                items <= 2 ? $owlControls.hide() : $owlControls.show();
            } else {
                items <= 1 ? $owlControls.hide() : $owlControls.show();
            }
        });

        $(this).owlCarousel({
            loop: true,
            items: 4,
            margin: 30,
            nav: true,
            navText: [
                '<i class="fa fa-angle-left"></i>',
                '<i class="fa fa-angle-right"></i>'
            ],
            dots: false,
            autoWidth: false,
            autoplay:true,
            autoplayTimeout:3000,
            autoplayHoverPause:true,
            responsive: {
                0: {
                    items: 1,
                    autoWidth: false
                },
                480: {
                    items: 1,
                    autoWidth: false
                },
                600: {
                    items: 2,
                    autoWidth: false
                },
                768: {
                    items: 3,
                    autoWidth: false
                },
                1000: {
                    items: 4,
                    autoWidth: false
                }
            }
        });
    });
}

// instance of function while Window Load event
jQuery(window).load(function () {
    (function ($) {
        languageSwitcher();
        reviewsCarousel();
    })(jQuery);
});
