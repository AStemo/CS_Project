import numpy as np

html_str="http://skyserver.sdss.org/dr15/SkyServerWS/ImgCutout/getjpeg?ra="


size=64
save_dir="/Users/stemo/google_drive/GitHub/CS_Project/Cutouts/Color/64/Mergers/"
#save_dir="/Users/stemo/google_drive/GitHub/CS_Project/Cutouts/Color/64/Non_Mergers/"

#size=128
#save_dir="/Users/stemo/google_drive/GitHub/CS_Project/Cutouts/Color/128/Mergers/"
#save_dir="/Users/stemo/google_drive/GitHub/CS_Project/Cutouts/Color/128/Non_Mergers/"

#size=256
#save_dir="/Users/stemo/google_drive/GitHub/CS_Project/Cutouts/Color/256/Mergers/"
#save_dir="/Users/stemo/google_drive/GitHub/CS_Project/Cutouts/Color/256/Non_Mergers/"


gals=np.genfromtxt("/Users/stemo/google_drive/GitHub/CS_Project/Catalogs/darg_mergers.csv", skip_header = 1, delimiter = ",")
script=[]
for i in range(len(gals)):
#for i in range(100):
    ids=gals[i][0]
    ra=gals[i][3]
    dec=gals[i][4]
    script.append("wget -O "+save_dir+str(int(ids))+".jpeg "+html_str+str(ra)+"\&dec="+str(dec)+"\&width="+str(size)+"\&height="+str(size))

#gals=np.genfromtxt("/Users/stemo/google_drive/GitHub/CS_Project/Catalogs/non_mergers_subset.csv", skip_header = 1, delimiter = ",")
#script=[]
#for i in range(len(gals)):
##for i in range(100):
#    ids=gals[i][0]
#    ra=gals[i][18]
#    dec=gals[i][19]
#    script.append("wget -O "+save_dir+str(int(ids))+".jpeg "+html_str+str(ra)+"\&dec="+str(dec)+"\&width="+str(size)+"\&height="+str(size))


np.savetxt("color_wget_script.sh", script, fmt = "%s")