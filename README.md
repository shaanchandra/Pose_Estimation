# Pose_Estimation
Pose estimation in animals using [DeepLabCut](https://github.com/AlexEMG/DeepLabCut)

The DeepLabCut library is based on the [DeepCut](https://arxiv.org/pdf/1511.06645.pdf) and [DeeperCut](https://arxiv.org/pdf/1605.03170.pdf) models and allows for class agnostic body part detection and subsequent body configuration learning for pose estimation. The authors claim that with just ***50-200*** annotated frames of any target of interest the model can achieve *human level accuracy*. 

The results below confirm this, though I trained it for just about 20k iters each example (recommended would be atleast 100k iters). During experimentaiton however it was obsevered that a representative training set is very important for the performance. This means that the training examples should contain all the different poses the subject exhibits/is expected to exihibit in the video and/or different lighting conditions (if any). Still, getting such generalizable performance from just 5-12% of annotated data is outstanding.

## Results

### Sample result: Ostrich
Total Frames: 526

Frames annotated (#) : 38

Frames annotated (%) : 7.2%

![Ostrich](https://github.com/shaanchandra/Pose_Estimation/blob/master/results/ostrich.gif)

### Sample result: Turkey
Total Frames: 421

Frames annotated (#) : 50

Frames annotated (%) : 11.8%

![Turkey](https://github.com/shaanchandra/Pose_Estimation/blob/master/results/turkey.gif)
