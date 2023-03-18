$(document).ready(function(){

    // navBar
    var nav_header = $('.header').offset().top;
    var nav_first = $('.ideas').offset().top-20;
    var nav_second = $('.intro').offset().top-20;
    var nav_thirth = $('.course').offset().top-20;
    var nav_fourth = $('.envir').offset().top-50;
    var nav_fifth = $('.award').offset().top-30;
    var nav_sixth = $('.footer').offset().top;

    function navBarScroll(click,target){
        $(click).click(function(){
            $('html,body').animate({scrollTop:target},1000);
        });
    }
    navBarScroll('.header .btn',nav_first);
    navBarScroll('.navBar .brand',nav_header);
    navBarScroll('.footer .title',nav_header);
    navBarScroll('.navBar li.list_first',nav_first);
    navBarScroll('.navBar li.list_second',nav_second);
    navBarScroll('.navBar li.list_thirth',nav_thirth);
    navBarScroll('.navBar li.list_fourth',nav_fourth);
    navBarScroll('.navBar li.list_fifth',nav_fifth);
    navBarScroll('.navBar li.list_sixth',nav_sixth);

    // header
    var slideShow = 1;
    function slideNow(target){
        $('.header ul li').removeClass('show');
        $(target).addClass('show');
    }
    function slideShowFn(){
        if(slideShow == 4) {
            slideShow = 1;
        }
        $('.header .main').removeClass('first');
        $('.header .main').removeClass('second');
        $('.header .main').removeClass('thirth');
        if(slideShow == 1) {
            $('.header .main').addClass('first');
            slideNow('.header ul li.page1')
        }else if(slideShow == 2) {
            $('.header .main').addClass('second');
            slideNow('.header ul li.page2')
        }else if(slideShow == 3) {
            $('.header .main').addClass('thirth');
            slideNow('.header ul li.page3')
        }
    }
    slideShowFn();
    slideShow += 1;

    $(window).scroll(function(){
        var scroll = $('html,body').scrollTop();
        $('.navBar .brand').removeClass('hide');

        if(scroll >= nav_sixth-10) {
            $('.navBar').removeClass('show');
            $('.navBar .brand').addClass('hide');
        }else if(scroll != 0) {
            $('.navBar').addClass('show');         
        }else {
            $('.navBar').removeClass('show');
        }

        function navBarList(min,max,aim){
            if(scroll >= min-10 & scroll < max-10){
                $('.navBar li').removeClass('now');
                $('.navBar li'+aim).addClass('now');
            }else if(aim == 'none'){
                $('.navBar li').removeClass('now');
            }
        }
        navBarList(nav_header,nav_first,'none');
        navBarList(nav_first,nav_second,'.list_first');
        navBarList(nav_second,nav_thirth,'.list_second');
        navBarList(nav_thirth,nav_fourth,'.list_thirth');
        navBarList(nav_fourth,nav_fifth,'.list_fourth');
        navBarList(nav_fifth,nav_sixth,'.list_fifth');
        navBarList(nav_sixth,nav_sixth+100,'.list_sixth');

    });

    var timer = setInterval(function(){
        slideShowFn();
        slideShow += 1;
    },7000);
    function stopTimer(n){
        clearInterval(n);
        console.log('stop '+n+' auto play')
    }
    
    $('.header ul li.page1').click(function(){
        slideShow = 1;
        stopTimer('timer');
        slideShowFn();
    });
    $('.header ul li.page2').click(function(){
        slideShow = 2;
        stopTimer('timer');
        slideShowFn();
    });
    $('.header ul li.page3').click(function(){
        slideShow = 3;
        stopTimer('timer');
        slideShowFn();
    });
    $('.header ul li').click(function(){
        slideNow(this);
    });


    // envir
    var envirShow = 1;
    function envirNow(target){
        $('.envir ul li').removeClass('show');
        $(target).addClass('show');
    }
    function envirShowFn(){
        if(envirShow == 5) {
            envirShow = 1;
        }
        $('.envir .main').removeClass('first');
        $('.envir .main').removeClass('second');
        $('.envir .main').removeClass('thirth');
        $('.envir .main').removeClass('fourth');
        if(envirShow == 1) {
            $('.envir .main').addClass('first');
            envirNow('.envir ul li.page1');
        }else if(envirShow == 2) {
            $('.envir .main').addClass('second');
            envirNow('.envir ul li.page2');
        }else if(envirShow == 3) {
            $('.envir .main').addClass('thirth');
            envirNow('.envir ul li.page3');
        }else if(envirShow == 4) {
            $('.envir .main').addClass('fourth');
            envirNow('.envir ul li.page4');
        }
    }
    envirShowFn();
    envirShow += 1;

    var timer_envir = setInterval(function(){
        envirShowFn();
        envirShow += 1;
    },7000);

    $('.envir ul li.page1').click(function(){
        envirShow = 1;
        stopTimer('timer_envir');
        envirShowFn();
    });
    $('.envir ul li.page2').click(function(){
        envirShow = 2;
        stopTimer('timer_envir');
        envirShowFn();
    });
    $('.envir ul li.page3').click(function(){
        envirShow = 3;
        stopTimer('timer_envir');
        envirShowFn();
    });
    $('.envir ul li.page4').click(function(){
        envirShow = 4;
        stopTimer('timer_envir');
        envirShowFn();
    });
    $('.envir ul li').click(function(){
        envirNow(this);
    });


    // rwd
    $('.navBar ul .close').click(function(){
        $('.navBar ul').toggleClass('hide');
    });
    $('.navBar ul li').click(function(){
        $('.navBar ul').toggleClass('hide');
    });
})

