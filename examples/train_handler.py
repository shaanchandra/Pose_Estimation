import deeplabcut
import os
import sys
import cv2
import time

import warnings
warnings.simplefilter('ignore')
# warnings.filterwarnings("ignore")
# with warnings.catch_warnings():
#     warnings.simplefilter("ignore")

def train():
    videofile_path = ['videos/ostrich.mp4'] #Enter a folder OR a list of videos to analyze.
    if not os.path.isfile(videofile_path[0]):
        sys.exit("File {} not found!!".format(videofile_path[0]))
    
    path_config_file = '/home/braincreator/Pose_estimation/DeepLabCut/examples/ostrich/Testing-Shan-2019-08-07/config.yaml'
    
    print("\n" + "="*80 + "\n\t\t\t\tTRAINING\n" + "="*80)
    print("\nCreating Training dataset from labeled frames...\n")
    deeplabcut.create_training_dataset(path_config_file)
    print("\nDataset created, Next stop Training!\n\n")
    deeplabcut.train_network(path_config_file, shuffle=1, saveiters=2000, displayiters=500, gputouse=None, maxiters=50000)

    print("\nEvauating network:\n" + "="*50)
    deeplabcut.evaluate_network(path_config_file, plotting=True)

    print("\n" + "="*80 + "\n\t\t\t\tANALYZE\n" + "="*80)
    deeplabcut.analyze_videos(path_config_file,videofile_path, gputouse = None, videotype='.mp4')
    
    print("\n" + "="*80 + "\n\t\t\t\tCreating video\n" + "="*80)
    deeplabcut.create_labeled_video(path_config_file, videofile_path, outputframerate = 5, draw_skeleton = True)


def watch():
    path1 = 'videos/cow_videoDeepCut_resnet50_TestingJul30shuffle1_20000_labeled.mp4'
    path2 = 'videos/cow_videoDeepCut_resnet101_TestingJul30shuffle1_46000_labeled.mp4'
    vs1 = cv2.VideoCapture(path1)
    vs2 = cv2.VideoCapture(path2)
    if vs1.isOpened() == False or vs2.isOpened == False:
        sys.exit('Video file cannot be read! Please check input_vidpath to ensure it is correctly pointing to the video file')
    
    while True:
        frame1 = vs1.read()
        frame2 = vs2.read()

        frame1 = frame1[1]
        frame2 = frame2[1]

        if frame1 is None or frame2 is None:
            break

        cv2.imshow("Frame 1", frame1)
        cv2.imshow("Frame 2", frame2)
        time.sleep(0.05)
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
    vs1.release()
    vs2.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    train()
    # watch()
