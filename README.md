<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#Local Setup">Local Setup</a></li>
        <li><a href="#Setting virtual environment and dependenciess">Setting virtual environment and dependencies</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About Blink Counter Project 
This pipeline includes scripts and example files for running a Blink Detection visualizer application and saving the cummulative blink per minute results to output file. 

### Overview of files 
(1) **BlinkCounterVideo.py** 
- This code file is used to visualize the blink count. Also, this code can be used to increase the accuracy of the blink count calculation for other code files.
- The blink is determined by the ratio between eye width and eye length, which the user can specify the position of the points on the face map to be used to calculate the ratio. Specifically, for counting blinks for a person with different eye shapes, the variable leftUp (that refers to left eye upper point) can be changed to face[159] from face[158]. It is recommended to first run the video, identify the green points on the person and adjust to that gives more stable result. Usually, this value doesn't need to be changed. 
- Another part that can be adjusted is the threshold which determines the blink count. This threshold typically range from 270-350 but this may also be dependent on the subject's shape of the eye. Also, there may be some inaccuracies if the person look away from the center by tilting or leaning towards or away. You can start with 300 and adjust this value to increase accuracy.
- In determining the value of the threshold, one practice you can use is to take a video of the screen and see what was the value on the display when the person blinked. If the person blinked and the value was 292, but you have set the threshold to be 300 for example, then you can adjust the threshold to be 290. Observe several blinks before determining the value for accuracy.
- Since the change of the threshold value differs due to shape of the eye, you don't have to repeat this process if you are going to determine blink counts for the same one person in different videos.

<img width="602" alt="Screenshot 2023-08-26 at 9 49 30 PM" src="https://github.com/michellekimgit/BlinkCounter/assets/94397733/334a0045-2a14-4b63-98a0-f5652f48f6d8">

<img width="602" alt="Screenshot 2023-08-26 at 9 51 07 PM" src="https://github.com/michellekimgit/BlinkCounter/assets/94397733/fc4e04de-4a68-465c-830c-175866000f97">

As you can see from the example above, the subject's ratioAvg value was only about 248 when opened the eyes, but becomes about 314 when closed the eyes. In this case, we can set variable threshold to be about 300 as below.

<img width="637" alt="Screenshot 2023-08-26 at 9 53 58 PM" src="https://github.com/michellekimgit/BlinkCounter/assets/94397733/e98bad10-ccbd-4e60-97ca-f17ea6f0325c">

(2) **BlinkCounter_all.py**
- This code file is used to save blink count results on multiple video files. It is recommended to use this code file only when you are having multiple videos of the **same** person, as you would need to adjust the blink threshold if computing blinks on multiple people. If you are using videos with different people, use below **BlinkCounter.py** for individual calculation.
- Once all the variables (location of eye on face map and especially the blink threshold) are determined with **BlinkCounterVideo.py** file (refer to the above file description for more information), update the variables to **BlinkCounter_all.py** code file to get all the result of blink counts within certain folder.
- Also before running the code, specify the folder directory where videos are located by changing the variable `video_dir`. 

(3) **BlinkCounter.py**
- This code is used to get blink count result for one individual. It is recommended to use this file if you have vidoes with different people that have different threshold values, or to test if the result successfully saves before running **BlinkCounter_all.py**. Additionally, this could be use for exception cases that don't continue to run during the BlinkCounter_all.py. - Exception case may be due to a case when a person doesn't appear in the beginning or the end as this application can only be used for video where one person is present in the video. If you want it to automatically skip exceptional cases, then you can use try and except conditions. However, this is not recommended as knowing which video has exceptional case may be helpful and if skip certain timestamp, it won't be recorded in the final result.
- For example, if the subject became missing at timestamp 116300 and the output is therefore not saving successfully, you can custom the code to exit the while True loop as below. 
 <img width="693" alt="Screenshot 2023-08-26 at 9 55 22 PM" src="https://github.com/michellekimgit/BlinkCounter/assets/94397733/12c672a7-a231-4065-a3ab-bbf4d84ee935">
