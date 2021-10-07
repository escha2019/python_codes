#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from keras.applications import VGG16
import keras as k


# In[2]:


# get imagenet model
vgg_conv = VGG16(weights='imagenet',  include_top=False, input_shape=(224, 224, 3) )
vgg_conv.summary()


# In[3]:


vgg_conv.layers.pop()
vgg_conv.layers.pop() 
vgg_conv.summary()


# In[17]:


last= vgg_conv.get_layer('block5_conv2').output
# build your own layers
x= k.layers.Flatten()(last)
#functional API
x2= k.layers.Dense(1024, activation='relu')(x)   # Fully Connect
my_preds= k.layers.Dense(200, activation='softmax')(x2)# combinemodified VGG with your FC+Softmax
my_model= k.Model(vgg_conv.input, my_preds)
# 
for layer in my_model.layers[:10]:#    
    layer.trainable= False      
#    Dense(32, trainable=False)
my_model.summary()
#my_model.compile(loss='crossentropy', optimizer='adam')

