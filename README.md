# KURULUM

Workspace Hazırlanışı

```
mkdir decompress_ws/src
cd decompress_ws
mkdir src
cd src
git clone https://github.com/huseyintutan/-iturover_compression_assignment.git
cd ..
catkin build

source decompress_ws/devel/setup.bash

sudo chmod +x src/bz2pub/scripts/bz2_publisher.py
sudo chmod +x src/pydecomp/scripts/decomp.py

```
# ÇALIŞTIRMA

```
roscore
rosrun bz2pub bz2_publisher.py
rosrun pydecomp decomp.py 
rostopic echo /solution
rostopic info /solution
```
### ÖRNEK ÇIKTI GÖRÜNTÜSÜ
<div align="center">
<img src="github.png" width="1240" height="768" />
</div>
