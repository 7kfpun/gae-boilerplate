(function(){
$.extend(_fw.meth,{  
  forms:{
    target:'input[type=text],input[type=password],input[type=tel],input[type=email],textarea',
    buttons:'a[rel=reset],a[rel=submit]',
    event:'click',
    validate:true,
    invalidCl:'invalid',
    errorCl:'error',
    errorMsg:'Please enter a valid values',
    mailHandlerURL:'/contact/',
    ownerEmail:'mona@getmewrite.com',
    stripHTML:true,
    smtpMailServer:'localhost',
    backBu:false,
    responseHTML:'<div class="contact-form-response"><p>Contact form submitted!<br>We will be in touch soon.</p><br></div>',
    afterFu:function(){},
    errorShow:function(el){
      var _=this
      el.parent().addClass(_.invalidCl)
    },
    errorHide:function(el){
      var _=this
      el.parent().removeClass(_.invalidCl)
    },
    validateFu:function(el,type){
      var _=this
      ;({
        name:function(){return /^[a-zA-Z'][a-zA-Z-' ]+[a-zA-Z']?$/.test(this.val())},
        email:function(){return /^(("[\w-\s]+")|([\w-]+(?:\.[\w-]+)*)|("[\w-\s]+")([\w-]+(?:\.[\w-]+)*))(@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$)|(@\[?((25[0-5]\.|2[0-4][0-9]\.|1[0-9]{2}\.|[0-9]{1,2}\.))((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\.){2}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\]?$)/i.test(this.val())},
        tel:function(){return /^\+?(\d[\d\-\+\(\) ]{5,}\d$)/.test(this.val())}
      })[type].call(el)
      ?_.errorHide(el)
      :_.errorShow(el)
    },
    valFu:function(){
      var _=this,
        elms=_.elms=
      ([$('input.name',_.form).each(function(){
        var th=$(this).bind('blur vldtn',function(){
          _.validateFu(th,'name')
        })
      }),
      $('[type=email]',_.form).each(function(){
        var th=$(this).bind('blur vldtn',function(){
          _.validateFu(th,'email')
        })
      }),
      $('[type=tel]',_.form).each(function(){
        var th=$(this).bind('blur vldtn',function(){
          _.validateFu(th,'tel')
        })
      }),
      $('textarea',_.form).each(function(){
        var th=$(this).bind('blur vldtn',function(){
          if(this.value.length<20)
            _.errorShow(th)
          else
            _.errorHide(th)
        })
      })])
    },
    submitFu:function(){
      var _=this,
        datas={}
      $(_.elms).each(function(){
        $(this).trigger('vldtn')
      })
      if(_.form.has('.'+_.invalidCl).length)
        alert(_.errorMsg)
      else
        datas={
          name:$('.name',_.form).val(),
          email:$('.email',_.form).val(),
          subject:$('.subject',_.form).val(),
          body:$('.body',_.form).val(),
          owner_email:_.ownerEmail,
          stripHTML:_.stripHTML
        },
        $.ajax({
          type: "POST",
          url:_.mailHandlerURL,
          data:datas,
          success: function(){
            _.showFu()
          }
        })      
    },
    showFu:function(){
      var opt=this
      opt.form.parent().height(opt.form.parent().height())
      opt.form.fadeOut(function(){
        opt.response=$('<div>'+opt.responseHTML+'</div>')
          .width(opt.form.width())
          .css({minHeight:opt.form.outerHeight(),width:opt.form.outerWidth()})
        if(opt.backBu)
          opt.backBu=$(opt.backBu),
          opt.response.append(opt.backBu),
          opt.backBu.click(function(){
            opt.hideResFu()
            opt.form[0].reset()
            return false
          })
        opt.form.before(opt.response)
        opt.form.parent().height('auto')
        
        opt.afterFu()
      })
    },
    hideResFu:function(){
      var opt=this
      opt.form.parent().height(opt.form.parent().height())
      opt.response.remove()
      opt.form.fadeIn(function(){
        opt.form.parent().height('auto')
      })
    },    
    init:function(opt){
      var form=opt.form=this,
        inputs=opt.inputs=$(opt.target,form)
      if(opt.validate)
        opt.valFu()
      inputs.each(function(){
        var th=$(this)
        th.data({defValue:th.attr('value')})
        th
          .bind('focus',function(){
            if(th.attr('value')==th.data('defValue'))
              th.attr({value:''})
          })
          .bind('blur',function(){
            if(th.attr('value')=='')
              th.attr({value:th.data('defValue')})
          })          
      })
      $(opt.buttons,form).each(function(){
        var th=$(this)
        th.bind(opt.event,function(){
          if(this.rel=='submit')
            opt.submitFu()
          else
            form[0][this.rel](),
            form.find('.'+opt.invalidCl).removeClass(opt.invalidCl)
          return false
        })
      })
    }
  },
  gSlider:{
    items:'>li',
    clone:true,
    show:4,
    duration:600,
    easing:'swing',
    cloneCl:'_clone',
    nextBu:false,
    prevBu:false,
    mwFu:function(){
      var _=this
    _.holder
      .bind('mousewheel',function(e,d){
        if(d<0){
          if(_.mousewheel)
            _.mousewheel=false,
            _.changeFu('next'),
            setTimeout(function(){
              _.mousewheel=true
            },140)
        }else{
          if(_.mousewheel)
            _.mousewheel=false,
            _.changeFu('prev'),
            setTimeout(function(){
              _.mousewheel=true
          },140)
        }
        return false
      })
    },
    preFu:function(){
      var _=this,
        itemW=_.itemW=_.itms.outerWidth()+parseInt(_.itms.css('marginRight'))+parseInt(_.itms.css('marginLeft'))
      if(_.clone)
        _.itms.clone().addClass(_.cloneCl).appendTo(_.ul),
          _.itms=$(_.items,_.ul)
      if(_.show)
        _.holder
          .width(itemW*_.show)
          .height(_.itms.height())
          .css({overflow:'hidden',zIndex:1})
      if(_.holder.css('position')=='static')
          _.holder.css({position:'relative',zIndex:1})
      _.ul.css({position:'relative',width:itemW*_.itms.length})
      var tmp=Math.round(_.itms.length/4),
        i=tmp
      while(i--)
        _.ul.find('li').eq(-1).prependTo(_.ul)
      _.ul
        .css({left:(_.sX=-Math.floor(tmp)*itemW)})
    },
    changeFu:function(side){
      var _=this
        itemW=_.itemW
      if(side=='next'||side=='prev')
        if(side=='prev')
          (_.itms=$(_.items,_.ul)).eq(-1)
            .prependTo(
              _.ul
                .stop()
                .css({
                  left:parseInt(_.ul.css('left'))-itemW
                })
            )
        else
          (_.itms=$(_.items,_.ul)).eq(0)
            .appendTo(
              _.ul
                .stop()
                .css({
                  left:parseInt(_.ul.css('left'))+itemW
                })
              )
      _.showFu()
    },
    showFu:function(){
      var _=this
      _.ul
        .stop()
        .animate({
          left:_.sX
        },{
          duration:_.duration,
          easing:_.easing
        })
    },
    init:function(_){
      var holder=_.holder=this,
        ul=_.ul=holder.children('ul'),
        itms=_.itms=$(_.items,_.ul)
      _.preFu()
      if(_.nextBu)
        $(_.nextBu)
          .click(function(){
            _.changeFu('next')
            return false
          })
      if(_.prevBu)
        $(_.prevBu)
          .click(function(){
            _.changeFu('prev')
            return false
          })
      if(_.mousewheel&&$.fn.mousewheel)
          _.mwFu()
    }
  },
  tabs:{
    items:'>ul>li',
    show:0,
    duration:400,
    easing:'swing',
    showEf:'',
    method:'display',
    preFu:function(_){
      if(_.method=='display')
        _.itms=$(_.items,_.me).hide()
      if(_.show!==false)
        _.changeFu(_,_.show)
    },
    navFu:function(str){
      var _=this
      _.n=-1
      _.next=$(str)
      _.showFu(_)
    },
    changeFu:function(_,n){
      if(n==_.n)
        return false
      _.n=n
      _.next=_.itms.eq(n)
      _.showFu(_)
      _.curr=_.next
    },
    hideFu:function(_,fu){
      /*var tmp=_.itms.not(':hidden')
      if(tmp.length)
        tmp.hide(_.showEf,{
          duration:_.duration,
          easing:_.easing,
          complete:function(){
            if(fu)
              fu()
          }
        })
      else
        fu()*/
    },
    showFu:function(_){
      _.itms.hide()
      _.next.fadeIn(_.duration)
      /*_.hideFu(_,function(){
        _.next.fadeIn()
          /*.show(_.showEf,{
            duration:_.duration,
            easing:_.easing
          })*/
      //})      
    },
    nextFu:function(){
      var _=this,
        n=_.n
      _.changeFu(_,++n<_.itms.length?n:0)
    },
    prevFu:function(_){
      var _=this,
        n=_.n
      _.changeFu(_,--n>=0?n:_.itms.length-1)
    },
    init:function(_){
      _.me=this
      _.preFu(_)      
    }
  },
  navs:{
    currentCl:'active',
    changeEv:'click',
    navLink:'a[rel=nav]',
    backLink:'a[rel=back]',
    area:'>a',
    hover:false,
    show:false,
    showFu:function(){},
    hideFu:function(){},
    click:false,
    navFu:function(){
      var _=this
      $(_.navLink)
        .live('click',function(){
          _.prev=_.li.parent().find('>.'+_.currentCl).data('num')
          _.li.removeClass(_.currentCl)
          _.refreshFu()
          _.click($(this).attr('href'))
          return false
        })
      $(_.backLink)
        .live('click',function(){
          _.changeFu(_,_.prev)
          return false
        })
    },
    preFu:function(_){
      _.li.each(function(i){
        $(this).data({num:i})
      })
    },
    hoverFu:function(){
      var _=this
      _.li
        .each(function(){
          var th=$(this)
            .bind('mouseleave',function(){
              if(!th.hasClass(_.currentCl))
                _.hideFu(th)
            })
            .bind('mouseenter',function(){
                _.showFu(th)
            })
          
            
        })
    },
    refreshFu:function(){
      var _=this
      _.li
        .each(function(i){
          var th=$(this)
          if(th.hasClass(_.currentCl))
            _.curr=th,
            _.n=i
        })
      if(_.n!==false)
        _.hideFu(_.li.not(_.curr)),
        _.showFu(_.curr)
    },
    changeFu:function(_,n){
      _.li.removeClass(_.currentCl)
      _.li.eq(n).addClass(_.currentCl)
      _.refreshFu()
      _.click(n)
    },
    init:function(_){
      _.me=_.holder=this
      _.ul=$('>ul',_.me)
      _.li=$('>li',_.ul)
      
      _.preFu(_)
      
      if(_.show===false)
        _.n=false
      
      if(_.click!==false)
        $(_.area,_.li).bind(_.changeEv,function(){
          _.changeFu(_,$(this).parent().data('num'))
          return false
        })

      _.refreshFu()
      
      if(_.hover)
        _.hoverFu()
      
      _.navFu()
    }
  }
})

$.fn.extend({
  tabs:function(opt){
    var th=this,
      _=th.data('tabs'),
      ret=false
    if(_)
      ret=(function(opt){
        return({
          number:function(n){
            _.changeFu(_,n)
            return _
          },
          object:function(obj){
            $.extend(_,obj)
            return _
          },
          string:function(str){
            _.navFu(str)
            return _
          },
          undefined:function(){
            return _
          }
        })[typeof opt](opt)
      })(opt)
    else
      ret=(function(opt){
        return({
          number:function(n){
            th._fw({tabs:{show:n}})
            return th.data('tabs')
          },
          object:function(obj){
            th._fw({tabs:opt})
            return th.data('tabs')
          },
          string:function(str){
            th.tabs().navFu(str)
            return _
          },
          undefined:function(){
            th._fw({tabs:{}})
            return th.data('tabs')
          }
        })[typeof opt](opt)
      })(opt)
    return ret||this    
  },
  navs:function(opt){
    var th=this,
      _=th.data('navs'),
      ret=false
    if(_)
      ret=(function(opt){
        return({
          number:function(n){
            _.changeFu(_,n)
            return _
          },
          object:function(obj){
            $.extend(_,obj)
            return _
          },
          string:function(str){
            if(str=='next')
              _.nextFu(_)
            if(str=='prev')
              _.prevFu(_)
            return _
          },
          undefined:function(){
            return _
          }
        })[typeof opt](opt)
      })(opt)
    else
      ret=(function(opt){
        return({
          number:function(n){
            th._fw({navs:{show:n}})
            return _
          },
          object:function(obj){
            th._fw({navs:opt})
            return _
          },
          undefined:function(){
            th._fw({navs:{}})
            return _
          }
        })[typeof opt](opt)
      })(opt)
    return ret||this    
  }
})

  

})(jQuery)
