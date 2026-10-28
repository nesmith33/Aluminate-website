from PIL import Image
from pathlib import Path
p=Path('/mnt/data/aluminate-v1'); im=Image.open('/mnt/data/a_clean_high_end_website_concept_branding_present.png'); print(im.size)
# crop imagery from visual concept, avoid embedded UI text where possible
crops={'hero.jpg':(305,65,770,365),'gallery.jpg':(236,395,766,612),'detail.jpg':(320,870,610,1060),'master.jpg':(980,0,1215,215),'can.jpg':(1065,540,1210,730)}
for n,b in crops.items():
 x=im.crop(b); x.save(p/n,quality=92)
