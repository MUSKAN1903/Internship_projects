#!/usr/bin/env python
# coding: utf-8

# # WELCOME TO CAFE*10 !!!!!!

# By Hunny Munjal & Muskan Singh

# In[12]:


import json

fd = open("RRECORD.json","r")
r = fd.read()
fd.close()

records = json.loads(r)


# ### here's our menu !

# In[13]:


records


# ### what would you like to order ??

# In[51]:


print("********WELCOME TO OUR CAFE**********")
print("what would you like to order ?")

ui_prod  = str(input("Enter the product_Id: "))
ui_quant = int(input("Enter the quantity: "))

print("Product: ", records[ui_prod]['name'])
print("Price: ", records[ui_prod]['pr'])
Billing_Amount = records[ui_prod]['pr'] * ui_quant
print("Billing Amount: ", Billing_Amount,"/-")


records[ui_prod]['qn'] = records[ui_prod]['qn'] - ui_quant


# In[53]:


js = json.dumps(records)

fd = open("RRECORD.json",'w')
fd.write(js)
fd.close()


# ### PAYMENT TRANSACTION !

# In[52]:


ui_cash  = int(input("Enter the money : "))
if (ui_cash<Billing_Amount):
    print("you're paying less than the biling amount, please recheck your billing amount!!!")
elif(ui_cash>Billing_Amount):
    print("change returned:",ui_cash-Billing_Amount)
    print("transaction successfull!!")
    print("ENJOY YOUR FOOD!!!!!!")
else:
    print("transaction successfull!!")
    print("ENJOY YOUR FOOD!!!!!!")
        


# LAUNCHING NEW PRODUCTS IN OUR CAFE

# In[ ]:


prod_id = str(input("Enter product id:"))
name = str(input("Enter name:"))
pr = int(input("Enter price:"))
qn = int(input("Enter quantity:"))

records[prod_id] = {'name': name, 'pr': pr, 'qn': qn}

js = json.dumps(records)

fd = open("RRECORD.json",'w')
fd.write(js)
fd.close()


# In[20]:


records


# # THANKYOU FOR VISITING !! SEE YOU SOON !
