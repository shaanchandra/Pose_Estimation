# Pose_Estimation
Pose estimation in animals using [DeepLabCut](https://github.com/AlexEMG/DeepLabCut)

The DeepLabCut library is based on the [DeepCut](https://arxiv.org/pdf/1511.06645.pdf) and [DeeperCut](https://arxiv.org/pdf/1605.03170.pdf) models and allows for class agnostic body part detection and subsequent body configuration learning for pose estimation. The authors claim that with just ***50-200*** annotated frames of any target of interest the model can achieve *human level accuracy*. 

The results below confirm this, though I trained it for just about 20k iters each example (recommended would be atleast 100k iters). During experimentaiton however it was obsevered that a representative training set is very important for the performance. This means that the training examples should contain all the different poses the subject exhibits/is expected to exihibit in the video and/or different lighting conditions (if any). Still, getting such generalizable performance from just 5-12% of annotated data is outstanding.

## Code

All the scripts to grab frames for annotation, labelling them using a GUI and creating a dataset are provided by the authors in the ```Demo_yourowndata.ipynb``` file under examples. You need to run these before training. 

Before running the labelling code, you need to specify the body parts and skeleton structure in the ```config.yaml``` (created when you run the cell for ```create_new_project```).

```extract_frames``` will open a GUI to scroll through the frames of the video and choose the frames you want to annotate. These frames will be stored under the folder *labelled_data*. 

```label_frames``` will open a GUI with the option to label the parts defined in the ```config.yaml``` file and in the frames chosen in the previous step. This will create a ***csv*** and ***h5*** file in the same destination as the frames which is used later in training.

```create_training_dataset``` will create a default ```pose_config.yaml``` file under *dlc_models* of the created directory. This includes a default set of training parameters like train, test split, model to use (resnet_50/resnet_101/resnet_152), max_iters, etc. Edit this according to the training needs before running the training step. 

```train_network``` will run training based on the hyperparameters specified in the ```pose_config.yaml```.

```create_labeled_video``` will create the processed video with annotatoions predicted by the model on each frame along with the skeleton as specified earlier (if *draw skeleton = True*). 

Things to ***NOTE***:

1. *intermediate_inference* option at layer 12 is only available for resnet_101 and resnet_152. For resent_50 you need to have it ```False``` or have layer = 1.
2. After annotating the data using ```label_frames```, please execute ```check_labels``` to cross-verify the annotations. I found that 5-10% of the times the anotations were slightly shifted/completely off from the place where I had marked them in the GUI.
3. The ipython notebook contains more information for more functionalities. Please refer to it as needed.

As future work, we can also do 3D pose estimation if we have videos from multiple cameras. Refer to the respective ipython notebook for more information. 

## Results

### Sample result: Ostrich
Total Frames: 526

Frames annotated (#) : 38

Frames annotated (%) : 7.2%

![Ostrich](https://gitlab.hq.braincreators.com/students/pose_estimation/blob/master/results/ostrich2.gif)

### Sample result: Cow
Total Frames: 2495

Frames annotated (#) : 125

Frames annotated (%) : 5%

![Cow](https://gitlab.hq.braincreators.com/students/pose_estimation/blob/master/results/cow.gif)

### Sample result: Turkey

(***NOTE:*** The library currently supports just single animal estimation in a video sequence (as seen below). Multi-animal estimation is expected in the coming releases)
 
Total Frames: 421

Frames annotated (#) : 50

Frames annotated (%) : 11.8%

![Turkey](https://gitlab.hq.braincreators.com/students/pose_estimation/blob/master/results/turkey.gif)
