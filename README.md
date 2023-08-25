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
## About The Project
Blink Counter project allows to use video recordings to count 


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
  

<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

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
