/********************************************************************
 *	Kalendae, a framework agnostic javascript date picker           *
 *	Copyright(c) 2013 Jarvis Badgley (chipersoft@gmail.com)         *
 *	http://github.com/ChiperSoft/Kalendae                           *
 *	Version 0.4.1                                                   *
 ********************************************************************/

(function(){var t,k,m=function(a,b){if("function"===typeof document.addEventListener||c.isIE8()){var d=!1;try{d=a instanceof Element}catch(l){d=!!a&&1===d.nodeType}d||"string"===typeof a||(b=a);var e=this,g=e.classes,h=e.settings=c.merge(e.defaults,{attachTo:a},b||{}),d=e.container=c.make("div",{"class":g.container}),m=e.calendars=[],v=k().day(h.weekStart),n,p=[],r,q,z;r=[];var t;q=0;n=h.months;c.isIE8()&&c.addClassName(d,"ie8");for(q=7;q--;)p.push(v.format(h.columnHeaderFormat)),v.add("days",1);
B(e);if("object"===typeof h.subscribe)for(q in h.subscribe)h.subscribe.hasOwnProperty(q)&&e.subscribe(q,h.subscribe[q]);e._sel=[];h.selected&&e.setSelected(h.selected,!1);n=h.viewStartDate?k(h.viewStartDate,h.format):0<e._sel.length?k(e._sel[0]):k();e.viewStartDate=n.date(1);if((n={past:h.months-1,"today-past":h.months-1,any:2<h.months?Math.floor(h.months/2):0,"today-future":0,future:0}[this.settings.direction])&&k().month()==k(e.viewStartDate).month())e.viewStartDate=k(e.viewStartDate).subtract({M:n}).date(1);
if("function"===typeof h.blackout)e.blackout=h.blackout;else if(h.blackout){var A=w(h.blackout,h.parseSplitDelimiter,h.format);e.blackout=function(a){a=k(a).yearDay();if(1>a||!e._sel)return!1;for(var d=A.length;d--;)if(A[d].yearDay()===a)return!0;return!1}}else e.blackout=function(){return!1};e.direction=e.directions[h.direction]?e.directions[h.direction]:e.directions.any;for(n=Math.max(h.months,1);n--;){r=c.make("div",{"class":g.calendar},d);r.setAttribute("data-cal-index",n);1<h.months&&(n==Math.max(h.months-
1,1)?c.addClassName(r,g.monthFirst):0===n?c.addClassName(r,g.monthLast):c.addClassName(r,g.monthMiddle));q=c.make("div",{"class":g.title},r);h.useYearNav||c.addClassName(q,g.disableYearNav);c.make("a",{"class":g.previousYear},q);c.make("a",{"class":g.previousMonth},q);c.make("a",{"class":g.nextYear},q);c.make("a",{"class":g.nextMonth},q);v=c.make("span",{"class":g.caption},q);z=c.make("div",{"class":g.header},r);q=0;do t=c.make("span",{},z),t.innerHTML=p[q];while(7>++q);z=c.make("div",{"class":g.days},
r);q=0;for(r=[];42>q++;)r.push(c.make("span",{},z));m.push({caption:v,days:r});n&&c.make("div",{"class":g.monthSeparator},d)}e.draw();c.addEvent(d,"mousedown",function(a,d){var b;if(c.hasClassName(d,g.nextMonth))!e.disableNext&&!1!==e.publish("view-changed",e,["next-month"])&&(e.viewStartDate.add("months",1),e.draw());else if(c.hasClassName(d,g.previousMonth))!e.disablePreviousMonth&&!1!==e.publish("view-changed",e,["previous-month"])&&(e.viewStartDate.subtract("months",1),e.draw());else if(c.hasClassName(d,
g.nextYear))!e.disableNext&&!1!==e.publish("view-changed",e,["next-year"])&&(e.viewStartDate.add("years",1),e.draw());else if(c.hasClassName(d,g.previousYear))!e.disablePreviousMonth&&!1!==e.publish("view-changed",e,["previous-year"])&&(e.viewStartDate.subtract("years",1),e.draw());else if(c.hasClassName(d.parentNode,g.days)&&c.hasClassName(d,g.dayActive)&&(b=d.getAttribute("data-date")))if(b=k(b,h.dayAttributeFormat).hours(12),!1!==e.publish("date-clicked",e,[b]))switch(h.mode){case "multiple":e.addSelected(b)||
e.removeSelected(b);break;case "range":e.addSelected(b);break;default:e.addSelected(b)}return!1});(h.attachTo=c.$(h.attachTo))&&h.attachTo.appendChild(d)}};m.prototype={defaults:{attachTo:null,months:1,weekStart:0,direction:"any",directionScrolling:!0,viewStartDate:null,blackout:null,selected:null,mode:"single",dayOutOfMonthClickable:!1,format:null,subscribe:null,columnHeaderFormat:"dd",titleFormat:"MMMM, YYYY",dayNumberFormat:"D",dayAttributeFormat:"YYYY-MM-DD",parseSplitDelimiter:/,\s*|\s+-\s+/,
rangeDelimiter:" - ",multipleDelimiter:", ",useYearNav:!0,dateClassMap:{}},classes:{container:"kalendae",calendar:"k-calendar",monthFirst:"k-first-month",monthMiddle:"k-middle-month",monthLast:"k-last-month",title:"k-title",previousMonth:"k-btn-previous-month",nextMonth:"k-btn-next-month",previousYear:"k-btn-previous-year",nextYear:"k-btn-next-year",caption:"k-caption",header:"k-header",days:"k-days",dayOutOfMonth:"k-out-of-month",dayInMonth:"k-in-month",dayActive:"k-active",daySelected:"k-selected",
dayInRange:"k-range",dayToday:"k-today",monthSeparator:"k-separator",disablePreviousMonth:"k-disable-previous-month-btn",disableNextMonth:"k-disable-next-month-btn",disablePreviousYear:"k-disable-previous-year-btn",disableNextYear:"k-disable-next-year-btn",disableYearNav:"k-disable-year-nav"},disablePreviousMonth:!1,disableNextMonth:!1,disablePreviousYear:!1,disableNextYear:!1,directions:{past:function(a){return k(a).yearDay()>=t.yearDay()},"today-past":function(a){return k(a).yearDay()>t.yearDay()},
any:function(){return!1},"today-future":function(a){return k(a).yearDay()<t.yearDay()},future:function(a){return k(a).yearDay()<=t.yearDay()}},getSelectedAsDates:function(){for(var a=[],b=0,d=this._sel.length;b<d;b++)a.push(this._sel[b].toDate());return a},getSelectedAsText:function(a){for(var b=[],d=0,c=this._sel.length;d<c;d++)b.push(this._sel[d].format(a||this.settings.format||"YYYY-MM-DD"));return b},getSelectedRaw:function(){for(var a=[],b=0,d=this._sel.length;b<d;b++)a.push(k(this._sel[b]));
return a},getSelected:function(a){a=this.getSelectedAsText(a);switch(this.settings.mode){case "range":return a.splice(2),a.join(this.settings.rangeDelimiter);case "multiple":return a.join(this.settings.multipleDelimiter);default:return a[0]}},isSelected:function(a){a=k(a).yearDay();if(1>a||!this._sel||1>this._sel.length)return!1;switch(this.settings.mode){case "range":var b=this._sel[0]?this._sel[0].yearDay():0,d=this._sel[1]?this._sel[1].yearDay():0;return b===a||d===a?1:!b||!d?0:a>b&&a<d||b<d&&
a<b&&a>d?-1:!1;case "multiple":for(b=this._sel.length;b--;)if(this._sel[b].yearDay()===a)return!0;return!1;default:return this._sel[0]&&this._sel[0].yearDay()===a}},setSelected:function(a,b){var d,c=w(a,this.settings.parseSplitDelimiter,this.settings.format),e=w(this.getSelected(),this.settings.parseSplitDelimiter,this.settings.format);for(d=e.length;d--;)this.removeSelected(e[d],b);for(d=c.length;d--;)this.addSelected(c[d],b);!1!==b&&this.draw()},addSelected:function(a,b){a=k(a,this.settings.format).hours(12);
this.settings.dayOutOfMonthClickable&&"range"!==this.settings.mode&&this.makeSelectedDateVisible(a);switch(this.settings.mode){case "multiple":if(this.isSelected(a))return!1;this._sel.push(a);break;case "range":1!==this._sel.length?this._sel=[a]:a.yearDay()>this._sel[0].yearDay()?this._sel[1]=a:this._sel=[a,this._sel[0]];break;default:this._sel=[a]}this._sel.sort(function(a,b){return a.yearDay()-b.yearDay()});this.publish("change",this,[a]);!1!==b&&this.draw();return!0},makeSelectedDateVisible:function(a){outOfViewMonth=
k(a).date("1").diff(this.viewStartDate,"months");0>outOfViewMonth?this.viewStartDate.subtract("months",1):0<outOfViewMonth&&outOfViewMonth>=this.settings.months&&this.viewStartDate.add("months",1)},removeSelected:function(a,b){a=k(a,this.settings.format).hours(12);for(var d=this._sel.length;d--;)if(this._sel[d].yearDay()===a.yearDay())return this._sel.splice(d,1),this.publish("change",this,[a]),!1!==b&&this.draw(),!0;return!1},draw:function(){var a=k(this.viewStartDate).hours(12),b,d=this.classes,
l,e,g,h=0,m,v=0,n,p=this.settings;m=this.calendars.length;do{b=k(a).date(1);b.day(b.day()<this.settings.weekStart?this.settings.weekStart-7:this.settings.weekStart);l=this.calendars[h];l.caption.innerHTML=a.format(this.settings.titleFormat);v=0;do e=l.days[v],g=[],(n=this.isSelected(b))&&g.push({"-1":d.dayInRange,1:d.daySelected,"true":d.daySelected}[n]),b.month()!=a.month()?g.push(d.dayOutOfMonth):g.push(d.dayInMonth),(!this.blackout(b)&&!(this.direction(b)||b.month()!=a.month()&&!1===p.dayOutOfMonthClickable)||
0<n)&&g.push(d.dayActive),b.yearDay()===t.yearDay()&&g.push(d.dayToday),n=b.format(this.settings.dayAttributeFormat),p.dateClassMap[n]&&g.push(p.dateClassMap[n]),e.innerHTML=b.format(p.dayNumberFormat),e.className=g.join(" "),e.setAttribute("data-date",n),b.add("days",1);while(42>++v);a.add("months",1)}while(++h<m);if(p.directionScrolling){if("today-past"===p.direction||"past"===p.direction)b=a.add({m:1}).diff(k(),"months",!0),0>=b?(this.disableNextMonth=!1,c.removeClassName(this.container,d.disableNextMonth)):
(this.disableNextMonth=!0,c.addClassName(this.container,d.disableNextMonth));else if("today-future"===p.direction||"future"===p.direction)b=a.subtract({m:1}).diff(k(),"months",!0),b>p.months?(this.disablePreviousMonth=!1,c.removeClassName(this.container,d.disablePreviousMonth)):(this.disablePreviousMonth=!0,c.addClassName(this.container,d.disablePreviousMonth));if("today-past"===p.direction||"past"===p.direction)b=a.add({m:12}).diff(k(),"months",!0),-11>=b?(this.disableNextYear=!1,c.removeClassName(this.container,
d.disableNextYear)):(this.disableNextYear=!0,c.addClassName(this.container,d.disableNextYear));else if("today-future"===p.direction||"future"===p.direction)b=a.subtract({m:12}).diff(k(),"months",!0),b>11+p.months?(this.disablePreviousYear=!1,c.removeClassName(this.container,d.disablePreviousYear)):(this.disablePreviousYear=!0,c.addClassName(this.container,d.disablePreviousYear))}}};var w=function(a,b,d){var l=[];"string"===typeof a?a=a.split(b):c.isArray(a)||(a=[a]);b=a.length;var e=0;do a[e]&&l.push(k(a[e],
d).hours(12));while(++e<b);return l};window.Kalendae=m;var c=m.util={isIE8:function(){return!(!/msie 8./i.test(navigator.appVersion)||/opera/i.test(navigator.userAgent)||!window.ActiveXObject||!XDomainRequest||window.msPerformance)},$:function(a){return"string"==typeof a?document.getElementById(a):a},$$:function(a){return document.querySelectorAll(a)},make:function(a,b,d){var c;a=document.createElement(a);if(b)for(c in b)b.hasOwnProperty(c)&&a.setAttribute(c,b[c]);d&&d.appendChild(a);return a},isVisible:function(a){return 0<
a.offsetWidth||0<a.offsetHeight},getStyle:function(a,b){var d;a.currentStyle?d=a.currentStyle[b]:window.getComputedStyle&&(d=window.getComputedStyle(a,null)[b]);return d},domReady:function(a){/in/.test(document.readyState)?setTimeout(function(){c.domReady(a)},9):a()},addEvent:function(a,b,d){var c=function(b){b=b||window.event;var c=d.apply(a,[b,b.target||b.srcElement]);!1===c&&(b.preventDefault?b.preventDefault():(b.returnValue=!1,b.cancelBubble=!0));return c};a.attachEvent?a.attachEvent("on"+b,
c):a.addEventListener(b,c,!1);return c},removeEvent:function(a,b,d){a.detachEvent?a.detachEvent("on"+b,d):a.removeEventListener(b,d,!1)},hasClassName:function(a,b){if(!(a=c.$(a)))return!1;var d=a.className;return 0<d.length&&(d==b||RegExp("(^|\\s)"+b+"(\\s|$)").test(d))},addClassName:function(a,b){if((a=c.$(a))&&!c.hasClassName(a,b))a.className+=(a.className?" ":"")+b},removeClassName:function(a,b){if(a=c.$(a))a.className=c.trimString(a.className.replace(RegExp("(^|\\s+)"+b+"(\\s+|$)")," "))},isFixed:function(a){do if("fixed"===
c.getStyle(a,"position"))return!0;while(a=a.offsetParent);return!1},scrollContainer:function(a){do{var b=c.getStyle(a,"overflow");if("auto"===b||"scroll"===b)return a}while((a=a.parentNode)&&a!=window.document.body);return null},getPosition:function(a,b){var d=a.offsetLeft,c=a.offsetTop,e={};if(!b)for(;a=a.offsetParent;)d+=a.offsetLeft,c+=a.offsetTop;e[0]=e.left=d;e[1]=e.top=c;return e},getHeight:function(a){return a.offsetHeight||a.scrollHeight},getWidth:function(a){return a.offsetWidth||a.scrollWidth},
trimString:function(a){return a.replace(/^\s+/,"").replace(/\s+$/,"")},merge:function(){for(var a=!0===arguments[0],b={},d=a?1:0;d<arguments.length;d++){var c=b,e=arguments[d];if("object"===typeof e){var g=void 0;for(g in e)e.hasOwnProperty(g)&&(a&&"object"===typeof c[g]&&"object"===typeof e[g]?_update(c[g],e[g]):c[g]=e[g])}}return b},isArray:function(a){return"[object Array]"==Object.prototype.toString.call(a)}};"function"===typeof document.addEventListener&&m.util.domReady(function(){for(var a=
c.$$(".auto-kal"),b=a.length,d,l;b--;)d=a[b],l=d.getAttribute("data-kal"),l=null==l||""==l?{}:(new Function("return {"+l+"};"))(),"INPUT"===d.tagName?new m.Input(d,l):new m(c.merge(l,{attachTo:d}))});m.Input=function(a,b){if("function"===typeof document.addEventListener||c.isIE8()){var d=this.input=c.$(a),l,e;if(!d||"INPUT"!==d.tagName)throw"First argument for Kalendae.Input must be an <input> element or a valid element id.";var g=this,h=g.classes;e=g.settings=c.merge(g.defaults,b);e.attachTo=window.document.body;
e.selected?l=!0:e.selected=d.value;m.call(g,e);e.closeButton&&(e=c.make("a",{"class":h.closeButton},g.container),c.addEvent(e,"click",function(){d.blur()}));l&&(d.value=g.getSelected());l=g.container;var k=!1;l.style.display="none";c.addClassName(l,h.positioned);c.addEvent(l,"mousedown",function(){k=!0});c.addEvent(window.document,"mousedown",function(){k=!1});c.addEvent(d,"focus",function(){g.setSelected(this.value);g.show()});c.addEvent(d,"blur",function(){k&&c.isIE8()?(k=!1,d.focus()):g.hide()});
c.addEvent(d,"keyup",function(){g.setSelected(this.value)});(h=c.scrollContainer(d))&&c.addEvent(h,"scroll",function(){d.blur()});g.subscribe("change",function(){d.value=g.getSelected()})}};m.Input.prototype=c.merge(m.prototype,{defaults:c.merge(m.prototype.defaults,{format:"MM/DD/YYYY",side:"bottom",closeButton:!0,offsetLeft:0,offsetTop:0}),classes:c.merge(m.prototype.classes,{positioned:"k-floating",closeButton:"k-btn-close"}),show:function(){var a=this.container,b=a.style,d=this.input,l=c.getPosition(d),
e=c.scrollContainer(d),e=e?e.scrollTop:0,g=this.settings;b.display="";switch(g.side){case "left":b.left=l.left-c.getWidth(a)+g.offsetLeft+"px";b.top=l.top+g.offsetTop-e+"px";break;case "right":b.left=l.left+c.getWidth(d)+"px";b.top=l.top+g.offsetTop-e+"px";break;case "top":b.left=l.left+g.offsetLeft+"px";b.top=l.top-c.getHeight(a)+g.offsetTop-e+"px";break;default:b.left=l.left+g.offsetLeft+"px",b.top=l.top+c.getHeight(d)+g.offsetTop-e+"px"}b.position=c.isFixed(d)?"fixed":"absolute";this.publish("show",
this)},hide:function(){this.container.style.display="none";this.publish("hide",this)}});var B=function(a){a||(a=this);var b=a.c_||{};a.publish=function(a,c,e){for(var g=(a=b[a])?a.length:0,h;g--;)if(h=a[g].apply(c,e||[]),"boolean"===typeof h)return h};a.subscribe=function(a,c,e){b[a]||(b[a]=[]);e?b[a].push(c):b[a].unshift(c);return[a,c]};a.unsubscribe=function(a){var c=b[a[0]];a=a[1];for(var e=c?c.length:0;e--;)c[e]===a&&c.splice(e,1)}};(function(a){function b(f,a){return function(b){return m(f.call(this,
b),a)}}function d(f){return function(a){return this.lang().ordinal(f.call(this,a))}}function c(){}function e(f){h(this,f)}function g(f){var a=this._data={},b=f.years||f.year||f.y||0,d=f.months||f.month||f.M||0,c=f.weeks||f.week||f.w||0,e=f.days||f.day||f.d||0,g=f.hours||f.hour||f.h||0,j=f.minutes||f.minute||f.m||0,h=f.seconds||f.second||f.s||0;f=f.milliseconds||f.millisecond||f.ms||0;this._milliseconds=f+1E3*h+6E4*j+36E5*g;this._days=e+7*c;this._months=d+12*b;a.milliseconds=f%1E3;h+=k(f/1E3);a.seconds=
h%60;j+=k(h/60);a.minutes=j%60;g+=k(j/60);a.hours=g%24;e+=k(g/24);e+=7*c;a.days=e%30;d+=k(e/30);a.months=d%12;b+=k(d/12);a.years=b}function h(f,a){for(var b in a)a.hasOwnProperty(b)&&(f[b]=a[b]);return f}function k(f){return 0>f?Math.ceil(f):Math.floor(f)}function m(f,a){for(var b=f+"";b.length<a;)b="0"+b;return b}function n(f,a,b){var d=a._milliseconds,c=a._days;a=a._months;d&&f._d.setTime(+f+d*b);c&&f.date(f.date()+c*b);a&&(d=f.date(),f.date(1).month(f.month()+a*b).date(Math.min(d,f.daysInMonth())))}
function p(f,a){var b=Math.min(f.length,a.length),d=Math.abs(f.length-a.length),c=0,e;for(e=0;e<b;e++)~~f[e]!==~~a[e]&&c++;return c+d}function r(f){if(!f)return j.fn._lang;!y[f]&&P&&require("./lang/"+f);return y[f]}function q(f){switch(f){case "DDDD":return Q;case "YYYY":return R;case "YYYYY":return S;case "S":case "SS":case "SSS":case "DDD":return T;case "MMM":case "MMMM":case "dd":case "ddd":case "dddd":case "a":case "A":return U;case "X":return V;case "Z":case "ZZ":return I;case "T":return W;case "MM":case "DD":case "YY":case "HH":case "hh":case "mm":case "ss":case "M":case "D":case "d":case "H":case "h":case "m":case "s":return X;
default:return RegExp(f.replace("\\",""))}}function t(f){var a,b=[];if(!f._d){for(a=0;7>a;a++)f._a[a]=b[a]=null==f._a[a]?2===a?1:0:f._a[a];b[3]+=f._tzh||0;b[4]+=f._tzm||0;a=new Date(0);f._useUTC?(a.setUTCFullYear(b[0],b[1],b[2]),a.setUTCHours(b[3],b[4],b[5],b[6])):(a.setFullYear(b[0],b[1],b[2]),a.setHours(b[3],b[4],b[5],b[6]));f._d=a}}function w(f){var a=f._f.match(J),b=f._i,d,c;f._a=[];for(d=0;d<a.length;d++)if((c=(q(a[d]).exec(b)||[])[0])&&(b=b.slice(b.indexOf(c)+c.length)),u[a[d]]){var e=f,g=void 0,
j=e._a;switch(a[d]){case "M":case "MM":j[1]=null==c?0:~~c-1;break;case "MMM":case "MMMM":g=r(e._l).monthsParse(c);null!=g?j[1]=g:e._isValid=!1;break;case "D":case "DD":case "DDD":case "DDDD":null!=c&&(j[2]=~~c);break;case "YY":j[0]=~~c+(68<~~c?1900:2E3);break;case "YYYY":case "YYYYY":j[0]=~~c;break;case "a":case "A":e._isPm="pm"===(c+"").toLowerCase();break;case "H":case "HH":case "h":case "hh":j[3]=~~c;break;case "m":case "mm":j[4]=~~c;break;case "s":case "ss":j[5]=~~c;break;case "S":case "SS":case "SSS":j[6]=
~~(1E3*("0."+c));break;case "X":e._d=new Date(1E3*parseFloat(c));break;case "Z":case "ZZ":e._useUTC=!0;if((g=(c+"").match(Y))&&g[1])e._tzh=~~g[1];g&&g[2]&&(e._tzm=~~g[2]);g&&"+"===g[0]&&(e._tzh=-e._tzh,e._tzm=-e._tzm)}null==c&&(e._isValid=!1)}f._isPm&&12>f._a[3]&&(f._a[3]+=12);!1===f._isPm&&12===f._a[3]&&(f._a[3]=0);t(f)}function A(f,a,b,c,d){return d.relativeTime(a||1,!!b,f,c)}function F(f,a,b){a=b-a;b-=f.day();b>a&&(b-=7);b<a-7&&(b+=7);return Math.ceil(j(f).add("d",b).dayOfYear()/7)}function G(f){var b=
f._i,c=f._f;if(null===b||""===b)return null;"string"===typeof b&&(f._i=b=r().preparse(b));if(j.isMoment(b))f=h({},b),f._d=new Date(+b._d);else if(c)if("[object Array]"===Object.prototype.toString.call(c)){for(var b=f,d,g,k=99;b._f.length;){d=h({},b);d._f=b._f.pop();w(d);c=new e(d);if(c.isValid()){g=c;break}d=p(d._a,c.toArray());d<k&&(k=d,g=c)}h(b,g)}else w(f);else if(g=f,b=g._i,c=Z.exec(b),b===a)g._d=new Date;else if(c)g._d=new Date(+c[1]);else if("string"===typeof b)if(c=g._i,aa.exec(c)){g._f="YYYY-MM-DDT";
for(b=0;4>b;b++)if(K[b][1].exec(c)){g._f+=K[b][0];break}I.exec(c)&&(g._f+=" Z");w(g)}else g._d=new Date(c);else"[object Array]"===Object.prototype.toString.call(b)?(g._a=b.slice(0),t(g)):g._d=b instanceof Date?new Date(+b):new Date(b);return new e(f)}function H(f,a){j.fn[f]=j.fn[f+"s"]=function(f){var b=this._isUTC?"UTC":"";return null!=f?(this._d["set"+b+a](f),this):this._d["get"+b+a]()}}function B(f){j.duration.fn[f]=function(){return this._data[f]}}function L(f,a){j.duration.fn["as"+f]=function(){return+this/
a}}for(var j,x=Math.round,s,y={},P="undefined"!==typeof module&&module.exports,Z=/^\/?Date\((\-?\d+)/i,J=/(\[[^\[]*\])|(\\)?(Mo|MM?M?M?|Do|DDDo|DD?D?D?|ddd?d?|do?|w[o|w]?|W[o|W]?|YYYYY|YYYY|YY|a|A|hh?|HH?|mm?|ss?|SS?S?|X|zz?|ZZ?|.)/g,M=/(\[[^\[]*\])|(\\)?(LT|LL?L?L?|l{1,4})/g,X=/\d\d?/,T=/\d{1,3}/,Q=/\d{3}/,R=/\d{1,4}/,S=/[+\-]?\d{1,6}/,U=/[0-9]*[a-z\u00A0-\u05FF\u0700-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+|[\u0600-\u06FF]+\s*?[\u0600-\u06FF]+/i,I=/Z|[\+\-]\d\d:?\d\d/i,W=/T/i,V=/[\+\-]?\d+(\.\d{1,3})?/,
aa=/^\s*\d{4}-\d\d-\d\d((T| )(\d\d(:\d\d(:\d\d(\.\d\d?\d?)?)?)?)?([\+\-]\d\d:?\d\d)?)?/,K=[["HH:mm:ss.S",/(T| )\d\d:\d\d:\d\d\.\d{1,3}/],["HH:mm:ss",/(T| )\d\d:\d\d:\d\d/],["HH:mm",/(T| )\d\d:\d\d/],["HH",/(T| )\d\d/]],Y=/([\+\-]|\d\d)/gi,C="Month Date Hours Minutes Seconds Milliseconds".split(" "),D={Milliseconds:1,Seconds:1E3,Minutes:6E4,Hours:36E5,Days:864E5,Months:2592E6,Years:31536E6},E={},N="DDD w W M D d".split(" "),O="MDHhmswW".split(""),u={M:function(){return this.month()+1},MMM:function(f){return this.lang().monthsShort(this,
f)},MMMM:function(f){return this.lang().months(this,f)},D:function(){return this.date()},DDD:function(){return this.dayOfYear()},d:function(){return this.day()},dd:function(f){return this.lang().weekdaysMin(this,f)},ddd:function(f){return this.lang().weekdaysShort(this,f)},dddd:function(f){return this.lang().weekdays(this,f)},w:function(){return this.week()},W:function(){return this.isoWeek()},YY:function(){return m(this.year()%100,2)},YYYY:function(){return m(this.year(),4)},YYYYY:function(){return m(this.year(),
5)},a:function(){return this.lang().meridiem(this.hours(),this.minutes(),!0)},A:function(){return this.lang().meridiem(this.hours(),this.minutes(),!1)},H:function(){return this.hours()},h:function(){return this.hours()%12||12},m:function(){return this.minutes()},s:function(){return this.seconds()},S:function(){return~~(this.milliseconds()/100)},SS:function(){return m(~~(this.milliseconds()/10),2)},SSS:function(){return m(this.milliseconds(),3)},Z:function(){var f=-this.zone(),a="+";0>f&&(f=-f,a="-");
return a+m(~~(f/60),2)+":"+m(~~f%60,2)},ZZ:function(){var f=-this.zone(),a="+";0>f&&(f=-f,a="-");return a+m(~~(10*f/6),4)},X:function(){return this.unix()}};N.length;)s=N.pop(),u[s+"o"]=d(u[s]);for(;O.length;)s=O.pop(),u[s+s]=b(u[s],2);u.DDDD=b(u.DDD,3);c.prototype={set:function(f){var a,b;for(b in f)a=f[b],"function"===typeof a?this[b]=a:this["_"+b]=a},_months:"January February March April May June July August September October November December".split(" "),months:function(f){return this._months[f.month()]},
_monthsShort:"Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(" "),monthsShort:function(f){return this._monthsShort[f.month()]},monthsParse:function(f){var a,b;this._monthsParse||(this._monthsParse=[]);for(a=0;12>a;a++)if(this._monthsParse[a]||(b=j([2E3,a]),b="^"+this.months(b,"")+"|^"+this.monthsShort(b,""),this._monthsParse[a]=RegExp(b.replace(".",""),"i")),this._monthsParse[a].test(f))return a},_weekdays:"Sunday Monday Tuesday Wednesday Thursday Friday Saturday".split(" "),weekdays:function(a){return this._weekdays[a.day()]},
_weekdaysShort:"Sun Mon Tue Wed Thu Fri Sat".split(" "),weekdaysShort:function(a){return this._weekdaysShort[a.day()]},_weekdaysMin:"Su Mo Tu We Th Fr Sa".split(" "),weekdaysMin:function(a){return this._weekdaysMin[a.day()]},_longDateFormat:{LT:"h:mm A",L:"MM/DD/YYYY",LL:"MMMM D YYYY",LLL:"MMMM D YYYY LT",LLLL:"dddd, MMMM D YYYY LT"},longDateFormat:function(a){var b=this._longDateFormat[a];!b&&this._longDateFormat[a.toUpperCase()]&&(b=this._longDateFormat[a.toUpperCase()].replace(/MMMM|MM|DD|dddd/g,
function(a){return a.slice(1)}),this._longDateFormat[a]=b);return b},meridiem:function(a,b,c){return 11<a?c?"pm":"PM":c?"am":"AM"},_calendar:{sameDay:"[Today at] LT",nextDay:"[Tomorrow at] LT",nextWeek:"dddd [at] LT",lastDay:"[Yesterday at] LT",lastWeek:"[last] dddd [at] LT",sameElse:"L"},calendar:function(a,b){var c=this._calendar[a];return"function"===typeof c?c.apply(b):c},_relativeTime:{future:"in %s",past:"%s ago",s:"a few seconds",m:"a minute",mm:"%d minutes",h:"an hour",hh:"%d hours",d:"a day",
dd:"%d days",M:"a month",MM:"%d months",y:"a year",yy:"%d years"},relativeTime:function(a,b,c,d){var e=this._relativeTime[c];return"function"===typeof e?e(a,b,c,d):e.replace(/%d/i,a)},pastFuture:function(a,b){var c=this._relativeTime[0<a?"future":"past"];return"function"===typeof c?c(b):c.replace(/%s/i,b)},ordinal:function(a){return this._ordinal.replace("%d",a)},_ordinal:"%d",preparse:function(a){return a},postformat:function(a){return a},week:function(a){return F(a,this._week.dow,this._week.doy)},
_week:{dow:0,doy:6}};j=function(a,b,c){return G({_i:a,_f:b,_l:c,_isUTC:!1})};j.utc=function(a,b,c){return G({_useUTC:!0,_isUTC:!0,_l:c,_i:a,_f:b})};j.unix=function(a){return j(1E3*a)};j.duration=function(a,b){var c=j.isDuration(a),d="number"===typeof a,e=c?a._data:d?{}:a;d&&(b?e[b]=a:e.milliseconds=a);d=new g(e);c&&a.hasOwnProperty("_lang")&&(d._lang=a._lang);return d};j.version="2.0.0";j.defaultFormat="YYYY-MM-DDTHH:mm:ssZ";j.lang=function(a,b){if(!a)return j.fn._lang._abbr;b?(b.abbr=a,y[a]||(y[a]=
new c),y[a].set(b)):y[a]||r(a);j.duration.fn._lang=j.fn._lang=r(a)};j.langData=function(a){a&&(a._lang&&a._lang._abbr)&&(a=a._lang._abbr);return r(a)};j.isMoment=function(a){return a instanceof e};j.isDuration=function(a){return a instanceof g};j.fn=e.prototype={clone:function(){return j(this)},valueOf:function(){return+this._d},unix:function(){return Math.floor(+this._d/1E3)},toString:function(){return this.format("ddd MMM DD YYYY HH:mm:ss [GMT]ZZ")},toDate:function(){return this._d},toJSON:function(){return j.utc(this).format("YYYY-MM-DD[T]HH:mm:ss.SSS[Z]")},
toArray:function(){return[this.year(),this.month(),this.date(),this.hours(),this.minutes(),this.seconds(),this.milliseconds()]},isValid:function(){null==this._isValid&&(this._isValid=this._a?!p(this._a,(this._isUTC?j.utc(this._a):j(this._a)).toArray()):!isNaN(this._d.getTime()));return!!this._isValid},utc:function(){this._isUTC=!0;return this},local:function(){this._isUTC=!1;return this},format:function(a){var b=this;a=a||j.defaultFormat;for(var c=function(a){return b.lang().longDateFormat(a)||a},
d=5;d--&&M.test(a);)a=a.replace(M,c);if(!E[a]){var e=c=a,g=e.match(J),h,k;h=0;for(k=g.length;h<k;h++)if(u[g[h]])g[h]=u[g[h]];else{var d=g,m=h,l;l=g[h];l=l.match(/\[.*\]/)?l.replace(/^\[|\]$/g,""):l.replace(/\\/g,"");d[m]=l}E[c]=function(a){var b="";for(h=0;h<k;h++)b+="function"===typeof g[h].call?g[h].call(a,e):g[h];return b}}a=E[a](b);return this.lang().postformat(a)},add:function(a,b){var c;c="string"===typeof a?j.duration(+b,a):j.duration(a,b);n(this,c,1);return this},subtract:function(a,b){var c;
c="string"===typeof a?j.duration(+b,a):j.duration(a,b);n(this,c,-1);return this},diff:function(a,b,c){a=this._isUTC?j(a).utc():j(a).local();var d=6E4*(this.zone()-a.zone()),e;b&&(b=b.replace(/s$/,""));"year"===b||"month"===b?(d=432E5*(this.daysInMonth()+a.daysInMonth()),e=12*(this.year()-a.year())+(this.month()-a.month()),e+=(this-j(this).startOf("month")-(a-j(a).startOf("month")))/d,"year"===b&&(e/=12)):(d=this-a-d,e="second"===b?d/1E3:"minute"===b?d/6E4:"hour"===b?d/36E5:"day"===b?d/864E5:"week"===
b?d/6048E5:d);return c?e:k(e)},from:function(a,b){return j.duration(this.diff(a)).lang(this.lang()._abbr).humanize(!b)},fromNow:function(a){return this.from(j(),a)},calendar:function(){var a=this.diff(j().startOf("day"),"days",!0);return this.format(this.lang().calendar(-6>a?"sameElse":-1>a?"lastWeek":0>a?"lastDay":1>a?"sameDay":2>a?"nextDay":7>a?"nextWeek":"sameElse",this))},isLeapYear:function(){var a=this.year();return 0===a%4&&0!==a%100||0===a%400},isDST:function(){return this.zone()<j([this.year()]).zone()||
this.zone()<j([this.year(),5]).zone()},day:function(a){var b=this._isUTC?this._d.getUTCDay():this._d.getDay();return null==a?b:this.add({d:a-b})},startOf:function(a){a=a.replace(/s$/,"");switch(a){case "year":this.month(0);case "month":this.date(1);case "week":case "day":this.hours(0);case "hour":this.minutes(0);case "minute":this.seconds(0);case "second":this.milliseconds(0)}"week"===a&&this.day(0);return this},endOf:function(a){return this.startOf(a).add(a.replace(/s?$/,"s"),1).subtract("ms",1)},
isAfter:function(a,b){b="undefined"!==typeof b?b:"millisecond";return+this.clone().startOf(b)>+j(a).startOf(b)},isBefore:function(a,b){b="undefined"!==typeof b?b:"millisecond";return+this.clone().startOf(b)<+j(a).startOf(b)},isSame:function(a,b){b="undefined"!==typeof b?b:"millisecond";return+this.clone().startOf(b)===+j(a).startOf(b)},zone:function(){return this._isUTC?0:this._d.getTimezoneOffset()},daysInMonth:function(){return j.utc([this.year(),this.month()+1,0]).date()},dayOfYear:function(a){var b=
x((j(this).startOf("day")-j(this).startOf("year"))/864E5)+1;return null==a?b:this.add("d",a-b)},isoWeek:function(a){var b=F(this,1,4);return null==a?b:this.add("d",7*(a-b))},week:function(a){var b=this.lang().week(this);return null==a?b:this.add("d",7*(a-b))},lang:function(b){if(b===a)return this._lang;this._lang=r(b);return this}};for(s=0;s<C.length;s++)H(C[s].toLowerCase().replace(/s$/,""),C[s]);H("year","FullYear");j.fn.days=j.fn.day;j.fn.weeks=j.fn.week;j.fn.isoWeeks=j.fn.isoWeek;j.duration.fn=
g.prototype={weeks:function(){return k(this.days()/7)},valueOf:function(){return this._milliseconds+864E5*this._days+2592E6*this._months},humanize:function(a){var b=+this,c;c=!a;var d=this.lang(),e=x(Math.abs(b)/1E3),g=x(e/60),j=x(g/60),h=x(j/24),k=x(h/365),e=45>e&&["s",e]||1===g&&["m"]||45>g&&["mm",g]||1===j&&["h"]||22>j&&["hh",j]||1===h&&["d"]||25>=h&&["dd",h]||45>=h&&["M"]||345>h&&["MM",x(h/30)]||1===k&&["y"]||["yy",k];e[2]=c;e[3]=0<b;e[4]=d;c=A.apply({},e);a&&(c=this.lang().pastFuture(b,c));return this.lang().postformat(c)},
lang:j.fn.lang};for(s in D)D.hasOwnProperty(s)&&(L(s,D[s]),B(s.toLowerCase()));L("Weeks",6048E5);j.lang("en",{ordinal:function(a){var b=a%10;return a+(1===~~(a%100/10)?"th":1===b?"st":2===b?"nd":3===b?"rd":"th")}});this.moment=j}).call("undefined"===typeof m?window:m);if(!m.moment)if(window.moment)m.moment=window.moment;else throw"Kalendae requires moment.js. You must use kalendae.standalone.js if moment is not available on the page.";k=m.moment;k.fn.stripTime=function(){this._d=new Date(864E5*Math.floor(this._d.valueOf()/
864E5));return this};k.fn.yearDay=function(a){var b=Math.floor(this._d/864E5);return"undefined"===typeof a?b:this.add({d:a-b})};t=m.moment().stripTime();if("undefined"!==typeof jQuery&&("function"===typeof document.addEventListener||c.isIE8()))jQuery.fn.kalendae=function(a){this.each(function(b,c){"INPUT"===c.tagName?$(c).data("kalendae",new m.Input(c,a)):$(c).data("kalendae",new m($.extend({},{attachTo:c},a)))});return this}})();
