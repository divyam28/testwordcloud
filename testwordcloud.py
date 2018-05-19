# modules for generating the word cloud
from os import path, getcwd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS

d = getcwd()
## join all documents in corpus
stp=list(set(STOPWORDS))
w=['hi','ur','dear','rt','even','really','still','...','now','please','getting','guy','want','day','will','using','make','give']
q=w+stp

text = open(path.join(d, 'text.txt')).read()
mask1 = np.array(Image.open(path.join(d, "test6.jpg")))
wc = WordCloud(background_color="white", max_words=1000, mask=mask1,stopwords=q,
               max_font_size=150, random_state=42)
wc.generate(text)
# create coloring from image
image_colors = ImageColorGenerator(mask1)

print(image_colors.image.shape)
print(wc.width, wc.height)

plt.figure(figsize=[5,5])
plt.tight_layout(pad=0)
plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
plt.show()
