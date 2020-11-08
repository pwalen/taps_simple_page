from selenium import webdriver
from tests.helpers.support_functions import *
import time

driver = webdriver.Chrome('/Users/pawelwalenda/chromedriver')

JS_DRAG_AND_DROP = "function h(a,b,c,d){var k=l.createEvent('DragEvent');k.initMouseEvent(b,!0,!0,l.defaultView,0,0,0,m,n,w,x,y,!1,0,null);Object.setPrototypeOf(k,null);k.dataTransfer=g;Object.setPrototypeOf(k,DragEvent.prototype);a.dispatchEvent(k);setTimeout(d,c)}var a=arguments,c=a[0],d=a[1],q=a[2]||0,r=a[3]||0,t=a[4]||1;a=a[5]||'';var x='alt'===a||'\ue00a'===a,w='ctrl'===a||'\ue009'===a,y='shift'===a||'\ue008'===a,l=c.ownerDocument;a=c.getBoundingClientRect();var e=d?d.getBoundingClientRect():a,m=a.left+a.width/2,n=a.top+a.height/2,u=e.left+(q?q:e.width/2),v=e.top+(r?r:e.height/2),p=l.elementFromPoint(m,n),f=l.elementFromPoint(u,v);for(d=p;d&&!d.draggable;)d=d.parentElement;if(!d||!c.contains(p))throw c=Error('source element is not interactable/draggable'),c.code=15,c;if(!f)throw c=Error('target element is not interactable'),c.code=15,c;var g={constructor:DataTransfer,effectAllowed:null,dropEffect:null,types:[],files:Object.setPrototypeOf([],null),_items:Object.setPrototypeOf([],{add:function(a,b){this[this.length]={_data:''+_data,kind:'string',type:b,getAsFile:function(){},getAsString:function(a){a(this._data)}};g.types.push(b)},remove:function(a){Array.prototype.splice.call(this,a&65535,1);g.types.splice(a&65535,1)},clear:function(a,b){this.length=0;g.types.length=0}}),setData:function(a,b){this.clearData(a);this._items.add(b,a)},getData:function(a){for(var b=this._items.length;b--&&this._items[b].type!==a;);return 0<=b?this._items[b]._data:null},clearData:function(a){for(var b=this._items.length;b--&&this._items[b].type!==a;);this._items.remove(b)},setDragImage:function(a){}};'items'in DataTransfer.prototype&&(g.items=g._items);e=f.getBoundingClientRect();h(p,'dragstart',t,function(){var a=f.getBoundingClientRect();m=a.left+u-e.left;n=a.top+v-e.top;h(f,'dragenter',1,function(){h(f,'dragover',t,function(){f=l.elementFromPoint(m,n);h(f,'drop',1,function(){h(p,'dragend',1,function(){})})})})})"

def drag_and_drop(driver, source, target=None, offsetX=0, offsetY=0, delay=25, key=None):
    driver.execute_script(JS_DRAG_AND_DROP, source, target, offsetX, offsetY, delay, key)
    time.sleep(delay * 2 / 1000)

# url from Elemental Selenium
url_es = 'http://the-internet.herokuapp.com/drag_and_drop'

# Elemental Selenium locators
column_a_by_id_es = 'column-a'
column_b_by_id_es = 'column-b'
column_a_by_xpath_es = '//*[@id="column-a"]'
column_b_by_xpath_es = '//*[@id="column-b"]'

# url from TAPS by Fabryka Testow
url_taps = 'http://simpletestsite.fabrykatestow.pl/'

# TAPS locators
column_a_by_id_taps = 'column-a'
column_b_by_id_taps = 'column-b'
column_a_by_xpath_taps = '//*[@id="column-a"]'
column_b_by_xpath_taps = '//*[@id="column-b"]'


driver.get(url_taps)
time.sleep(2)

draganddrop_tab = 'draganddrop-header'
draganddrop_content = 'draganddrop-content'

click_draganddrop_tab = driver.find_element_by_id(draganddrop_tab)
click_draganddrop_tab.click()
wait_for_visibility_of_element(driver, draganddrop_content)

draggable = driver.find_element_by_id(column_a_by_id_taps)
droppable = driver.find_element_by_id(column_b_by_id_taps)

drag_and_drop(driver, draggable, droppable)

time.sleep(3)
driver.quit()
