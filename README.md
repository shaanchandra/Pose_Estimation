# Pose_Estimation
Pose estimation in animals using [DeepLabCut](https://github.com/AlexEMG/DeepLabCut)

The DeepLabCut library is based on the [DeepCut](https://arxiv.org/pdf/1511.06645.pdf) and [DeeperCut](https://arxiv.org/pdf/1605.03170.pdf) models and allows for class agnostic body part detection and subsequent body configuration learning for pose estimation. The authors claim that with just ***50-200*** annotated frames of any target of interest the model can achieve *human level accuracy*. 

The results below confirm this, though I trained it for just about 20k iters each example (recommended would be atleast 100k iters). During experimentaiton however it was obsevered that a representative training set is very important for the performance. This means that the training examples should contain all the different poses the subject exhibits/is expected to exihibit in the video and/or different lighting conditions (if any). Still, getting such generalizable performance from just 5-12% of annotated data is outstanding.

## Code

All the scripts to grab frames for annotation, labelling them using a GUI and creating a dataset are provided by the authors in the ```Demo_yourowndata.ipynb``` file under examples. You need to run these first before training. 

Before running the labelling code, you need to specify the body parts and skeleton structure in the ```config.yaml```. 

These steps also create a default ```pose_config.yaml``` file under *dlc_models* of the created directory. This includes a default set of training parameters like model to use (resnet_50/resnet_101/resnet_152), maxiters, etc. Edit this according to the training needs before running the training step. 

(***NOTE:*** *intermediate_inference* option at layer 12 is only available for resnet_101 and resnet_152. For resent_50 you need to have it ```False``` or have layer = 1. )

## Results

### Sample result: Ostrich
Total Frames: 526

Frames annotated (#) : 38

Frames annotated (%) : 7.2%

![Ostrich](https://github.com/shaanchandra/Pose_Estimation/blob/master/results/ostrich2.gif)

### Sample result: Cow
Total Frames: 2495

Frames annotated (#) : 125

Frames annotated (%) : 5%

![Cow](https://github.com/shaanchandra/Pose_Estimation/blob/master/results/cow.gif)

### Sample result: Turkey

(***NOTE:*** The library currently supports just single animal estimation in a video sequence (as seen below). Multi-animal estimation is expected in the coming releases)
 
Total Frames: 421

Frames annotated (#) : 50

Frames annotated (%) : 11.8%

![Turkey](https://github.com/shaanchandra/Pose_Estimation/blob/master/results/turkey.gif)
