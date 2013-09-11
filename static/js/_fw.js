//CORE
;(function($,undefined){
  var _timer=[],
    _fw=window._fw=$.fn._fw=function(_){
      var i,name=[]
      for(i in _)
        if(_.hasOwnProperty(i))
          name.push(i)
      $(this).each(function(){
        for(var i=0,opt={};i<name.length;i++)
          if(_fw.meth[name[i]])            
            $.extend(opt,clone(_fw.meth[name[i]]),_[name[i]]),
            opt.init.call($(this).data(name[i],opt),opt)
      })
      return this
    },
    _meth=_fw.meth={},
    _hlp=_fw.hlp={
      clone:function(obj){
        if(!obj||typeof obj!=typeof {})
          return obj
        if(obj instanceof Array)
          return [].concat(obj)
        var tmp=new obj.constructor(),
          i
        for(i in obj)
          if(obj.hasOwnProperty(i))
            tmp[i]=clone(obj[i])
        return tmp
      },
      srlz:function(str){
        if(!str)
          return {}
        str=str.split(/[\/&]/)
        for(var i=0,tmp,ret={};i<str.length;i++)
          if(str[i])
            tmp=str[i].split('='),
            ret[tmp[1]?tmp[0]:i]=tmp[1]?tmp[1]:tmp[0]
        return ret
      },
      dStr:function(obj){
        var key,
          ret=''
        for(key in obj)
          if(obj.hasOwnProperty(key))
            if(key/1==''/1)
              ret+=!ret?obj[key]+'/':obj[key]
            else
              ret+=!ret?key+'='+obj[key]+'&':key+'='+obj[key]
        return ret
      }
    },
    clone=_hlp.clone
})(jQuery)


;(function($){
$.fn.extend({
  wait:function(_fu){
    var cntx=this,
      imgs=[]
    $('img',this).each(function(i){
      imgs[i]=$.Deferred()
      if(this.complete)
        imgs[i].resolve.call(this)
      else
        $(this).load(imgs[i].resolve)
    })
    $.when.apply($,imgs).done(function(){
      _fu.call(cntx)
    })
    return this
  },
  praParent:function(expr,fu){
    var th=this,
      test=function(o){
        var i,
          tf=true
        if(fu)
          fu.call(o)
        if(typeof expr===typeof '')
          return o.is(expr)
        if(typeof expr===typeof {}){
          for(i in expr)
            tf=!!any(o.css(i),expr[i].split(' '))
          return tf
        }
      }
    if(!th.length)return false
    while(th=th.parent())
      if(test(th))
        break
      else
        if(th.is('html'))
          return false
    return th
  }
})
})(jQuery)

;(function($){
var types = ['DOMMouseScroll', 'mousewheel'];
$.event.special.mousewheel = {
  setup: function() {
    if ( this.addEventListener )
      for ( var i=types.length; i; )
        this.addEventListener( types[--i], handler, false );
    else
      this.onmousewheel = handler;
  },  
  teardown: function() {
    if ( this.removeEventListener )
      for ( var i=types.length; i; )
        this.removeEventListener( types[--i], handler, false );
    else
      this.onmousewheel = null;
  }
};
$.fn.extend({
  mousewheel: function(fn) {
    return fn ? this.bind("mousewheel", fn) : this.trigger("mousewheel");
  },  
  unmousewheel: function(fn) {
    return this.unbind("mousewheel", fn);
  }
});
function handler(event) {
  var args = [].slice.call( arguments, 1 ), delta = 0, returnValue = true;  
  event = $.event.fix(event || window.event);
  event.type = "mousewheel";  
  if ( event.wheelDelta ) delta = event.wheelDelta/120;
  if ( event.detail     ) delta = -event.detail/3;  
  // Add events and delta to the front of the arguments
  args.unshift(event, delta);
  return $.event.handle.apply(this, args);}
})(jQuery);
//prototype extends
Array.prototype.lastIndexOf=Array.prototype.lastIndexOf||function(val,i){
i=this.length-i||this.length
while(--i^-1)
  if(this[i]==val)
    return i
return -1
}

Array.prototype.indexOf=Array.prototype.indexOf||function(val,i){
i=i-1||-1
while(++i^this.length)
  if(this[i]==val)
    return i
return -1
}
