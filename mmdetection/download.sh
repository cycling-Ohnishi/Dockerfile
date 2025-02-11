#!/bin/bash

mkdir -p coco/images && cd $_

wget http://images.cocodataset.org/zips/train2017.zip
wget http://images.cocodataset.org/zips/val2017.zip
wget http://images.cocodataset.org/zips/test2017.zip

unzip -p train2017.zip
unzip -p val2017.zip
unzip -p test2017.zip

rm train2017.zip
rm val2017.zip
rm test2017.zip

cd ../
wget http://images.cocodataset.org/annotations/annotations_trainval2017.zip
unzip -p annotations_trainval2017.zip
rm annotations_trainval2017.zip
