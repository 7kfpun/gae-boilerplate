function show_splash(){
  var ssDuration=600,
    ssEasing='easeOutBounce',
    navDuration=200,
    navEasing='easeOutQuint'
  var content=$('#content'),
    nav=$('nav>ul>li>a')
  content
    .fadeOut(400,function(){
      nav.each(function(){
        var th=$(this),
          span=$('span',th)
        span
          .stop()
          .animate({top:'-100%'})
        th
          .unbind('mouseenter mouseleave')
          .stop()
          .animate({
            height:496,
            paddingBottom:10
          },{
            duration:ssDuration,
            easing:ssEasing,
            complete:function(){
              $(this)
                .bind('mouseenter',function(){
                  var th=$(this)
                  th
                    .stop()
                    .animate({
                      backgroundPosition:'0px -20px'
                    },{
                      duration:navDuration,
                      easing:navEasing
                    })
                })
                .bind('mouseleave',function(){
                  var th=$(this)
                  th
                    .stop()
                    .animate({
                      backgroundPosition:'0px 0px'
                    },{
                      duration:navDuration,
                      easing:navEasing
                    })
                })
            }
          })          
        th.parent()
          .stop()
          .animate({
            height:516,
            borderBottom:0
          },{
            duration:ssDuration,
            easing:ssEasing
          })
      })
    })
  $('.sf').removeClass('sf-js-enabled')
  $('.backBu').fadeOut()
  splash=true
}

function show_subpages(){  
  var ssDuration=600,
    ssEasing='easeOutBounce'
  $('nav>ul>li>a').each(function(){
    var th=$(this),
      span=$('span',th)
    span
      .show()
      .css({position:'absolute',top:'-100%'})
    th
      .unbind('mouseenter mouseleave')
      .stop()
      .animate({
        backgroundPosition:'0px 0px',
        height:73
      },{
        duration:ssDuration,
        easing:ssEasing,        
        complete:function(){
          th
            .css({paddingBottom:0})
          span            
            .stop()
            .animate({top:0},{duration:300})
          th.parent()
            .stop()
            .css({
              borderBottom:'1px '+th.css('backgroundColor')+' solid',
              height:73
            })
            .animate({            
              borderBottomWidth:10
            },{
              duration:200
            })
        }
      })
  })
  setTimeout(function(){
    var content=$('#content'),
      navs=$('nav')
    content
      .show()        
      .tabs({
        duration:200,
        showEf:''
      })
    navs.navs().refreshFu()
    $('.sf').addClass('sf-js-enabled')
    $('.backBu').fadeIn()
  },ssDuration)
}

$(window).load(function(){
  $('.gspinner').fadeOut()
  
  var ul=$('.scroll-wrap ul'),
    ulW=ul.width()-ul.parent().width(),
    slider=$('.track>div')
  
  slider.slider({
    min:1,max:100,value:0,
    slide:function(e,ui){
      ul
        .stop()
        .animate({left:-ui.value*ulW/100},1000)
    },
    change:function(e,ui){
      ul
        .stop()
        .animate({left:-ui.value*ulW/100},1000)
    }
  })
  
  $('.scroll-wrap .lf')
    .click(function(){
      var curr=slider.slider('value')
      curr-=20
      slider.slider('value',curr=curr>0?curr:1)
      return false
    })
  $('.scroll-wrap .rg')
    .click(function(){
      var curr=slider.slider('value')
      curr+=20
      slider.slider('value',curr=curr<ulW?curr:ulW)
      return false
    })
})

$(function(){
  window.splash=true
  var content=$('#content'),
    navs=$('nav')
  navs
    .navs({
      hover:true,
      click:function(n){
        if(splash)
          show_subpages(),
          splash=false          
        //Cufon.refresh()
        content.tabs(n)
      }        
    })
  content.show()
  var gSlider=$('.gSlider')
    ._fw({
      gSlider:{
        easing:'easeOutBack',
        duration:1000,
        clone:true,
        show:4,
        mousewheel:true
      }
    }).width(940)
    .data('gSlider')
  $('.gSlider-controls .prev').click(function(){
    gSlider.changeFu('prev')
    return false
  })
  $('.gSlider-controls .next').click(function(){
    gSlider.changeFu('next')
    return false
  })
  $('#form1')._fw({
    forms:{
      backBu:'<a href="#" class="btn">back</a>'
    }
  })
  content.hide()
  
  
  $('.more')
    .bind('mouseenter',function(){
      $(this)
        .stop()
        .animate({
          color:'#9e702a',
          backgroundColor:'#fff'
        },{
          duration:400,
          easing:'easeInQuint'
        })
    })
    .bind('mouseleave',function(){
      $(this)
        .stop()
        .animate({
          color:'#fff',
          backgroundColor:'#e3a13c'
        },{
          duration:400,
          easing:'easeOutQuint'
        })
    })
  $('#form1 .btns a')
    .bind('mouseenter',function(){
      $(this)
        .stop()
        .animate({
          color:'#000',
          backgroundColor:'#fff'
        },{
          duration:400,
          easing:'easeInQuint'
        })
    })
    .bind('mouseleave',function(){
      $(this)
        .stop()
        .animate({
          color:'#fff',
          backgroundColor:'#4061a3'
        },{
          duration:400,
          easing:'easeOutQuint'
        })
    })
  $('.list a')
    .bind('mouseenter',function(){
      $(this)
        .stop()
        .animate({
          color:'#6c6721',
          paddingLeft:18
        },{
          duration:100,
          easing:'easeInQuint'
        })
        .animate({
          paddingLeft:28
        },{
          duration:100
        })
    })
    .bind('mouseleave',function(){
      $(this)
        .stop()
        .animate({
          color:'#fff',
          paddingLeft:28
        },{
          duration:200,          
          easing:'easeOutQuint'
        })
    })
    
  show_splash()
  
  $('.sf').superfish()
  $('.sf').removeClass('sf-js-enabled')
  
  $(".scroll-wrap li a").fancybox();
  
  $('.backBu').click(function(){
    $('nav li a').trigger('mouseout')
    show_splash()
    return false
  }).hide()

  $('h1 a').click(function() {
    show_splash();
  })
})