- Lastly, before running this file, you should first specify the filename and dir (directory) variables in the bottom of the code. Don't forget to also update the varialbes such as threshold or the location of eye on face map. The choice of the values can be determined by using the BlinkCounterVideo.py which shows the position of each variables (leftUp, leftDown, leftLeft etc) of the eye and the value of ratio (ratioAvg) for each frame, along with the video and ratioAvg values. Refer to the above file description of **BlinkCounterVideo.py** for more information.

<!-- GETTING STARTED -->
## Getting Started
### Local Setup 

 * The first step is to clone this repository on your local system.
 * First, open your terminal and go to the directory folder you would like to clone the repository. <br>
       `ls` : to check the list of <br> 
       `cd` : to go to the file/folder directory <br> 
       `cd..` : to go back to previous directory root<br> 
   For example, if your BlinkCounter folder is located at your Documents, you would run "cd Documents/BlinkCounter". Then you would run "ls" to check if all the three components are in the list. <br> 
 * One way to clone the repository is to use HTTPS. Copy the link (refer to the image below) and on terminal enter `git clone -b <branch-name> <HTTPS Link>`. Since there is only a main branch, you can also simply clone by entering `git clone <HTTPS Link>`. 
 * For more details, use the following link [how to clone repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository). You can also copy the SSH on Github as below image.
 * To create your own branch, go to the directory and `git checkout -b <new-branch-name>`
 * Once you see a folder on your directory, open the folder (you can simply drag from your File Explorer) on Visual Studio Code.

### Setting virtual environment and dependencies
* Assuming that you are on Mac, create a local environment by following the steps below: 

1. Open Visual Studio Code and open your SpaceDock folder containing all the four components above.
2. Open terminal and go to your directory <br> 
3. Run the following codes in your terminal.
   
```sh
python -m venv myenv python==3.7
source myenv/bin/activate
```
At this point, make sure that you see (myenv) in front of your directory at your terminal. If you see other environments such as (base) it may be because you are connected to the base conda environment. 
Avoid the case as below: 

<img width="599" alt="Screenshot 2023-08-26 at 9 39 46 PM" src="https://github.com/michellekimgit/BlinkCounter/assets/94397733/24c74ec8-17d2-471d-8c98-6064195c4e22">

You should not see the (base) after the environment you have activated.
Deactivtate by running `conda deactivate` in your terminal.<br>

* Install below packages using `pip install <package==version>`. Make sure you are installing the right packages. 
  ```sh
  wheel==0.36.2
  mediapipe==0.8.9.1
  cvzone==1.5.4
  Pillow==9.0.0
  numpy==1.21.5
  opencv-python==4.5.5.62
  packaging==21.3
  pyparsing==3.0.6
  python-dateutil==2.8.2
  setuptools==57.0.0
  six==1.16.0
  ```
* Alternatively, you can run `pip install requirements.txt`
* If there is an error after installing packages such as protobuf and receive an error message to downgrade certain dependent package, run `pip uninstall protobuf` and run `pip install protobuf==3.20` (or other lower version) 
* You can also check the list of packages using `pip list`

### Running Code files
After setting the virtual environment, then you can run each code by simply running `python run <code file name>` on terminal.
It is recommended to use visual studio code to run the files as you can easily find the code file names on the sidebar. 
Make sure to read the file descriptions on the above About the  project section before running the code as it explains what variables can be adjusted to increase accuracy and successfully save the results. 

Your terminal should be looking like this: 

<img width="785" alt="Screenshot 2023-08-26 at 9 38 23 PM" src="https://github.com/michellekimgit/BlinkCounter/assets/94397733/31038ac4-37dc-4188-b7e2-8894b91d11da">


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

**What can be adjusted or added** 
- Set threshold or eye location in face map as argument to BlinkCounterAll.py and BlinkCounter.py file.
- Automating the process of specifying the blink threshold for each individual.
- Easing the process of setting file and folder names for each code files. 

**How to contribute**
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Michelle (Minsol) Kim - mk101@wellesley.edu - mk9728@mit.edu

Project Link: [https://github.com/michellekimgit/BlinkCounter](https://github.com/michellekimgit/BlinkCounter)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
