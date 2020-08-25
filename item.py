# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 01:10:26 2020

@author: intis
"""

from bs4 import BeautifulSoup
import requests as req
import pandas as pd

data_dict = dict( product_name = [],
                 catagory = [],
                 img_link=[],
                 price = [],
                 UNSPSC = [],
                 item_no = [],
                 #specification_field = [],
                 #specification_value = [],
                 
    )



def process():
    brand_url = "https://www.henryschein.com/us-en/specialmarkets_d/c/browsesupplies"
    brand_links = parse_item_link(soup_object(brand_url))[0:10]
    product_links = parse_all_link(brand_links)

    status = scrape_product_info(product_links)

    if status:
        export_csv(data_dict)

        return True
    else:
        return False
#process()
def soup_object(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
    login_url = 'https://www.henryschein.com/us-en/Profiles/Login.aspx?redirdone=1'
    payload = {'ctl00$ucHeader$ucSessionBar$ucLogin$txtLogonName':'atest3381','ctl00$ucHeader$ucSessionBar$ucLogin$txtPassword':'Atest#3381'}
    with req.Session() as s: 
        post = s.post(login_url,data = payload)
        resp = s.get(url,headers = headers)
        resp_data = resp.text
        soup = BeautifulSoup(resp_data,'html.parser')
   
   
    return soup

def parse_item_link(soup):
    #cons = soup.find('ul',class_='hs-categories display grid clear-fix')
    #cat_link = []
    man_link = []
    #for con in cons:
        #link = con.find_all('a')
        #link = [i.get('href') for i in link]
        #for y in link:
            #cat_link.append(y.get('href'))
        #cat_link = link
        #re_link = cat_link.append(link)
    c = soup.find_all('ul',attrs={'data-tabs-contents':'alpha'})
    for i in c:
        x = i.find_all('a')
        for y in x:
            f = y.get('href')
            man_link.append(f)
    #total = cat_link,man_link
    #total = cat_link,man_link
    
    print('ok')
    return man_link
    #return cat_link,man_link

def parse_all_link(links):
    
    #cat_url = []
    man_url = []
    for link in links:
        
        link_soup = soup_object(link)
        #x = link_soup.find_all('ul',attrs={'style':'padding: 1em .5em .5em'})
        #for i in x:
            #z = i.find_all('a')
            #for y in z:
                #a = y.get('href')
                #cat_url.append(a)
        m = link_soup.find_all('h2',class_='product-name') 
        for i in m:
            n = i.find_all('a')
            for y in n:
                p = y.get('href')
                man_url.append(p)
                print(p)
    print('ok')
              
    #return cat_url,man_url
    return man_url

#def inside_link(gets):
    #hole = []
    #for get in gets:
        #soup = soup_object(get)
        #m = soup.find_all('h2',class_='product-name')
        #print(m)
        #for i in m:
            #n = i.find_all('a')
            #for y in n:
                #p = y.get('href')
               # hole.append(p)
   #print('ok')
    #return hole
    
def  scrape_product_info(product_links):
    url = 'https://www.henryschein.com'
    for index, product_link in enumerate(product_links):
        c = soup_object(product_link)
        #try:
        ##cols = c.find('div',class_='popup-content')
            #cols = c.find('h2',class_='heading show-progress active')
        #except:
        #cols = c.find('h2',class_='heading show-progress active')
        #cols = c.find(class_='product no-padding product-additional-info')
        #cols = c.find('div',class_='content')
        #try:
        #cols = c.find('ul',class_='attr-list')
        #except: 
        #cols = c.find(class_='product-attributes')
        cols = c.find(class_='product')
            
            #cols = c.find('section',class_='product-attributes hs-accordion clear-fix')
        
        
        
        try:
            
            
            #for col in cols:
        
    
            data_dict['product_name'].append(c.find('h2',class_='product-title medium strong').\
                                                 text.replace('\r','').replace('\n','').replace('  ','').split('/')[0])
                
                 
            data_dict['catagory'].append(c.find('ul',class_='small-above').find_next('div',class_='value').text.replace('\r','').replace('\n','').replace('  ',''))
                
            data_dict['UNSPSC'].append(c.find('ul',class_='small-above').find_all('div',class_='value')[1].text.replace('\r','').replace('\n','').replace('  ',''))
                
                
            data_dict['item_no'].append(c.find('small',class_='x-small').find_next('strong').text.replace('\r','').replace('\n','').replace('  ',''))
                
                
            data_dict['img_link'].append((url + c.find('div',class_='hs-product-slideshow').find('img').get('src')))
                
            data_dict['price'].append(c.find('div',class_='product-price').text.strip())
    
                    
                
                    
                    #l = col.find_all('li')
                    #for i in l:
                        #data_dict['specification_field'].append(i.find(class_='field').text.strip())
                    #data_dict['specification_field'].append(col.find('ul',class_='small-above').find('div',class_='field').text.replace('\r','').replace('\n','').replace('  ',''))
                    #l = col.find('ul',class_='attr-list')
                    #for i in l.find_all(class_='field'):
                        #data_dict['specification_field'].append(i.text.strip())
                #except:
                    #data_dict['specification_field'].append('N/A')
                    #pass
                
                #try:
                    #for i in range(len(col.select('.value'))):
                        #data_dict['specification_value'].append(col.select('.value')[i].text.strip())
                   #l = col.find_all('li')
                   #for i in l:
                       #data_dict['specification_value'].append(i.find(class_='value').text.strip())
                        
                    #for i in col.select('.value'):
                        #data_dict['specification_value'].append(i.text.strip())
                    #data_dict['specification_value'].append(col.find('li').find('div',class_='value').text.replace('\r','').replace('\n','').replace('  ',''))
                #except:
                    #data_dict['specification_value'].append('N/A')
                    #pass
                #data_dict['price'].append(c.find('div',class_='product-price').text.strip())
            return True
        except:
            pass
    
def export_csv(data_dict):
    dataFrame = pd.DataFrame(data_dict)
    dataFrame.to_csv("data.csv", mode='w', header=True, index=False)
    print("Data.csv exported")
    return True