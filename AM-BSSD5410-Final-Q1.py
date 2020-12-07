from PIL import Image
"""Steganography on a given image, encode and decode messages"""
#These links helped me
#https://www.geeksforgeeks.org/image-based-steganography-using-python/
#https://dev.to/erikwhiting88/let-s-hide-a-secret-message-in-an-image-with-python-and-opencv-1jf5

#store pixels function, to get the pixels array of the image
def storePixels(im):
    im = im.convert('RGB')
    width = int(im.size[0])
    height = int(im.size[1])
    pixel_array=[]
    for i in range (width):
        for j in range(height):
            r,g,b = im.getpixel((i,j))
            pixel_array.append([[r,g,b]])
    return pixel_array
#end def store pixels

#def encode image, to encode the message inside the original image
def encode_image(image,message):
      image_ = storePixels(image)
      lenght_of_message = len(message)
      h=0
      #Here I will read the message and replace ord of each of each letter
      #with a red pixel, untill the message lenght is done.
      for i in range(len(image_)):
          for b in range(len(image_[0])):
            if lenght_of_message > 0:
                image_[i - 1][b - 1][0]=ord(message[h])
                h+=1
            if lenght_of_message <=0:
                    image_[i - 1][b - 1][0] = 0
            lenght_of_message = lenght_of_message - 1
      return image_
#end def encoded_image

#decoded image function, to decode the secret message.
def decode_image(image_):
  decoded_message=''
  # I will check here the red pixels, and depend on the different one,
  #add letters till the message is over.
  for i in range(len(image_)):
    for j in range(len(image_[0])):
      if image_[i-1][j-1][0] != 0:
        decoded_message= decoded_message+ chr(image_[i-1][j-1][0])
      else:
          return decoded_message
#end def decoded_image

#draw function to display image
def draw(encoded_list):
    array = []
    #take list of pixels, and put them into new image, then sava the image.
    for sublist in encoded_list:
        for item in sublist:
            array.append(item)
    list_of_tuples = [tuple(x) for x in array]
    im=Image.new('RGB',(411,408))
    counter_=0
    for i in range (411):
        for j in range(408):
            im.putpixel((i, j), (list_of_tuples[counter_]))
            counter_+= 1
    im.save("Encoded_starts.png")
#end def draw

#main
def main():
   #main function, choose encode or decode and enter the message, and user can check the encoded image.
   while True:
    mode=input('Please enter mode (E)ncode or (D)ecode:')
    if mode=='E':
     message=input('Please enter phrase:')
     im= Image.open('stars.png')
     encoded= encode_image(im,message)
     draw(encoded)
    if mode=='D':
     encoded_image= Image.open('Encoded_starts.png')
     encoded_pixels_=storePixels(encoded_image)
     decoded_message= decode_image(encoded_pixels_)
     print(decoded_message)
#end def main

if __name__ == '__main__':
 main()