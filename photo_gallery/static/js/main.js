AOS.init({
    duration: 800,
    easing: 'slide',
    once: false
});
jQuery(document).ready(function ($) {
    "use strict";
    $('#opensearchBox').click(
        function () {
            $("#searchbarOverlay").toggle();
        }
    )
    $.ajax({
        type: 'GET',
        url: "http://localhost:8000/categories/all"
    }).then(function (data) {
        data.data.map(element => {
            var option = new Option(element.name, element.id, false, false);
            console.log(option)
            $('#category_id').append(option).trigger('change')
        })
    });
    $.ajax({
        type: 'GET',
        url: "http://localhost:8000/locations/all"
    }).then(function (data) {
        data.data.map(element => {
            var option = new Option(element.name, element.id, false, false);
            $('#location_id').append(option).trigger('change')
        })
    });


    $('#category_id').select2({
        placeholder: 'Select category',
    })
    $('#location_id').select2({
        placeholder: 'Select location',
    })
    $('#closeSearchBox').click(
        function () {
            $("#searchbarOverlay").toggle();
        }
    )
    var closeSearch = function () {
        $("#searchbarOverlay").style.display = "none";
    }
    $('#searchForm').on('submit'
        , function (form) {
            form.preventDefault()
            console.log($(form).serialize())
            const location_id = $('#location_id').val()
            const category_id = $('#category_id').val()
            if (location_id && category_id) {
                $('#searchResult').html(
                    `
								<div class='row align-content-stretch'>
								 <div class="col-12">
       								 <h2 class="text-white mb-4">Searching</h2>
   								 </div>								
								</div>
								`
                )

                $.ajax(
                    {
                        data: {location_id, category_id},
                        type: 'GET',
                        url: "http://localhost:8000/images/search",
                        success: function (response) {
                            if (response.data && response.data.length > 0) {
                                const jsonRes = response.data
                                console.log(jsonRes)
                                $('#searchResult').html(
                                    `
								<div class='row align-content-stretch'>
								 <div class="col-12">
       								 <h2 class="text-white mb-4">'${jsonRes.length}' results found</h2>
   								 </div>								
								</div>
								`
                                )
                                jsonRes.map(element => $('#searchResult .row').append(`
<div class="col-6 col-md-6 col-lg-3 aos-init" data-aos="fade-up" data-aos-delay="200">
            <a href="${element.url}" class="d-block photo-item" data-fancybox="gallery" data-caption="'${element.name}' was shot at '${element.location}' and belongs to '${element.category}'">
                <img src="${element.url}" alt="${element.name}" class="img-fluid">
                <div class="photo-text-more">
                    <span class="icon icon-search"></span>
                </div>
            </a>
        </div>
						`))
                            } else {
                                $('#searchResult').html(`
    <div class="col-12">
        <h2 class="text-white mb-4">OOPS! No result found</h2>
    </div>`)
                            }
                        }
                    }
                )
            }

        })


    var siteMenuClone = function () {

        $('.js-clone-nav').each(function () {
            var $this = $(this);
            $this.clone().attr('class', 'site-nav-wrap').appendTo('.site-mobile-menu-body');
        });



        $(window).resize(function () {
            var $this = $(this),
                w = $this.width();

            if (w > 768) {
                if ($('body').hasClass('offcanvas-menu')) {
                    $('body').removeClass('offcanvas-menu');
                }
            }
        })

        $('body').on('click', '.js-menu-toggle', function (e) {
            var $this = $(this);
            e.preventDefault();

            if ($('body').hasClass('offcanvas-menu')) {
                $('body').removeClass('offcanvas-menu');
                $this.removeClass('active');
            } else {
                $('body').addClass('offcanvas-menu');
                $this.addClass('active');
            }
        })
        $(document).mouseup(function (e) {
            var container = $(".site-mobile-menu");
            if (!container.is(e.target) && container.has(e.target).length === 0) {
                if ($('body').hasClass('offcanvas-menu')) {
                    $('body').removeClass('offcanvas-menu');
                }
            }
        });
    };
    siteMenuClone();
    $.fancybox.defaults.buttons = [
        'slideShow',
        'share',
        'zoom',
        'fullScreen',
        'close'
    ];
    const typed = new Typed('.homepage-main-text', {
        strings: [
            "Welcome ^1000<br> to ^1000<br> photo ^1000<br> <b>Gallery</b>"],
        typeSpeed: 20
    })
});